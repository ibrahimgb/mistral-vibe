---
title: "vibe.core.llm.types"
tldr: "Module vibe.core.llm.types"
tags: [reference, api]
---

# [**vibe.core.llm.types**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/types.py)

## [**BackendLike**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/types.py#L13)

The [**BackendLike**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/types.py#L13) protocol (extending `Protocol`) port protocol for dependency-injectable llm backends. It exposes `__aenter__()`, `__aexit__()`, `complete()`, `complete_streaming()`, `count_tokens()`.

**Public API:**

- `async def __aenter__()`
- `async def __aexit__()`
- `async def complete()` — Complete a chat conversation using the specified model and provider.
- `def complete_streaming()` — Equivalent of the complete method, but yields LLMEvent objects
- `async def count_tokens()` — Count the number of tokens in the prompt without generating a real response.

