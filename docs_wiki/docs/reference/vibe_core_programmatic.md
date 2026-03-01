---
title: "vibe.core.programmatic"
tldr: "Module vibe.core.programmatic"
tags: [reference, api]
---

# [**vibe.core.programmatic**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/programmatic.py)

This module defines the constants `_DEFAULT_CLIENT_METADATA`.

## [**run_programmatic()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/programmatic.py#L24)

```python
def run_programmatic(config: VibeConfig, prompt: str, max_turns: int | None, max_price: float | None, output_format: OutputFormat, previous_messages: list[LLMMessage] | None, agent_name: str, client_metadata: ClientMetadata) -> str | None
```

