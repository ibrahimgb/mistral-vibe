---
title: "vibe.cli.textual_ui.widgets.chat_input.container"
tldr: "Module vibe.cli.textual_ui.widgets.chat_input.container"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.chat_input.container**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/container.py)

This module defines the constants `SAFETY_BORDER_CLASSES`.

## [**ChatInputContainer**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/container.py#L30)

The [**ChatInputContainer**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/chat_input/container.py#L30) class (extending `Vertical`). It exposes `__init__()`, `compose()`, `on_mount()`, `value()`, `focus_input()` among 12 public methods. Internally it relies on `_format_insertion()`.

**Public API:**

- `def __init__()`
- `def compose()`
- `def on_mount()`
- `def input_widget()`
- `def value()`
- `def value()`
- `def focus_input()`
- `def render_completion_suggestions()`
- `def clear_completion_suggestions()`
- `def replace_completion_range()`
- `def on_chat_input_body_submitted()`
- `def switching_mode()`
- `def switching_mode()`
- `def set_safety()`
- `def set_agent_name()`

**Internal helpers:**

- `_format_insertion()` — Format the insertion text with appropriate spacing.

