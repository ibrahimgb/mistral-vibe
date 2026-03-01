---
title: "vibe.acp.tools.builtins.search_replace"
tldr: "Module vibe.acp.tools.builtins.search_replace"
tags: [reference, api]
---

# [**vibe.acp.tools.builtins.search_replace**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/search_replace.py)

## [**AcpSearchReplaceState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/search_replace.py#L24)

The [**AcpSearchReplaceState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/search_replace.py#L24) Pydantic model (extending `BaseToolState`, `AcpToolState`). Key fields include `file_backup_content`.

## [**SearchReplace**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/search_replace.py#L28)

The [**SearchReplace**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/search_replace.py#L28) class (extending `CoreSearchReplaceTool`, `BaseAcpTool[AcpSearchReplaceState]`). It exposes `tool_call_session_update()`, `tool_result_session_update()`.

**Public API:**

- `def tool_call_session_update()`
- `def tool_result_session_update()`

