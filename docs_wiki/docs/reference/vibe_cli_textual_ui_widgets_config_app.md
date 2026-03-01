---
title: "vibe.cli.textual_ui.widgets.config_app"
tldr: "Module vibe.cli.textual_ui.widgets.config_app"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.config_app**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/config_app.py)

## [**SettingDefinition**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/config_app.py#L18)

The [**SettingDefinition**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/config_app.py#L18) class (extending `TypedDict`).

## [**ConfigApp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/config_app.py#L25)

The [**ConfigApp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/config_app.py#L25) class (extending `Container`). It exposes `__init__()`, `compose()`, `on_mount()`, `action_move_up()`, `action_move_down()` among 9 public methods. Internally it relies on `_update_display()`.

**Public API:**

- `def __init__()`
- `def compose()`
- `def on_mount()`
- `def action_move_up()`
- `def action_move_down()`
- `def action_toggle_setting()`
- `def action_cycle()`
- `def action_close()`
- `def on_blur()`

**Internal helpers:**

- `_update_display()`

