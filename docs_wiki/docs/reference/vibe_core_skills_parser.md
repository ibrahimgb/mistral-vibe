---
title: "vibe.core.skills.parser"
tldr: "Module vibe.core.skills.parser"
tags: [reference, api]
---

# [**vibe.core.skills.parser**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/skills/parser.py)

This module defines the constants `FM_BOUNDARY`.

## [**SkillParseError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/skills/parser.py#L9)

The [**SkillParseError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/skills/parser.py#L9) class (extending `Exception`). It exposes `__init__()`.

**Public API:**

- `def __init__()`

## [**parse_frontmatter()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/skills/parser.py#L18)

```python
def parse_frontmatter(content: str) -> tuple[dict[str, Any], str]
```

