---
title: "vibe.core.skills.models"
tldr: "Module vibe.core.skills.models"
tags: [reference, api]
---

# [**vibe.core.skills.models**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/skills/models.py)

## [**SkillMetadata**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/skills/models.py#L9)

The [**SkillMetadata**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/skills/models.py#L9) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `name`, `description`, `license`, `compatibility`, `metadata`, `allowed_tools`, `user_invocable`. It exposes `parse_allowed_tools()`, `normalize_metadata()`.

**Public API:**

- `def parse_allowed_tools()`
- `def normalize_metadata()`

## [**SkillInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/skills/models.py#L65)

The [**SkillInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/skills/models.py#L65) Pydantic model (extending `BaseModel`). Key fields include `name`, `description`, `license`, `compatibility`, `metadata`, `allowed_tools`, `user_invocable`, `skill_path`, …. It exposes `from_metadata()`.

**Public API:**

- `def skill_dir()`
- `def from_metadata()`

