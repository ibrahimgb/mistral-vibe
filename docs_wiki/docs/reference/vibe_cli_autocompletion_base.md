---
title: "vibe.cli.autocompletion.base"
tldr: "Module vibe.cli.autocompletion.base"
tags: [reference, api]
---

# [**vibe.cli.autocompletion.base**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/autocompletion/base.py)

## [**CompletionResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/autocompletion/base.py#L7)

The [**CompletionResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/autocompletion/base.py#L7) enum (extending `StrEnum`). Key fields include `IGNORED`, `HANDLED`, `SUBMIT`.

## [**CompletionView**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/autocompletion/base.py#L13)

The [**CompletionView**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/autocompletion/base.py#L13) protocol (extending `Protocol`). It exposes `render_completion_suggestions()`, `clear_completion_suggestions()`, `replace_completion_range()`.

**Public API:**

- `def render_completion_suggestions()`
- `def clear_completion_suggestions()`
- `def replace_completion_range()`

