---
title: "vibe.cli.textual_ui.windowing.history"
tldr: "Module vibe.cli.textual_ui.windowing.history"
tags: [reference, api]
---

# [**vibe.cli.textual_ui.windowing.history**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history.py)

## [**non_system_history_messages()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history.py#L17)

```python
def non_system_history_messages(messages: Sequence[LLMMessage]) -> list[LLMMessage]
```

## [**build_tool_call_map()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history.py#L21)

```python
def build_tool_call_map(messages: Sequence[LLMMessage]) -> dict[str, str]
```

## [**build_history_widgets()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history.py#L32)

```python
def build_history_widgets(batch: Sequence[LLMMessage], tool_call_map: dict[str, str]) -> list[Widget]
```

## [**split_history_tail()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history.py#L79)

```python
def split_history_tail(history_messages: list[LLMMessage], tail_size: int) -> tuple[list[LLMMessage], list[LLMMessage], int]
```

## [**visible_history_indices()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history.py#L88)

```python
def visible_history_indices(children: list[Widget], history_widget_indices: WeakKeyDictionary[Widget, int]) -> list[int]
```

## [**visible_history_widgets_count()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/textual_ui/windowing/history.py#L98)

```python
def visible_history_widgets_count(children: list[Widget]) -> int
```

