---
title: "tests.acp.test_proxy_setup_acp"
tldr: "Module tests.acp.test_proxy_setup_acp"
tags: [reference, api]
---

# `tests.acp.test_proxy_setup_acp`

**Source:** [`tests/acp/test_proxy_setup_acp.py`](tests/acp/test_proxy_setup_acp.py) · 271 lines

## `TestAvailableCommandsUpdate`

**Source:** [`tests/acp/test_proxy_setup_acp.py#L36`](tests/acp/test_proxy_setup_acp.py#L36)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_available_commands_sent_on_new_session()` | acp_agent_loop | `None` | — |

## `TestProxySetupCommand`

**Source:** [`tests/acp/test_proxy_setup_acp.py#L59`](tests/acp/test_proxy_setup_acp.py#L59)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_proxy_setup_shows_help_when_no_args()` | acp_agent_loop, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_proxy_setup_sets_value()` | acp_agent_loop, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_proxy_setup_unsets_value()` | acp_agent_loop, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_proxy_setup_invalid_key_returns_error()` | acp_agent_loop, tmp_path, monkeypatch | `None` | — |
| 🔄 `test_proxy_setup_case_insensitive()` | acp_agent_loop, tmp_path, monkeypatch | `None` | — |

## `acp_agent_loop()`

```python
def acp_agent_loop(backend) -> VibeAcpAgentLoop
```

**Source:** [`tests/acp/test_proxy_setup_acp.py#L17`](tests/acp/test_proxy_setup_acp.py#L17)

## `_get_fake_client()`

```python
def _get_fake_client(acp_agent_loop: VibeAcpAgentLoop) -> FakeClient
```

**Source:** [`tests/acp/test_proxy_setup_acp.py#L31`](tests/acp/test_proxy_setup_acp.py#L31)

