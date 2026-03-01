---
title: "tests.core.test_agents"
tldr: "Module tests.core.test_agents"
tags: [reference, api]
---

# `tests.core.test_agents`

**Source:** [`tests/core/test_agents.py`](tests/core/test_agents.py) · 80 lines

## `TestAgentProfile`

**Source:** [`tests/core/test_agents.py#L10`](tests/core/test_agents.py#L10)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_explore_agent_is_subagent()` |  | `None` | Test that EXPLORE agent has SUBAGENT type. |
| `test_explore_agent_has_safe_safety()` |  | `None` | Test that EXPLORE agent has SAFE safety level. |
| `test_explore_agent_has_enabled_tools()` |  | `None` | Test that EXPLORE agent has expected enabled tools. |
| `test_builtin_agents_contains_explore()` |  | `None` | Test that BUILTIN_AGENTS includes explore. |

## `TestAgentManager`

**Source:** [`tests/core/test_agents.py#L31`](tests/core/test_agents.py#L31)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `manager()` |  | `AgentManager` | — |
| `test_get_subagents_returns_only_subagents()` | manager | `None` | Test that only SUBAGENT type agents are returned. |
| `test_get_subagents_includes_explore()` | manager | `None` | Test that EXPLORE is included in subagents. |
| `test_get_subagents_excludes_agents()` | manager | `None` | Test that AGENT type agents are not returned. |
| `test_get_builtin_agent()` | manager | `None` | Test getting a builtin agent by name. |
| `test_get_nonexistent_agent_raises()` | manager | `None` | Test that getting a nonexistent agent raises ValueError. |
| `test_get_default_agent()` | manager | `None` | Test getting the default agent. |

