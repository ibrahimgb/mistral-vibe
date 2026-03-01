---
title: "vibe.core.tools.builtins.write_file"
tldr: "Module vibe.core.tools.builtins.write_file"
tags: [reference, api]
---

# [**vibe.core.tools.builtins.write_file**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/write_file.py)

## [**WriteFileArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/write_file.py#L23)

The [**WriteFileArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/write_file.py#L23) Pydantic model (extending `BaseModel`). Key fields include `path`, `content`, `overwrite`.

## [**WriteFileResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/write_file.py#L31)

The [**WriteFileResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/write_file.py#L31) Pydantic model (extending `BaseModel`). Key fields include `path`, `bytes_written`, `file_existed`, `content`.

## [**WriteFileConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/write_file.py#L38)

The [**WriteFileConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/write_file.py#L38) Pydantic model (extending `BaseToolConfig`). Key fields include `permission`, `max_write_bytes`, `create_parent_dirs`.

## [**WriteFile**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/write_file.py#L44)

The [**WriteFile**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/write_file.py#L44) class (extending `BaseTool[WriteFileArgs, WriteFileResult, WriteFileConfig, BaseToolState]`, `ToolUIData[WriteFileArgs, WriteFileResult]`). It exposes `format_call_display()`, `get_result_display()`, `get_status_text()`, `resolve_permission()`, `run()`. Internally it relies on `_prepare_and_validate_path()`.

**Public API:**

- `def format_call_display()`
- `def get_result_display()`
- `def get_status_text()`
- `def resolve_permission()`
- `async def run()`

**Internal helpers:**

- `_prepare_and_validate_path()`

