---
title: "vibe.acp.tools.builtins.read_file"
tldr: "Module vibe.acp.tools.builtins.read_file"
tags: [reference, api]
---

# [**vibe.acp.tools.builtins.read_file**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/read_file.py)

## [**AcpReadFileState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/read_file.py#L18)

The [**AcpReadFileState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/read_file.py#L18) Pydantic model (extending `BaseToolState`, `AcpToolState`).

## [**ReadFile**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/read_file.py#L22)

The [**ReadFile**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/read_file.py#L22) class (extending `CoreReadFileTool`, `BaseAcpTool[AcpReadFileState]`). Internally it relies on `_read_file()`.

**Internal helpers:**

- `_read_file()`

