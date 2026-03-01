---
title: "vibe.acp.utils"
tldr: "Module vibe.acp.utils"
tags: [reference, api]
---

# [**vibe.acp.utils**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py)

This module defines the constants `TOOL_OPTIONS`.

## [**ToolOption**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L33)

The [**ToolOption**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L33) enum (extending `StrEnum`). Key fields include `ALLOW_ONCE`, `ALLOW_ALWAYS`, `REJECT_ONCE`, `REJECT_ALWAYS`.

## [**is_valid_acp_mode()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L59)

```python
def is_valid_acp_mode(profiles: list[AgentProfile], mode_name: str) -> bool
```

## [**make_mode_response()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L65)

```python
def make_mode_response(profiles: list[AgentProfile], current_mode_id: str) -> tuple[SessionModeState, SessionConfigOption]
```

## [**make_model_response()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L105)

```python
def make_model_response(models: list[ModelConfig], current_model_id: str) -> tuple[SessionModelState, SessionConfigOption]
```

## [**create_compact_start_session_update()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L135)

```python
def create_compact_start_session_update(event: CompactStartEvent) -> ToolCallStart
```

## [**create_compact_end_session_update()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L158)

```python
def create_compact_end_session_update(event: CompactEndEvent) -> ToolCallProgress
```

## [**get_proxy_help_text()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L184)

```python
def get_proxy_help_text() -> str
```

## [**create_user_message_replay()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L216)

```python
def create_user_message_replay(msg: LLMMessage) -> UserMessageChunk
```

## [**create_assistant_message_replay()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L225)

```python
def create_assistant_message_replay(msg: LLMMessage) -> AgentMessageChunk | None
```

## [**create_reasoning_replay()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L237)

```python
def create_reasoning_replay(msg: LLMMessage) -> AgentThoughtChunk | None
```

## [**create_tool_call_replay()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L248)

```python
def create_tool_call_replay(tool_call_id: str, tool_name: str, arguments: str | None) -> ToolCallStart
```

## [**create_tool_result_replay()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/utils.py#L260)

```python
def create_tool_result_replay(msg: LLMMessage) -> ToolCallProgress | None
```

