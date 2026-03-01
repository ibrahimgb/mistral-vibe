---
title: "tests.tools.test_mcp"
tldr: "Module tests.tools.test_mcp"
tags: [reference, api]
---

# `tests.tools.test_mcp`

**Source:** [`tests/tools/test_mcp.py`](tests/tools/test_mcp.py) · 553 lines

## `TestRemoteTool`

**Source:** [`tests/tools/test_mcp.py#L25`](tests/tools/test_mcp.py#L25)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_creates_remote_tool_with_valid_data()` |  | `—` | — |
| `test_uses_default_schema_when_none_provided()` |  | `—` | — |
| `test_rejects_empty_name()` |  | `—` | — |
| `test_rejects_whitespace_only_name()` |  | `—` | — |
| `test_normalizes_schema_from_object_with_model_dump()` |  | `—` | — |
| `test_rejects_invalid_input_schema()` |  | `—` | — |

## `TestMCPToolResult`

**Source:** [`tests/tools/test_mcp.py#L69`](tests/tools/test_mcp.py#L69)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_creates_result_with_text()` |  | `—` | — |
| `test_creates_result_with_structured_content()` |  | `—` | — |

## `TestParseCallResult`

**Source:** [`tests/tools/test_mcp.py#L88`](tests/tools/test_mcp.py#L88)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_parses_text_content()` |  | `—` | — |
| `test_parses_structured_content()` |  | `—` | — |
| `test_prefers_structured_over_text()` |  | `—` | — |
| `test_joins_multiple_text_blocks()` |  | `—` | — |

## `TestMCPStderrCapture`

Tests for _mcp_stderr_capture and _stderr_logger_thread.

**Source:** [`tests/tools/test_mcp.py#L131`](tests/tools/test_mcp.py#L131)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_mcp_stderr_capture_returns_writable_stream()` |  | `—` | — |
| `test_stderr_logger_thread_logs_decoded_lines()` |  | `—` | — |
| 🔄 `test_mcp_stderr_capture_logs_written_data()` |  | `—` | — |
| 🔄 `test_mcp_stderr_capture_ignores_empty_lines()` |  | `—` | — |

## `TestCreateMCPHttpProxyToolClass`

**Source:** [`tests/tools/test_mcp.py#L191`](tests/tools/test_mcp.py#L191)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_creates_tool_class_with_correct_name()` |  | `—` | — |
| `test_creates_tool_class_with_url_based_alias()` |  | `—` | — |
| `test_includes_description_with_hint()` |  | `—` | — |
| `test_stores_timeout_settings()` |  | `—` | — |
| `test_returns_correct_parameters()` |  | `—` | — |

## `TestCreateMCPStdioProxyToolClass`

**Source:** [`tests/tools/test_mcp.py#L250`](tests/tools/test_mcp.py#L250)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_creates_tool_class_with_alias()` |  | `—` | — |
| `test_creates_tool_class_with_command_based_alias()` |  | `—` | — |
| `test_stores_env_settings()` |  | `—` | — |
| `test_stores_timeout_settings()` |  | `—` | — |
| `test_includes_hint_in_description()` |  | `—` | — |

## `TestMCPConfigModels`

**Source:** [`tests/tools/test_mcp.py#L303`](tests/tools/test_mcp.py#L303)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_mcp_base_default_timeouts()` |  | `—` | — |
| `test_mcp_base_custom_timeouts()` |  | `—` | — |
| `test_mcp_base_rejects_non_positive_timeout()` |  | `—` | — |
| `test_mcp_stdio_with_env()` |  | `—` | — |
| `test_mcp_stdio_argv_with_string_command()` |  | `—` | — |
| `test_mcp_stdio_argv_with_list_command()` |  | `—` | — |
| `test_mcp_http_default_timeouts()` |  | `—` | — |
| `test_mcp_streamable_http_default_timeouts()` |  | `—` | — |
| `test_mcp_name_normalization()` |  | `—` | — |

## `TestMCPRegistry`

**Source:** [`tests/tools/test_mcp.py#L378`](tests/tools/test_mcp.py#L378)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_server_key_is_stable()` |  | `—` | — |
| `test_different_configs_produce_different_keys()` |  | `—` | — |
| `test_get_tools_caches_discovery()` |  | `—` | — |
| `test_get_tools_returns_empty_for_no_servers()` |  | `—` | — |
| `test_clear_drops_cache()` |  | `—` | — |
| `test_cache_survives_multiple_get_tools_calls()` |  | `—` | — |
| `test_disjoint_server_lists_across_agents()` |  | `—` | — |
| 🔄 `test_discover_http_success()` |  | `—` | — |
| 🔄 `test_discover_http_failure_returns_none()` |  | `—` | — |
| 🔄 `test_discover_stdio_success()` |  | `—` | — |
| 🔄 `test_discover_stdio_failure_returns_none()` |  | `—` | — |
| `test_get_tools_discovers_only_uncached()` |  | `—` | — |

??? note "Private Methods"

    - `def _make_http_server(self, name: str, url: str) -> MCPHttp`
    - `def _make_stdio_server(self, name: str, command: str) -> MCPStdio`

