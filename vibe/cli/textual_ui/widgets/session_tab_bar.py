"""Session tab bar widget for displaying and switching between parallel sessions."""

from __future__ import annotations

from typing import TYPE_CHECKING, ClassVar

from textual.app import ComposeResult
from textual.binding import Binding, BindingType
from textual.containers import Horizontal
from textual.message import Message
from textual.reactive import reactive
from textual.widgets import Static

if TYPE_CHECKING:
    from vibe.cli.textual_ui.session_manager import SessionState


class SessionTab(Static):
    """A single tab representing one session."""

    DEFAULT_CSS = """
    SessionTab {
        width: auto;
        height: 1;
        padding: 0 1;
        color: $text-muted;
    }
    SessionTab.active {
        color: $text;
        text-style: bold;
    }
    SessionTab.running {
        color: $warning;
    }
    SessionTab.running.active {
        color: $warning;
        text-style: bold;
    }
    """

    class Clicked(Message):
        def __init__(self, session_id: str) -> None:
            super().__init__()
            self.session_id = session_id

    def __init__(self, session_id: str, label: str, *, is_active: bool = False, is_running: bool = False) -> None:
        super().__init__()
        self._session_id = session_id
        self._label = label
        self._is_active = is_active
        self._is_running = is_running
        self._refresh_tab()

    def _refresh_tab(self) -> None:
        prefix = "●" if self._is_running else "○"
        marker = "▸" if self._is_active else " "
        self.update(f"{marker}{prefix} {self._label}")
        self.set_class(self._is_active, "active")
        self.set_class(self._is_running, "running")

    def set_active(self, active: bool) -> None:
        self._is_active = active
        self._refresh_tab()

    def set_running(self, running: bool) -> None:
        self._is_running = running
        self._refresh_tab()

    def set_label(self, label: str) -> None:
        self._label = label
        self._refresh_tab()

    async def on_click(self) -> None:
        self.post_message(self.Clicked(self._session_id))


class SessionTabBar(Horizontal):
    """Horizontal bar of session tabs."""

    DEFAULT_CSS = """
    SessionTabBar {
        width: 100%;
        height: 1;
        background: $surface;
        dock: top;
        display: none;
    }
    SessionTabBar.visible {
        display: block;
    }
    """

    def __init__(self) -> None:
        super().__init__(id="session-tab-bar")
        self._tabs: dict[str, SessionTab] = {}

    def update_sessions(self, sessions: list[SessionState], active_id: str | None) -> None:
        """Rebuild tabs from session list. Only shows bar when >1 session exists."""
        show = len(sessions) > 1
        self.set_class(show, "visible")

        existing_ids = set(self._tabs.keys())
        new_ids = {s.session_id for s in sessions}

        # Remove tabs for deleted sessions
        for sid in existing_ids - new_ids:
            tab = self._tabs.pop(sid)
            tab.remove()

        # Add/update tabs
        for i, session in enumerate(sessions):
            label = session.label or f"Session {i + 1}"
            if session.session_id in self._tabs:
                tab = self._tabs[session.session_id]
                tab.set_label(label)
                tab.set_active(session.session_id == active_id)
                tab.set_running(session.agent_running)
            else:
                tab = SessionTab(
                    session.session_id,
                    label,
                    is_active=session.session_id == active_id,
                    is_running=session.agent_running,
                )
                self._tabs[session.session_id] = tab
                self.mount(tab)
