---
title: "vibe.cli.update_notifier.update"
tldr: "Module vibe.cli.update_notifier.update"
tags: [reference, api]
---

# [**vibe.cli.update_notifier.update**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/update.py)

This module defines the constants `UPDATE_CACHE_TTL_SECONDS`, `UPDATE_COMMANDS`.

## [**UpdateAvailability**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/update.py#L23)

The [**UpdateAvailability**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/update.py#L23) dataclass. Key fields include `latest_version`, `should_notify`.

## [**UpdateError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/update.py#L28)

The [**UpdateError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/update.py#L28) class (extending `Exception`). It exposes `__init__()`.

**Public API:**

- `def __init__()`

## [**get_update_if_available()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/update.py#L82)

```python
async def get_update_if_available(update_notifier: UpdateGateway, current_version: str, update_cache_repository: UpdateCacheRepository, get_current_timestamp: Callable[[], int]) -> UpdateAvailability | None
```

## [**do_update()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/update.py#L128)

```python
async def do_update() -> bool
```

