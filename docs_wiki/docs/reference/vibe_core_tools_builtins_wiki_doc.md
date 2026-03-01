---
title: "vibe.core.tools.builtins.wiki_doc"
tldr: "Wiki documentation tool — build, manage, and query the Code Wiki."
tags: [reference, api]
---

# [**vibe.core.tools.builtins.wiki_doc**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py)

Wiki documentation tool — build, manage, and query the Code Wiki.

Provides actions:
- ``build``  — run the full analysis + generation pipeline
- ``list_pages`` — list generated wiki pages
- ``analyze`` — run analysis only, return project stats

## [**WikiAction**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py#L30)

The [**WikiAction**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py#L30) enum (extending `StrEnum`). Key fields include `BUILD`, `UPDATE`, `LIST_PAGES`, `ANALYZE`.

## [**WikiDocArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py#L37)

The [**WikiDocArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py#L37) Pydantic model (extending `BaseModel`). Key fields include `action`, `project_root`, `output_dir`, `force`.

## [**WikiDocResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py#L53)

The [**WikiDocResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py#L53) Pydantic model (extending `BaseModel`). Key fields include `message`, `build_mode`, `pages`, `changed_files`, `stats`.

## [**WikiDocConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py#L61)

The [**WikiDocConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py#L61) Pydantic model (extending `BaseToolConfig`). Key fields include `permission`.

## [**WikiDocState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py#L65)

The [**WikiDocState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py#L65) Pydantic model (extending `BaseToolState`). Key fields include `last_output_dir`.

## [**WikiDoc**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py#L69)

The [**WikiDoc**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_doc.py#L69) class (extending `BaseTool[WikiDocArgs, WikiDocResult, WikiDocConfig, WikiDocState]`, `ToolUIData[WikiDocArgs, WikiDocResult]`). It exposes `format_call_display()`, `get_result_display()`, `get_status_text()`, `run()`. Internally it relies on `_analyze()`.

**Public API:**

- `def format_call_display()`
- `def get_result_display()`
- `def get_status_text()`
- `async def run()`

**Internal helpers:**

- `_analyze()`

