---
title: "tests.cli.test_question_app"
tldr: "Module tests.cli.test_question_app"
tags: [reference, api]
---

# `tests.cli.test_question_app`

**Source:** [`tests/cli/test_question_app.py`](tests/cli/test_question_app.py) · 513 lines

## `TestQuestionAppState`

**Source:** [`tests/cli/test_question_app.py#L64`](tests/cli/test_question_app.py#L64)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_init_state()` | single_question_args | `—` | — |
| `test_total_options_single_select()` | single_question_args | `—` | — |
| `test_total_options_multi_select_includes_submit()` | multi_select_args | `—` | — |
| `test_is_other_selected()` | single_question_args | `—` | — |
| `test_is_submit_selected()` | multi_select_args | `—` | — |
| `test_is_submit_selected_false_for_single_select()` | single_question_args | `—` | — |
| `test_store_other_text_per_question()` | multi_question_args | `—` | — |
| `test_save_regular_option_answer()` | single_question_args | `—` | — |
| `test_save_other_option_answer()` | single_question_args | `—` | — |
| `test_save_other_option_empty_does_not_save()` | single_question_args | `—` | — |
| `test_all_answered_false_initially()` | multi_question_args | `—` | — |
| `test_all_answered_true_when_complete()` | multi_question_args | `—` | — |
| `test_multi_select_toggle()` | multi_select_args | `—` | — |
| `test_multi_select_save_answer()` | multi_select_args | `—` | — |
| `test_multi_select_with_other()` | multi_select_args | `—` | — |

## `TestQuestionAppActions`

**Source:** [`tests/cli/test_question_app.py#L241`](tests/cli/test_question_app.py#L241)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_action_move_down()` | single_question_args | `—` | — |
| `test_action_move_up()` | single_question_args | `—` | — |
| `test_switch_question_preserves_other_text()` | multi_question_args | `—` | — |

## `TestMultiSelectOtherBehavior`

**Source:** [`tests/cli/test_question_app.py#L282`](tests/cli/test_question_app.py#L282)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_multi_select_other_does_not_advance_on_save()` | multi_select_args | `—` | — |
| `test_multi_select_other_toggle_adds_to_selections()` | multi_select_args | `—` | — |
| `test_multi_select_save_with_other_and_regular_options()` | multi_select_args | `—` | — |
| `test_multi_select_other_without_text_not_in_answer()` | multi_select_args | `—` | — |
| `test_multi_select_can_toggle_after_selecting_other()` | multi_select_args | `—` | — |
| `test_multi_select_empty_selections_does_not_save()` | multi_select_args | `—` | — |

## `TestSingleSelectOtherBehavior`

**Source:** [`tests/cli/test_question_app.py#L388`](tests/cli/test_question_app.py#L388)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_single_select_other_with_text_saves()` | single_question_args | `—` | — |
| `test_single_select_other_without_text_does_not_save()` | single_question_args | `—` | — |
| `test_single_select_regular_option_saves_immediately()` | single_question_args | `—` | — |

## `TestMultiSelectAutoSelect`

**Source:** [`tests/cli/test_question_app.py#L428`](tests/cli/test_question_app.py#L428)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_typing_auto_selects_other()` | multi_select_args | `—` | — |
| `test_clearing_auto_deselects_other()` | multi_select_args | `—` | — |
| `test_auto_select_preserves_other_selections()` | multi_select_args | `—` | — |

## `TestMultiSelectSubmit`

**Source:** [`tests/cli/test_question_app.py#L492`](tests/cli/test_question_app.py#L492)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_navigate_to_submit()` | multi_select_args | `—` | — |
| `test_submit_wraps_around()` | multi_select_args | `—` | — |

## `single_question_args()`

```python
def single_question_args()
```

**Source:** [`tests/cli/test_question_app.py#L13`](tests/cli/test_question_app.py#L13)

## `multi_question_args()`

```python
def multi_question_args()
```

**Source:** [`tests/cli/test_question_app.py#L29`](tests/cli/test_question_app.py#L29)

## `multi_select_args()`

```python
def multi_select_args()
```

**Source:** [`tests/cli/test_question_app.py#L47`](tests/cli/test_question_app.py#L47)

