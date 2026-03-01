---
title: "vibe.cli.textual_ui.windowing.history_windowing"
tldr: "Module vibe.cli.textual_ui.windowing.history_windowing"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.windowing.history_windowing**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history_windowing.py)

## [**HistoryResumePlan**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history_windowing.py#L19)

The [**HistoryResumePlan**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history_windowing.py#L19) dataclass. Key fields include `tool_call_map`, `tail_messages`, `backfill_messages`, `tail_start_index`.

**Public API:**

- `def has_backfill()`

## [**should_resume_history()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history_windowing.py#L30)

```python
def should_resume_history(messages_children: list[Widget]) -> bool
```

## [**create_resume_plan()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history_windowing.py#L34)

```python
def create_resume_plan(history_messages: list[LLMMessage], tail_size: int) -> HistoryResumePlan | None
```

## [**sync_backfill_state()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history_windowing.py#L50)

```python
def sync_backfill_state() -> tuple[bool, dict[str, str] | None]
```

