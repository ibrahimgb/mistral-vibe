---
title: "vibe.core.tools.builtins.websearch"
tldr: "Module vibe.core.tools.builtins.websearch"
tags: [reference, api]
---

# [**vibe.core.tools.builtins.websearch**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/websearch.py)

## [**WebSearchSource**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/websearch.py#L25)

The [**WebSearchSource**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/websearch.py#L25) Pydantic model (extending `BaseModel`). Key fields include `title`, `url`.

## [**WebSearchArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/websearch.py#L30)

The [**WebSearchArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/websearch.py#L30) Pydantic model (extending `BaseModel`). Key fields include `query`.

## [**WebSearchResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/websearch.py#L34)

The [**WebSearchResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/websearch.py#L34) Pydantic model (extending `BaseModel`). Key fields include `answer`, `sources`.

## [**WebSearchConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/websearch.py#L39)

The [**WebSearchConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/websearch.py#L39) Pydantic model (extending `BaseToolConfig`). Key fields include `permission`, `timeout`, `model`.

## [**WebSearch**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/websearch.py#L48)

The [**WebSearch**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/websearch.py#L48) class (extending `BaseTool[WebSearchArgs, WebSearchResult, WebSearchConfig, BaseToolState]`, `ToolUIData[WebSearchArgs, WebSearchResult]`). It exposes `is_available()`, `run()`, `get_call_display()`, `get_result_display()`, `get_status_text()`. Internally it relies on `_parse_response()`.

**Public API:**

- `def is_available()`
- `async def run()`
- `def get_call_display()`
- `def get_result_display()`
- `def get_status_text()`

**Internal helpers:**

- `_parse_response()`

