---
title: "tests.test_ui_external_editor"
tldr: "Tests for the external editor UI integration (Ctrl+G keybind)."
tags: [reference, api]
---

# `tests.test_ui_external_editor`

**Source:** [`tests/test_ui_external_editor.py`](tests/test_ui_external_editor.py) · 69 lines

Tests for the external editor UI integration (Ctrl+G keybind).

## `mock_suspend()`

```python
def mock_suspend()
```

Mock context manager to replace app.suspend().

**Source:** [`tests/test_ui_external_editor.py#L15`](tests/test_ui_external_editor.py#L15)

## `test_ctrl_g_opens_external_editor_and_updates_input()`

```python
async def test_ctrl_g_opens_external_editor_and_updates_input(vibe_app: VibeApp) -> None
```

Test that Ctrl+G triggers external editor and updates input with result.

**Source:** [`tests/test_ui_external_editor.py#L21`](tests/test_ui_external_editor.py#L21)

## `test_ctrl_g_works_with_empty_input()`

```python
async def test_ctrl_g_works_with_empty_input(vibe_app: VibeApp) -> None
```

Test that Ctrl+G works when input is empty.

**Source:** [`tests/test_ui_external_editor.py#L48`](tests/test_ui_external_editor.py#L48)

