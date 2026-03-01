---
title: "vibe.cli.textual_ui.widgets.spinner"
tldr: "Module vibe.cli.textual_ui.widgets.spinner"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.spinner**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py)

This module defines the constants `_SPINNER_CLASSES`.

## [**HasSetInterval**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L18)

The [**HasSetInterval**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L18) protocol (extending `Protocol`). It exposes `set_interval()`.

**Public API:**

- `def set_interval()`

## [**Spinner**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L24)

The [**Spinner**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L24) abstract base class (extending `ABC`). It exposes `__init__()`, `next_frame()`, `current_frame()`, `reset()`.

**Public API:**

- `def __init__()`
- `def next_frame()`
- `def current_frame()`
- `def reset()`

## [**BrailleSpinner**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L42)

The [**BrailleSpinner**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L42) class (extending `Spinner`).

## [**PulseSpinner**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L57)

The [**PulseSpinner**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L57) class (extending `Spinner`).

## [**SpinnerType**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L72)

The [**SpinnerType**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L72) enum (extending `Enum`). Key fields include `BRAILLE`, `PULSE`, `SNAKE`.

## [**SnakeSpinner**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L78)

The [**SnakeSpinner**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L78) class (extending `Spinner`). It exposes `__init__()`, `current_frame()`, `next_frame()`, `reset()`.

**Public API:**

- `def __init__()`
- `def current_direction()`
- `def current_frame()`
- `def next_frame()`
- `def reset()`

## [**SpinnerMixin**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L143)

The [**SpinnerMixin**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L143) class. It exposes `init_spinner()`, `start_spinner_timer()`, `refresh_spinner()`, `stop_spinning()`, `on_unmount()`.

**Public API:**

- `def init_spinner()`
- `def start_spinner_timer()`
- `def refresh_spinner()`
- `def stop_spinning()`
- `def on_unmount()`

## [**create_spinner()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/spinner.py#L138)

```python
def create_spinner(spinner_type: SpinnerType) -> Spinner
```

