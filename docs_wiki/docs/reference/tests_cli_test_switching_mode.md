---
title: "tests.cli.test_switching_mode"
tldr: "Module tests.cli.test_switching_mode"
tags: [reference, api]
---

# `tests.cli.test_switching_mode`

**Source:** [`tests/cli/test_switching_mode.py`](tests/cli/test_switching_mode.py) · 109 lines

## `test_submit_ignored_while_switching_mode()`

```python
async def test_submit_ignored_while_switching_mode() -> None
```

Enter press during mode switch must not clear input or send a message.

**Source:** [`tests/cli/test_switching_mode.py#L12`](tests/cli/test_switching_mode.py#L12)

## `test_submit_works_after_switching_mode_ends()`

```python
async def test_submit_works_after_switching_mode_ends() -> None
```

After switching_mode is set back to False, Enter should work normally.

**Source:** [`tests/cli/test_switching_mode.py#L34`](tests/cli/test_switching_mode.py#L34)

## `test_spinner_shown_while_switching_mode()`

```python
async def test_spinner_shown_while_switching_mode() -> None
```

Prompt widget is hidden and spinner is mounted when switching_mode is True.

**Source:** [`tests/cli/test_switching_mode.py#L57`](tests/cli/test_switching_mode.py#L57)

## `test_spinner_removed_after_switching_mode_ends()`

```python
async def test_spinner_removed_after_switching_mode_ends() -> None
```

Prompt is restored and spinner removed when switching_mode becomes False.

**Source:** [`tests/cli/test_switching_mode.py#L77`](tests/cli/test_switching_mode.py#L77)

## `test_rapid_switching_mode_no_duplicate_spinners()`

```python
async def test_rapid_switching_mode_no_duplicate_spinners() -> None
```

Rapidly toggling switching_mode must never produce duplicate spinners.

**Source:** [`tests/cli/test_switching_mode.py#L95`](tests/cli/test_switching_mode.py#L95)

