---
title: "vibe.core.output_formatters"
tldr: "Module vibe.core.output_formatters"
tags: [reference, api]
---

# [**vibe.core.output_formatters**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/output_formatters.py)

## [**OutputFormatter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/output_formatters.py#L11)

The [**OutputFormatter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/output_formatters.py#L11) abstract base class (extending `ABC`). It exposes `__init__()`, `on_message_added()`, `on_event()`, `finalize()`.

**Public API:**

- `def __init__()`
- `def on_message_added()`
- `def on_event()`
- `def finalize()` — Finalize output and return any final text to be printed.

## [**TextOutputFormatter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/output_formatters.py#L35)

The [**TextOutputFormatter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/output_formatters.py#L35) class (extending `OutputFormatter`). It exposes `on_message_added()`, `on_event()`, `finalize()`.

**Public API:**

- `def on_message_added()`
- `def on_event()`
- `def finalize()`

## [**JsonOutputFormatter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/output_formatters.py#L47)

The [**JsonOutputFormatter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/output_formatters.py#L47) class (extending `OutputFormatter`). It exposes `on_message_added()`, `on_event()`, `finalize()`.

**Public API:**

- `def on_message_added()`
- `def on_event()`
- `def finalize()`

## [**StreamingJsonOutputFormatter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/output_formatters.py#L62)

The [**StreamingJsonOutputFormatter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/output_formatters.py#L62) class (extending `OutputFormatter`). It exposes `on_message_added()`, `on_event()`, `finalize()`.

**Public API:**

- `def on_message_added()`
- `def on_event()`
- `def finalize()`

## [**create_formatter()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/output_formatters.py#L75)

```python
def create_formatter(format_type: OutputFormat, stream: TextIO) -> OutputFormatter
```

