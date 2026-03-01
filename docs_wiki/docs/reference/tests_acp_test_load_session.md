---
title: "tests.acp.test_load_session"
tldr: "Module tests.acp.test_load_session"
tags: [reference, api]
---

# `tests.acp.test_load_session`

**Source:** [`tests/acp/test_load_session.py`](tests/acp/test_load_session.py) · 344 lines

## `TestLoadSession`

**Source:** [`tests/acp/test_load_session.py#L62`](tests/acp/test_load_session.py#L62)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_load_session_response_structure()` | acp_agent_with_session_config, temp_session_dir, create_test_session | `None` | — |
| 🔄 `test_load_session_registers_session_with_original_id()` | acp_agent_with_session_config, temp_session_dir, create_test_session | `None` | — |
| 🔄 `test_load_session_injects_messages_into_agent_loop()` | acp_agent_with_session_config, temp_session_dir, create_test_session | `None` | — |
| 🔄 `test_load_session_replays_user_messages()` | acp_agent_with_session_config, temp_session_dir, create_test_session | `None` | — |
| 🔄 `test_load_session_replays_assistant_messages()` | acp_agent_with_session_config, temp_session_dir, create_test_session | `None` | — |
| 🔄 `test_load_session_replays_tool_calls()` | acp_agent_with_session_config, temp_session_dir, create_test_session | `None` | — |
| 🔄 `test_load_session_replays_reasoning_content()` | acp_agent_with_session_config, temp_session_dir, create_test_session | `None` | — |
| 🔄 `test_load_session_not_found_raises_error()` | acp_agent_with_session_config | `None` | — |
| 🔄 `test_load_session_replays_full_conversation()` | acp_agent_with_session_config, temp_session_dir, create_test_session | `None` | — |

## `acp_agent_with_session_config()`

```python
def acp_agent_with_session_config(backend: FakeBackend, temp_session_dir: Path, monkeypatch: pytest.MonkeyPatch) -> tuple[VibeAcpAgentLoop, FakeClient]
```

**Source:** [`tests/acp/test_load_session.py#L26`](tests/acp/test_load_session.py#L26)

