---
title: "vibe.cli.textual_ui.widgets.tools"
tldr: "Module vibe.cli.textual_ui.widgets.tools"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.tools**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tools.py)

## [**ToolCallMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tools.py#L15)

The [**ToolCallMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tools.py#L15) class (extending `StatusMessage`). It exposes `__init__()`, `compose()`, `on_mount()`, `get_content()`, `update_event()` among 8 public methods.

**Public API:**

- `def __init__()`
- `def compose()`
- `def on_mount()`
- `def tool_call_id()`
- `def get_content()`
- `def update_event()`
- `def set_stream_message()` — Update the stream message displayed below the tool call indicator.
- `def stop_spinning()` — Stop the spinner and hide the stream widget.
- `def set_result_text()`

## [**ToolResultMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tools.py#L89)

The [**ToolResultMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/tools.py#L89) class (extending `Static`). It exposes `__init__()`, `compose()`, `on_mount()`, `set_collapsed()`, `toggle_collapsed()`. Internally it relies on `_render_result()`.

**Public API:**

- `def __init__()`
- `def tool_name()`
- `def compose()`
- `async def on_mount()`
- `async def set_collapsed()`
- `async def toggle_collapsed()`

**Internal helpers:**

- `_render_result()`

