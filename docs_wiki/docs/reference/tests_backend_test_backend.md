---
title: "tests.backend.test_backend"
tldr: "Test data for this module was generated using real LLM provider API responses,"
tags: [reference, api]
---

# `tests.backend.test_backend`

**Source:** [`tests/backend/test_backend.py`](tests/backend/test_backend.py) · 437 lines

Test data for this module was generated using real LLM provider API responses,
with responses simplified and formatted to make them readable and maintainable.

To update or modify test parameters:
1. Make actual API calls to the target providers
2. Use the raw API responses as a base for updating test data
3. Simplify only where necessary for readability while preserving core structure

The closer test data remains to real API responses, the more reliable and accurate
the tests will be. Always prefer real API data over manually constructed examples.

## `TestBackend`

**Source:** [`tests/backend/test_backend.py#L46`](tests/backend/test_backend.py#L46)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_backend_complete()` | base_url, json_response, result_data | `—` | — |
| 🔄 `test_backend_complete_streaming()` | base_url, chunks, result_data | `—` | — |
| 🔄 `test_backend_complete_streaming_error()` | base_url, backend_class, response | `—` | — |
| 🔄 `test_backend_streaming_payload_includes_stream_options()` | base_url, provider_name, expected_stream_options | `—` | — |
| 🔄 `test_backend_user_agent()` | backend_type | `—` | — |
| 🔄 `test_backend_user_agent_when_streaming()` | backend_type | `—` | — |

??? note "Private Methods"

    - `def _build_fast_retry_config() -> RetryConfig`

## `TestMistralRetry`

**Source:** [`tests/backend/test_backend.py#L415`](tests/backend/test_backend.py#L415)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_client_creation_includes_timeout_and_retry_config()` |  | `—` | — |

??? note "Private Methods"

    - `def _create_test_backend() -> MistralBackend`

