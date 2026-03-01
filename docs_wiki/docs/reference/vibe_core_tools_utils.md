---
title: "vibe.core.tools.utils"
tldr: "Module vibe.core.tools.utils"
tags: [reference, api]
---

# [**vibe.core.tools.utils**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/utils.py)

## [**resolve_path_permission()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/utils.py#L9)

```python
def resolve_path_permission(path_str: str) -> ToolPermission | None
```

Resolve permission for a file path against glob patterns.

Returns NEVER on denylist match, ALWAYS on allowlist match, None otherwise.

## [**is_path_within_workdir()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/utils.py#L32)

```python
def is_path_within_workdir(path_str: str) -> bool
```

Return True if the resolved path is inside cwd.

## [**resolve_file_tool_permission()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/utils.py#L44)

```python
def resolve_file_tool_permission(path_str: str) -> ToolPermission | None
```

Resolve permission for a file-based tool invocation.

Checks allowlist/denylist first, then escalates to ASK for paths outside
the working directory (unless the tool is configured as NEVER).
Returns None to fall back to the tool's default config permission.

