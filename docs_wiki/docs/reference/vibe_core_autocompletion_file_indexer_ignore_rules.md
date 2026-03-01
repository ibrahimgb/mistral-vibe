---
title: "vibe.core.autocompletion.file_indexer.ignore_rules"
tldr: "Module vibe.core.autocompletion.file_indexer.ignore_rules"
tags: [reference, api]
---

# [**vibe.core.autocompletion.file_indexer.ignore_rules**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/ignore_rules.py)

This module defines the constants `DEFAULT_IGNORE_PATTERNS`, `WALK_SKIP_DIR_NAMES`.

## [**CompiledPattern**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/ignore_rules.py#L48)

The [**CompiledPattern**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/ignore_rules.py#L48) dataclass. Key fields include `raw`, `stripped`, `is_exclude`, `dir_only`, `name_only`, `anchor_root`.

## [**IgnoreRules**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/ignore_rules.py#L57)

The [**IgnoreRules**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/ignore_rules.py#L57) class. It exposes `__init__()`, `get_walk_skip_dir_names()`, `ensure_for_root()`, `should_ignore()`, `reset()`. Internally it relies on `_build_patterns()`.

**Public API:**

- `def __init__()`
- `def get_walk_skip_dir_names()`
- `def ensure_for_root()`
- `def should_ignore()`
- `def reset()`

**Internal helpers:**

- `_build_patterns()`

