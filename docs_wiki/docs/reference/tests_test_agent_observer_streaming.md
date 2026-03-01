---
title: "tests.test_agent_observer_streaming"
tldr: "Module tests.test_agent_observer_streaming"
tags: [reference, api]
---

# `tests.test_agent_observer_streaming`

**Source:** [`tests/test_agent_observer_streaming.py`](tests/test_agent_observer_streaming.py) · 644 lines

## `InjectBeforeMiddleware`

**Source:** [`tests/test_agent_observer_streaming.py#L42`](tests/test_agent_observer_streaming.py#L42)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `before_turn()` | context | `MiddlewareResult` | Inject a message just before the current step executes. |
| `reset()` | reset_reason | `None` | — |

## `make_config()`

```python
def make_config() -> VibeConfig
```

**Source:** [`tests/test_agent_observer_streaming.py#L55`](tests/test_agent_observer_streaming.py#L55)

## `observer_capture()`

```python
def observer_capture() -> tuple[list[tuple[Role, str | None]], Callable[[LLMMessage], None]]
```

**Source:** [`tests/test_agent_observer_streaming.py#L73`](tests/test_agent_observer_streaming.py#L73)

## `test_act_flushes_batched_messages_with_injection_middleware()`

```python
async def test_act_flushes_batched_messages_with_injection_middleware(observer_capture) -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L85`](tests/test_agent_observer_streaming.py#L85)

## `test_stop_action_flushes_user_msg_before_returning()`

```python
async def test_stop_action_flushes_user_msg_before_returning(observer_capture) -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L113`](tests/test_agent_observer_streaming.py#L113)

## `test_act_emits_user_and_assistant_msgs()`

```python
async def test_act_emits_user_and_assistant_msgs(observer_capture) -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L135`](tests/test_agent_observer_streaming.py#L135)

## `test_act_streams_chunks_in_order()`

```python
async def test_act_streams_chunks_in_order() -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L153`](tests/test_agent_observer_streaming.py#L153)

## `test_act_streaming_does_not_cleanup_tmp_files_directly()`

```python
async def test_act_streaming_does_not_cleanup_tmp_files_directly() -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L185`](tests/test_agent_observer_streaming.py#L185)

## `test_act_handles_streaming_with_tool_call_events_in_sequence()`

```python
async def test_act_handles_streaming_with_tool_call_events_in_sequence() -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L206`](tests/test_agent_observer_streaming.py#L206)

## `test_act_handles_tool_call_chunk_with_content()`

```python
async def test_act_handles_tool_call_chunk_with_content() -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L258`](tests/test_agent_observer_streaming.py#L258)

## `test_act_merges_streamed_tool_call_arguments()`

```python
async def test_act_merges_streamed_tool_call_arguments() -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L309`](tests/test_agent_observer_streaming.py#L309)

## `test_act_handles_user_cancellation_during_streaming()`

```python
async def test_act_handles_user_cancellation_during_streaming() -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L367`](tests/test_agent_observer_streaming.py#L367)

## `test_act_flushes_and_logs_when_streaming_errors()`

```python
async def test_act_flushes_and_logs_when_streaming_errors(observer_capture) -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L426`](tests/test_agent_observer_streaming.py#L426)

## `test_rate_limit()`

```python
async def test_rate_limit(observer_capture) -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L445`](tests/test_agent_observer_streaming.py#L445)

## `_snapshot_events()`

```python
def _snapshot_events(events: list) -> list[tuple[str, str]]
```

**Source:** [`tests/test_agent_observer_streaming.py#L475`](tests/test_agent_observer_streaming.py#L475)

## `test_reasoning_yields_before_content_on_transition()`

```python
async def test_reasoning_yields_before_content_on_transition() -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L484`](tests/test_agent_observer_streaming.py#L484)

## `test_reasoning_yields_per_chunk()`

```python
async def test_reasoning_yields_per_chunk() -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L506`](tests/test_agent_observer_streaming.py#L506)

## `test_content_yields_before_reasoning_on_transition()`

```python
async def test_content_yields_before_reasoning_on_transition() -> None
```

When content chunks arrive and reasoning arrives, content yields first.

**Source:** [`tests/test_agent_observer_streaming.py#L536`](tests/test_agent_observer_streaming.py#L536)

## `test_interleaved_reasoning_content_preserves_order()`

```python
async def test_interleaved_reasoning_content_preserves_order() -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L561`](tests/test_agent_observer_streaming.py#L561)

## `test_only_reasoning_chunks_yields_reasoning_event()`

```python
async def test_only_reasoning_chunks_yields_reasoning_event() -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L591`](tests/test_agent_observer_streaming.py#L591)

## `test_final_buffers_flush_in_correct_order()`

```python
async def test_final_buffers_flush_in_correct_order() -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L609`](tests/test_agent_observer_streaming.py#L609)

## `test_empty_content_chunks_do_not_trigger_false_yields()`

```python
async def test_empty_content_chunks_do_not_trigger_false_yields() -> None
```

**Source:** [`tests/test_agent_observer_streaming.py#L627`](tests/test_agent_observer_streaming.py#L627)

