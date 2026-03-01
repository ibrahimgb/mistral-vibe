---
title: "tests.backend.test_vertex_anthropic_adapter"
tldr: "Module tests.backend.test_vertex_anthropic_adapter"
tags: [reference, api]
---

# `tests.backend.test_vertex_anthropic_adapter`

**Source:** [`tests/backend/test_vertex_anthropic_adapter.py`](tests/backend/test_vertex_anthropic_adapter.py) · 637 lines

## `TestBuildVertexEndpoint`

**Source:** [`tests/backend/test_vertex_anthropic_adapter.py#L41`](tests/backend/test_vertex_anthropic_adapter.py#L41)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_non_streaming()` |  | `—` | — |
| `test_streaming()` |  | `—` | — |
| `test_base_url()` |  | `—` | — |
| `test_global_endpoint()` |  | `—` | — |
| `test_global_base_url()` |  | `—` | — |

## `TestPrepareRequest`

**Source:** [`tests/backend/test_vertex_anthropic_adapter.py#L76`](tests/backend/test_vertex_anthropic_adapter.py#L76)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_basic_request()` | adapter, provider | `—` | — |
| `test_streaming_request()` | adapter, provider | `—` | — |
| `test_no_beta_features_for_vertex()` | adapter, provider | `—` | Vertex AI doesn't support the same beta features as direct Anthropic API. |
| `test_with_extended_thinking()` | adapter, provider | `—` | — |
| `test_with_tools()` | adapter, provider | `—` | — |
| `test_missing_project_id()` | adapter | `—` | — |
| `test_missing_region()` | adapter | `—` | — |
| `test_default_max_tokens()` | adapter, provider | `—` | — |

## `TestParseFullResponse`

**Source:** [`tests/backend/test_vertex_anthropic_adapter.py#L235`](tests/backend/test_vertex_anthropic_adapter.py#L235)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_simple_text_response()` | adapter, provider | `—` | — |
| `test_response_with_tool_calls()` | adapter, provider | `—` | — |
| `test_response_with_thinking()` | adapter, provider | `—` | — |
| `test_response_with_cache_tokens()` | adapter, provider | `—` | — |
| `test_response_with_redacted_thinking()` | adapter, provider | `—` | — |
| `test_response_empty_usage()` | adapter, provider | `—` | — |

## `TestStreamingEvents`

**Source:** [`tests/backend/test_vertex_anthropic_adapter.py#L318`](tests/backend/test_vertex_anthropic_adapter.py#L318)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_message_start()` | adapter, provider | `—` | — |
| `test_message_start_without_usage()` | adapter, provider | `—` | — |
| `test_content_block_start_tool_use()` | adapter, provider | `—` | — |
| `test_content_block_start_thinking()` | adapter, provider | `—` | — |
| `test_content_block_start_redacted_thinking()` | adapter, provider | `—` | — |
| `test_content_block_delta_text()` | adapter, provider | `—` | — |
| `test_content_block_delta_thinking()` | adapter, provider | `—` | — |
| `test_content_block_delta_input_json()` | adapter, provider | `—` | — |
| `test_content_block_stop()` | adapter, provider | `—` | — |
| `test_message_delta_with_usage()` | adapter, provider | `—` | — |
| `test_message_delta_without_usage()` | adapter, provider | `—` | — |
| `test_unknown_event_returns_empty_chunk()` | adapter, provider | `—` | — |
| `test_signature_delta()` | adapter, provider | `—` | — |
| `test_message_start_resets_state()` | adapter, provider | `—` | — |
| `test_full_streaming_sequence()` | adapter, provider | `—` | — |

## `TestHelperMethods`

**Source:** [`tests/backend/test_vertex_anthropic_adapter.py#L513`](tests/backend/test_vertex_anthropic_adapter.py#L513)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_has_thinking_content_true()` | adapter | `—` | — |
| `test_has_thinking_content_false()` | adapter | `—` | — |
| `test_has_thinking_content_empty()` | adapter | `—` | — |
| `test_has_thinking_content_non_list_content()` | adapter | `—` | — |
| `test_add_cache_control_to_last_user_message()` | adapter | `—` | — |
| `test_add_cache_control_skips_non_user()` | adapter | `—` | — |
| `test_add_cache_control_skips_string_content()` | adapter | `—` | — |
| `test_add_cache_control_tool_result()` | adapter | `—` | — |
| `test_add_cache_control_empty_messages()` | adapter | `—` | — |

## `TestVertexCredentials`

**Source:** [`tests/backend/test_vertex_anthropic_adapter.py#L578`](tests/backend/test_vertex_anthropic_adapter.py#L578)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_initializes_credentials_on_first_access()` | mock_default | `—` | — |
| `test_caches_credentials_across_calls()` | mock_default | `—` | — |
| `test_refreshes_when_token_invalid()` | mock_default | `—` | — |
| `test_skips_refresh_when_token_valid()` | mock_default | `—` | — |
| `test_raises_when_token_is_none()` | mock_default | `—` | — |

??? note "Private Methods"

    - `def _make_creds(self) -> MagicMock`

## `adapter()`

```python
def adapter()
```

**Source:** [`tests/backend/test_vertex_anthropic_adapter.py#L19`](tests/backend/test_vertex_anthropic_adapter.py#L19)

## `provider()`

```python
def provider()
```

**Source:** [`tests/backend/test_vertex_anthropic_adapter.py#L31`](tests/backend/test_vertex_anthropic_adapter.py#L31)

