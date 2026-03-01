---
title: "vibe.core.tools.mcp.registry"
tldr: "Module vibe.core.tools.mcp.registry"
tags: [reference, api]
---

# [**vibe.core.tools.mcp.registry**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/registry.py)

## [**MCPRegistry**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/registry.py#L21)

The [**MCPRegistry**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/registry.py#L21) class shared cache for mcp server tool discovery. It exposes `__init__()`, `get_tools()`, `clear()`. Internally it relies on `_discover_http()`, `_discover_stdio()`.

**Public API:**

- `def __init__()`
- `def get_tools()` — Return proxy tool classes for *servers*, using cache when possible.
- `def clear()` — Drop all cached entries, forcing re-discovery on next use.

**Internal helpers:**

- `_discover_http()`
- `_discover_stdio()`

