---
title: "vibe.core.session.session_migration"
tldr: "Module vibe.core.session.session_migration"
tags: [reference, api]
---

# [**vibe.core.session.session_migration**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/session/session_migration.py)

## [**migrate_sessions_entrypoint()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/session/session_migration.py#L11)

```python
def migrate_sessions_entrypoint(session_config: SessionLoggingConfig) -> int
```

## [**migrate_sessions()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/session/session_migration.py#L15)

```python
async def migrate_sessions(session_config: SessionLoggingConfig) -> int
```

Helper for migrating session data from singular JSON files to the format introduced in Vibe 2.0 with per-session folders with split metadata and message files.

