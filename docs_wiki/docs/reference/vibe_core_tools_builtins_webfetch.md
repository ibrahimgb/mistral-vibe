---
title: "vibe.core.tools.builtins.webfetch"
tldr: "Module vibe.core.tools.builtins.webfetch"
tags: [reference, api]
---

# [**vibe.core.tools.builtins.webfetch**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/webfetch.py)

This module defines the constants `_HONEST_USER_AGENT`, `_HTTP_FORBIDDEN`.

## [**_Converter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/webfetch.py#L30)

The [**_Converter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/webfetch.py#L30) class (extending `MarkdownConverter`).

## [**WebFetchArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/webfetch.py#L36)

The [**WebFetchArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/webfetch.py#L36) Pydantic model (extending `BaseModel`). Key fields include `url`, `timeout`.

## [**WebFetchResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/webfetch.py#L43)

The [**WebFetchResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/webfetch.py#L43) Pydantic model (extending `BaseModel`). Key fields include `url`, `content`, `content_type`.

## [**WebFetchConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/webfetch.py#L49)

The [**WebFetchConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/webfetch.py#L49) Pydantic model (extending `BaseToolConfig`). Key fields include `permission`, `default_timeout`, `max_timeout`, `max_content_bytes`, `user_agent`.

## [**WebFetch**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/webfetch.py#L66)

The [**WebFetch**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/webfetch.py#L66) class (extending `BaseTool[WebFetchArgs, WebFetchResult, WebFetchConfig, BaseToolState]`, `ToolUIData[WebFetchArgs, WebFetchResult]`). It exposes `run()`, `get_call_display()`, `get_result_display()`, `get_status_text()`. Internally it relies on `_fetch_url()`.

**Public API:**

- `async def run()`
- `def get_call_display()`
- `def get_result_display()`
- `def get_status_text()`

**Internal helpers:**

- `_fetch_url()`

