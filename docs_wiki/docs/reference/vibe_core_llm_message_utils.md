---
title: "vibe.core.llm.message_utils"
tldr: "Module vibe.core.llm.message_utils"
tags: [reference, api]
---

# [**vibe.core.llm.message_utils**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/message_utils.py)

## [**merge_consecutive_user_messages()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/message_utils.py#L8)

```python
def merge_consecutive_user_messages(messages: Sequence[LLMMessage]) -> list[LLMMessage]
```

Merge consecutive user messages into a single message.

This handles cases where middleware injects messages resulting in
consecutive user messages before sending to the API.

