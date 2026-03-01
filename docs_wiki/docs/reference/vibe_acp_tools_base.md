---
title: "vibe.acp.tools.base"
tldr: "Module vibe.acp.tools.base"
tags: [reference, api]
---

# [**vibe.acp.tools.base**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/base.py)

## [**ToolCallSessionUpdateProtocol**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/base.py#L18)

The [**ToolCallSessionUpdateProtocol**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/base.py#L18) protocol (extending `Protocol`). It exposes `tool_call_session_update()`.

**Public API:**

- `def tool_call_session_update()`

## [**ToolResultSessionUpdateProtocol**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/base.py#L24)

The [**ToolResultSessionUpdateProtocol**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/base.py#L24) protocol (extending `Protocol`). It exposes `tool_result_session_update()`.

**Public API:**

- `def tool_result_session_update()`

## [**AcpToolState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/base.py#L31)

The [**AcpToolState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/base.py#L31) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `client`, `session_id`, `tool_call_id`.

## [**BaseAcpTool**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/base.py#L43)

The [**BaseAcpTool**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/base.py#L43) class (extending `BaseTool`). It exposes `get_tool_instance()`, `update_tool_state()`.

**Public API:**

- `def get_tool_instance()`
- `def update_tool_state()`

