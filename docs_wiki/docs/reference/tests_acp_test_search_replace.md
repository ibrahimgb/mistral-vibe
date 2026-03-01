---
title: "tests.acp.test_search_replace"
tldr: "Module tests.acp.test_search_replace"
tags: [reference, api]
---

# `tests.acp.test_search_replace`

**Source:** [`tests/acp/test_search_replace.py`](tests/acp/test_search_replace.py) · 354 lines

## `MockClient`

**Source:** [`tests/acp/test_search_replace.py#L19`](tests/acp/test_search_replace.py#L19)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | file_content, read_error, write_error | `None` | — |
| 🔄 `read_text_file()` | path, session_id, limit, line | `ReadTextFileResponse` | — |
| 🔄 `write_text_file()` | content, path, session_id | `None` | — |
| 🔄 `session_update()` | session_id, update | `None` | — |

## `TestAcpSearchReplaceBasic`

**Source:** [`tests/acp/test_search_replace.py#L91`](tests/acp/test_search_replace.py#L91)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_get_name()` |  | `None` | — |

## `TestAcpSearchReplaceExecution`

**Source:** [`tests/acp/test_search_replace.py#L96`](tests/acp/test_search_replace.py#L96)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_run_success()` | acp_search_replace_tool, mock_client, tmp_path | `None` | — |
| 🔄 `test_run_with_backup()` | mock_client, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_run_read_error()` | mock_client, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_run_write_error()` | mock_client, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_run_without_required_state()` | tmp_path, client, session_id, expected_error, monkeypatch | `None` | — |

## `TestAcpSearchReplaceSessionUpdates`

**Source:** [`tests/acp/test_search_replace.py#L262`](tests/acp/test_search_replace.py#L262)

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

**Source:** [`tests/acp/test_search_replace.py#L73`](tests/acp/test_search_replace.py#L73)

## `acp_search_replace_tool()`

```python
def acp_search_replace_tool(mock_client: MockClient, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> SearchReplace
```

**Source:** [`tests/acp/test_search_replace.py#L78`](tests/acp/test_search_replace.py#L78)

