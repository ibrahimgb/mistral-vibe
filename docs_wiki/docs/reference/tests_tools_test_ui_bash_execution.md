---
title: "tests.tools.test_ui_bash_execution"
tldr: "Module tests.tools.test_ui_bash_execution"
tags: [reference, api]
---

# `tests.tools.test_ui_bash_execution`

**Source:** [`tests/tools/test_ui_bash_execution.py`](tests/tools/test_ui_bash_execution.py) · 120 lines

## `_wait_for_bash_output_message()`

```python
async def _wait_for_bash_output_message(vibe_app: VibeApp, pilot, timeout: float) -> BashOutputMessage
```

**Source:** [`tests/tools/test_ui_bash_execution.py#L13`](tests/tools/test_ui_bash_execution.py#L13)

## `assert_no_command_error()`

```python
def assert_no_command_error(vibe_app: VibeApp) -> None
```

**Source:** [`tests/tools/test_ui_bash_execution.py#L24`](tests/tools/test_ui_bash_execution.py#L24)

## `test_ui_reports_no_output()`

```python
async def test_ui_reports_no_output(vibe_app: VibeApp) -> None
```

**Source:** [`tests/tools/test_ui_bash_execution.py#L44`](tests/tools/test_ui_bash_execution.py#L44)

## `test_ui_shows_success_in_case_of_zero_code()`

```python
async def test_ui_shows_success_in_case_of_zero_code(vibe_app: VibeApp) -> None
```

**Source:** [`tests/tools/test_ui_bash_execution.py#L57`](tests/tools/test_ui_bash_execution.py#L57)

## `test_ui_shows_failure_in_case_of_non_zero_code()`

```python
async def test_ui_shows_failure_in_case_of_non_zero_code(vibe_app: VibeApp) -> None
```

**Source:** [`tests/tools/test_ui_bash_execution.py#L69`](tests/tools/test_ui_bash_execution.py#L69)

## `test_ui_handles_non_utf8_output()`

```python
async def test_ui_handles_non_utf8_output(vibe_app: VibeApp) -> None
```

Assert the UI accepts decoding a non-UTF8 sequence like `printf 'ð'`.
Whereas `printf 'ð'` prints a smiley face (😋) and would work even without those changes.

**Source:** [`tests/tools/test_ui_bash_execution.py#L81`](tests/tools/test_ui_bash_execution.py#L81)

## `test_ui_handles_utf8_output()`

```python
async def test_ui_handles_utf8_output(vibe_app: VibeApp) -> None
```

**Source:** [`tests/tools/test_ui_bash_execution.py#L98`](tests/tools/test_ui_bash_execution.py#L98)

## `test_ui_handles_non_utf8_stderr()`

```python
async def test_ui_handles_non_utf8_stderr(vibe_app: VibeApp) -> None
```

**Source:** [`tests/tools/test_ui_bash_execution.py#L111`](tests/tools/test_ui_bash_execution.py#L111)

