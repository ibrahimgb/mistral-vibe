---
title: "vibe.cli.textual_ui.widgets.messages"
tldr: "Module vibe.cli.textual_ui.widgets.messages"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.widgets.messages**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py)

## [**NonSelectableStatic**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L15)

The [**NonSelectableStatic**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L15) class (extending `NoMarkupStatic`). It exposes `text_selection()`, `get_selection()`.

**Public API:**

- `def text_selection()`
- `def text_selection()`
- `def get_selection()`

## [**ExpandingBorder**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L28)

The [**ExpandingBorder**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L28) class (extending `NonSelectableStatic`). It exposes `render()`, `on_resize()`.

**Public API:**

- `def render()`
- `def on_resize()`

## [**UserMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L37)

The [**UserMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L37) class (extending `Static`). It exposes `__init__()`, `compose()`, `set_pending()`.

**Public API:**

- `def __init__()`
- `def compose()`
- `async def set_pending()`

## [**StreamingMessageBase**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L63)

The [**StreamingMessageBase**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L63) class (extending `Static`). It exposes `__init__()`, `append_content()`, `write_initial_content()`, `stop_stream()`, `is_stripped_content_empty()`.

**Public API:**

- `def __init__()`
- `async def append_content()`
- `async def write_initial_content()`
- `async def stop_stream()`
- `def is_stripped_content_empty()`

## [**AssistantMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L113)

The [**AssistantMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L113) class (extending `StreamingMessageBase`). It exposes `__init__()`, `compose()`.

**Public API:**

- `def __init__()`
- `def compose()`

## [**ReasoningMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L126)

The [**ReasoningMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L126) class (extending `SpinnerMixin`, `StreamingMessageBase`). It exposes `__init__()`, `compose()`, `on_mount()`, `on_resize()`, `on_click()` among 6 public methods.

**Public API:**

- `def __init__()`
- `def compose()`
- `def on_mount()`
- `def on_resize()`
- `async def on_click()`
- `async def set_collapsed()`

## [**UserCommandMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L192)

The [**UserCommandMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L192) class (extending `Static`). It exposes `__init__()`, `compose()`.

**Public API:**

- `def __init__()`
- `def compose()`

## [**WhatsNewMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L205)

The [**WhatsNewMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L205) class (extending `Static`). It exposes `__init__()`, `compose()`.

**Public API:**

- `def __init__()`
- `def compose()`

## [**InterruptMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L215)

The [**InterruptMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L215) class (extending `Static`). It exposes `__init__()`, `compose()`.

**Public API:**

- `def __init__()`
- `def compose()`

## [**BashOutputMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L229)

The [**BashOutputMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L229) class (extending `Static`). It exposes `__init__()`, `compose()`.

**Public API:**

- `def __init__()`
- `def compose()`

## [**ErrorMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L249)

The [**ErrorMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L249) class (extending `Static`). It exposes `__init__()`, `compose()`, `set_collapsed()`.

**Public API:**

- `def __init__()`
- `def compose()`
- `def set_collapsed()`

## [**WarningMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L269)

The [**WarningMessage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/widgets/messages.py#L269) class (extending `Static`). It exposes `__init__()`, `compose()`.

**Public API:**

- `def __init__()`
- `def compose()`

