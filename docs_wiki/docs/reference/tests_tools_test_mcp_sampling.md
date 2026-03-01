---
title: "tests.tools.test_mcp_sampling"
tldr: "Module tests.tools.test_mcp_sampling"
tags: [reference, api]
---

# `tests.tools.test_mcp_sampling`

**Source:** [`tests/tools/test_mcp_sampling.py`](tests/tools/test_mcp_sampling.py) · 171 lines

## `TestExtractTextContent`

**Source:** [`tests/tools/test_mcp_sampling.py#L51`](tests/tools/test_mcp_sampling.py#L51)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_single_text_block()` |  | `None` | — |
| `test_list_of_text_blocks()` |  | `None` | — |
| `test_unsupported_single_block()` |  | `None` | — |
| `test_mixed_blocks_skips_non_text()` |  | `None` | — |

## `TestMapSamplingMessages`

**Source:** [`tests/tools/test_mcp_sampling.py#L72`](tests/tools/test_mcp_sampling.py#L72)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_maps_user_message()` |  | `None` | — |
| `test_maps_assistant_message()` |  | `None` | — |
| `test_maps_multiple_messages()` |  | `None` | — |

## `TestMCPSamplingHandler`

**Source:** [`tests/tools/test_mcp_sampling.py#L105`](tests/tools/test_mcp_sampling.py#L105)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_basic_text_response()` |  | `None` | — |
| 🔄 `test_system_prompt_prepended()` |  | `None` | — |
| 🔄 `test_calls_backend_with_messages()` |  | `None` | Verify the handler forwards messages to the backend. |
| 🔄 `test_returns_error_on_backend_failure()` |  | `None` | — |

## `_make_config()`

```python
def _make_config(model_name: str) -> MagicMock
```

**Source:** [`tests/tools/test_mcp_sampling.py#L24`](tests/tools/test_mcp_sampling.py#L24)

## `_make_params()`

```python
def _make_params(messages: list[SamplingMessage] | None, system_prompt: str | None, temperature: float | None, max_tokens: int) -> CreateMessageRequestParams
```

**Source:** [`tests/tools/test_mcp_sampling.py#L33`](tests/tools/test_mcp_sampling.py#L33)

