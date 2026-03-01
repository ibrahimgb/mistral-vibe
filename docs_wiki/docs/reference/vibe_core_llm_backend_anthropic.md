---
title: "vibe.core.llm.backend.anthropic"
tldr: "Module vibe.core.llm.backend.anthropic"
tags: [reference, api]
---

# [**vibe.core.llm.backend.anthropic**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/anthropic.py)

This module defines the constants `STREAMING_EVENT_TYPES`.

## [**AnthropicMapper**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/anthropic.py#L22)

The [**AnthropicMapper**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/anthropic.py#L22) class shared mapper for converting messages to/from anthropic api format. It exposes `prepare_messages()`, `prepare_tools()`, `prepare_tool_choice()`, `parse_response()`, `parse_streaming_event()`. Internally it relies on `_handle_block_start()`, `_handle_block_delta()`.

**Public API:**

- `def prepare_messages()`
- `def prepare_tools()`
- `def prepare_tool_choice()`
- `def parse_response()`
- `def parse_streaming_event()`

**Internal helpers:**

- `_handle_block_start()`
- `_handle_block_delta()`

## [**AnthropicAdapter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/anthropic.py#L318)

The [**AnthropicAdapter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/anthropic.py#L318) class (extending `APIAdapter`). It exposes `__init__()`, `prepare_request()`, `parse_response()`. Internally it relies on `_apply_thinking_config()`, `_build_payload()`, `_parse_streaming_event()`.

**Public API:**

- `def __init__()`
- `def prepare_request()`
- `def parse_response()`

**Internal helpers:**

- `_apply_thinking_config()`
- `_build_payload()`
- `_parse_streaming_event()`
- `_parse_content_block_start()`
- `_parse_content_block_delta()`

