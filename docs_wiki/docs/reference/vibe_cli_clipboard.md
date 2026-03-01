---
title: "vibe.cli.clipboard"
tldr: "Module vibe.cli.clipboard"
tags: [reference, api]
---

# [**vibe.cli.clipboard**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/clipboard.py)

This module defines the constants `_PREVIEW_MAX_LENGTH`, `_CMD_STRATEGIES`, `_COPY_METHODS`, `_PASTE_CMD_STRATEGIES`, `_READ_CLIPBOARD_METHODS`.

## [**_get_selected_texts()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/clipboard.py#L127)

```python
def _get_selected_texts(app: App) -> list[str]
```

## [**copy_selection_to_clipboard()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/clipboard.py#L151)

```python
def copy_selection_to_clipboard(app: App, show_toast: bool) -> str | None
```

