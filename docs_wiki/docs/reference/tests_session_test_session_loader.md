---
title: "tests.session.test_session_loader"
tldr: "Module tests.session.test_session_loader"
tags: [reference, api]
---

# `tests.session.test_session_loader`

**Source:** [`tests/session/test_session_loader.py`](tests/session/test_session_loader.py) · 954 lines

## `TestSessionLoaderFindLatestSession`

**Source:** [`tests/session/test_session_loader.py#L89`](tests/session/test_session_loader.py#L89)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_find_latest_session_no_sessions()` | session_config | `None` | Test finding latest session when no sessions exist. |
| `test_find_latest_session_single_session()` | session_config, create_test_session | `None` | Test finding latest session with a single session. |
| `test_find_latest_session_multiple_sessions()` | session_config, create_test_session | `None` | Test finding latest session with multiple sessions. |
| `test_find_latest_session_nonexistent_save_dir()` |  | `None` | Test finding latest session when save directory doesn't exist. |
| `test_find_latest_session_with_invalid_sessions()` | session_config | `None` | Test finding latest session when only invalid sessions exist. |
| `test_find_latest_session_with_mixed_valid_invalid()` | session_config, create_test_session | `None` | Test finding latest session when both valid and invalid sessions exist. |
| `test_find_latest_session_with_invalid_json()` | session_config, create_test_session | `None` | Test finding latest session when sessions have invalid JSON. |
| `test_find_latest_session_skips_empty_messages_file()` | session_config, create_test_session | `None` | — |
| `test_find_latest_session_skips_messages_json_not_dict()` | session_config, create_test_session | `None` | — |
| `test_find_latest_session_skips_metadata_json_not_dict()` | session_config, create_test_session | `None` | — |
| `test_find_latest_session_skips_unreadable_messages_file()` | session_config, create_test_session | `None` | — |
| `test_find_latest_session_skips_unreadable_metadata_file()` | session_config, create_test_session | `None` | — |

## `TestSessionLoaderFindSessionById`

**Source:** [`tests/session/test_session_loader.py#L287`](tests/session/test_session_loader.py#L287)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_find_session_by_id_exact_match()` | session_config, create_test_session | `None` | Test finding session by exact ID match. |
| `test_find_session_by_id_short_uuid()` | session_config, create_test_session | `None` | Test finding session by short UUID. |
| `test_find_session_by_id_partial_match()` | session_config, create_test_session | `None` | Test finding session by partial ID match |
| `test_find_session_by_id_multiple_matches()` | session_config, create_test_session | `None` | Test finding session when multiple sessions match (should return most recent). |
| `test_find_session_by_id_no_match()` | session_config, create_test_session | `None` | Test finding session by ID when no match exists. |
| `test_find_session_by_id_nonexistent_save_dir()` |  | `None` | Test finding session by ID when save directory doesn't exist. |

## `TestSessionLoaderDoesSessionExist`

**Source:** [`tests/session/test_session_loader.py#L365`](tests/session/test_session_loader.py#L365)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_does_session_exist_no_messages()` | session_config, create_test_session | `None` | — |
| `test_does_session_exist_success()` | session_config, create_test_session | `None` | — |

## `TestSessionLoaderLoadSession`

**Source:** [`tests/session/test_session_loader.py#L386`](tests/session/test_session_loader.py#L386)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_load_session_success()` | session_config, create_test_session | `None` | Test successfully loading a session. |
| `test_load_session_empty_messages()` | session_config | `None` | Test loading session with empty messages file. |
| `test_load_session_invalid_json_messages()` | session_config | `None` | Test loading session with invalid JSON in messages file. |
| `test_load_session_invalid_json_metadata()` | session_config | `None` | Test loading session with invalid JSON in metadata file. |
| `test_load_session_no_metadata_file()` | session_config | `None` | Test loading session when metadata file doesn't exist. |
| `test_load_session_nonexistent_directory()` | session_config | `None` | Test loading session from non-existent directory. |

## `TestSessionLoaderEdgeCases`

**Source:** [`tests/session/test_session_loader.py#L511`](tests/session/test_session_loader.py#L511)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_find_latest_session_with_different_prefixes()` | session_config | `None` | Test finding latest session when sessions have different prefixes. |
| `test_find_session_by_id_with_special_characters()` | session_config, create_test_session | `None` | Test finding session by ID containing special characters. |
| `test_load_session_with_complex_messages()` | session_config | `None` | Test loading session with complex message structures. |
| `test_load_session_system_prompt_ignored_in_messages()` | session_config | `None` | Test that system prompt is ignored when written in messages.jsonl. |

## `TestSessionLoaderListSessions`

**Source:** [`tests/session/test_session_loader.py#L673`](tests/session/test_session_loader.py#L673)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_list_sessions_empty()` | session_config | `None` | — |
| `test_list_sessions_returns_all_sessions()` | session_config, create_test_session_with_cwd | `None` | — |
| `test_list_sessions_filters_by_cwd()` | session_config, create_test_session_with_cwd | `None` | — |
| `test_list_sessions_includes_all_fields()` | session_config, create_test_session_with_cwd | `None` | — |
| `test_list_sessions_skips_invalid_sessions()` | session_config, create_test_session_with_cwd | `None` | — |
| `test_list_sessions_nonexistent_save_dir()` |  | `None` | — |
| `test_list_sessions_handles_missing_environment()` | session_config | `None` | — |
| `test_list_sessions_handles_none_title()` | session_config, create_test_session_with_cwd | `None` | — |

## `TestSessionLoaderGetFirstUserMessage`

Tests for SessionLoader.get_first_user_message method.

**Source:** [`tests/session/test_session_loader.py#L827`](tests/session/test_session_loader.py#L827)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_first_user_message()` | session_config, create_test_session | `None` | Test that get_first_user_message returns the first user message. |
| `test_returns_fallback_for_missing_session()` | session_config | `None` | Test that get_first_user_message returns fallback when session not found. |
| `test_returns_no_user_messages_fallback()` | session_config, create_test_session | `None` | Test fallback when session has no user messages. |
| `test_replaces_newlines_with_spaces()` | session_config, create_test_session | `None` | Test that newlines in messages are replaced with spaces. |
| `test_handles_empty_user_message()` | session_config, create_test_session | `None` | Test handling of empty user message content. |
| `test_handles_whitespace_only_message()` | session_config, create_test_session | `None` | Test handling of whitespace-only user message. |
| `test_handles_invalid_session_as_not_found()` | session_config | `None` | Test that invalid sessions (bad JSON) are treated as not found. |
| `test_skips_non_user_messages()` | session_config, create_test_session | `None` | Test that only user messages are considered, not assistant/system. |

## `temp_session_dir()`

```python
def temp_session_dir(tmp_path: Path) -> Path
```

Create a temporary directory for session loader tests.

**Source:** [`tests/session/test_session_loader.py#L16`](tests/session/test_session_loader.py#L16)

## `session_config()`

```python
def session_config(temp_session_dir: Path) -> SessionLoggingConfig
```

Create a session logging config for testing.

**Source:** [`tests/session/test_session_loader.py#L24`](tests/session/test_session_loader.py#L24)

## `create_test_session()`

```python
def create_test_session()
```

Helper fixture to create a test session with messages and metadata.

**Source:** [`tests/session/test_session_loader.py#L32`](tests/session/test_session_loader.py#L32)

## `create_test_session_with_cwd()`

```python
def create_test_session_with_cwd()
```

**Source:** [`tests/session/test_session_loader.py#L641`](tests/session/test_session_loader.py#L641)

