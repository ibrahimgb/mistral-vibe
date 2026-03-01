---
title: "vibe.cli.textual_ui.widgets.chat_input.waveform"
tldr: "Real-time centre-driven waveform visualizer for the recording state."
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.chat_input.waveform**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/waveform.py)

Real-time centre-driven waveform visualizer for the recording state.

Renders a 25×7 grid that is **doubly symmetric** (top↔bottom **and**
left↔right).  A single ``centerAmplitude`` value—derived from the
microphone RMS level—drives the whole animation.  Columns further from
the centre have proportionally lower amplitude (linear falloff).

Colour is determined solely by vertical distance from the centre row:
``d = 0`` → green, ``d = 1`` → yellow, ``d = 2`` → orange,
``d ≥ 3`` → red.  Inactive cells are blank.

This module defines the constants `_COLS`, `_ROWS`, `_CENTER_ROW`, `_CENTER_COL`, `_MAX_AMP`, `_COLORS`, `_COLOR_RED`, `_FILLED`, `_GAP`.

## [**VoiceWaveform**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/waveform.py#L80)

The [**VoiceWaveform**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/waveform.py#L80) class (extending `Static`) live waveform widget shown while audio is being recorded. It exposes `__init__()`, `on_mount()`, `on_unmount()`. Internally it relies on `_refresh_waveform()`.

**Public API:**

- `def __init__()`
- `def on_mount()`
- `def on_unmount()`

**Internal helpers:**

- `_refresh_waveform()`

## [**_render_grid()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/waveform.py#L49)

```python
def _render_grid(center_amplitude: float) -> Text
```

Build the 25×7 Rich Text grid from a single centre amplitude.

*center_amplitude* is in the range ``0.0`` – ``3.0``.

