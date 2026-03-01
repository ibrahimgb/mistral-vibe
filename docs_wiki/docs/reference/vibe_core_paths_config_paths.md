---
title: "vibe.core.paths.config_paths"
tldr: "Module vibe.core.paths.config_paths"
tags: [reference, api]
---

# [**vibe.core.paths.config_paths**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/paths/config_paths.py)

This module defines the constants `CONFIG_FILE`, `CONFIG_DIR`, `PROMPTS_DIR`, `HISTORY_FILE`.

## [**ConfigPath**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/paths/config_paths.py#L13)

The [**ConfigPath**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/paths/config_paths.py#L13) class (extending `GlobalPath`).

**Public API:**

- `def path()`

## [**discover_local_tools_dirs()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/paths/config_paths.py#L43)

```python
def discover_local_tools_dirs(root: Path) -> list[Path]
```

## [**discover_local_skills_dirs()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/paths/config_paths.py#L47)

```python
def discover_local_skills_dirs(root: Path) -> list[Path]
```

## [**discover_local_agents_dirs()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/paths/config_paths.py#L51)

```python
def discover_local_agents_dirs(root: Path) -> list[Path]
```

## [**unlock_config_paths()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/paths/config_paths.py#L55)

```python
def unlock_config_paths() -> None
```

