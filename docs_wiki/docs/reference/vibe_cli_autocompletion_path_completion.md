---
title: "vibe.cli.autocompletion.path_completion"
tldr: "Module vibe.cli.autocompletion.path_completion"
tags: [reference, api]
---

# [**vibe.cli.autocompletion.path_completion**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/autocompletion/path_completion.py)

This module defines the constants `MAX_SUGGESTIONS_COUNT`.

## [**PathCompletionController**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/autocompletion/path_completion.py#L15)

The [**PathCompletionController**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/autocompletion/path_completion.py#L15) class. It exposes `__init__()`, `can_handle()`, `reset()`, `on_text_changed()`, `on_key()`. Internally it relies on `_update_suggestions()`.

**Public API:**

- `def __init__()`
- `def can_handle()`
- `def reset()`
- `def on_text_changed()`
- `def on_key()`

**Internal helpers:**

- `_update_suggestions()`

