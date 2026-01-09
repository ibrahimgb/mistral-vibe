from __future__ import annotations

import asyncio
from bisect import bisect_right
from dataclasses import dataclass

from textual.app import ComposeResult
from textual.await_complete import AwaitComplete
from textual.widget import Widget
from textual.widgets import Static


@dataclass(slots=True)
class _Entry:
    widget: Widget
    height: int | None = None
    mounted: bool = False


class VirtualMessages(Widget):
    """A message container that virtualizes message widgets.

    The UI remains "widget per message", but only a small window of widgets
    around the viewport stays mounted. Off-screen content is represented by
    top/bottom spacers sized from cached per-message heights.
    """

    DEFAULT_CSS = """
    VirtualMessages {
        layout: vertical;
        width: 100%;
        height: auto;
    }

    VirtualMessages > #vm-top,
    VirtualMessages > #vm-bottom {
        width: 100%;
        height: 0;
        padding: 0;
        margin: 0;
    }
    """

    def __init__(
        self, *, buffer_lines: int = 40, default_estimated_height: int = 3, **kwargs
    ):
        super().__init__(**kwargs)
        self._entries: list[_Entry] = []
        self._buffer_lines = buffer_lines
        self._default_estimated_height = max(1, default_estimated_height)

        self._top_spacer: Static | None = None
        self._bottom_spacer: Static | None = None

        self._prefix: list[int] = [0]
        self._prefix_dirty: bool = False
        self._range_start: int = 0
        self._range_end: int = -1
        self._relative_scroll_y: int = 0
        self._viewport_height: int = 0

        self._measure_scheduled = False
        self._rebuild_scheduled = False

    def compose(self) -> ComposeResult:
        self._top_spacer = Static("", id="vm-top")
        self._bottom_spacer = Static("", id="vm-bottom")
        yield self._top_spacer
        yield self._bottom_spacer

    # --- public API / compatibility ---

    def mount(
        self,
        *widgets: Widget,
        before: int | str | Widget | None = None,
        after: int | str | Widget | None = None,
    ) -> AwaitComplete:
        """Compatibility shim: treat mounting as appending messages.

        Textual's `Widget.mount` returns an awaitable. Callers in the app and
        tests frequently do `await messages_area.mount(widget)`.
        """
        internal_ids = {"vm-top", "vm-bottom"}

        # Textual mounts our own spacer widgets during composition.
        # We must not treat those as "messages"; only user-facing message widgets
        # get recorded/virtualized.

        internal_widgets: list[Widget] = []
        message_widgets: list[Widget] = []
        for widget in widgets:
            if getattr(widget, "id", None) in internal_ids:
                internal_widgets.append(widget)
            else:
                message_widgets.append(widget)

        internal_awaitable = (
            super().mount(*internal_widgets, before=before, after=after)
            if internal_widgets
            else None
        )

        for widget in message_widgets:
            # Record the message widget in our internal list. The actual mounting
            # is performed later by `_rebuild_visible_children_async`, which mounts
            # only a window around the viewport.
            self.append_message(widget)

        async def await_mount() -> None:
            if internal_awaitable is not None:
                await internal_awaitable
            # `VirtualMessages` composes its internal containers on mount.
            # Tests may call `await messages_area.mount(...)` before those
            # children are attached, so we wait a tick until they are.
            for _ in range(20):
                if self._bottom_spacer is not None and self._bottom_spacer.is_attached:
                    break
                await asyncio.sleep(0)
            await self._rebuild_visible_children_async(force=True)

        return AwaitComplete(await_mount())

    def remove_children(self, selector: str | type | object = "*") -> AwaitComplete:
        """Clear all message entries without removing internal spacer widgets."""
        del selector

        async def await_remove() -> None:
            self._entries.clear()
            self._prefix = [0]
            self._prefix_dirty = False
            self._range_start = 0
            self._range_end = -1

            for child in list(self.children):
                if child is self._top_spacer or child is self._bottom_spacer:
                    continue
                await child.remove()

            if self._top_spacer is not None:
                self._top_spacer.styles.height = 0
            if self._bottom_spacer is not None:
                self._bottom_spacer.styles.height = 0

        return AwaitComplete(await_remove())

    def append_message(self, widget: Widget) -> None:
        self._entries.append(_Entry(widget=widget))
        # Keep prefix sums in sync incrementally for fast scrolling.
        # (If prefix is marked dirty for any reason, defer rebuilding until needed.)
        if not self._prefix_dirty and len(self._prefix) == len(self._entries):
            self._prefix.append(self._prefix[-1] + self._default_estimated_height)
        else:
            self._prefix_dirty = True

    def set_viewport(self, *, relative_scroll_y: int, viewport_height: int) -> None:
        self._relative_scroll_y = max(0, int(relative_scroll_y))
        self._viewport_height = max(0, int(viewport_height))
        self._update_visible_window()

    # --- virtualization core ---

    def _entry_height(self, entry: _Entry) -> int:
        return (
            entry.height if entry.height is not None else self._default_estimated_height
        )

    def _ensure_prefix(self) -> None:
        """Ensure prefix sums are up-to-date.

        This must be fast on scroll; rebuilding the entire prefix list for every
        scroll tick becomes O(n) and causes lag on long transcripts.
        """
        expected_len = len(self._entries) + 1
        if not self._prefix_dirty and len(self._prefix) == expected_len:
            return

        prefix = [0]
        total = 0
        for entry in self._entries:
            total += self._entry_height(entry)
            prefix.append(total)
        self._prefix = prefix
        self._prefix_dirty = False

    def _rebuild_prefix_from(self, first_changed_index: int) -> None:
        """Recompute prefix sums from a given entry index onward."""
        if first_changed_index <= 0:
            self._prefix_dirty = True
            self._ensure_prefix()
            return

        expected_len = len(self._entries) + 1
        if len(self._prefix) != expected_len:
            self._prefix_dirty = True
            self._ensure_prefix()
            return

        total = self._prefix[first_changed_index]
        for idx in range(first_changed_index, len(self._entries)):
            total += self._entry_height(self._entries[idx])
            self._prefix[idx + 1] = total

    def _compute_range(self) -> tuple[int, int]:
        if not self._entries:
            return (0, -1)

        self._ensure_prefix()

        y0 = max(0, self._relative_scroll_y - self._buffer_lines)
        y1 = self._relative_scroll_y + self._viewport_height + self._buffer_lines

        start = max(0, bisect_right(self._prefix, y0) - 1)
        end = max(0, bisect_right(self._prefix, y1) - 1)
        end = min(len(self._entries) - 1, end)
        return (start, end)

    def _update_spacers(self, start: int, end: int) -> None:
        if self._top_spacer is None or self._bottom_spacer is None:
            return

        top_height = self._prefix[start] if 0 <= start <= len(self._entries) else 0
        bottom_height = 0
        if end >= 0:
            bottom_height = self._prefix[-1] - self._prefix[end + 1]

        top_height = max(0, int(top_height))
        bottom_height = max(0, int(bottom_height))

        self._top_spacer.display = top_height > 0
        self._bottom_spacer.display = bottom_height > 0

        self._top_spacer.styles.height = top_height
        self._bottom_spacer.styles.height = bottom_height

    def _update_visible_window(self, *, force: bool = False) -> None:
        if self._top_spacer is None or self._bottom_spacer is None:
            return

        start, end = self._compute_range()
        if not force and start == self._range_start and end == self._range_end:
            return

        self._range_start, self._range_end = start, end
        self._update_spacers(start, end)

        self._schedule_rebuild_visible()

    def _schedule_rebuild_visible(self) -> None:
        if self._rebuild_scheduled:
            return
        self._rebuild_scheduled = True

        def kick() -> None:
            self._rebuild_scheduled = False
            self.run_worker(self._rebuild_visible_children_async(), exclusive=False)

        self.call_after_refresh(kick)

    async def _rebuild_visible_children_async(self, *, force: bool = False) -> None:
        if self._top_spacer is None or self._bottom_spacer is None:
            return
        if not self._bottom_spacer.is_attached:
            return

        self._update_visible_window(force=force)

        desired_indices = (
            range(self._range_start, self._range_end + 1)
            if self._range_end >= self._range_start
            else range(0)
        )
        desired_widgets = [self._entries[i].widget for i in desired_indices]
        desired_set = set(desired_widgets)

        current_children = [
            child
            for child in list(self.children)
            if child is not self._top_spacer and child is not self._bottom_spacer
        ]
        for child in current_children:
            if child not in desired_set:
                await child.remove()

        if not desired_widgets:
            self._schedule_measure()
            return

        current_children = [
            child
            for child in list(self.children)
            if child is not self._top_spacer and child is not self._bottom_spacer
        ]
        current_set = set(current_children)

        for idx, widget in enumerate(desired_widgets):
            if widget in current_set:
                continue

            before_widget: Widget | None = None
            for next_widget in desired_widgets[idx + 1 :]:
                if next_widget in current_set:
                    before_widget = next_widget
                    break

            if before_widget is not None:
                await super().mount(widget, before=before_widget)
            else:
                await super().mount(widget, before=self._bottom_spacer)

            current_set.add(widget)

        for entry in self._entries:
            entry.mounted = entry.widget.is_attached

        self._schedule_measure()

    def _schedule_measure(self) -> None:
        if self._measure_scheduled:
            return
        self._measure_scheduled = True
        self.call_after_refresh(self._measure_visible)

    def _measure_visible(self) -> None:
        self._measure_scheduled = False
        if self._top_spacer is None or self._bottom_spacer is None:
            return

        changed = False
        first_changed_index: int | None = None
        for idx in range(self._range_start, self._range_end + 1):
            if idx < 0 or idx >= len(self._entries):
                continue
            entry = self._entries[idx]
            if not entry.mounted:
                continue
            try:
                height = int(entry.widget.size.height)
            except Exception:
                continue
            if height <= 0:
                continue
            if entry.height != height:
                entry.height = height
                changed = True
                first_changed_index = (
                    idx
                    if first_changed_index is None
                    else min(first_changed_index, idx)
                )

        if changed:
            if first_changed_index is None:
                self._prefix_dirty = True
                self._ensure_prefix()
            else:
                self._ensure_prefix()
                self._rebuild_prefix_from(first_changed_index)
            self._update_spacers(self._range_start, self._range_end)
