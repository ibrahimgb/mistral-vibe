"""Session management for parallel multi-session workflows.

Each session wraps an AgentLoop and its associated UI/task state,
enabling concurrent agent execution with isolated contexts.
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any
from uuid import uuid4
from weakref import WeakKeyDictionary

from vibe.cli.textual_ui.handlers.event_handler import EventHandler
from vibe.cli.textual_ui.windowing import LOAD_MORE_BATCH_SIZE, SessionWindowing
from vibe.core.agent_loop import AgentLoop

if TYPE_CHECKING:
    from textual.widget import Widget

    from vibe.cli.textual_ui.widgets.loading import LoadingWidget


@dataclass
class SessionState:
    """All per-session mutable state, previously held as singular attrs on VibeApp."""

    session_id: str
    agent_loop: AgentLoop
    label: str = ""
    agent_task: asyncio.Task[None] | None = None
    agent_running: bool = False
    interrupt_requested: bool = False
    pending_approval: asyncio.Future[Any] | None = None
    pending_question: asyncio.Future[Any] | None = None
    loading_widget: LoadingWidget | None = None
    event_handler: EventHandler | None = None
    windowing: SessionWindowing = field(
        default_factory=lambda: SessionWindowing(
            load_more_batch_size=LOAD_MORE_BATCH_SIZE,
        ),
    )
    tool_call_map: dict[str, str] | None = None
    history_widget_indices: WeakKeyDictionary[Widget, int] = field(
        default_factory=WeakKeyDictionary,
    )
    last_mounted_user_message: Any = None
    messages_container_id: str = ""

    def __post_init__(self) -> None:
        if not self.messages_container_id:
            self.messages_container_id = f"messages-{self.session_id[:8]}"

    def reset_ui_state(self) -> None:
        """Reset windowing and tool tracking for this session."""
        self.windowing.reset()
        self.tool_call_map = None
        self.history_widget_indices = WeakKeyDictionary()


class SessionManager:
    """Manages multiple isolated sessions for parallel workflows."""

    def __init__(self) -> None:
        self._sessions: dict[str, SessionState] = {}
        self._active_id: str | None = None
        self._session_order: list[str] = []

    @property
    def active_session(self) -> SessionState | None:
        if self._active_id is None:
            return None
        return self._sessions.get(self._active_id)

    @property
    def active_id(self) -> str | None:
        return self._active_id

    def add_session(self, session: SessionState) -> None:
        """Add an existing SessionState (e.g. the initial session from app startup)."""
        self._sessions[session.session_id] = session
        if session.session_id not in self._session_order:
            self._session_order.append(session.session_id)
        if self._active_id is None:
            self._active_id = session.session_id

    def create_session(self, config: Any, **agent_kwargs: Any) -> SessionState:
        """Create a new session with a fresh AgentLoop."""
        session_id = str(uuid4())[:8]
        agent_loop = AgentLoop(config=config, **agent_kwargs)
        session = SessionState(
            session_id=session_id,
            agent_loop=agent_loop,
        )
        self._sessions[session.session_id] = session
        self._session_order.append(session.session_id)
        return session

    def switch_to(self, session_id: str) -> SessionState:
        """Activate a different session. Returns the newly active session."""
        if session_id not in self._sessions:
            msg = f"Session '{session_id}' not found"
            raise KeyError(msg)
        self._active_id = session_id
        return self._sessions[session_id]

    def get(self, session_id: str) -> SessionState | None:
        return self._sessions.get(session_id)

    def list_sessions(self) -> list[SessionState]:
        """Return sessions in creation order."""
        return [self._sessions[sid] for sid in self._session_order if sid in self._sessions]

    def remove_session(self, session_id: str) -> SessionState | None:
        """Remove a session. Returns the removed session or None."""
        session = self._sessions.pop(session_id, None)
        if session_id in self._session_order:
            self._session_order.remove(session_id)
        if self._active_id == session_id:
            self._active_id = self._session_order[0] if self._session_order else None
        return session

    def next_session_id(self) -> str | None:
        """Get the next session ID in order (for cycling with keyboard shortcut)."""
        if not self._session_order or self._active_id is None:
            return None
        try:
            idx = self._session_order.index(self._active_id)
            next_idx = (idx + 1) % len(self._session_order)
            return self._session_order[next_idx]
        except ValueError:
            return None

    def prev_session_id(self) -> str | None:
        """Get the previous session ID in order (for cycling with keyboard shortcut)."""
        if not self._session_order or self._active_id is None:
            return None
        try:
            idx = self._session_order.index(self._active_id)
            prev_idx = (idx - 1) % len(self._session_order)
            return self._session_order[prev_idx]
        except ValueError:
            return None

    @property
    def session_count(self) -> int:
        return len(self._sessions)
