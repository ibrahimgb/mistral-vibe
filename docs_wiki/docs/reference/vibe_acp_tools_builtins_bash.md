---
title: "vibe.acp.tools.builtins.bash"
tldr: "Module vibe.acp.tools.builtins.bash"
tags: [reference, api]
---

# [**vibe.acp.tools.builtins.bash**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/bash.py)

## [**AcpBashState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/bash.py#L22)

The [**AcpBashState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/bash.py#L22) Pydantic model (extending `BaseToolState`, `AcpToolState`).

## [**Bash**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/bash.py#L26)

The [**Bash**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/bash.py#L26) class (extending `CoreBashTool`, `BaseAcpTool[AcpBashState]`). It exposes `run()`, `get_summary()`, `tool_call_session_update()`, `tool_result_session_update()`.

**Public API:**

- `async def run()`
- `def get_summary()`
- `def tool_call_session_update()`
- `def tool_result_session_update()`

