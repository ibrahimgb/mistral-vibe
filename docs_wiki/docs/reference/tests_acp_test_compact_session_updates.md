---
title: "tests.acp.test_compact_session_updates"
tldr: "Module tests.acp.test_compact_session_updates"
tags: [reference, api]
---

# `tests.acp.test_compact_session_updates`

**Source:** [`tests/acp/test_compact_session_updates.py`](tests/acp/test_compact_session_updates.py) · 80 lines

## `TestCompactEventHandling`

**Source:** [`tests/acp/test_compact_session_updates.py#L33`](tests/acp/test_compact_session_updates.py#L33)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_prompt_handles_compact_events()` | acp_agent_loop | `None` | Verify prompt() sends tool_call session updates for compact events. |

## `acp_agent_loop()`

```python
def acp_agent_loop(backend: FakeBackend) -> VibeAcpAgentLoop
```

**Source:** [`tests/acp/test_compact_session_updates.py#L18`](tests/acp/test_compact_session_updates.py#L18)

