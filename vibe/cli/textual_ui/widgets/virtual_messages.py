from __future__ import annotations

from rich.markdown import Markdown
from textual.app import App, ComposeResult
from textual.containers import Vertical
from textual.widget import Widget
from textual.widgets import Static, VerticalScroll


class MessageWidget(Static):
    """Single chat message (Markdown rendered once)."""

    def __init__(self, text: str):
        super().__init__()
        self._renderable = Markdown(text)

    def render(self):
        return self._renderable


class ChatView(Widget):
    """
    Virtualized chat view.
    Only visible messages are mounted.
    """

    DEFAULT_CSS = """
    ChatView {
        height: 100%;
    }
    """

    def __init__(self):
        super().__init__()

        self.messages: list[str] = []
        self.visible_start = 0
        self.visible_end = 0
        self.estimated_message_height = 6
        self.buffer = 3

    def compose(self) -> ComposeResult:
        with VerticalScroll() as self.scroll:
            self.top_spacer = Static("")
            self.viewport = Vertical()
            self.bottom_spacer = Static("")

            yield self.top_spacer
            yield self.viewport
            yield self.bottom_spacer

    def add_message(self, text: str):
        self.messages.append(text)
        self._refresh_viewport()

    def _refresh_viewport(self):
        if not self.messages:
            return

        viewport_height = self.scroll.size.height
        scroll_y = self.scroll.scroll_y

        # Convert scroll offset → message index
        first_visible = max(0, scroll_y // self.estimated_message_height)

        visible_count = (viewport_height // self.estimated_message_height) + 1

        start = max(0, first_visible - self.buffer)
        end = min(len(self.messages), first_visible + visible_count + self.buffer)

        # Avoid unnecessary rebuilds
        if start == self.visible_start and end == self.visible_end:
            return

        self.visible_start = start
        self.visible_end = end

        # Clear viewport
        self.viewport.remove_children()

        # Mount visible messages
        for text in self.messages[start:end]:
            self.viewport.mount(MessageWidget(text))

        # Update spacers
        self.top_spacer.update("\n" * (start * self.estimated_message_height))

        remaining = len(self.messages) - end
        self.bottom_spacer.update("\n" * (remaining * self.estimated_message_height))

    # -------------------------
    # Event hooks
    # -------------------------

    def on_mount(self):
        self.set_interval(0.05, self._refresh_viewport)


# --------------------------------------------------
# Demo app
# --------------------------------------------------


class DemoApp(App):
    CSS = """
    Screen {
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:
        self.chat = ChatView()
        yield self.chat

    def on_mount(self):
        # Generate lots of messages to show virtualization
        for i in range(200):
            self.chat.add_message(
                f"### Message {i}\n\n"
                f"Some markdown content.\n\n"
                f"```python\nprint({i})\n```"
            )


if __name__ == "__main__":
    DemoApp().run()
