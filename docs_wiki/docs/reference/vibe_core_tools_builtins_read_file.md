---
title: "vibe.core.tools.builtins.read_file"
tldr: "Module vibe.core.tools.builtins.read_file"
tags: [reference, api]
---

# [**vibe.core.tools.builtins.read_file**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/read_file.py)

## [**_ReadResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/read_file.py#L26)

The [**_ReadResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/read_file.py#L26) class (extending `NamedTuple`).

## [**ReadFileArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/read_file.py#L32)

The [**ReadFileArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/read_file.py#L32) Pydantic model (extending `BaseModel`). Key fields include `path`, `offset`, `limit`.

## [**ReadFileResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/read_file.py#L43)

The [**ReadFileResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/read_file.py#L43) Pydantic model (extending `BaseModel`). Key fields include `path`, `content`, `lines_read`, `was_truncated`.

## [**ReadFileToolConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/read_file.py#L52)

The [**ReadFileToolConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/read_file.py#L52) Pydantic model (extending `BaseToolConfig`). Key fields include `permission`, `max_read_bytes`.

## [**ReadFile**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/read_file.py#L60)

The [**ReadFile**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/read_file.py#L60) class (extending `BaseTool[ReadFileArgs, ReadFileResult, ReadFileToolConfig, BaseToolState]`, `ToolUIData[ReadFileArgs, ReadFileResult]`). It exposes `run()`, `resolve_permission()`, `format_call_display()`, `get_result_display()`, `get_status_text()`. Internally it relies on `_read_file()`.

**Public API:**

- `async def run()`
- `def resolve_permission()`
- `def format_call_display()`
- `def get_result_display()`
- `def get_status_text()`

**Internal helpers:**

- `_read_file()`

