from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any, ClassVar

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.message import Message
from textual.widget import Widget
from textual.widgets import Static
from textual.worker import Worker, WorkerState

from vibe.cli.history_manager import HistoryManager
from vibe.cli.textual_ui.widgets.chat_input.mic_button import MicButton
from vibe.cli.textual_ui.widgets.chat_input.text_area import ChatTextArea, InputMode
from vibe.cli.textual_ui.widgets.no_markup_static import NoMarkupStatic
from vibe.cli.textual_ui.widgets.spinner import SpinnerMixin, SpinnerType
from vibe.core.logger import logger

# Lazy-loaded at first use so the app still starts if no mic is available
_recorder_available: bool | None = None


def _check_recorder() -> bool:
    global _recorder_available  # noqa: PLW0603
    if _recorder_available is None:
        try:
            import sounddevice  # noqa: F401
            _recorder_available = True
        except (ImportError, OSError):
            _recorder_available = False
    return _recorder_available


class _PromptSpinner(SpinnerMixin, Static):
    SPINNER_TYPE: ClassVar[SpinnerType] = SpinnerType.BRAILLE

    def __init__(self) -> None:
        self._indicator_widget: Static | None = None
        self.init_spinner()
        super().__init__(self._spinner.current_frame(), id="prompt-spinner")

    def on_mount(self) -> None:
        self._indicator_widget = self
        self.start_spinner_timer()


