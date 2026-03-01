---
title: "vibe.acp.tools.builtins.write_file"
tldr: "Module vibe.acp.tools.builtins.write_file"
tags: [reference, api]
---

# [**vibe.acp.tools.builtins.write_file**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/write_file.py)

## [**AcpWriteFileState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/write_file.py#L24)

The [**AcpWriteFileState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/write_file.py#L24) Pydantic model (extending `BaseToolState`, `AcpToolState`).

## [**WriteFile**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/write_file.py#L28)

The [**WriteFile**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/write_file.py#L28) class (extending `CoreWriteFileTool`, `BaseAcpTool[AcpWriteFileState]`). It exposes `tool_call_session_update()`, `tool_result_session_update()`.

**Public API:**

- `def tool_call_session_update()`
- `def tool_result_session_update()`

