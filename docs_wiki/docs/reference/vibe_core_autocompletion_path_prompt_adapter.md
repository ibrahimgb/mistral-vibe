---
title: "vibe.core.autocompletion.path_prompt_adapter"
tldr: "Module vibe.core.autocompletion.path_prompt_adapter"
tags: [reference, api]
---

# [**vibe.core.autocompletion.path_prompt_adapter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/path_prompt_adapter.py)

This module defines the constants `DEFAULT_MAX_EMBED_BYTES`, `BINARY_MIME_PREFIXES`.

## [**render_path_prompt()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/path_prompt_adapter.py#L18)

```python
def render_path_prompt(message: str) -> str
```

## [**_path_prompt_to_content_blocks()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/path_prompt_adapter.py#L29)

```python
def _path_prompt_to_content_blocks(payload: PathPromptPayload) -> list[ResourceBlock]
```

## [**_format_content_block()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/path_prompt_adapter.py#L89)

```python
def _format_content_block(block: ResourceBlock) -> str | None
```

## [**_is_probably_text()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/path_prompt_adapter.py#L128)

```python
def _is_probably_text(path: PathResource, data: bytes) -> bool
```

