---
title: "vibe.cli.textual_ui.widgets.chat_input.body"
tldr: "Module vibe.cli.textual_ui.widgets.chat_input.body"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.chat_input.body**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/body.py)

## [**_PromptSpinner**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/body.py#L36)

The [**_PromptSpinner**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/body.py#L36) class (extending `SpinnerMixin`, `Static`). It exposes `__init__()`, `on_mount()`.

**Public API:**

- `def __init__()`
- `def on_mount()`

## [**ChatInputBody**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/body.py#L49)

The [**ChatInputBody**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/body.py#L49) class (extending `Widget`). It exposes `__init__()`, `compose()`, `on_mount()`, `on_chat_text_area_mode_changed()`, `on_chat_text_area_history_previous()` among 15 public methods. Internally it relies on `_toggle_recording()`, `_start_recording()`, `_remove_waveform()`.

**Public API:**

- `def __init__()`
- `def compose()`
- `def on_mount()`
- `def on_chat_text_area_mode_changed()`
- `def on_chat_text_area_history_previous()`
- `def on_chat_text_area_history_next()`
- `def on_chat_text_area_history_reset()`
- `def on_chat_text_area_submitted()`
- `def switching_mode()`
- `def switching_mode()`
- `def value()`
- `def value()`
- `def focus_input()`
- `def set_completion_reset_callback()`
- `def replace_input()`
- `def on_button_pressed()` — Handle mic button presses to toggle recording.
- `def on_worker_state_changed()` — Handle the result of the transcription worker.

**Internal helpers:**

- `_toggle_recording()` — Start or stop audio recording.
- `_start_recording()`
- `_remove_waveform()` — Remove the live waveform and restore the text input.

