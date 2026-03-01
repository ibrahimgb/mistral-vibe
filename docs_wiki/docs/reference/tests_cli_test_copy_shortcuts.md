---
title: "tests.cli.test_copy_shortcuts"
tldr: "Module tests.cli.test_copy_shortcuts"
tags: [reference, api]
---

# `tests.cli.test_copy_shortcuts`

**Source:** [`tests/cli/test_copy_shortcuts.py`](tests/cli/test_copy_shortcuts.py) · 59 lines

## `test_ctrl_y_triggers_copy_selection()`

```python
async def test_ctrl_y_triggers_copy_selection() -> None
```

Test that ctrl+y keybinding triggers copy_selection_to_clipboard.

**Source:** [`tests/cli/test_copy_shortcuts.py#L11`](tests/cli/test_copy_shortcuts.py#L11)

## `test_ctrl_shift_c_triggers_copy_selection()`

```python
async def test_ctrl_shift_c_triggers_copy_selection() -> None
```

Test that ctrl+shift+c keybinding triggers copy_selection_to_clipboard.

**Source:** [`tests/cli/test_copy_shortcuts.py#L22`](tests/cli/test_copy_shortcuts.py#L22)

## `test_mouse_up_respects_autocopy_config_enabled()`

```python
async def test_mouse_up_respects_autocopy_config_enabled() -> None
```

Test that mouse up copies when autocopy_to_clipboard is True.

**Source:** [`tests/cli/test_copy_shortcuts.py#L33`](tests/cli/test_copy_shortcuts.py#L33)

## `test_mouse_up_respects_autocopy_config_disabled()`

```python
async def test_mouse_up_respects_autocopy_config_disabled() -> None
```

Test that mouse up does not copy when autocopy_to_clipboard is False.

**Source:** [`tests/cli/test_copy_shortcuts.py#L48`](tests/cli/test_copy_shortcuts.py#L48)

