from __future__ import annotations

from textual.containers import VerticalScroll


class ChatScroll(VerticalScroll):
    """VerticalScroll that notifies the app when scroll position changes."""

    def watch_scroll_y(self, old_value: float, new_value: float) -> None:
        super().watch_scroll_y(old_value, new_value)
        if round(old_value) != round(new_value):
            self._notify_app()

    def on_resize(self) -> None:
        self._notify_app()

    def _notify_app(self) -> None:
        update = getattr(self.app, "_update_message_virtualization", None)
        if update is not None:
            try:
                self.app.call_after_refresh(update)
            except Exception:
                pass
