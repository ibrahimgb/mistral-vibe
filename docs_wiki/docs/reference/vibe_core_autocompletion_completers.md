---
title: "vibe.core.autocompletion.completers"
tldr: "Module vibe.core.autocompletion.completers"
tags: [reference, api]
---

# [**vibe.core.autocompletion.completers**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/completers.py)

This module defines the constants `DEFAULT_MAX_ENTRIES_TO_PROCESS`, `DEFAULT_TARGET_MATCHES`.

## [**Completer**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/completers.py#L14)

The [**Completer**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/completers.py#L14) class. It exposes `get_completions()`, `get_completion_items()`, `get_replacement_range()`.

**Public API:**

- `def get_completions()`
- `def get_completion_items()`
- `def get_replacement_range()`

## [**CommandCompleter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/completers.py#L29)

The [**CommandCompleter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/completers.py#L29) class (extending `Completer`). It exposes `__init__()`, `get_completions()`, `get_completion_items()`, `get_replacement_range()`.

**Public API:**

- `def __init__()`
- `def get_completions()`
- `def get_completion_items()`
- `def get_replacement_range()`

## [**PathCompleter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/completers.py#L69)

The [**PathCompleter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/completers.py#L69) class (extending `Completer`). It exposes `__init__()`, `get_completions()`, `get_completion_items()`, `get_replacement_range()`. Internally it relies on `_build_search_context()`, `_matches_prefix()`, `_score_matches()`.

**Public API:**

- `def __init__()`
- `def get_completions()`
- `def get_completion_items()`
- `def get_replacement_range()`

**Internal helpers:**

- `_build_search_context()`
- `_matches_prefix()`
- `_score_matches()`

## [**MultiCompleter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/completers.py#L232)

The [**MultiCompleter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/completers.py#L232) class (extending `Completer`). It exposes `__init__()`, `get_completions()`, `get_replacement_range()`.

**Public API:**

- `def __init__()`
- `def get_completions()`
- `def get_replacement_range()`

