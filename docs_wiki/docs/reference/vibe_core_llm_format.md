---
title: "vibe.core.llm.format"
tldr: "Module vibe.core.llm.format"
tags: [reference, api]
---

# [**vibe.core.llm.format**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py)

## [**ParsedToolCall**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py#L21)

The [**ParsedToolCall**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py#L21) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `tool_name`, `raw_args`, `call_id`.

## [**ResolvedToolCall**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py#L28)

The [**ResolvedToolCall**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py#L28) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `tool_name`, `tool_class`, `validated_args`, `call_id`.

**Public API:**

- `def args_dict()`

## [**FailedToolCall**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py#L40)

The [**FailedToolCall**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py#L40) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `tool_name`, `call_id`, `error`.

## [**ParsedMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py#L47)

The [**ParsedMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py#L47) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `tool_calls`.

## [**ResolvedMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py#L52)

The [**ResolvedMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py#L52) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `tool_calls`, `failed_calls`.

## [**APIToolFormatHandler**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py#L58)

The [**APIToolFormatHandler**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/format.py#L58) class. It exposes `get_available_tools()`, `get_tool_choice()`, `process_api_response_message()`, `parse_message()`, `resolve_tool_calls()` among 7 public methods.

**Public API:**

- `def name()`
- `def get_available_tools()`
- `def get_tool_choice()`
- `def process_api_response_message()`
- `def parse_message()`
- `def resolve_tool_calls()`
- `def create_tool_response_message()`
- `def create_failed_tool_response_message()`

