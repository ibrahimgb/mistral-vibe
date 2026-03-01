---
title: "tests.core.test_telemetry_send"
tldr: "Module tests.core.test_telemetry_send"
tags: [reference, api]
---

# `tests.core.test_telemetry_send`

**Source:** [`tests/core/test_telemetry_send.py`](tests/core/test_telemetry_send.py) · 274 lines

## `TestTelemetryClient`

**Source:** [`tests/core/test_telemetry_send.py#L46`](tests/core/test_telemetry_send.py#L46)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_send_telemetry_event_does_nothing_when_api_key_is_none()` | monkeypatch | `None` | — |
| `test_send_telemetry_event_does_nothing_when_disabled()` | monkeypatch | `None` | — |
| 🔄 `test_send_telemetry_event_posts_when_enabled()` | monkeypatch | `None` | — |
| `test_send_tool_call_finished_payload_shape()` | telemetry_events | `None` | — |
| `test_send_tool_call_finished_nb_files_created_write_file_new()` | telemetry_events | `None` | — |
| `test_send_tool_call_finished_nb_files_modified_write_file_overwrite()` | telemetry_events | `None` | — |
| `test_send_tool_call_finished_decision_none()` | telemetry_events | `None` | — |
| `test_send_user_copied_text_payload()` | telemetry_events | `None` | — |
| `test_send_user_cancelled_action_payload()` | telemetry_events | `None` | — |
| `test_send_auto_compact_triggered_payload()` | telemetry_events | `None` | — |
| `test_send_slash_command_used_payload()` | telemetry_events | `None` | — |
| `test_send_new_session_payload()` | telemetry_events | `None` | — |

## `_make_resolved_tool_call()`

```python
def _make_resolved_tool_call(tool_name: str, args_dict: dict[str, Any]) -> ResolvedToolCall
```

**Source:** [`tests/core/test_telemetry_send.py#L22`](tests/core/test_telemetry_send.py#L22)

## `_run_telemetry_tasks()`

```python
def _run_telemetry_tasks() -> None
```

**Source:** [`tests/core/test_telemetry_send.py#L38`](tests/core/test_telemetry_send.py#L38)

