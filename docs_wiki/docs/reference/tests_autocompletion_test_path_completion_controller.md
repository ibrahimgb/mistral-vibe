---
title: "tests.autocompletion.test_path_completion_controller"
tldr: "Module tests.autocompletion.test_path_completion_controller"
tags: [reference, api]
---

# `tests.autocompletion.test_path_completion_controller`

**Source:** [`tests/autocompletion/test_path_completion_controller.py`](tests/autocompletion/test_path_completion_controller.py) · 258 lines

## `StubView`

**Bases:** `CompletionView`

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L13`](tests/autocompletion/test_path_completion_controller.py#L13)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `None` | — |
| `render_completion_suggestions()` | suggestions, selected_index | `None` | — |
| `clear_completion_suggestions()` |  | `None` | — |
| `replace_completion_range()` | start, end, replacement | `None` | — |

## `file_tree()`

```python
def file_tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L32`](tests/autocompletion/test_path_completion_controller.py#L32)

## `make_controller()`

```python
def make_controller(max_entries_to_process: int | None, target_matches: int | None) -> tuple[PathCompletionController, StubView]
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L48`](tests/autocompletion/test_path_completion_controller.py#L48)

## `test_lists_root_entries()`

```python
def test_lists_root_entries(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L63`](tests/autocompletion/test_path_completion_controller.py#L63)

## `test_suggests_hidden_entries_only_with_dot_prefix()`

```python
def test_suggests_hidden_entries_only_with_dot_prefix(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L73`](tests/autocompletion/test_path_completion_controller.py#L73)

## `test_lists_nested_entries_when_prefixing_with_folder_name()`

```python
def test_lists_nested_entries_when_prefixing_with_folder_name(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L82`](tests/autocompletion/test_path_completion_controller.py#L82)

## `test_resets_when_fragment_invalid()`

```python
def test_resets_when_fragment_invalid(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L95`](tests/autocompletion/test_path_completion_controller.py#L95)

## `test_applies_selected_completion_on_tab_keycode()`

```python
def test_applies_selected_completion_on_tab_keycode(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L109`](tests/autocompletion/test_path_completion_controller.py#L109)

## `test_applies_selected_completion_on_enter_keycode()`

```python
def test_applies_selected_completion_on_enter_keycode(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L120`](tests/autocompletion/test_path_completion_controller.py#L120)

## `test_navigates_and_cycles_across_suggestions()`

```python
def test_navigates_and_cycles_across_suggestions(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L132`](tests/autocompletion/test_path_completion_controller.py#L132)

## `test_limits_suggestions_to_ten()`

```python
def test_limits_suggestions_to_ten(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L158`](tests/autocompletion/test_path_completion_controller.py#L158)

## `test_does_not_handle_when_cursor_at_beginning_of_input()`

```python
def test_does_not_handle_when_cursor_at_beginning_of_input(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L186`](tests/autocompletion/test_path_completion_controller.py#L186)

## `test_does_not_handle_when_cursor_before_or_at_the_at_symbol()`

```python
def test_does_not_handle_when_cursor_before_or_at_the_at_symbol(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L194`](tests/autocompletion/test_path_completion_controller.py#L194)

## `test_does_handle_when_cursor_after_the_at_symbol_even_in_the_middle_of_the_input()`

```python
def test_does_handle_when_cursor_after_the_at_symbol_even_in_the_middle_of_the_input(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L203`](tests/autocompletion/test_path_completion_controller.py#L203)

## `test_lists_immediate_children_when_path_ends_with_slash()`

```python
def test_lists_immediate_children_when_path_ends_with_slash(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L212`](tests/autocompletion/test_path_completion_controller.py#L212)

## `test_respects_max_entries_to_process_limit()`

```python
def test_respects_max_entries_to_process_limit(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L225`](tests/autocompletion/test_path_completion_controller.py#L225)

## `test_respects_target_matches_limit_for_listing()`

```python
def test_respects_target_matches_limit_for_listing(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L237`](tests/autocompletion/test_path_completion_controller.py#L237)

## `test_respects_target_matches_limit_for_fuzzy_search()`

```python
def test_respects_target_matches_limit_for_fuzzy_search(file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_path_completion_controller.py#L249`](tests/autocompletion/test_path_completion_controller.py#L249)

