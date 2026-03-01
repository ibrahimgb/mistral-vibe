---
title: "vibe.cli.update_notifier.ports.update_cache_repository"
tldr: "Module vibe.cli.update_notifier.ports.update_cache_repository"
tags: [reference, api]
---

# [**vibe.cli.update_notifier.ports.update_cache_repository**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_cache_repository.py)

## [**UpdateCache**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_cache_repository.py#L8)

The [**UpdateCache**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_cache_repository.py#L8) dataclass. Key fields include `latest_version`, `stored_at_timestamp`, `seen_whats_new_version`.

## [**UpdateCacheRepository**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_cache_repository.py#L14)

The [**UpdateCacheRepository**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_cache_repository.py#L14) protocol (extending `Protocol`). It exposes `get()`, `set()`.

**Public API:**

- `async def get()`
- `async def set()`

