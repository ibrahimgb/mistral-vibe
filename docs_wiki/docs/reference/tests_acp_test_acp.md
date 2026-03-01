---
title: "tests.acp.test_acp"
tldr: "Module tests.acp.test_acp"
tags: [reference, api]
---

# `tests.acp.test_acp`

**Source:** [`tests/acp/test_acp.py`](tests/acp/test_acp.py) · 965 lines

## Constants

- `RESPONSE_TIMEOUT`
- `MOCK_ENTRYPOINT_PATH`
- `PLAYGROUND_DIR`

## `JsonRpcRequest`

*✅ Pydantic*

**Bases:** `BaseModel`

**Source:** [`tests/acp/test_acp.py#L104`](tests/acp/test_acp.py#L104)

## `JsonRpcError`

*✅ Pydantic*

**Bases:** `BaseModel`

**Source:** [`tests/acp/test_acp.py#L111`](tests/acp/test_acp.py#L111)

## `JsonRpcResponse`

*✅ Pydantic*

**Bases:** `BaseModel`

**Source:** [`tests/acp/test_acp.py#L117`](tests/acp/test_acp.py#L117)

## `JsonRpcNotification`

*✅ Pydantic*

**Bases:** `BaseModel`

**Source:** [`tests/acp/test_acp.py#L124`](tests/acp/test_acp.py#L124)

## `InitializeJsonRpcRequest`

**Bases:** `JsonRpcRequest`

**Source:** [`tests/acp/test_acp.py#L133`](tests/acp/test_acp.py#L133)

## `InitializeJsonRpcResponse`

**Bases:** `JsonRpcResponse`

**Source:** [`tests/acp/test_acp.py#L138`](tests/acp/test_acp.py#L138)

## `NewSessionJsonRpcRequest`

**Bases:** `JsonRpcRequest`

**Source:** [`tests/acp/test_acp.py#L142`](tests/acp/test_acp.py#L142)

## `NewSessionJsonRpcResponse`

**Bases:** `JsonRpcResponse`

**Source:** [`tests/acp/test_acp.py#L147`](tests/acp/test_acp.py#L147)

## `PromptJsonRpcRequest`

**Bases:** `JsonRpcRequest`

**Source:** [`tests/acp/test_acp.py#L151`](tests/acp/test_acp.py#L151)

## `PromptJsonRpcResponse`

**Bases:** `JsonRpcResponse`

**Source:** [`tests/acp/test_acp.py#L156`](tests/acp/test_acp.py#L156)

## `UpdateJsonRpcNotification`

**Bases:** `JsonRpcNotification`

**Source:** [`tests/acp/test_acp.py#L160`](tests/acp/test_acp.py#L160)

## `RequestPermissionJsonRpcRequest`

**Bases:** `JsonRpcRequest`

**Source:** [`tests/acp/test_acp.py#L165`](tests/acp/test_acp.py#L165)

## `RequestPermissionJsonRpcResponse`

**Bases:** `JsonRpcResponse`

**Source:** [`tests/acp/test_acp.py#L170`](tests/acp/test_acp.py#L170)

## `ReadTextFileJsonRpcRequest`

**Bases:** `JsonRpcRequest`

**Source:** [`tests/acp/test_acp.py#L174`](tests/acp/test_acp.py#L174)

## `ReadTextFileJsonRpcResponse`

**Bases:** `JsonRpcResponse`

**Source:** [`tests/acp/test_acp.py#L179`](tests/acp/test_acp.py#L179)

## `WriteTextFileJsonRpcRequest`

**Bases:** `JsonRpcRequest`

**Source:** [`tests/acp/test_acp.py#L183`](tests/acp/test_acp.py#L183)

## `WriteTextFileJsonRpcResponse`

**Bases:** `JsonRpcResponse`

**Source:** [`tests/acp/test_acp.py#L188`](tests/acp/test_acp.py#L188)

## `TestSessionManagement`

**Source:** [`tests/acp/test_acp.py#L387`](tests/acp/test_acp.py#L387)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_multiple_sessions_unique_ids()` | vibe_home_dir | `None` | — |

## `TestSessionUpdates`

**Source:** [`tests/acp/test_acp.py#L426`](tests/acp/test_acp.py#L426)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_agent_loop_message_chunk_structure()` | vibe_home_dir | `None` | — |
| 🔄 `test_tool_call_update_structure()` | vibe_home_dir | `None` | — |

## `TestToolCallStructure`

**Source:** [`tests/acp/test_acp.py#L581`](tests/acp/test_acp.py#L581)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_tool_call_request_permission_structure()` | vibe_home_grep_ask | `None` | — |
| 🔄 `test_tool_call_update_approved_structure()` | vibe_home_grep_ask | `None` | — |
| 🔄 `test_tool_call_update_rejected_structure()` | vibe_home_grep_ask | `None` | — |
| 🔄 `test_tool_call_in_progress_update_structure()` | vibe_home_grep_ask | `None` | — |
| 🔄 `test_tool_call_result_update_failure_structure()` | vibe_home_grep_ask | `None` | — |

## `TestCancellationStructure`

**Source:** [`tests/acp/test_acp.py#L884`](tests/acp/test_acp.py#L884)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_tool_call_update_cancelled_structure()` | vibe_home_dir | `None` | — |

## `deep_merge()`

```python
def deep_merge(target: dict, source: dict) -> None
```

**Source:** [`tests/acp/test_acp.py#L44`](tests/acp/test_acp.py#L44)

## `_create_vibe_home_dir()`

```python
def _create_vibe_home_dir(tmp_path: Path) -> Path
```

Create a temporary vibe home directory with a minimal config file.

**Source:** [`tests/acp/test_acp.py#L65`](tests/acp/test_acp.py#L65)

## `vibe_home_dir()`

```python
def vibe_home_dir(tmp_path: Path) -> Path
```

Create a temporary vibe home directory with a minimal config file.

**Source:** [`tests/acp/test_acp.py#L93`](tests/acp/test_acp.py#L93)

## `vibe_home_grep_ask()`

```python
def vibe_home_grep_ask(tmp_path: Path) -> Path
```

Create a temporary vibe home directory with grep configured to ask permission.

**Source:** [`tests/acp/test_acp.py#L99`](tests/acp/test_acp.py#L99)

## `get_acp_agent_loop_process()`

```python
async def get_acp_agent_loop_process(mock_env: dict[str, str], vibe_home: Path) -> AsyncGenerator[asyncio.subprocess.Process]
```

**Source:** [`tests/acp/test_acp.py#L192`](tests/acp/test_acp.py#L192)

## `send_json_rpc()`

```python
async def send_json_rpc(process: asyncio.subprocess.Process, message: JsonRpcMessage) -> None
```

**Source:** [`tests/acp/test_acp.py#L225`](tests/acp/test_acp.py#L225)

## `read_response()`

```python
async def read_response(process: asyncio.subprocess.Process, timeout: float) -> str | None
```

**Source:** [`tests/acp/test_acp.py#L237`](tests/acp/test_acp.py#L237)

## `read_response_for_id()`

```python
async def read_response_for_id(process: asyncio.subprocess.Process, expected_id: int | str, timeout: float) -> str | None
```

**Source:** [`tests/acp/test_acp.py#L265`](tests/acp/test_acp.py#L265)

## `read_multiple_responses()`

```python
async def read_multiple_responses(process: asyncio.subprocess.Process, max_count: int, timeout_per_response: float) -> list[str]
```

**Source:** [`tests/acp/test_acp.py#L288`](tests/acp/test_acp.py#L288)

## `parse_conversation()`

```python
def parse_conversation(message_texts: list[str]) -> list[JsonRpcMessage]
```

**Source:** [`tests/acp/test_acp.py#L303`](tests/acp/test_acp.py#L303)

## `initialize_session()`

```python
async def initialize_session(acp_agent_loop_process: asyncio.subprocess.Process) -> str
```

**Source:** [`tests/acp/test_acp.py#L361`](tests/acp/test_acp.py#L361)

## `start_session_with_request_permission()`

```python
async def start_session_with_request_permission(process: asyncio.subprocess.Process, prompt: str) -> RequestPermissionJsonRpcRequest
```

**Source:** [`tests/acp/test_acp.py#L554`](tests/acp/test_acp.py#L554)

