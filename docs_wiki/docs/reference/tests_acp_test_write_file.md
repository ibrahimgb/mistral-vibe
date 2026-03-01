---
title: "tests.acp.test_write_file"
tldr: "Module tests.acp.test_write_file"
tags: [reference, api]
---

# `tests.acp.test_write_file`

**Source:** [`tests/acp/test_write_file.py`](tests/acp/test_write_file.py) · 277 lines

## `MockClient`

**Source:** [`tests/acp/test_write_file.py#L18`](tests/acp/test_write_file.py#L18)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | write_error, file_exists | `None` | — |
| 🔄 `write_text_file()` | content, path, session_id | `None` | — |
| 🔄 `session_update()` | session_id, update | `None` | — |

## `TestAcpWriteFileBasic`

**Source:** [`tests/acp/test_write_file.py#L64`](tests/acp/test_write_file.py#L64)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_get_name()` |  | `None` | — |

## `TestAcpWriteFileExecution`

**Source:** [`tests/acp/test_write_file.py#L69`](tests/acp/test_write_file.py#L69)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_run_success_new_file()` | acp_write_file_tool, mock_client, tmp_path | `None` | — |
| 🔄 `test_run_success_overwrite()` | mock_client, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_run_write_error()` | mock_client, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_run_without_connection()` | tmp_path, monkeypatch | `None` | — |
| 🔄 `test_run_without_session_id()` | tmp_path, monkeypatch | `None` | — |

## `TestAcpWriteFileSessionUpdates`

**Source:** [`tests/acp/test_write_file.py#L190`](tests/acp/test_write_file.py#L190)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_tool_call_session_update()` |  | `None` | — |
| `test_tool_call_session_update_invalid_args()` |  | `None` | — |
| `test_tool_result_session_update()` |  | `None` | — |
| `test_tool_result_session_update_invalid_result()` |  | `None` | — |

## `mock_client()`

```python
def mock_client() -> MockClient
```

**Source:** [`tests/acp/test_write_file.py#L46`](tests/acp/test_write_file.py#L46)

## `acp_write_file_tool()`

```python
def acp_write_file_tool(mock_client: MockClient, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> WriteFile
```

**Source:** [`tests/acp/test_write_file.py#L51`](tests/acp/test_write_file.py#L51)

