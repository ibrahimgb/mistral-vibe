---
title: "tests.e2e.mock_server"
tldr: "Module tests.e2e.mock_server"
tags: [reference, api]
---

# `tests.e2e.mock_server`

**Source:** [`tests/e2e/mock_server.py`](tests/e2e/mock_server.py) · 149 lines

## `StreamOptionsPayload`

**Bases:** `TypedDict`

**Source:** [`tests/e2e/mock_server.py#L11`](tests/e2e/mock_server.py#L11)

## `ChatMessagePayload`

**Bases:** `TypedDict`

**Source:** [`tests/e2e/mock_server.py#L16`](tests/e2e/mock_server.py#L16)

## `ChatCompletionsRequestPayload`

**Bases:** `TypedDict`

**Source:** [`tests/e2e/mock_server.py#L21`](tests/e2e/mock_server.py#L21)

## `StreamingMockServer`

**Source:** [`tests/e2e/mock_server.py#L32`](tests/e2e/mock_server.py#L32)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `build_chunk()` |  | `StreamChunk` | — |
| `build_tool_call_delta()` |  | `dict[str, object]` | — |
| `__init__()` |  | `None` | — |
| `api_base()` |  | `str` | — |
| `start()` |  | `None` | — |
| `stop()` |  | `None` | — |

??? note "Private Methods"

    - `def _stream_chunks() -> list[StreamChunk]`
    - `def _build_handler(self) -> type[BaseHTTPRequestHandler]`

