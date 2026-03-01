---
title: "vibe.cli.textual_ui.windowing.state"
tldr: "Module vibe.cli.textual_ui.windowing.state"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.windowing.state**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/state.py)

This module defines the constants `HISTORY_RESUME_TAIL_MESSAGES`, `LOAD_MORE_BATCH_SIZE`.

## [**LoadMoreBatch**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/state.py#L15)

The [**LoadMoreBatch**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/state.py#L15) dataclass. Key fields include `start_index`, `messages`.

## [**SessionWindowing**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/state.py#L20)

The [**SessionWindowing**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/state.py#L20) class. It exposes `__init__()`, `reset()`, `set_backfill()`, `next_load_more_batch()`, `recompute_backfill()`.

**Public API:**

- `def __init__()`
- `def remaining()`
- `def has_backfill()`
- `def reset()`
- `def set_backfill()`
- `def next_load_more_batch()`
- `def recompute_backfill()`

## [**HistoryLoadMoreManager**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/state.py#L71)

The [**HistoryLoadMoreManager**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/state.py#L71) class. It exposes `__init__()`, `show()`, `hide()`, `set_visible()`, `set_enabled()` among 6 public methods.

**Public API:**

- `def __init__()`
- `async def show()`
- `async def hide()`
- `async def set_visible()`
- `def set_enabled()`
- `def set_remaining()`

