---
title: "tests.backend.test_anthropic_adapter"
tldr: "Module tests.backend.test_anthropic_adapter"
tags: [reference, api]
---

# `tests.backend.test_anthropic_adapter`

**Source:** [`tests/backend/test_anthropic_adapter.py`](tests/backend/test_anthropic_adapter.py) · 586 lines

## `TestMapperPrepareMessages`

**Source:** [`tests/backend/test_anthropic_adapter.py#L39`](tests/backend/test_anthropic_adapter.py#L39)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_system_extracted()` | mapper | `—` | — |
| `test_user_message()` | mapper | `—` | — |
| `test_assistant_text()` | mapper | `—` | — |
| `test_assistant_with_reasoning_content_and_signature()` | mapper | `—` | — |
| `test_assistant_with_reasoning_content()` | mapper | `—` | — |
| `test_assistant_with_tool_calls()` | mapper | `—` | — |
| `test_tool_result_appended_to_user()` | mapper | `—` | — |
| `test_tool_result_new_user_when_no_prior()` | mapper | `—` | — |

## `TestMapperPrepareTools`

**Source:** [`tests/backend/test_anthropic_adapter.py#L125`](tests/backend/test_anthropic_adapter.py#L125)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_none_returns_none()` | mapper | `—` | — |
| `test_empty_returns_none()` | mapper | `—` | — |
| `test_converts_tools()` | mapper | `—` | — |

## `TestMapperToolChoice`

**Source:** [`tests/backend/test_anthropic_adapter.py#L148`](tests/backend/test_anthropic_adapter.py#L148)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_none()` | mapper | `—` | — |
| `test_auto()` | mapper | `—` | — |
| `test_none_str()` | mapper | `—` | — |
| `test_any()` | mapper | `—` | — |
| `test_required()` | mapper | `—` | — |
| `test_specific_tool()` | mapper | `—` | — |

## `TestMapperParseResponse`

**Source:** [`tests/backend/test_anthropic_adapter.py#L171`](tests/backend/test_anthropic_adapter.py#L171)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_text()` | mapper | `—` | — |
| `test_thinking()` | mapper | `—` | — |
| `test_redacted_thinking()` | mapper | `—` | — |
| `test_tool_use()` | mapper | `—` | — |
| `test_cache_tokens()` | mapper | `—` | — |

## `TestMapperStreamingEvents`

**Source:** [`tests/backend/test_anthropic_adapter.py#L232`](tests/backend/test_anthropic_adapter.py#L232)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_text_delta()` | mapper | `—` | — |
| `test_thinking_delta()` | mapper | `—` | — |
| `test_tool_use_start()` | mapper | `—` | — |
| `test_input_json_delta()` | mapper | `—` | — |
| `test_message_start_usage()` | mapper | `—` | — |
| `test_message_delta_usage()` | mapper | `—` | — |
| `test_unknown_event()` | mapper | `—` | — |
| `test_signature_delta()` | mapper | `—` | — |

## `TestAdapterPrepareRequest`

**Source:** [`tests/backend/test_anthropic_adapter.py#L301`](tests/backend/test_anthropic_adapter.py#L301)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_basic()` | adapter, provider | `—` | — |
| `test_beta_features()` | adapter, provider | `—` | — |
| `test_api_key_header()` | adapter, provider | `—` | — |
| `test_streaming()` | adapter, provider | `—` | — |
| `test_default_max_tokens()` | adapter, provider | `—` | — |
| `test_with_thinking()` | adapter, provider | `—` | — |
| `test_system_cached()` | adapter, provider | `—` | — |
| `test_with_tools()` | adapter, provider | `—` | — |
| `test_thinking_levels_budget_model()` | adapter, provider, level, expected_budget | `—` | — |
| `test_thinking_levels_adaptive_model()` | adapter, provider, level | `—` | — |
| `test_history_forced_thinking_budget_model()` | adapter, provider | `—` | — |
| `test_history_forced_thinking_adaptive_model()` | adapter, provider | `—` | — |

## `TestAdapterParseResponse`

**Source:** [`tests/backend/test_anthropic_adapter.py#L541`](tests/backend/test_anthropic_adapter.py#L541)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_non_streaming()` | adapter, provider | `—` | — |
| `test_streaming_text_delta()` | adapter, provider | `—` | — |
| `test_streaming_message_start()` | adapter, provider | `—` | — |
| `test_streaming_unknown_returns_empty()` | adapter, provider | `—` | — |
| `test_cache_control_last_user_message()` | adapter | `—` | — |
| `test_cache_control_skips_non_user()` | adapter | `—` | — |
| `test_cache_control_empty()` | adapter | `—` | — |

## `mapper()`

```python
def mapper()
```

**Source:** [`tests/backend/test_anthropic_adapter.py#L20`](tests/backend/test_anthropic_adapter.py#L20)

## `adapter()`

```python
def adapter()
```

**Source:** [`tests/backend/test_anthropic_adapter.py#L25`](tests/backend/test_anthropic_adapter.py#L25)

## `provider()`

```python
def provider()
```

**Source:** [`tests/backend/test_anthropic_adapter.py#L30`](tests/backend/test_anthropic_adapter.py#L30)

