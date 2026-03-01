---
title: "tests.autocompletion.test_ui_chat_autocompletion"
tldr: "Module tests.autocompletion.test_ui_chat_autocompletion"
tags: [reference, api]
---

# `tests.autocompletion.test_ui_chat_autocompletion`

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py`](tests/autocompletion/test_ui_chat_autocompletion.py) · 306 lines

## `test_popup_appears_with_matching_suggestions()`

```python
async def test_popup_appears_with_matching_suggestions(vibe_app: VibeApp) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L16`](tests/autocompletion/test_ui_chat_autocompletion.py#L16)

## `test_popup_hides_when_input_cleared()`

```python
async def test_popup_hides_when_input_cleared(vibe_app: VibeApp) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L31`](tests/autocompletion/test_ui_chat_autocompletion.py#L31)

## `test_pressing_tab_writes_selected_command_and_keeps_popup_visible()`

```python
async def test_pressing_tab_writes_selected_command_and_keeps_popup_visible(vibe_app: VibeApp) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L42`](tests/autocompletion/test_ui_chat_autocompletion.py#L42)

## `ensure_selected_command()`

```python
def ensure_selected_command(popup: CompletionPopup, expected_alias: str) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L56`](tests/autocompletion/test_ui_chat_autocompletion.py#L56)

## `test_arrow_navigation_updates_selected_suggestion()`

```python
async def test_arrow_navigation_updates_selected_suggestion(vibe_app: VibeApp) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L74`](tests/autocompletion/test_ui_chat_autocompletion.py#L74)

## `test_arrow_navigation_cycles_through_suggestions()`

```python
async def test_arrow_navigation_cycles_through_suggestions(vibe_app: VibeApp) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L88`](tests/autocompletion/test_ui_chat_autocompletion.py#L88)

## `test_pressing_enter_submits_selected_command_and_hides_popup()`

```python
async def test_pressing_enter_submits_selected_command_and_hides_popup(vibe_app: VibeApp, telemetry_events: list[dict]) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L102`](tests/autocompletion/test_ui_chat_autocompletion.py#L102)

## `file_tree()`

```python
def file_tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L131`](tests/autocompletion/test_ui_chat_autocompletion.py#L131)

## `test_path_completion_popup_lists_files_and_directories()`

```python
async def test_path_completion_popup_lists_files_and_directories(vibe_app: VibeApp, file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L150`](tests/autocompletion/test_ui_chat_autocompletion.py#L150)

## `test_path_completion_popup_shows_up_to_ten_results()`

```python
async def test_path_completion_popup_shows_up_to_ten_results(vibe_app: VibeApp, file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L164`](tests/autocompletion/test_ui_chat_autocompletion.py#L164)

## `test_pressing_tab_writes_selected_path_name_and_hides_popup()`

```python
async def test_pressing_tab_writes_selected_path_name_and_hides_popup(vibe_app: VibeApp, file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L194`](tests/autocompletion/test_ui_chat_autocompletion.py#L194)

## `test_pressing_enter_writes_selected_path_name_and_hides_popup()`

```python
async def test_pressing_enter_writes_selected_path_name_and_hides_popup(vibe_app: VibeApp, file_tree: Path) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L209`](tests/autocompletion/test_ui_chat_autocompletion.py#L209)

## `test_fuzzy_matches_subsequence_characters()`

```python
async def test_fuzzy_matches_subsequence_characters(file_tree: Path, vibe_app: VibeApp) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L224`](tests/autocompletion/test_ui_chat_autocompletion.py#L224)

## `test_fuzzy_matches_word_boundaries()`

```python
async def test_fuzzy_matches_word_boundaries(file_tree: Path, vibe_app: VibeApp) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L238`](tests/autocompletion/test_ui_chat_autocompletion.py#L238)

## `test_finds_files_recursively_by_filename()`

```python
async def test_finds_files_recursively_by_filename(file_tree: Path, vibe_app: VibeApp) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L252`](tests/autocompletion/test_ui_chat_autocompletion.py#L252)

## `test_finds_files_recursively_with_partial_path()`

```python
async def test_finds_files_recursively_with_partial_path(file_tree: Path, vibe_app: VibeApp) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L266`](tests/autocompletion/test_ui_chat_autocompletion.py#L266)

## `test_does_not_trigger_completion_when_navigating_history()`

```python
async def test_does_not_trigger_completion_when_navigating_history(file_tree: Path, vibe_app: VibeApp) -> None
```

**Source:** [`tests/autocompletion/test_ui_chat_autocompletion.py#L280`](tests/autocompletion/test_ui_chat_autocompletion.py#L280)

