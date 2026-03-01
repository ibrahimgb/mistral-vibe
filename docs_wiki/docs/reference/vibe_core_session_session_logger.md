---
title: "vibe.core.session.session_logger"
tldr: "Module vibe.core.session.session_logger"
tags: [reference, api]
---

# [**vibe.core.session.session_logger**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/session/session_logger.py)

This module defines the constants `TMP_CLEANUP_INTERVAL`.

## [**SessionLogger**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/session/session_logger.py#L32)

The [**SessionLogger**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/session/session_logger.py#L32) class. It exposes `__init__()`, `persist_metadata()`, `persist_messages()`, `save_interaction()`, `reset_session()` among 8 public methods.

**Public API:**

- `def __init__()`
- `def save_folder()`
- `def metadata_filepath()`
- `def messages_filepath()`
- `def git_commit()`
- `def git_branch()`
- `def username()`
- `async def persist_metadata()`
- `async def persist_messages()`
- `async def save_interaction()`
- `def reset_session()` — Clear existing session info and setup a new session
- `def resume_existing_session()`
- `def cleanup_tmp_files()` — Delete temporary files created more than 5 minutes ago
- `def maybe_cleanup_tmp_files()`

