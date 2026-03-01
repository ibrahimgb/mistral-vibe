---
title: "vibe.core.llm.exceptions"
tldr: "Module vibe.core.llm.exceptions"
tags: [reference, api]
---

# [**vibe.core.llm.exceptions**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/exceptions.py)

## [**ErrorDetail**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/exceptions.py#L14)

The [**ErrorDetail**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/exceptions.py#L14) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `message`.

## [**PayloadSummary**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/exceptions.py#L19)

The [**PayloadSummary**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/exceptions.py#L19) Pydantic model (extending `BaseModel`). Key fields include `model`, `message_count`, `approx_chars`, `temperature`, `has_tools`, `tool_choice`.

## [**BackendError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/exceptions.py#L28)

The [**BackendError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/exceptions.py#L28) class (extending `RuntimeError`). It exposes `__init__()`. Internally it relies on `_fmt()`.

**Public API:**

- `def __init__()`

**Internal helpers:**

- `_fmt()`

## [**ErrorResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/exceptions.py#L83)

The [**ErrorResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/exceptions.py#L83) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `error`, `message`, `detail`.

**Public API:**

- `def primary_message()`

## [**BackendErrorBuilder**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/exceptions.py#L107)

The [**BackendErrorBuilder**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/exceptions.py#L107) class. It exposes `build_http_error()`, `build_request_error()`.

**Public API:**

- `def build_http_error()`
- `def build_request_error()`

