---
title: "tests.acp.test_bash"
tldr: "Module tests.acp.test_bash"
tags: [reference, api]
---

# `tests.acp.test_bash`

**Source:** [`tests/acp/test_bash.py`](tests/acp/test_bash.py) · 495 lines

## `MockTerminalHandle`

**Source:** [`tests/acp/test_bash.py#L15`](tests/acp/test_bash.py#L15)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | terminal_id, exit_code, output, wait_delay | `None` | — |
| 🔄 `wait_for_exit()` |  | `WaitForTerminalExitResponse` | — |
| 🔄 `current_output()` |  | `TerminalOutputResponse` | — |
| 🔄 `kill()` |  | `None` | — |
| 🔄 `release()` |  | `None` | — |

## `MockClient`

**Source:** [`tests/acp/test_bash.py#L43`](tests/acp/test_bash.py#L43)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | terminal_handle | `None` | — |
| 🔄 `create_terminal()` | command, session_id, args, cwd, env, output_byte_limit | `CreateTerminalResponse` | — |
| 🔄 `terminal_output()` | session_id, terminal_id | `TerminalOutputResponse` | — |
| 🔄 `wait_for_terminal_exit()` | session_id, terminal_id | `WaitForTerminalExitResponse` | — |
| 🔄 `release_terminal()` | session_id, terminal_id | `None` | — |
| 🔄 `kill_terminal()` | session_id, terminal_id | `None` | — |
| 🔄 `session_update()` | session_id, update | `None` | — |

## `TestAcpBashBasic`

**Source:** [`tests/acp/test_bash.py#L115`](tests/acp/test_bash.py#L115)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_get_name()` |  | `None` | — |
| `test_get_summary_simple_command()` |  | `None` | — |
| `test_get_summary_with_timeout()` |  | `None` | — |

## `TestAcpBashExecution`

**Source:** [`tests/acp/test_bash.py#L130`](tests/acp/test_bash.py#L130)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_run_success()` | acp_bash_tool, mock_client | `None` | — |
| 🔄 `test_run_creates_terminal_with_env_vars()` | mock_client | `None` | — |
| 🔄 `test_run_with_nonzero_exit_code()` | mock_client | `None` | — |
| 🔄 `test_run_create_terminal_failure()` | mock_client | `None` | — |
| 🔄 `test_run_without_client()` |  | `None` | — |
| 🔄 `test_run_without_session_id()` |  | `None` | — |
| 🔄 `test_run_with_none_exit_code()` | mock_client | `None` | — |

## `TestAcpBashTimeout`

**Source:** [`tests/acp/test_bash.py#L270`](tests/acp/test_bash.py#L270)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_run_with_timeout_raises_error_and_kills()` | mock_client | `None` | — |
| 🔄 `test_run_timeout_handles_kill_failure()` | mock_client | `None` | — |

## `TestAcpBashEmbedding`

**Source:** [`tests/acp/test_bash.py#L327`](tests/acp/test_bash.py#L327)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_run_with_embedding()` | mock_client | `None` | — |
| 🔄 `test_run_embedding_without_tool_call_id()` | mock_client | `None` | — |
| 🔄 `test_run_embedding_handles_exception()` | mock_client | `None` | — |

## `TestAcpBashConfig`

**Source:** [`tests/acp/test_bash.py#L384`](tests/acp/test_bash.py#L384)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_run_uses_config_default_timeout()` | mock_client | `None` | — |

## `TestAcpBashCleanup`

**Source:** [`tests/acp/test_bash.py#L409`](tests/acp/test_bash.py#L409)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_run_releases_terminal_on_success()` | mock_client | `None` | — |
| 🔄 `test_run_releases_terminal_on_timeout()` | mock_client | `None` | — |
| 🔄 `test_run_handles_release_failure()` | mock_client | `None` | — |

## `mock_client()`

```python
def mock_client() -> MockClient
```

**Source:** [`tests/acp/test_bash.py#L99`](tests/acp/test_bash.py#L99)

## `acp_bash_tool()`

```python
def acp_bash_tool(mock_client: MockClient) -> Bash
```

**Source:** [`tests/acp/test_bash.py#L104`](tests/acp/test_bash.py#L104)

