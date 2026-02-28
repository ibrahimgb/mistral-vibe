"""Microphone toggle button for the chat input bar."""

from __future__ import annotations

from typing import Any

from textual.widgets import Button


class MicButton(Button):
    """A small toggle button that starts / stops audio recording.

    Visual states
    -------------
    * Default      – shows ○ (idle).
    * Recording    – shows ● and has the ``.recording`` CSS class.
    * Transcribing – shows … and has the ``.transcribing`` CSS class.
    """

    LABEL_IDLE = "○"
    LABEL_RECORDING = "●"
    LABEL_TRANSCRIBING = "…"

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(self.LABEL_IDLE, **kwargs)
        self._recording = False
        self._transcribing = False

    # --- state helpers ---------------------------------------------------
    @property
    def is_recording(self) -> bool:
        return self._recording

    @property
    def is_transcribing(self) -> bool:
        return self._transcribing

    def set_recording(self) -> None:
        self._recording = True
        self._transcribing = False
        self.label = self.LABEL_RECORDING
        self.add_class("recording")
        self.remove_class("transcribing")

    def set_transcribing(self) -> None:
        self._recording = False
        self._transcribing = True
        self.label = self.LABEL_TRANSCRIBING
        self.remove_class("recording")
        self.add_class("transcribing")

    def set_idle(self) -> None:
        self._recording = False
        self._transcribing = False
        self.label = self.LABEL_IDLE
        self.remove_class("recording")
        self.remove_class("transcribing")
