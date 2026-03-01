---
title: "vibe.core.tools.builtins.task"
tldr: "Module vibe.core.tools.builtins.task"
tags: [reference, api]
---

# [**vibe.core.tools.builtins.task**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/task.py)

## [**TaskArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/task.py#L35)

The [**TaskArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/task.py#L35) Pydantic model (extending `BaseModel`). Key fields include `task`, `agent`.

## [**TaskResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/task.py#L43)

The [**TaskResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/task.py#L43) Pydantic model (extending `BaseModel`). Key fields include `response`, `turns_used`, `completed`.

## [**TaskToolConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/task.py#L49)

The [**TaskToolConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/task.py#L49) Pydantic model (extending `BaseToolConfig`). Key fields include `permission`, `allowlist`.

## [**Task**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/task.py#L54)

The [**Task**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/task.py#L54) class (extending `BaseTool[TaskArgs, TaskResult, TaskToolConfig, BaseToolState]`, `ToolUIData[TaskArgs, TaskResult]`). It exposes `get_call_display()`, `get_result_display()`, `get_status_text()`, `resolve_permission()`, `run()`.

**Public API:**

- `def get_call_display()`
- `def get_result_display()`
- `def get_status_text()`
- `def resolve_permission()`
- `async def run()`

