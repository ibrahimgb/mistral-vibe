---
title: "vibe.core.tools.builtins.search_replace"
tldr: "Module vibe.core.tools.builtins.search_replace"
tags: [reference, api]
---

# [**vibe.core.tools.builtins.search_replace**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py)

This module defines the constants `SEARCH_REPLACE_BLOCK_RE`, `SEARCH_REPLACE_BLOCK_WITH_FENCE_RE`.

## [**SearchReplaceBlock**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L35)

The [**SearchReplaceBlock**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L35) class (extending `NamedTuple`).

## [**FuzzyMatch**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L40)

The [**FuzzyMatch**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L40) class (extending `NamedTuple`).

## [**BlockApplyResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L47)

The [**BlockApplyResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L47) class (extending `NamedTuple`).

## [**SearchReplaceArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L54)

The [**SearchReplaceArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L54) Pydantic model (extending `BaseModel`). Key fields include `file_path`, `content`.

## [**SearchReplaceResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L59)

The [**SearchReplaceResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L59) Pydantic model (extending `BaseModel`). Key fields include `file`, `blocks_applied`, `lines_changed`, `content`, `warnings`.

## [**SearchReplaceConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L67)

The [**SearchReplaceConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L67) Pydantic model (extending `BaseToolConfig`). Key fields include `max_content_size`, `create_backup`, `fuzzy_threshold`.

## [**SearchReplace**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L73)

The [**SearchReplace**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/search_replace.py#L73) class (extending `BaseTool[SearchReplaceArgs, SearchReplaceResult, SearchReplaceConfig, BaseToolState]`, `ToolUIData[SearchReplaceArgs, SearchReplaceResult]`). It exposes `format_call_display()`, `get_result_display()`, `get_status_text()`, `resolve_permission()`, `run()`. Internally it relies on `_prepare_and_validate_args()`, `_apply_blocks()`, `_find_best_fuzzy_match()`.

**Public API:**

- `def format_call_display()`
- `def get_result_display()`
- `def get_status_text()`
- `def resolve_permission()`
- `async def run()`

**Internal helpers:**

- `_prepare_and_validate_args()`
- `_apply_blocks()`
- `_find_best_fuzzy_match()`
- `_create_unified_diff()`
- `_parse_search_replace_blocks()` — Parse SEARCH/REPLACE blocks from content.
- `_find_search_context()`

