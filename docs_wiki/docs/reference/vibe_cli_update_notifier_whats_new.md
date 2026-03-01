---
title: "vibe.cli.update_notifier.whats_new"
tldr: "Module vibe.cli.update_notifier.whats_new"
tags: [reference, api]
---

# [**vibe.cli.update_notifier.whats_new**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/whats_new.py)

## [**should_show_whats_new()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/whats_new.py#L12)

```python
async def should_show_whats_new(current_version: str, repository: UpdateCacheRepository) -> bool
```

## [**load_whats_new_content()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/whats_new.py#L21)

```python
def load_whats_new_content() -> str | None
```

## [**mark_version_as_seen()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/whats_new.py#L32)

```python
async def mark_version_as_seen(version: str, repository: UpdateCacheRepository) -> None
```

