---
title: "vibe.core.autocompletion.path_prompt"
tldr: "Module vibe.core.autocompletion.path_prompt"
tags: [reference, api]
---

# [**vibe.core.autocompletion.path_prompt**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/path_prompt.py)

## [**PathResource**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/path_prompt.py#L9)

The [**PathResource**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/path_prompt.py#L9) dataclass. Key fields include `path`, `alias`, `kind`.

## [**PathPromptPayload**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/path_prompt.py#L16)

The [**PathPromptPayload**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/path_prompt.py#L16) dataclass. Key fields include `display_text`, `prompt_text`, `resources`.

## [**build_path_prompt_payload()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/autocompletion/path_prompt.py#L22)

```python
def build_path_prompt_payload(message: str) -> PathPromptPayload
```

