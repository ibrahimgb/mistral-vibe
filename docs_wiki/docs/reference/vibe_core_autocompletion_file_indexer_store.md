---
title: "vibe.core.autocompletion.file_indexer.store"
tldr: "Module vibe.core.autocompletion.file_indexer.store"
tags: [reference, api]
---

# [**vibe.core.autocompletion.file_indexer.store**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/store.py)

## [**FileIndexStats**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/store.py#L13)

The [**FileIndexStats**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/store.py#L13) dataclass. Key fields include `rebuilds`, `incremental_updates`.

## [**IndexEntry**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/store.py#L19)

The [**IndexEntry**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/store.py#L19) dataclass. Key fields include `rel`, `rel_lower`, `name`, `path`, `is_dir`.

## [**FileIndexStore**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/store.py#L27)

The [**FileIndexStore**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/store.py#L27) class. It exposes `__init__()`, `clear()`, `rebuild()`, `snapshot()`, `apply_changes()`. Internally it relies on `_walk_directory()`.

**Public API:**

- `def __init__()`
- `def root()`
- `def clear()`
- `def rebuild()`
- `def snapshot()`
- `def apply_changes()`

**Internal helpers:**

- `_walk_directory()`

