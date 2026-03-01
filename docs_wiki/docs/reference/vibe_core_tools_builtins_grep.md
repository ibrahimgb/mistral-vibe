---
title: "vibe.core.tools.builtins.grep"
tldr: "Module vibe.core.tools.builtins.grep"
tags: [reference, api]
---

# [**vibe.core.tools.builtins.grep**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/grep.py)

## [**GrepBackend**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/grep.py#L27)

The [**GrepBackend**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/grep.py#L27) enum (extending `StrEnum`). Key fields include `RIPGREP`, `GNU_GREP`.

## [**GrepToolConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/grep.py#L32)

The [**GrepToolConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/grep.py#L32) Pydantic model (extending `BaseToolConfig`). Key fields include `permission`, `max_output_bytes`, `default_max_matches`, `default_timeout`, `exclude_patterns`, `codeignore_file`.

## [**GrepArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/grep.py#L78)

The [**GrepArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/grep.py#L78) Pydantic model (extending `BaseModel`). Key fields include `pattern`, `path`, `max_matches`, `use_default_ignore`.

## [**GrepResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/grep.py#L89)

The [**GrepResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/grep.py#L89) Pydantic model (extending `BaseModel`). Key fields include `matches`, `match_count`, `was_truncated`.

## [**Grep**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/grep.py#L97)

The [**Grep**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/grep.py#L97) class (extending `BaseTool[GrepArgs, GrepResult, GrepToolConfig, BaseToolState]`, `ToolUIData[GrepArgs, GrepResult]`). It exposes `run()`, `format_call_display()`, `get_result_display()`, `get_status_text()`. Internally it relies on `_build_ripgrep_command()`, `_execute_search()`.

**Public API:**

- `async def run()`
- `def format_call_display()`
- `def get_result_display()`
- `def get_status_text()`

**Internal helpers:**

- `_build_ripgrep_command()`
- `_execute_search()`

