---
title: "tests.acp.test_set_config_option"
tldr: "Module tests.acp.test_set_config_option"
tags: [reference, api]
---

# `tests.acp.test_set_config_option`

**Source:** [`tests/acp/test_set_config_option.py`](tests/acp/test_set_config_option.py) · 287 lines

## `TestACPSetConfigOptionMode`

**Source:** [`tests/acp/test_set_config_option.py#L57`](tests/acp/test_set_config_option.py#L57)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_set_config_option_mode_to_auto_approve()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_config_option_mode_to_plan()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_config_option_mode_invalid_returns_none()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_config_option_mode_empty_string_returns_none()` | acp_agent_loop | `None` | — |

## `TestACPSetConfigOptionModel`

**Source:** [`tests/acp/test_set_config_option.py#L152`](tests/acp/test_set_config_option.py#L152)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_set_config_option_model_success()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_config_option_model_invalid_returns_none()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_config_option_model_empty_string_returns_none()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_config_option_model_saves_to_config()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_config_option_model_does_not_save_on_invalid()` | acp_agent_loop | `None` | — |

## `TestACPSetConfigOptionInvalidConfigId`

**Source:** [`tests/acp/test_set_config_option.py#L258`](tests/acp/test_set_config_option.py#L258)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_set_config_option_invalid_config_id_returns_none()` | acp_agent_loop | `None` | — |
| 🔄 `test_set_config_option_empty_config_id_returns_none()` | acp_agent_loop | `None` | — |

## `acp_agent_loop()`

```python
def acp_agent_loop(backend) -> VibeAcpAgentLoop
```

**Source:** [`tests/acp/test_set_config_option.py#L17`](tests/acp/test_set_config_option.py#L17)

