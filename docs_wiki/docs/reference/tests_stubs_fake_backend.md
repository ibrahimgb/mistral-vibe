---
title: "tests.stubs.fake_backend"
tldr: "Module tests.stubs.fake_backend"
tags: [reference, api]
---

# `tests.stubs.fake_backend`

**Source:** [`tests/stubs/fake_backend.py`](tests/stubs/fake_backend.py) · 149 lines

## `FakeBackend`

Minimal async backend stub to drive Agent.act without network.

Provide a finite sequence of LLMResult objects to be returned by
`complete`. When exhausted, returns an empty assistant message.

**Source:** [`tests/stubs/fake_backend.py#L10`](tests/stubs/fake_backend.py#L10)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `__init__()` | chunks | `None` | Fake backend that will output the given chunks in the order they are given. |
| `requests_messages()` |  | `list[list[LLMMessage]]` | — |
| `requests_extra_headers()` |  | `list[dict[str, str] | None]` | — |
| `requests_metadata()` |  | `list[dict[str, str] | None]` | — |
| 🔄 `__aenter__()` |  | `—` | — |
| 🔄 `__aexit__()` | exc_type, exc_val, exc_tb | `—` | — |
| 🔄 `complete()` |  | `LLMChunk` | — |
| 🔄 `complete_streaming()` |  | `AsyncGenerator[LLMChunk]` | — |
| 🔄 `count_tokens()` |  | `int` | — |

??? note "Private Methods"

    - `def _default_token_counter(messages: Sequence[LLMMessage]) -> int`

