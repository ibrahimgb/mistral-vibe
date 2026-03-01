---
title: "tests.cli.test_clipboard"
tldr: "Module tests.cli.test_clipboard"
tags: [reference, api]
---

# `tests.cli.test_clipboard`

**Source:** [`tests/cli/test_clipboard.py`](tests/cli/test_clipboard.py) · 325 lines

## `MockWidget`

**Source:** [`tests/cli/test_clipboard.py#L22`](tests/cli/test_clipboard.py#L22)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | text_selection, get_selection_result, get_selection_raises | `None` | — |
| `get_selection()` | selection | `tuple[str, object]` | — |

## `mock_app()`

```python
def mock_app() -> App
```

**Source:** [`tests/cli/test_clipboard.py#L42`](tests/cli/test_clipboard.py#L42)

## `test_copy_selection_to_clipboard_no_notification()`

```python
def test_copy_selection_to_clipboard_no_notification(mock_app: MagicMock, widgets: list[MockWidget], description: str) -> None
```

**Source:** [`tests/cli/test_clipboard.py#L78`](tests/cli/test_clipboard.py#L78)

## `test_copy_selection_to_clipboard_success()`

```python
def test_copy_selection_to_clipboard_success(mock_copy_to_clipboard: MagicMock, mock_app: MagicMock) -> None
```

**Source:** [`tests/cli/test_clipboard.py#L91`](tests/cli/test_clipboard.py#L91)

## `test_copy_selection_to_clipboard_shows_failure_when_all_strategies_raise()`

```python
def test_copy_selection_to_clipboard_shows_failure_when_all_strategies_raise(mock_copy_to_clipboard: MagicMock, mock_app: MagicMock) -> None
```

When _copy_to_clipboard raises (all strategies failed), user sees 'Failed to copy' toast.

**Source:** [`tests/cli/test_clipboard.py#L112`](tests/cli/test_clipboard.py#L112)

## `test_copy_selection_to_clipboard_multiple_widgets()`

```python
def test_copy_selection_to_clipboard_multiple_widgets(mock_app: MagicMock) -> None
```

**Source:** [`tests/cli/test_clipboard.py#L131`](tests/cli/test_clipboard.py#L131)

## `test_copy_selection_to_clipboard_preview_shortening()`

```python
def test_copy_selection_to_clipboard_preview_shortening(mock_app: MagicMock) -> None
```

**Source:** [`tests/cli/test_clipboard.py#L157`](tests/cli/test_clipboard.py#L157)

## `test_copy_to_clipboard_stops_after_verified_copy()`

```python
def test_copy_to_clipboard_stops_after_verified_copy() -> None
```

Stops iterating once _read_clipboard confirms the text landed.

**Source:** [`tests/cli/test_clipboard.py#L176`](tests/cli/test_clipboard.py#L176)

## `test_copy_to_clipboard_tries_all_when_verify_fails()`

```python
def test_copy_to_clipboard_tries_all_when_verify_fails() -> None
```

Tries all strategies when _read_clipboard never confirms.

**Source:** [`tests/cli/test_clipboard.py#L191`](tests/cli/test_clipboard.py#L191)

## `test_copy_to_clipboard_raises_when_all_strategies_raise()`

```python
def test_copy_to_clipboard_raises_when_all_strategies_raise() -> None
```

RuntimeError is raised when every strategy fails.

**Source:** [`tests/cli/test_clipboard.py#L206`](tests/cli/test_clipboard.py#L206)

## `test_read_clipboard_returns_first_successful_reader()`

```python
def test_read_clipboard_returns_first_successful_reader() -> None
```

**Source:** [`tests/cli/test_clipboard.py#L218`](tests/cli/test_clipboard.py#L218)

## `test_read_clipboard_falls_through_on_failure()`

```python
def test_read_clipboard_falls_through_on_failure() -> None
```

**Source:** [`tests/cli/test_clipboard.py#L229`](tests/cli/test_clipboard.py#L229)

## `test_read_clipboard_skips_failing_reader()`

```python
def test_read_clipboard_skips_failing_reader() -> None
```

**Source:** [`tests/cli/test_clipboard.py#L235`](tests/cli/test_clipboard.py#L235)

## `test_copy_pbcopy()`

```python
def test_copy_pbcopy(mock_run: MagicMock) -> None
```

**Source:** [`tests/cli/test_clipboard.py#L244`](tests/cli/test_clipboard.py#L244)

## `test_copy_xclip()`

```python
def test_copy_xclip(mock_run: MagicMock) -> None
```

**Source:** [`tests/cli/test_clipboard.py#L250`](tests/cli/test_clipboard.py#L250)

## `test_copy_wl_copy()`

```python
def test_copy_wl_copy(mock_run: MagicMock) -> None
```

**Source:** [`tests/cli/test_clipboard.py#L258`](tests/cli/test_clipboard.py#L258)

## `test_copy_methods_includes_available_commands()`

```python
def test_copy_methods_includes_available_commands() -> None
```

_COPY_METHODS is built at import time using _has_cmd; re-import with mocked shutil.which.

**Source:** [`tests/cli/test_clipboard.py#L263`](tests/cli/test_clipboard.py#L263)

## `test_copy_osc52_writes_correct_sequence()`

```python
def test_copy_osc52_writes_correct_sequence(mock_file: MagicMock, monkeypatch: pytest.MonkeyPatch) -> None
```

**Source:** [`tests/cli/test_clipboard.py#L282`](tests/cli/test_clipboard.py#L282)

## `test_copy_osc52_with_tmux()`

```python
def test_copy_osc52_with_tmux(mock_file: MagicMock, monkeypatch: pytest.MonkeyPatch) -> None
```

**Source:** [`tests/cli/test_clipboard.py#L299`](tests/cli/test_clipboard.py#L299)

## `test_copy_osc52_unicode()`

```python
def test_copy_osc52_unicode(mock_file: MagicMock, monkeypatch: pytest.MonkeyPatch) -> None
```

**Source:** [`tests/cli/test_clipboard.py#L314`](tests/cli/test_clipboard.py#L314)

