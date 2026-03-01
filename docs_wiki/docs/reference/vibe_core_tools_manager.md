---
title: "vibe.core.tools.manager"
tldr: "Module vibe.core.tools.manager"
tags: [reference, api]
---

# [**vibe.core.tools.manager**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/manager.py)

## [**NoSuchToolError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/manager.py#L57)

The [**NoSuchToolError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/manager.py#L57) class (extending `Exception`) exception raised when a tool is not found.

## [**ToolManager**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/manager.py#L61)

The [**ToolManager**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/manager.py#L61) class manages tool discovery and instantiation for an agent. It exposes `__init__()`, `discover_tool_defaults()`, `get_tool_config()`, `get()`, `reset_all()` among 6 public methods. Internally it relies on `_iter_tool_classes()`, `_load_tools_from_file()`.

**Public API:**

- `def __init__()`
- `def discover_tool_defaults()`
- `def available_tools()`
- `def get_tool_config()`
- `def get()` — Get a tool instance, creating it lazily on first call.
- `def reset_all()`
- `def invalidate_tool()`

**Internal helpers:**

- `_iter_tool_classes()` — Iterate over all search_paths to find tool classes.
- `_load_tools_from_file()`

## [**_try_canonical_module_name()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/manager.py#L23)

```python
def _try_canonical_module_name(path: Path) -> str | None
```

Extract canonical module name for vibe package files.

Prevents Pydantic class identity mismatches when the same module
is imported via dynamic discovery and regular imports.

## [**_compute_module_name()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/manager.py#L46)

```python
def _compute_module_name(path: Path) -> str
```

Return canonical module name for vibe files, hash-based synthetic name otherwise.

