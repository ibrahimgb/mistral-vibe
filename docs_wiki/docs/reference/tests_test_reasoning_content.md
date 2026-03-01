---
title: "tests.test_reasoning_content"
tldr: "Module tests.test_reasoning_content"
tags: [reference, api]
---

# `tests.test_reasoning_content`

**Source:** [`tests/test_reasoning_content.py`](tests/test_reasoning_content.py) · 531 lines

## `TestMistralMapperParseContent`

**Source:** [`tests/test_reasoning_content.py#L33`](tests/test_reasoning_content.py#L33)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_parse_content_string_returns_content_only()` |  | `—` | — |
| `test_parse_content_text_chunk_returns_content_only()` |  | `—` | — |
| `test_parse_content_thinking_chunk_extracts_reasoning()` |  | `—` | — |
| `test_parse_content_multiple_thinking_chunks_concatenates()` |  | `—` | — |
| `test_parse_content_thinking_only_returns_empty_content()` |  | `—` | — |
| `test_parse_content_empty_list_returns_empty()` |  | `—` | — |

## `TestMistralMapperPrepareMessage`

**Source:** [`tests/test_reasoning_content.py#L110`](tests/test_reasoning_content.py#L110)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_prepare_assistant_message_without_reasoning()` |  | `—` | — |
| `test_prepare_assistant_message_with_reasoning_creates_chunks()` |  | `—` | — |
| `test_prepare_assistant_message_with_reasoning_and_none_content()` |  | `—` | — |

## `TestGenericBackendReasoningContent`

**Source:** [`tests/test_reasoning_content.py#L172`](tests/test_reasoning_content.py#L172)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_complete_extracts_reasoning_content()` |  | `—` | — |
| 🔄 `test_complete_streaming_extracts_reasoning_content()` |  | `—` | — |

## `TestAPIToolFormatHandlerReasoningContent`

**Source:** [`tests/test_reasoning_content.py#L262`](tests/test_reasoning_content.py#L262)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_process_api_response_message_extracts_reasoning_content()` |  | `—` | — |
| `test_process_api_response_message_handles_missing_reasoning_content()` |  | `—` | — |

## `TestAgentLoopStreamingReasoningEvents`

**Source:** [`tests/test_reasoning_content.py#L292`](tests/test_reasoning_content.py#L292)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_streaming_accumulates_reasoning_in_message()` |  | `—` | — |
| 🔄 `test_streaming_content_only_no_reasoning()` |  | `—` | — |

## `TestLLMMessageReasoningContent`

**Source:** [`tests/test_reasoning_content.py#L333`](tests/test_reasoning_content.py#L333)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_llm_message_from_dict_with_reasoning_content()` |  | `—` | — |
| `test_llm_message_model_dump_includes_reasoning_content()` |  | `—` | — |
| `test_llm_message_model_dump_excludes_none_reasoning_content()` |  | `—` | — |

## `TestReasoningFieldNameConversion`

**Source:** [`tests/test_reasoning_content.py#L362`](tests/test_reasoning_content.py#L362)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_reasoning_to_api_keeps_default_field()` |  | `—` | — |
| `test_reasoning_to_api_renames_to_custom_field()` |  | `—` | — |
| `test_reasoning_from_api_converts_custom_field()` |  | `—` | — |
| `test_reasoning_from_api_keeps_default_field()` |  | `—` | — |
| 🔄 `test_complete_with_custom_reasoning_field_name()` |  | `—` | — |
| 🔄 `test_streaming_with_custom_reasoning_field_name()` |  | `—` | — |

## `TestMistralReasoningFieldNameValidation`

**Source:** [`tests/test_reasoning_content.py#L507`](tests/test_reasoning_content.py#L507)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_mistral_backend_rejects_custom_reasoning_field_name()` |  | `—` | — |
| `test_mistral_backend_accepts_default_reasoning_field_name()` |  | `—` | — |

## `make_config()`

```python
def make_config() -> VibeConfig
```

**Source:** [`tests/test_reasoning_content.py#L20`](tests/test_reasoning_content.py#L20)

