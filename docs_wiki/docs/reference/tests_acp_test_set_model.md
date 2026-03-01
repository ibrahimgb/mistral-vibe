---
title: "tests.acp.test_set_model"
tldr: "Module tests.acp.test_set_model"
tags: [reference, api]
---

# `tests.acp.test_set_model`

**Source:** [`tests/acp/test_set_model.py`](tests/acp/test_set_model.py) · 306 lines

## `TestACPSetModel`

**Source:** [`tests/acp/test_set_model.py#L57`](tests/acp/test_set_model.py#L57)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_set_model_success()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_model_invalid_model_returns_none()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_model_to_same_model()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_model_saves_to_config()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_model_does_not_save_on_invalid_model()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_model_with_empty_string()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_model_updates_active_model()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_model_calls_reload_with_initial_messages()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_model_preserves_conversation_history()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_model_resets_stats_with_new_model_pricing()` | acp_agent_loop | `None` | — |

## `acp_agent_loop()`

```python
def acp_agent_loop(backend) -> VibeAcpAgentLoop
```

**Source:** [`tests/acp/test_set_model.py#L17`](tests/acp/test_set_model.py#L17)

