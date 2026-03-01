---
title: "vibe.core.llm.backend.base"
tldr: "Module vibe.core.llm.backend.base"
tags: [reference, api]
---

# [**vibe.core.llm.backend.base**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/base.py)

## [**PreparedRequest**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/base.py#L12)

The [**PreparedRequest**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/base.py#L12) class (extending `NamedTuple`).

## [**APIAdapter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/base.py#L19)

The [**APIAdapter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/base.py#L19) protocol (extending `Protocol`). It exposes `prepare_request()`, `parse_response()`.

**Public API:**

- `def prepare_request()`
- `def parse_response()`

