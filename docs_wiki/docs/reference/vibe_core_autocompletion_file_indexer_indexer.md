---
title: "vibe.core.autocompletion.file_indexer.indexer"
tldr: "Module vibe.core.autocompletion.file_indexer.indexer"
tags: [reference, api]
---

# [**vibe.core.autocompletion.file_indexer.indexer**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/indexer.py)

## [**_RebuildTask**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/indexer.py#L20)

The [**_RebuildTask**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/indexer.py#L20) dataclass. Key fields include `cancel_event`, `done_event`.

## [**FileIndexer**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/indexer.py#L25)

The [**FileIndexer**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/file_indexer/indexer.py#L25) class. It exposes `__init__()`, `get_index()`, `refresh()`, `shutdown()`, `__del__()`. Internally it relies on `_rebuild_worker()`.

**Public API:**

- `def __init__()`
- `def stats()`
- `def get_index()`
- `def refresh()`
- `def shutdown()`
- `def __del__()`

**Internal helpers:**

- `_rebuild_worker()`

