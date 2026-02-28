"""Real-time centre-driven waveform visualizer for the recording state.

Renders a 25×7 grid that is **doubly symmetric** (top↔bottom **and**
left↔right).  A single ``centerAmplitude`` value—derived from the
microphone RMS level—drives the whole animation.  Columns further from
the centre have proportionally lower amplitude (linear falloff).

Colour is determined solely by vertical distance from the centre row:
``d = 0`` → green, ``d = 1`` → yellow, ``d = 2`` → orange,
``d ≥ 3`` → red.  Inactive cells are blank.
"""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from rich.text import Text
from textual.timer import Timer
from textual.widgets import Static

if TYPE_CHECKING:
    from vibe.core.voice.recorder import AudioRecorder

# ── grid constants ────────────────────────────────────────────────
_COLS = 25                 # columns 0–24
_ROWS = 7                  # rows 0–6
_CENTER_ROW = 3            # vertical centre
_CENTER_COL = 12           # horizontal centre
_MAX_AMP = 3               # maximum row-extent above/below centre

# Colour by vertical distance from centre row
_COLORS: dict[int, str] = {
    0: "#22c55e",   # green
    1: "#eab308",   # yellow
    2: "#f97316",   # orange
}
_COLOR_RED = "#ef4444"      # d ≥ 3

# Characters
_FILLED = "█"
_GAP    = " "


def _color_for_distance(d: int) -> str:
    return _COLORS.get(d, _COLOR_RED)


def _render_grid(center_amplitude: float) -> Text:
    """Build the 25×7 Rich Text grid from a single centre amplitude.

    *center_amplitude* is in the range ``0.0`` – ``3.0``.
    """
    # Compute per-column amplitude (symmetric about _CENTER_COL)
    amplitudes: list[int] = []
    for x in range(_COLS):
        distance = abs(x - _CENTER_COL)
        falloff = max(0.0, 1.0 - distance / _CENTER_COL)
        amplitudes.append(round(center_amplitude * falloff))

    result = Text()
    for row in range(_ROWS):
        d_row = abs(row - _CENTER_ROW)             # vertical dist from centre
        line = Text()
        for col in range(_COLS):
            amp = amplitudes[col]
            if d_row <= amp:
                line.append(_FILLED, style=_color_for_distance(d_row))
            else:
                line.append(" ")
            if col < _COLS - 1:
                line.append(_GAP)
        result.append_text(line)
        if row < _ROWS - 1:
            result.append("\n")

    return result


class VoiceWaveform(Static):
    """Live waveform widget shown while audio is being recorded.

    The widget polls the recorder's RMS levels at 10 Hz, derives a
    single ``centerAmplitude`` (0–3), and redraws the symmetric grid.
    A pulsing red dot and elapsed timer are shown to the right of
    the centre row.
    """

    def __init__(self, recorder: AudioRecorder, **kwargs: object) -> None:
        super().__init__("", **kwargs)
        self._recorder = recorder
        self._start_time = time.monotonic()
        self._dot_visible = True
        self._timer: Timer | None = None
        # Smoothed amplitude (exponential moving average)
        self._smooth_amp: float = 0.0

    def on_mount(self) -> None:
        self._timer = self.set_interval(0.1, self._refresh_waveform)

    def on_unmount(self) -> None:
        if self._timer is not None:
            self._timer.stop()
            self._timer = None

    # ── core refresh ──────────────────────────────────────────────

    def _refresh_waveform(self) -> None:
        # Pulsing dot (toggle every ~0.5 s)
        elapsed_ticks = int((time.monotonic() - self._start_time) / 0.5)
        self._dot_visible = elapsed_ticks % 2 == 0

        # Derive centre amplitude from latest RMS levels
        levels = self._recorder.get_levels() if self._recorder.is_recording else []
        if levels:
            # Use the last few samples for a responsive but not jittery value
            recent = levels[-5:] if len(levels) >= 5 else levels
            raw_amp = max(recent) * _MAX_AMP       # scale 0–1 → 0–3
        else:
            raw_amp = 0.0

        # Exponential smoothing so the wave expands/contracts fluidly
        alpha = 0.35
        self._smooth_amp = alpha * raw_amp + (1.0 - alpha) * self._smooth_amp
        center_amplitude = max(0.0, min(float(_MAX_AMP), self._smooth_amp))

        grid = _render_grid(center_amplitude)

        # Timer text
        elapsed = int(time.monotonic() - self._start_time)
        minutes, seconds = divmod(elapsed, 60)
        dot = "●" if self._dot_visible else " "
        timer_text = Text()
        timer_text.append(f"  {dot}", style="bold red" if self._dot_visible else "")
        timer_text.append(f" {minutes:02d}:{seconds:02d}", style="bold #888888")

        # Splice timer onto the centre row
        lines = grid.plain.split("\n")
        result = Text()
        offset = 0
        for i, line_str in enumerate(lines):
            row_slice = grid[offset : offset + len(line_str)]
            offset += len(line_str) + 1  # +1 for \n
            result.append_text(row_slice)
            if i == _CENTER_ROW:
                result.append_text(timer_text)
            if i < _ROWS - 1:
                result.append("\n")

        self.update(result)
