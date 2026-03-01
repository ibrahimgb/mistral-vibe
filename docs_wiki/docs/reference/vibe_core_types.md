---
title: "vibe.core.types"
tldr: "Module vibe.core.types"
tags: [reference, api]
---

# [**vibe.core.types**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py)

## [**AgentStats**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L28)

The [**AgentStats**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L28) Pydantic model (extending `BaseModel`). Key fields include `steps`, `session_prompt_tokens`, `session_completion_tokens`, `tool_calls_agreed`, `tool_calls_rejected`, `tool_calls_failed`, `tool_calls_succeeded`, `context_tokens`, …. It exposes `__setattr__()`, `trigger_listeners()`, `add_listener()`, `create_fresh()`, `update_pricing()` among 6 public methods.

**Public API:**

- `def __setattr__()`
- `def trigger_listeners()`
- `def add_listener()`
- `def create_fresh()`
- `def session_total_llm_tokens()`
- `def last_turn_total_tokens()`
- `def session_cost()` — Calculate the total session cost in dollars based on token usage and pricing.
- `def update_pricing()` — Update pricing info when model changes.
- `def reset_context_state()` — Reset context-related fields while preserving cumulative session stats.

## [**SessionInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L122)

The [**SessionInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L122) Pydantic model (extending `BaseModel`). Key fields include `session_id`, `start_time`, `message_count`, `stats`, `save_dir`.

## [**SessionMetadata**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L130)

The [**SessionMetadata**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L130) Pydantic model (extending `BaseModel`). Key fields include `session_id`, `start_time`, `end_time`, `git_commit`, `git_branch`, `environment`, `username`.

## [**ClientMetadata**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L140)

The [**ClientMetadata**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L140) Pydantic model (extending `BaseModel`). Key fields include `name`, `version`.

## [**EntrypointMetadata**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L145)

The [**EntrypointMetadata**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L145) Pydantic model (extending `BaseModel`). Key fields include `agent_entrypoint`, `agent_version`, `client_name`, `client_version`.

## [**AvailableFunction**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L155)

The [**AvailableFunction**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L155) Pydantic model (extending `BaseModel`). Key fields include `name`, `description`, `parameters`.

## [**AvailableTool**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L161)

The [**AvailableTool**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L161) Pydantic model (extending `BaseModel`). Key fields include `type`, `function`.

## [**FunctionCall**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L166)

The [**FunctionCall**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L166) Pydantic model (extending `BaseModel`). Key fields include `name`, `arguments`.

## [**ToolCall**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L171)

The [**ToolCall**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L171) Pydantic model (extending `BaseModel`). Key fields include `id`, `index`, `function`, `type`.

## [**Role**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L195)

The [**Role**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L195) enum (extending `StrEnum`). Key fields include `system`, `user`, `assistant`, `tool`.

## [**ApprovalResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L202)

The [**ApprovalResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L202) enum (extending `StrEnum`). Key fields include `YES`, `NO`.

## [**LLMMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L207)

The [**LLMMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L207) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `role`, `content`, `reasoning_content`, `reasoning_signature`, `tool_calls`, `name`, `tool_call_id`, …. It exposes `__add__()`.

**Public API:**

- `def __add__()` — Careful: this is not commutative!

## [**LLMUsage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L301)

The [**LLMUsage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L301) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `prompt_tokens`, `completion_tokens`. It exposes `__add__()`.

**Public API:**

- `def __add__()`

## [**LLMChunk**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L313)

The [**LLMChunk**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L313) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `message`, `usage`. It exposes `__add__()`.

**Public API:**

- `def __add__()`

## [**BaseEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L326)

The [**BaseEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L326) abstract base class (extending `BaseModel`, `ABC`). Key fields include `model_config`.

## [**UserMessageEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L330)

The [**UserMessageEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L330) class (extending `BaseEvent`).

## [**AssistantEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L335)

The [**AssistantEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L335) class (extending `BaseEvent`). It exposes `__add__()`.

**Public API:**

- `def __add__()`

## [**ReasoningEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L349)

The [**ReasoningEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L349) class (extending `BaseEvent`).

## [**ToolCallEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L354)

The [**ToolCallEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L354) class (extending `BaseEvent`).

## [**ToolResultEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L362)

The [**ToolResultEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L362) class (extending `BaseEvent`).

## [**ToolStreamEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L373)

The [**ToolStreamEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L373) class (extending `BaseEvent`).

## [**CompactStartEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L379)

The [**CompactStartEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L379) class (extending `BaseEvent`).

## [**CompactEndEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L389)

The [**CompactEndEvent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L389) class (extending `BaseEvent`).

## [**OutputFormat**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L400)

The [**OutputFormat**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L400) enum (extending `StrEnum`). Key fields include `TEXT`, `JSON`, `STREAMING`.

## [**MessageList**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L419)

The [**MessageList**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L419) class (extending `Sequence[LLMMessage]`). It exposes `__init__()`, `append()`, `insert()`, `extend()`, `reset()` among 13 public methods.

**Public API:**

- `def __init__()`
- `def append()`
- `def insert()`
- `def extend()`
- `def reset()` — Replace contents silently (never notifies).
- `def silent()` — Context manager that suppresses notifications.
- `def __len__()`
- `def __getitem__()`
- `def __getitem__()`
- `def __getitem__()`
- `def __iter__()`
- `def __contains__()`
- `def __bool__()`

## [**RateLimitError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L481)

The [**RateLimitError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/types.py#L481) class (extending `Exception`). It exposes `__init__()`.

**Public API:**

- `def __init__()`

