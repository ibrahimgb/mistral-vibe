---
title: "vibe.core.tools.base"
tldr: "Module vibe.core.tools.base"
tags: [reference, api]
---

# [**vibe.core.tools.base**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py)

This module defines the constants `ARGS_COUNT`.

## [**InvokeContext**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L37)

The [**InvokeContext**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L37) dataclass context passed to tools during invocation. Key fields include `tool_call_id`, `approval_callback`, `agent_manager`, `user_input_callback`, `sampling_callback`, `session_dir`, `entrypoint_metadata`.

## [**ToolError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L49)

The [**ToolError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L49) class (extending `Exception`) raised when the tool encounters an unrecoverable problem.

## [**ToolInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L53)

The [**ToolInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L53) Pydantic model (extending `BaseModel`) information about a tool. Key fields include `name`, `description`, `parameters`.

## [**ToolPermissionError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L67)

The [**ToolPermissionError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L67) class (extending `Exception`) raised when a tool permission is not allowed.

## [**ToolPermission**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L71)

The [**ToolPermission**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L71) enum (extending `StrEnum`). Key fields include `ALWAYS`, `NEVER`, `ASK`. It exposes `by_name()`.

**Public API:**

- `def by_name()`

## [**BaseToolConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L86)

The [**BaseToolConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L86) Pydantic model (extending `BaseModel`) configuration for a tool. Key fields include `model_config`, `permission`, `allowlist`, `denylist`.

## [**BaseToolState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L102)

The [**BaseToolState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L102) Pydantic model (extending `BaseModel`). Key fields include `model_config`.

## [**BaseTool**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L108)

The [**BaseTool**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/base.py#L108) abstract base class (extending `ABC`). It exposes `__init__()`, `run()`, `get_tool_prompt()`, `invoke()`, `from_config()` among 10 public methods. Internally it relies on `_get_tool_args_results()`, `_extract_result_type()`.

**Public API:**

- `def __init__()`
- `async def run()` — Invoke the tool with the given arguments.
- `def get_tool_prompt()` — Loads and returns the content of the tool's .md prompt file, if it exists.
- `async def invoke()` — Validate arguments and run the tool.
- `def from_config()`
- `def get_parameters()` — Return a cleaned-up JSON-schema dict describing the arguments model
- `def get_name()`
- `def is_available()`
- `def create_config_with_permission()`
- `def resolve_permission()` — Per-invocation permission override, checked before config-level permission.

**Internal helpers:**

- `_get_tool_args_results()` — Extract <ToolArgs, ToolResult> from the annotated signature of `run`.
- `_extract_result_type()` — Extract the ToolResult type from AsyncGenerator[ToolStreamEvent | ToolResult, None].

