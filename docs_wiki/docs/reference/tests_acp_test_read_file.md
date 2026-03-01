---
title: "tests.acp.test_read_file"
tldr: "Module tests.acp.test_read_file"
tags: [reference, api]
---

# `tests.acp.test_read_file`

**Source:** [`tests/acp/test_read_file.py`](tests/acp/test_read_file.py) · 247 lines

## `MockClient`

**Source:** [`tests/acp/test_read_file.py#L18`](tests/acp/test_read_file.py#L18)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | file_content, read_error | `None` | — |
| 🔄 `read_text_file()` | path, session_id, limit, line | `ReadTextFileResponse` | — |
| 🔄 `session_update()` | session_id, update | `None` | — |

## `TestAcpReadFileBasic`

**Source:** [`tests/acp/test_read_file.py#L82`](tests/acp/test_read_file.py#L82)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_get_name()` |  | `None` | — |

## `TestAcpReadFileExecution`

**Source:** [`tests/acp/test_read_file.py#L87`](tests/acp/test_read_file.py#L87)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_run_success()` | acp_read_file_tool, mock_client, tmp_path | `None` | — |
| 🔄 `test_run_with_offset()` | mock_client, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_run_with_limit()` | mock_client, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_run_with_offset_and_limit()` | mock_client, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_run_read_error()` | mock_client, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_run_without_connection()` | tmp_path, monkeypatch | `None` | — |
| 🔄 `test_run_without_session_id()` | tmp_path, monkeypatch | `None` | — |

## `mock_client()`

```python
def mock_client() -> MockClient
```

**Source:** [`tests/acp/test_read_file.py#L64`](tests/acp/test_read_file.py#L64)

## `acp_read_file_tool()`

```python
def acp_read_file_tool(mock_client: MockClient, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> ReadFile
```

**Source:** [`tests/acp/test_read_file.py#L69`](tests/acp/test_read_file.py#L69)

