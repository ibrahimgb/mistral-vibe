---
title: "vibe.core.agents.models"
tldr: "Module vibe.core.agents.models"
tags: [reference, api]
---

# [**vibe.core.agents.models**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agents/models.py)

This module defines the constants `CHAT_AGENT_TOOLS`, `PLAN_AGENT_TOOLS`, `DEFAULT`, `PLAN`, `CHAT`, `ACCEPT_EDITS`, `AUTO_APPROVE`, `EXPLORE`, `BUILTIN_AGENTS`.

## [**AgentSafety**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agents/models.py#L23)

The [**AgentSafety**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agents/models.py#L23) enum (extending `StrEnum`). Key fields include `SAFE`, `NEUTRAL`, `DESTRUCTIVE`, `YOLO`.

## [**AgentType**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agents/models.py#L30)

The [**AgentType**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agents/models.py#L30) enum (extending `StrEnum`). Key fields include `AGENT`, `SUBAGENT`.

## [**BuiltinAgentName**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agents/models.py#L35)

The [**BuiltinAgentName**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agents/models.py#L35) enum (extending `StrEnum`). Key fields include `DEFAULT`, `CHAT`, `PLAN`, `ACCEPT_EDITS`, `AUTO_APPROVE`, `EXPLORE`.

## [**AgentProfile**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agents/models.py#L45)

The [**AgentProfile**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agents/models.py#L45) dataclass. Key fields include `name`, `display_name`, `description`, `safety`, `agent_type`, `overrides`. It exposes `apply_to_config()`, `from_toml()`.

**Public API:**

- `def apply_to_config()`
- `def from_toml()`

