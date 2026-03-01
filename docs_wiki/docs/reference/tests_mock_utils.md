---
title: "tests.mock.utils"
tldr: "Module tests.mock.utils"
tags: [reference, api]
---

# `tests.mock.utils`

**Source:** [`tests/mock/utils.py`](tests/mock/utils.py) · 60 lines

## Constants

- `MOCK_DATA_ENV_VAR`

## `mock_llm_chunk()`

```python
def mock_llm_chunk(content: str, reasoning_content: str | None, role: Role, tool_calls: list[ToolCall] | None, name: str | None, tool_call_id: str | None, prompt_tokens: int, completion_tokens: int) -> LLMChunk
```

**Source:** [`tests/mock/utils.py#L18`](tests/mock/utils.py#L18)

## `get_mocking_env()`

```python
def get_mocking_env(mock_chunks: list[LLMChunk] | None) -> dict[str, str]
```

**Source:** [`tests/mock/utils.py#L44`](tests/mock/utils.py#L44)

## `collect_result()`

```python
async def collect_result(gen: AsyncGenerator[ToolStreamEvent | T, None]) -> T
```

**Source:** [`tests/mock/utils.py#L53`](tests/mock/utils.py#L53)

