---
title: "tests.autocompletion.test_slash_command_controller"
tldr: "Module tests.autocompletion.test_slash_command_controller"
tags: [reference, api]
---

# `tests.autocompletion.test_slash_command_controller`

**Source:** [`tests/autocompletion/test_slash_command_controller.py`](tests/autocompletion/test_slash_command_controller.py) · 235 lines

## `Suggestion`

**Bases:** `NamedTuple`

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L12`](tests/autocompletion/test_slash_command_controller.py#L12)

## `SuggestionEvent`

**Bases:** `NamedTuple`

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L17`](tests/autocompletion/test_slash_command_controller.py#L17)

## `Replacement`

**Bases:** `NamedTuple`

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L22`](tests/autocompletion/test_slash_command_controller.py#L22)

## `StubView`

**Bases:** `CompletionView`

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L28`](tests/autocompletion/test_slash_command_controller.py#L28)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `None` | — |
| `render_completion_suggestions()` | suggestions, selected_index | `None` | — |
| `clear_completion_suggestions()` |  | `None` | — |
| `replace_completion_range()` | start, end, replacement | `None` | — |

## `key_event()`

```python
def key_event(key: str) -> events.Key
```

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L47`](tests/autocompletion/test_slash_command_controller.py#L47)

## `make_controller()`

```python
def make_controller() -> tuple[SlashCommandController, StubView]
```

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L51`](tests/autocompletion/test_slash_command_controller.py#L51)

## `test_on_text_change_emits_matching_suggestions_in_insertion_order_and_ignores_duplicates()`

```python
def test_on_text_change_emits_matching_suggestions_in_insertion_order_and_ignores_duplicates() -> None
```

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L75`](tests/autocompletion/test_slash_command_controller.py#L75)

## `test_on_text_change_filters_suggestions_case_insensitively()`

```python
def test_on_text_change_filters_suggestions_case_insensitively() -> None
```

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L90`](tests/autocompletion/test_slash_command_controller.py#L90)

## `test_on_text_change_clears_suggestions_when_no_matches()`

```python
def test_on_text_change_clears_suggestions_when_no_matches() -> None
```

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L99`](tests/autocompletion/test_slash_command_controller.py#L99)

## `test_on_text_change_limits_the_number_of_results_and_preserves_insertion_order()`

```python
def test_on_text_change_limits_the_number_of_results_and_preserves_insertion_order() -> None
```

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L108`](tests/autocompletion/test_slash_command_controller.py#L108)

## `test_on_key_tab_applies_selected_completion()`

```python
def test_on_key_tab_applies_selected_completion() -> None
```

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L128`](tests/autocompletion/test_slash_command_controller.py#L128)

## `test_on_key_down_and_up_cycle_selection()`

```python
def test_on_key_down_and_up_cycle_selection() -> None
```

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L138`](tests/autocompletion/test_slash_command_controller.py#L138)

## `test_on_key_enter_submits_selected_completion()`

```python
def test_on_key_enter_submits_selected_completion() -> None
```

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L155`](tests/autocompletion/test_slash_command_controller.py#L155)

## `test_callable_entries_updates_completions_dynamically()`

```python
def test_callable_entries_updates_completions_dynamically() -> None
```

Test that CommandCompleter with a callable updates entries when the callable returns different values.

This simulates config reload where available skills change.

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L167`](tests/autocompletion/test_slash_command_controller.py#L167)

## `test_callable_entries_reflects_enabled_disabled_skills()`

```python
def test_callable_entries_reflects_enabled_disabled_skills() -> None
```

Test that skill enable/disable changes are reflected in completions.

This simulates the scenario where a user changes enabled_skills in config
and runs /reload.

**Source:** [`tests/autocompletion/test_slash_command_controller.py#L202`](tests/autocompletion/test_slash_command_controller.py#L202)

