---
title: "vibe.core.session.session_loader"
tldr: "Module vibe.core.session.session_loader"
tags: [reference, api]
---

# [**vibe.core.session.session_loader**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/session/session_loader.py)

This module defines the constants `METADATA_FILENAME`, `MESSAGES_FILENAME`.

## [**SessionInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/session/session_loader.py#L18)

The [**SessionInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/session/session_loader.py#L18) class (extending `TypedDict`).

## [**SessionLoader**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/session/session_loader.py#L25)

The [**SessionLoader**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/session/session_loader.py#L25) class. It exposes `latest_session()`, `find_latest_session()`, `find_session_by_id()`, `does_session_exist()`, `list_sessions()` among 8 public methods. Internally it relies on `_is_valid_session()`.

**Public API:**

- `def latest_session()`
- `def find_latest_session()`
- `def find_session_by_id()`
- `def does_session_exist()`
- `def list_sessions()`
- `def load_metadata()`
- `def load_session()`
- `def get_first_user_message()` — Get the first user message from a session for preview.

**Internal helpers:**

- `_is_valid_session()` — Check if a session directory contains valid metadata and messages.

