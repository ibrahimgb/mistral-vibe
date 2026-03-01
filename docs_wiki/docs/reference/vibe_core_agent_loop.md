---
title: "vibe.core.agent_loop"
tldr: "Module vibe.core.agent_loop"
tags: [reference, api]
---

# [**vibe.core.agent_loop**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py)

## [**ToolExecutionResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L111)

The [**ToolExecutionResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L111) enum (extending `StrEnum`). Key fields include `SKIP`, `EXECUTE`.

## [**ToolDecision**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L116)

The [**ToolDecision**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L116) Pydantic model (extending `BaseModel`). Key fields include `verdict`, `approval_type`, `feedback`.

## [**AgentLoopError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L122)

The [**AgentLoopError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L122) class (extending `Exception`) base exception for agentloop errors.

## [**AgentLoopStateError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L126)

The [**AgentLoopStateError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L126) class (extending `AgentLoopError`) raised when agent loop is in an invalid state.

## [**AgentLoopLLMResponseError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L130)

The [**AgentLoopLLMResponseError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L130) class (extending `AgentLoopError`) raised when llm response is malformed or missing expected data.

## [**TeleportError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L134)

The [**TeleportError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L134) class (extending `AgentLoopError`) raised when teleport to vibe nuage fails.

## [**AgentLoop**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L142)

The [**AgentLoop**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agent_loop.py#L142) class. It exposes `__init__()`, `set_tool_permission()`, `emit_new_session_telemetry()`, `act()`, `teleport_to_vibe_nuage()` among 11 public methods. Internally it relies on `_setup_middleware()`, `_handle_middleware_result()`, `_conversation_loop()`.

**Public API:**

- `def __init__()`
- `def agent_profile()`
- `def config()`
- `def auto_approve()`
- `def set_tool_permission()`
- `def emit_new_session_telemetry()`
- `async def act()`
- `def teleport_service()`
- `def teleport_to_vibe_nuage()`
- `def set_approval_callback()`
- `def set_user_input_callback()`
- `async def clear_history()`
- `async def compact()`
- `async def switch_agent()`
- `async def reload_with_initial_messages()`

**Internal helpers:**

- `_setup_middleware()` — Configure middleware pipeline for this conversation.
- `_handle_middleware_result()`
- `_conversation_loop()`
- `_stream_assistant_events()`
- `_process_one_tool_call()`
- `_chat()`
- `_chat_streaming()`
- `_should_execute_tool()`
- `_ask_approval()`
- `_fill_missing_tool_responses()`

