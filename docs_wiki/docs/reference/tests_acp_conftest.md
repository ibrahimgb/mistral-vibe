---
title: "tests.acp.conftest"
tldr: "Module tests.acp.conftest"
tags: [reference, api]
---

# `tests.acp.conftest`

**Source:** [`tests/acp/conftest.py`](tests/acp/conftest.py) · 97 lines

## `backend()`

```python
def backend() -> FakeBackend
```

**Source:** [`tests/acp/conftest.py#L18`](tests/acp/conftest.py#L18)

## `_create_acp_agent()`

```python
def _create_acp_agent() -> VibeAcpAgentLoop
```

**Source:** [`tests/acp/conftest.py#L28`](tests/acp/conftest.py#L28)

## `acp_agent_loop()`

```python
def acp_agent_loop(backend: FakeBackend) -> VibeAcpAgentLoop
```

**Source:** [`tests/acp/conftest.py#L39`](tests/acp/conftest.py#L39)

## `temp_session_dir()`

```python
def temp_session_dir(tmp_path: Path) -> Path
```

**Source:** [`tests/acp/conftest.py#L49`](tests/acp/conftest.py#L49)

## `create_test_session()`

```python
def create_test_session()
```

Create a test session with configurable messages and metadata.

Supports both messages parameter (for load_session tests) and
end_time parameter (for list_sessions tests).

**Source:** [`tests/acp/conftest.py#L56`](tests/acp/conftest.py#L56)

