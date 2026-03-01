---
title: "tests.test_ui_input_history"
tldr: "Module tests.test_ui_input_history"
tags: [reference, api]
---

# `tests.test_ui_input_history`

**Source:** [`tests/test_ui_input_history.py`](tests/test_ui_input_history.py) · 119 lines

## `history_file()`

```python
def history_file(tmp_path: Path) -> Path
```

**Source:** [`tests/test_ui_input_history.py#L15`](tests/test_ui_input_history.py#L15)

## `inject_history_file()`

```python
def inject_history_file(vibe_app: VibeApp, history_file: Path) -> None
```

**Source:** [`tests/test_ui_input_history.py#L25`](tests/test_ui_input_history.py#L25)

## `test_ui_navigation_through_input_history()`

```python
async def test_ui_navigation_through_input_history(vibe_app: VibeApp, history_file: Path) -> None
```

**Source:** [`tests/test_ui_input_history.py#L32`](tests/test_ui_input_history.py#L32)

## `test_ui_does_nothing_if_command_completion_is_active()`

```python
async def test_ui_does_nothing_if_command_completion_is_active(vibe_app: VibeApp, history_file: Path) -> None
```

**Source:** [`tests/test_ui_input_history.py#L57`](tests/test_ui_input_history.py#L57)

## `test_ui_does_not_prevent_arrow_down_to_move_cursor_to_bottom_lines()`

```python
async def test_ui_does_not_prevent_arrow_down_to_move_cursor_to_bottom_lines(vibe_app: VibeApp)
```

**Source:** [`tests/test_ui_input_history.py#L73`](tests/test_ui_input_history.py#L73)

## `test_ui_resumes_arrow_down_after_manual_move()`

```python
async def test_ui_resumes_arrow_down_after_manual_move(vibe_app: VibeApp, tmp_path: Path) -> None
```

**Source:** [`tests/test_ui_input_history.py#L99`](tests/test_ui_input_history.py#L99)

