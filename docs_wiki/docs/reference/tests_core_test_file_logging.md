---
title: "tests.core.test_file_logging"
tldr: "Module tests.core.test_file_logging"
tags: [reference, api]
---

# `tests.core.test_file_logging`

**Source:** [`tests/core/test_file_logging.py`](tests/core/test_file_logging.py) · 280 lines

## `TestStructuredFormatter`

**Source:** [`tests/core/test_file_logging.py#L28`](tests/core/test_file_logging.py#L28)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_format_contains_required_fields()` |  | `None` | — |
| `test_format_includes_exception()` |  | `None` | — |
| `test_format_escapes_newlines_in_message()` |  | `None` | — |
| `test_format_escapes_newlines_in_exception()` |  | `None` | — |
| `test_format_output_is_single_line()` |  | `None` | — |

## `TestApplyLoggingConfig`

**Source:** [`tests/core/test_file_logging.py#L156`](tests/core/test_file_logging.py#L156)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_adds_handler_to_logger()` | mock_log_dir, monkeypatch | `None` | — |
| `test_creates_log_file()` | mock_log_dir, monkeypatch | `None` | — |
| `test_log_entry_format()` | mock_log_dir, monkeypatch | `None` | — |
| `test_respects_log_level()` | mock_log_dir, monkeypatch | `None` | — |
| `test_creates_log_directory_if_missing()` | tmp_path, monkeypatch | `None` | — |
| `test_debug_mode_overrides_log_level()` | mock_log_dir, monkeypatch | `None` | — |
| `test_invalid_log_level_defaults_to_warning()` | mock_log_dir, monkeypatch | `None` | — |
| `test_log_max_bytes_from_env()` | mock_log_dir, monkeypatch | `None` | — |

## `mock_log_dir()`

```python
def mock_log_dir(tmp_path: Path)
```

Mock LOG_DIR and LOG_FILE to use tmp_path for testing.

**Source:** [`tests/core/test_file_logging.py#L15`](tests/core/test_file_logging.py#L15)

