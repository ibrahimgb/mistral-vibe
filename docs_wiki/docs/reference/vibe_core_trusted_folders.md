---
title: "vibe.core.trusted_folders"
tldr: "Module vibe.core.trusted_folders"
tags: [reference, api]
---

# [**vibe.core.trusted_folders**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/trusted_folders.py)

This module defines the constants `AGENTS_MD_FILENAMES`.

## [**TrustedFoldersManager**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/trusted_folders.py#L25)

The [**TrustedFoldersManager**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/trusted_folders.py#L25) class. It exposes `__init__()`, `is_trusted()`, `add_trusted()`, `add_untrusted()`.

**Public API:**

- `def __init__()`
- `def is_trusted()`
- `def add_trusted()`
- `def add_untrusted()`

## [**has_agents_md_file()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/trusted_folders.py#L14)

```python
def has_agents_md_file(path: Path) -> bool
```

## [**has_trustable_content()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/trusted_folders.py#L18)

```python
def has_trustable_content(path: Path) -> bool
```

