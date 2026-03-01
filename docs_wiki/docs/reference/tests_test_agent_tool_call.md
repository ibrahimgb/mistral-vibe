---
title: "tests.test_agent_tool_call"
tldr: "Module tests.test_agent_tool_call"
tags: [reference, api]
---

# `tests.test_agent_tool_call`

**Source:** [`tests/test_agent_tool_call.py`](tests/test_agent_tool_call.py) · 534 lines

## `act_and_collect_events()`

```python
async def act_and_collect_events(agent_loop: AgentLoop, prompt: str) -> list[BaseEvent]
```

**Source:** [`tests/test_agent_tool_call.py#L33`](tests/test_agent_tool_call.py#L33)

## `make_config()`

```python
def make_config(todo_permission: ToolPermission) -> VibeConfig
```

**Source:** [`tests/test_agent_tool_call.py#L37`](tests/test_agent_tool_call.py#L37)

## `make_todo_tool_call()`

```python
def make_todo_tool_call(call_id: str, index: int, arguments: str | None) -> ToolCall
```

**Source:** [`tests/test_agent_tool_call.py#L48`](tests/test_agent_tool_call.py#L48)

## `make_agent_loop()`

```python
def make_agent_loop() -> AgentLoop
```

**Source:** [`tests/test_agent_tool_call.py#L57`](tests/test_agent_tool_call.py#L57)

## `test_single_tool_call_executes_under_auto_approve()`

```python
async def test_single_tool_call_executes_under_auto_approve(telemetry_events: list[dict]) -> None
```

**Source:** [`tests/test_agent_tool_call.py#L78`](tests/test_agent_tool_call.py#L78)

## `test_tool_call_requires_approval_if_not_auto_approved()`

```python
async def test_tool_call_requires_approval_if_not_auto_approved(telemetry_events: list[dict]) -> None
```

**Source:** [`tests/test_agent_tool_call.py#L125`](tests/test_agent_tool_call.py#L125)

## `test_tool_call_approved_by_callback()`

```python
async def test_tool_call_approved_by_callback(telemetry_events: list[dict]) -> None
```

**Source:** [`tests/test_agent_tool_call.py#L168`](tests/test_agent_tool_call.py#L168)

## `test_tool_call_rejected_when_auto_approve_disabled_and_rejected_by_callback()`

```python
async def test_tool_call_rejected_when_auto_approve_disabled_and_rejected_by_callback(telemetry_events: list[dict]) -> None
```

**Source:** [`tests/test_agent_tool_call.py#L208`](tests/test_agent_tool_call.py#L208)

## `test_tool_call_skipped_when_permission_is_never()`

```python
async def test_tool_call_skipped_when_permission_is_never(telemetry_events: list[dict]) -> None
```

**Source:** [`tests/test_agent_tool_call.py#L253`](tests/test_agent_tool_call.py#L253)

## `test_approval_always_sets_tool_permission_for_subsequent_calls()`

```python
async def test_approval_always_sets_tool_permission_for_subsequent_calls() -> None
```

**Source:** [`tests/test_agent_tool_call.py#L297`](tests/test_agent_tool_call.py#L297)

## `test_tool_call_with_invalid_action()`

```python
async def test_tool_call_with_invalid_action() -> None
```

**Source:** [`tests/test_agent_tool_call.py#L358`](tests/test_agent_tool_call.py#L358)

## `test_tool_call_with_duplicate_todo_ids()`

```python
async def test_tool_call_with_duplicate_todo_ids() -> None
```

**Source:** [`tests/test_agent_tool_call.py#L383`](tests/test_agent_tool_call.py#L383)

## `test_tool_call_with_exceeding_max_todos()`

```python
async def test_tool_call_with_exceeding_max_todos() -> None
```

**Source:** [`tests/test_agent_tool_call.py#L414`](tests/test_agent_tool_call.py#L414)

## `test_tool_call_can_be_interrupted()`

```python
async def test_tool_call_can_be_interrupted() -> None
```

Test that tool calls can be interrupted via asyncio.CancelledError.

Note: KeyboardInterrupt is no longer handled here as ctrl+C now quits the app directly.

**Source:** [`tests/test_agent_tool_call.py#L442`](tests/test_agent_tool_call.py#L442)

## `test_fill_missing_tool_responses_inserts_placeholders()`

```python
async def test_fill_missing_tool_responses_inserts_placeholders() -> None
```

**Source:** [`tests/test_agent_tool_call.py#L482`](tests/test_agent_tool_call.py#L482)

## `test_ensure_assistant_after_tool_appends_understood()`

```python
async def test_ensure_assistant_after_tool_appends_understood() -> None
```

**Source:** [`tests/test_agent_tool_call.py#L518`](tests/test_agent_tool_call.py#L518)