class ChatInputBody(Widget):
    class Submitted(Message):
        def __init__(self, value: str) -> None:
            self.value = value
            super().__init__()

    def __init__(
        self,
        history_file: Path | None = None,
        nuage_enabled: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self.input_widget: ChatTextArea | None = None
        self.prompt_widget: NoMarkupStatic | None = None
        self._nuage_enabled = nuage_enabled
        self._switching_mode = False

        if history_file:
            self.history = HistoryManager(history_file)
        else:
            self.history = None

        self._completion_reset: Callable[[], None] | None = None

    def compose(self) -> ComposeResult:
        with Horizontal():
            self.prompt_widget = NoMarkupStatic(">", id="prompt")
            yield self.prompt_widget

            self.input_widget = ChatTextArea(
                id="input", nuage_enabled=self._nuage_enabled
            )
            yield self.input_widget

            if _check_recorder():
                self._mic_button = MicButton(id="mic-button")
                yield self._mic_button

    def on_mount(self) -> None:
        if self.input_widget:
            self.input_widget.focus()

    def _parse_mode_and_text(self, text: str) -> tuple[InputMode, str]:
        if text.startswith("!"):
            return "!", text[1:]
        elif text.startswith("/"):
            return "/", text[1:]
        elif text.startswith("&") and self._nuage_enabled:
            return "&", text[1:]
        else:
            return ">", text

    def _update_prompt(self) -> None:
        if not self.input_widget or not self.prompt_widget:
            return

        self.prompt_widget.update(self.input_widget.input_mode)

    def on_chat_text_area_mode_changed(self, event: ChatTextArea.ModeChanged) -> None:
        if self.prompt_widget:
            self.prompt_widget.update(event.mode)

    def _load_history_entry(self, text: str, cursor_col: int | None = None) -> None:
        if not self.input_widget:
            return

        mode, display_text = self._parse_mode_and_text(text)

        self.input_widget._navigating_history = True
        self.input_widget.set_mode(mode)
        self.input_widget.load_text(display_text)

        first_line = display_text.split("\n")[0]
        col = cursor_col if cursor_col is not None else len(first_line)
        cursor_pos = (0, col)

        self.input_widget.move_cursor(cursor_pos)
        self.input_widget._last_cursor_col = col
        self.input_widget._cursor_pos_after_load = cursor_pos
        self.input_widget._cursor_moved_since_load = False

        self._update_prompt()
        self._notify_completion_reset()

    def on_chat_text_area_history_previous(
        self, event: ChatTextArea.HistoryPrevious
    ) -> None:
        if not self.history or not self.input_widget:
            return

        if self.history._current_index == -1:
            self.input_widget._original_text = self.input_widget.text

        if (
            self.history._current_index != -1
            and self.input_widget._last_used_prefix is not None
            and self.input_widget._last_used_prefix != event.prefix
        ):
            self.history.reset_navigation()

        self.input_widget._last_used_prefix = event.prefix
        previous = self.history.get_previous(
            self.input_widget._original_text, prefix=event.prefix
        )

        if previous is not None:
            self._load_history_entry(previous)

    def on_chat_text_area_history_next(self, event: ChatTextArea.HistoryNext) -> None:
        if not self.history or not self.input_widget:
            return

        if self.history._current_index == -1:
            return

        if (
            self.input_widget._last_used_prefix is not None
            and self.input_widget._last_used_prefix != event.prefix
        ):
            self.history.reset_navigation()

        self.input_widget._last_used_prefix = event.prefix

        has_next = any(
            self.history._entries[i].startswith(event.prefix)
            for i in range(self.history._current_index + 1, len(self.history._entries))
        )

        original_matches = self.input_widget._original_text.startswith(event.prefix)

        if has_next or original_matches:
            next_entry = self.history.get_next(prefix=event.prefix)
            if next_entry is not None:
                cursor_col = (
                    len(event.prefix) if self.history._current_index == -1 else None
                )
                self._load_history_entry(next_entry, cursor_col=cursor_col)

    def on_chat_text_area_history_reset(self, event: ChatTextArea.HistoryReset) -> None:
        if self.history:
            self.history.reset_navigation()
        if self.input_widget:
            self.input_widget._original_text = ""
            self.input_widget._cursor_pos_after_load = None
            self.input_widget._cursor_moved_since_load = False

    def on_chat_text_area_submitted(self, event: ChatTextArea.Submitted) -> None:
        event.stop()

        if self._switching_mode:
            return

        if not self.input_widget:
            return

        value = event.value.strip()
        if not value:
            return

        if self.history:
            self.history.add(value)
            self.history.reset_navigation()

        self.input_widget.clear_text()
        self._update_prompt()

        self._notify_completion_reset()

        self.post_message(self.Submitted(value))

    @property
    def switching_mode(self) -> bool:
        return self._switching_mode

    @switching_mode.setter
    def switching_mode(self, value: bool) -> None:
        self._switching_mode = value
        if value:
            if self.prompt_widget:
                self.prompt_widget.display = False
            if not self.query(_PromptSpinner):
                self.query_one(Horizontal).mount(_PromptSpinner(), before=0)
        else:
            for spinner in self.query(_PromptSpinner):
                spinner.remove()
            if self.prompt_widget:
                self.prompt_widget.display = True
                self._update_prompt()

    @property
    def value(self) -> str:
        if not self.input_widget:
            return ""
        return self.input_widget.get_full_text()

    @value.setter
    def value(self, text: str) -> None:
        if self.input_widget:
            mode, display_text = self._parse_mode_and_text(text)
            self.input_widget.set_mode(mode)
            self.input_widget.load_text(display_text)
            self._update_prompt()

    def focus_input(self) -> None:
        if self.input_widget:
            self.input_widget.focus()

    def set_completion_reset_callback(
        self, callback: Callable[[], None] | None
    ) -> None:
        self._completion_reset = callback

    def _notify_completion_reset(self) -> None:
        if self._completion_reset:
            self._completion_reset()

    def replace_input(self, text: str, cursor_offset: int | None = None) -> None:
        if not self.input_widget:
            return

        self.input_widget.load_text(text)
        self.input_widget.reset_history_state()
        self._update_prompt()

        if cursor_offset is not None:
            self.input_widget.set_cursor_offset(max(0, min(cursor_offset, len(text))))

    # ------------------------------------------------------------------
    # Voice recording / transcription
    # ------------------------------------------------------------------

    def on_button_pressed(self, event: MicButton.Pressed) -> None:
        """Handle mic button presses to toggle recording."""
        if not isinstance(event.button, MicButton):
            return
        event.stop()
        self._toggle_recording()

    def _toggle_recording(self) -> None:
        """Start or stop audio recording."""
        if not hasattr(self, "_mic_button"):
            self.notify("Audio recording is not available", severity="error")
            return

        if self._mic_button.is_transcribing:
            return  # transcription in flight, ignore clicks

        if self._mic_button.is_recording:
            self._stop_recording()
        else:
            self._start_recording()

    def _start_recording(self) -> None:
        from vibe.core.voice.recorder import AudioRecorder

        if not hasattr(self, "_recorder"):
            self._recorder = AudioRecorder()

        try:
            self._recorder.start()
        except Exception as exc:
            logger.warning("Failed to start recording: %s", exc)
            self.notify(f"Cannot record: {exc}", severity="error")
            return

        self._mic_button.set_recording()

        # Mount live waveform, hide text input
        if self.prompt_widget:
            self.prompt_widget.display = False
        if self.input_widget:
            self.input_widget.display = False

        from vibe.cli.textual_ui.widgets.chat_input.waveform import VoiceWaveform

        waveform = VoiceWaveform(self._recorder, id="voice-waveform")
        self.query_one(Horizontal).mount(waveform, after=0)

    def _remove_waveform(self) -> None:
        """Remove the live waveform and restore the text input."""
        from vibe.cli.textual_ui.widgets.chat_input.waveform import VoiceWaveform

        for w in self.query(VoiceWaveform):
            w.remove()
        if self.prompt_widget:
            self.prompt_widget.display = True
        if self.input_widget:
            self.input_widget.display = True

    def _stop_recording(self) -> None:
        self._remove_waveform()

        try:
            wav_bytes = self._recorder.stop()
        except ValueError as exc:
            # recording too short
            self._mic_button.set_idle()
            self.notify(str(exc), severity="warning")
            return
        except Exception as exc:
            self._mic_button.set_idle()
            logger.warning("Recording error: %s", exc)
            self.notify(f"Recording failed: {exc}", severity="error")
            return

        self._mic_button.set_transcribing()
        self.notify("Transcribing…")
        self.run_worker(self._transcribe(wav_bytes), name="voice-transcribe", exclusive=True)

    async def _transcribe(self, wav_bytes: bytes) -> str:
        from vibe.core.voice.transcriber import transcribe_audio

        return await transcribe_audio(wav_bytes)

    def on_worker_state_changed(self, event: Worker.StateChanged) -> None:
        """Handle the result of the transcription worker."""
        if event.worker.name != "voice-transcribe":
            return

        match event.state:
            case WorkerState.SUCCESS:
                text = event.worker.result
                if text and self.input_widget:
                    self.input_widget.load_text(text)
                    self.input_widget.focus()
                    self.notify("Transcription ready – review and press Enter to send")
                if hasattr(self, "_mic_button"):
                    self._mic_button.set_idle()

            case WorkerState.ERROR:
                error = event.worker.error
                logger.warning("Transcription failed: %s", error)
                self.notify(f"Transcription failed: {error}", severity="error")
                if hasattr(self, "_mic_button"):
                    self._mic_button.set_idle()

            case WorkerState.CANCELLED:
                if hasattr(self, "_mic_button"):
                    self._mic_button.set_idle()
