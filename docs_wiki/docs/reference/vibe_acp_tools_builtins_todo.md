---
title: "vibe.acp.tools.builtins.todo"
tldr: "Module vibe.acp.tools.builtins.todo"
tags: [reference, api]
---

# [**vibe.acp.tools.builtins.todo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/todo.py)

## [**AcpTodoState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/todo.py#L23)

The [**AcpTodoState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/todo.py#L23) class (extending `TodoState`, `AcpToolState`).

## [**Todo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/todo.py#L27)

The [**Todo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/tools/builtins/todo.py#L27) class (extending `CoreTodoTool`, `BaseAcpTool[AcpTodoState]`). It exposes `tool_call_session_update()`, `tool_result_session_update()`.

**Public API:**

- `def tool_call_session_update()`
- `def tool_result_session_update()`

