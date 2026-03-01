---
title: "vibe.core.llm.backend.generic"
tldr: "Module vibe.core.llm.backend.generic"
tags: [reference, api]
---

# [**vibe.core.llm.backend.generic**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/generic.py)

This module defines the constants `ADAPTERS`.

## [**OpenAIAdapter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/generic.py#L30)

The [**OpenAIAdapter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/generic.py#L30) class (extending `APIAdapter`). It exposes `build_payload()`, `build_headers()`, `prepare_request()`, `parse_response()`.

**Public API:**

- `def build_payload()`
- `def build_headers()`
- `def prepare_request()`
- `def parse_response()`

## [**GenericBackend**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/generic.py#L165)

The [**GenericBackend**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/generic.py#L165) class. It exposes `__init__()`, `__aenter__()`, `__aexit__()`, `complete()`, `complete_streaming()` among 7 public methods. Internally it relies on `_make_streaming_request()`.

**Public API:**

- `def __init__()` — Initialize the backend.
- `async def __aenter__()`
- `async def __aexit__()`
- `async def complete()`
- `async def complete_streaming()`
- `async def count_tokens()`
- `async def close()`

**Internal helpers:**

- `_make_streaming_request()`

