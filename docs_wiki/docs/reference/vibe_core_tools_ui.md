---
title: "vibe.core.tools.ui"
tldr: "Module vibe.core.tools.ui"
tags: [reference, api]
---

# [**vibe.core.tools.ui**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/ui.py)

## [**ToolCallDisplay**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/ui.py#L13)

The [**ToolCallDisplay**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/ui.py#L13) Pydantic model (extending `BaseModel`). Key fields include `summary`, `content`.

## [**ToolResultDisplay**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/ui.py#L18)

The [**ToolResultDisplay**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/ui.py#L18) Pydantic model (extending `BaseModel`). Key fields include `success`, `message`, `warnings`.

## [**ToolUIData**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/ui.py#L24)

The [**ToolUIData**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/ui.py#L24) abstract base class (extending `ABC`). It exposes `get_no_args_display()`, `get_invalid_args_display()`, `format_call_display()`, `get_call_display()`, `get_result_display()` among 6 public methods.

**Public API:**

- `def get_no_args_display()`
- `def get_invalid_args_display()`
- `def format_call_display()`
- `def get_call_display()`
- `def get_result_display()`
- `def get_status_text()`

## [**ToolUIDataAdapter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/ui.py#L67)

The [**ToolUIDataAdapter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/ui.py#L67) class. It exposes `__init__()`, `get_call_display()`, `get_result_display()`, `get_status_text()`.

**Public API:**

- `def __init__()`
- `def get_call_display()`
- `def get_result_display()`
- `def get_status_text()`

