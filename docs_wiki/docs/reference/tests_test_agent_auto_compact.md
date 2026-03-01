---
title: "tests.test_agent_auto_compact"
tldr: "Module tests.test_agent_auto_compact"
tags: [reference, api]
---

# `tests.test_agent_auto_compact`

**Source:** [`tests/test_agent_auto_compact.py`](tests/test_agent_auto_compact.py) · 123 lines

## `test_auto_compact_emits_correct_events()`

```python
async def test_auto_compact_emits_correct_events(telemetry_events: list[dict]) -> None
```

**Source:** [`tests/test_agent_auto_compact.py#L19`](tests/test_agent_auto_compact.py#L19)

## `test_auto_compact_observer_sees_user_msg_not_summary()`

```python
async def test_auto_compact_observer_sees_user_msg_not_summary() -> None
```

Observer sees the original user message and final response.

Compact internals (summary request, LLM summary) are invisible
to the observer because they happen inside silent() / reset().

**Source:** [`tests/test_agent_auto_compact.py#L53`](tests/test_agent_auto_compact.py#L53)

## `test_auto_compact_observer_does_not_see_summary_request()`

```python
async def test_auto_compact_observer_does_not_see_summary_request() -> None
```

The compact summary request and LLM response must not leak to observer.

**Source:** [`tests/test_agent_auto_compact.py#L83`](tests/test_agent_auto_compact.py#L83)

## `test_compact_replaces_messages_with_summary()`

```python
async def test_compact_replaces_messages_with_summary() -> None
```

After compact, messages list contains only system + summary.

**Source:** [`tests/test_agent_auto_compact.py#L108`](tests/test_agent_auto_compact.py#L108)

