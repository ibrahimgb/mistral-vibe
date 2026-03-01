---
title: "vibe.cli.textual_ui.widgets.session_picker"
tldr: "Module vibe.cli.textual_ui.widgets.session_picker"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.session_picker**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/session_picker.py)

This module defines the constants `_SECONDS_PER_MINUTE`, `_SECONDS_PER_HOUR`, `_SECONDS_PER_DAY`, `_SECONDS_PER_WEEK`.

## [**SessionPickerApp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/session_picker.py#L60)

The [**SessionPickerApp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/session_picker.py#L60) class (extending `Container`) session picker for /resume command. It exposes `__init__()`, `compose()`, `on_mount()`, `on_option_list_option_selected()`, `action_cancel()`.

**Public API:**

- `def __init__()`
- `def compose()`
- `def on_mount()`
- `def on_option_list_option_selected()`
- `def action_cancel()`

## [**_format_relative_time()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/session_picker.py#L25)

```python
def _format_relative_time(iso_time: str | None) -> str
```

