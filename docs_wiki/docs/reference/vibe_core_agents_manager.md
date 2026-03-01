---
title: "vibe.core.agents.manager"
tldr: "Module vibe.core.agents.manager"
tags: [reference, api]
---

# [**vibe.core.agents.manager**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agents/manager.py)

## [**AgentManager**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agents/manager.py#L22)

The [**AgentManager**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/agents/manager.py#L22) class. It exposes `__init__()`, `switch_profile()`, `register_agent()`, `invalidate_config()`, `get_agent()` among 8 public methods. Internally it relies on `_discover_agents()`.

**Public API:**

- `def __init__()`
- `def available_agents()`
- `def config()`
- `def switch_profile()`
- `def register_agent()`
- `def invalidate_config()`
- `def get_agent()`
- `def get_subagents()`
- `def get_agent_order()`
- `def next_agent()`

**Internal helpers:**

- `_discover_agents()`

