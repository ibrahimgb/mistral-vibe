from __future__ import annotations

from rich.markdown import Markdown
from textual import Widget
from textual.app import ComposeResult
from textual.containers import Vertical
from textual.widgets import Static, VerticalScroll


class MessageWidget(Static):
    def __init__(self, content: str):
        super().__init__()
        self.content = content

    def render(self):
        return Markdown(self.content)


class ChatView(Widget):
    def compose(self) -> ComposeResult:
        with VerticalScroll():
            self.messages_container = Vertical()
            yield self.messages_container

    def add_message(self, text: str):
        self.messages_container.mount(MessageWidget(text))
