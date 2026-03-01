---
title: "vibe.core.teleport.git"
tldr: "Module vibe.core.teleport.git"
tags: [reference, api]
---

# [**vibe.core.teleport.git**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/git.py)

## [**GitRepoInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/git.py#L18)

The [**GitRepoInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/git.py#L18) dataclass. Key fields include `remote_url`, `owner`, `repo`, `branch`, `commit`, `diff`.

## [**GitRepository**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/git.py#L27)

The [**GitRepository**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/git.py#L27) class. It exposes `__init__()`, `__aenter__()`, `__aexit__()`, `is_supported()`, `get_info()` among 8 public methods.

**Public API:**

- `def __init__()`
- `async def __aenter__()`
- `async def __aexit__()`
- `async def is_supported()`
- `async def get_info()`
- `async def is_commit_pushed()`
- `async def get_unpushed_commit_count()`
- `async def push_current_branch()`

