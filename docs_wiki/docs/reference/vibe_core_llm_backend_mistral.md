---
title: "vibe.core.llm.backend.mistral"
tldr: "Module vibe.core.llm.backend.mistral"
tags: [reference, api]
---

# [**vibe.core.llm.backend.mistral**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/mistral.py)

## [**ParsedContent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/mistral.py#L32)

The [**ParsedContent**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/mistral.py#L32) class (extending `NamedTuple`).

## [**MistralMapper**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/mistral.py#L37)

The [**MistralMapper**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/mistral.py#L37) class. It exposes `prepare_message()`, `prepare_tool()`, `prepare_tool_choice()`, `parse_content()`, `parse_tool_calls()`.

**Public API:**

- `def prepare_message()`
- `def prepare_tool()`
- `def prepare_tool_choice()`
- `def parse_content()`
- `def parse_tool_calls()`

## [**MistralBackend**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/mistral.py#L154)

The [**MistralBackend**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/mistral.py#L154) class. It exposes `__init__()`, `__aenter__()`, `__aexit__()`, `complete()`, `complete_streaming()` among 6 public methods.

**Public API:**

- `def __init__()`
- `async def __aenter__()`
- `async def __aexit__()`
- `async def complete()`
- `async def complete_streaming()`
- `async def count_tokens()`

