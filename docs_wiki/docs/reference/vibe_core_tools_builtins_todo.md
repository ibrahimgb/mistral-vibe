---
title: "vibe.core.tools.builtins.todo"
tldr: "Module vibe.core.tools.builtins.todo"
tags: [reference, api]
---

# [**vibe.core.tools.builtins.todo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py)

## [**TodoStatus**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L21)

The [**TodoStatus**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L21) enum (extending `StrEnum`). Key fields include `PENDING`, `IN_PROGRESS`, `COMPLETED`, `CANCELLED`.

## [**TodoPriority**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L28)

The [**TodoPriority**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L28) enum (extending `StrEnum`). Key fields include `LOW`, `MEDIUM`, `HIGH`.

## [**TodoItem**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L34)

The [**TodoItem**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L34) Pydantic model (extending `BaseModel`). Key fields include `id`, `content`, `status`, `priority`.

## [**TodoArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L41)

The [**TodoArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L41) Pydantic model (extending `BaseModel`). Key fields include `action`, `todos`.

## [**TodoResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L48)

The [**TodoResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L48) Pydantic model (extending `BaseModel`). Key fields include `message`, `todos`, `total_count`.

## [**TodoConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L54)

The [**TodoConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L54) Pydantic model (extending `BaseToolConfig`). Key fields include `permission`, `max_todos`.

## [**TodoState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L59)

The [**TodoState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L59) Pydantic model (extending `BaseToolState`). Key fields include `todos`.

## [**Todo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L63)

The [**Todo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/todo.py#L63) class (extending `BaseTool[TodoArgs, TodoResult, TodoConfig, TodoState]`, `ToolUIData[TodoArgs, TodoResult]`). It exposes `format_call_display()`, `get_result_display()`, `get_status_text()`, `run()`.

**Public API:**

- `def format_call_display()`
- `def get_result_display()`
- `def get_status_text()`
- `async def run()`

