---
title: "tests.stubs.fake_client"
tldr: "Module tests.stubs.fake_client"
tags: [reference, api]
---

# `tests.stubs.fake_client`

**Source:** [`tests/stubs/fake_client.py`](tests/stubs/fake_client.py) · 134 lines

## `FakeClient`

**Bases:** `Client`

**Source:** [`tests/stubs/fake_client.py#L36`](tests/stubs/fake_client.py#L36)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `None` | — |
| 🔄 `session_update()` | session_id, update | `None` | — |
| 🔄 `request_permission()` | options, session_id, tool_call | `RequestPermissionResponse` | — |
| 🔄 `read_text_file()` | path, session_id, limit, line | `ReadTextFileResponse` | — |
| 🔄 `write_text_file()` | content, path, session_id | `WriteTextFileResponse | None` | — |
| 🔄 `create_terminal()` | command, session_id, args, cwd, env, output_byte_limit | `CreateTerminalResponse` | — |
| 🔄 `terminal_output()` | session_id, terminal_id | `TerminalOutputResponse` | — |
| 🔄 `release_terminal()` | session_id, terminal_id | `ReleaseTerminalResponse | None` | — |
| 🔄 `wait_for_terminal_exit()` | session_id, terminal_id | `WaitForTerminalExitResponse` | — |
| 🔄 `kill_terminal()` | session_id, terminal_id | `KillTerminalCommandResponse | None` | — |
| 🔄 `ext_method()` | method, params | `dict[str, Any]` | — |
| 🔄 `ext_notification()` | method, params | `None` | — |
| 🔄 `close()` |  | `None` | — |
| `on_connect()` | conn | `None` | — |
| 🔄 `__aenter__()` |  | `FakeClient` | — |
| 🔄 `__aexit__()` | exc_type, exc, tb | `None` | — |

