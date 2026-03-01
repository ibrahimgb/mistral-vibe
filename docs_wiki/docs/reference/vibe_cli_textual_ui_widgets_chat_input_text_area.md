---
title: "vibe.cli.textual_ui.widgets.chat_input.text_area"
tldr: "Module vibe.cli.textual_ui.widgets.chat_input.text_area"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.chat_input.text_area**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/text_area.py)

## [**ChatTextArea**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/text_area.py#L19)

The [**ChatTextArea**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/text_area.py#L19) class (extending `TextArea`). It exposes `__init__()`, `on_blur()`, `set_app_focus()`, `on_click()`, `action_insert_newline()` among 15 public methods. Internally it relies on `_handle_history_down()`, `_on_key()`.

**Public API:**

- `def __init__()`
- `def on_blur()`
- `def set_app_focus()`
- `def on_click()`
- `def action_insert_newline()`
- `def action_open_external_editor()`
- `def on_text_area_changed()`
- `def set_completion_manager()`
- `def get_cursor_offset()`
- `def set_cursor_offset()`
- `def reset_history_state()`
- `def clear_text()`
- `def get_full_text()`
- `def mode_characters()`
- `def input_mode()`
- `def set_mode()`
- `def adjust_from_full_text_coords()` — Translate from full-text coordinates to widget coordinates.

**Internal helpers:**

- `_handle_history_down()`
- `_on_key()`

