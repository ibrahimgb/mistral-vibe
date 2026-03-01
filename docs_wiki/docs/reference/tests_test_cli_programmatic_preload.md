---
title: "tests.test_cli_programmatic_preload"
tldr: "Module tests.test_cli_programmatic_preload"
tags: [reference, api]
---

# `tests.test_cli_programmatic_preload`

**Source:** [`tests/test_cli_programmatic_preload.py`](tests/test_cli_programmatic_preload.py) · 144 lines

## `SpyStreamingFormatter`

**Source:** [`tests/test_cli_programmatic_preload.py#L14`](tests/test_cli_programmatic_preload.py#L14)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` |  | `None` | — |
| `on_message_added()` | message | `None` | — |
| `on_event()` | _event | `None` | — |
| `finalize()` |  | `str | None` | — |

## `test_run_programmatic_preload_streaming_is_batched()`

```python
def test_run_programmatic_preload_streaming_is_batched(monkeypatch: pytest.MonkeyPatch, telemetry_events: list[dict]) -> None
```

**Source:** [`tests/test_cli_programmatic_preload.py#L28`](tests/test_cli_programmatic_preload.py#L28)

## `test_run_programmatic_ignores_system_messages_in_previous()`

```python
def test_run_programmatic_ignores_system_messages_in_previous(monkeypatch: pytest.MonkeyPatch) -> None
```

**Source:** [`tests/test_cli_programmatic_preload.py#L100`](tests/test_cli_programmatic_preload.py#L100)

