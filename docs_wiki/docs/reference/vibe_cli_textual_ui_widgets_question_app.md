---
title: "vibe.cli.textual_ui.widgets.question_app"
tldr: "Module vibe.cli.textual_ui.widgets.question_app"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.question_app**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/question_app.py)

## [**QuestionApp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/question_app.py#L26)

The [**QuestionApp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/question_app.py#L26) class (extending `Container`). It exposes `__init__()`, `compose()`, `on_mount()`, `action_move_up()`, `action_move_down()` among 14 public methods. Internally it relies on `_format_option_prefix()`, `_update_other_row()`, `_update_submit()`.

**Public API:**

- `def __init__()`
- `def compose()`
- `async def on_mount()`
- `def action_move_up()`
- `def action_move_down()`
- `def action_next_question()`
- `def action_prev_question()`
- `def action_select()`
- `def action_cancel()`
- `def on_input_submitted()`
- `def on_input_changed()`
- `def on_key()`
- `def on_blur()`
- `def on_input_blurred()`

**Internal helpers:**

- `_format_option_prefix()` — Format the prefix for an option line (cursor + number + checkbox if multi).
- `_update_other_row()`
- `_update_submit()`
- `_handle_multi_select_action()` — Handle Enter key in multi-select mode: toggle option or submit.
- `_handle_single_select_action()` — Handle Enter key in single-select mode: select and advance.
- `_toggle_selection()` — Toggle an option's selection state (multi-select only).
- `_sync_other_selection_with_text()` — Auto-select/deselect 'Other' option based on whether text is entered (multi-select only).
- `_save_multi_select_answer()` — Save answer for multi-select question (combines all selected options).
- `_save_single_select_answer()` — Save answer for single-select question.

