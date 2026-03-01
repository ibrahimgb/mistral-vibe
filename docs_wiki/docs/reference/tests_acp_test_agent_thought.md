---
title: "tests.acp.test_agent_thought"
tldr: "Module tests.acp.test_agent_thought"
tags: [reference, api]
---

# `tests.acp.test_agent_thought`

**Source:** [`tests/acp/test_agent_thought.py`](tests/acp/test_agent_thought.py) · 154 lines

## `TestACPAgentThought`

**Source:** [`tests/acp/test_agent_thought.py#L54`](tests/acp/test_agent_thought.py#L54)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_prompt_with_reasoning_emits_agent_thought_chunk()` | acp_agent_loop_with_reasoning | `None` | — |
| 🔄 `test_prompt_without_reasoning_does_not_emit_agent_thought_chunk()` | acp_agent_loop | `None` | — |
| 🔄 `test_agent_thought_chunk_contains_text_content_block()` | acp_agent_loop_with_reasoning | `None` | — |
| 🔄 `test_agent_thought_chunk_contains_message_id()` | acp_agent_loop_with_reasoning | `None` | — |

## `_create_backend_with_reasoning()`

```python
def _create_backend_with_reasoning(reasoning_content: str, content: str) -> FakeBackend
```

**Source:** [`tests/acp/test_agent_thought.py#L18`](tests/acp/test_agent_thought.py#L18)

## `backend_with_reasoning()`

```python
def backend_with_reasoning() -> FakeBackend
```

**Source:** [`tests/acp/test_agent_thought.py#L34`](tests/acp/test_agent_thought.py#L34)

## `acp_agent_loop_with_reasoning()`

```python
def acp_agent_loop_with_reasoning(backend_with_reasoning: FakeBackend) -> VibeAcpAgentLoop
```

**Source:** [`tests/acp/test_agent_thought.py#L39`](tests/acp/test_agent_thought.py#L39)

