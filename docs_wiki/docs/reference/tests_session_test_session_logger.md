---
title: "tests.session.test_session_logger"
tldr: "Module tests.session.test_session_logger"
tags: [reference, api]
---

# `tests.session.test_session_logger`

**Source:** [`tests/session/test_session_logger.py`](tests/session/test_session_logger.py) · 782 lines

## `TestSessionLoggerInitialization`

**Source:** [`tests/session/test_session_logger.py#L69`](tests/session/test_session_logger.py#L69)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_enabled_session_logger_initialization()` | session_config | `None` | Test that SessionLogger initializes correctly when enabled. |
| `test_disabled_session_logger_initialization()` | disabled_session_config | `None` | Test that SessionLogger initializes correctly when disabled. |

## `TestSessionLoggerMetadata`

**Source:** [`tests/session/test_session_logger.py#L109`](tests/session/test_session_logger.py#L109)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_session_metadata_initialization()` | mock_getuser, mock_subprocess, session_config | `None` | Test that session metadata is correctly initialized. |
| `test_session_metadata_with_git_errors()` | mock_getuser, mock_subprocess, session_config | `None` | Test that session metadata handles git command errors gracefully. |

## `TestSessionLoggerSaveInteraction`

**Source:** [`tests/session/test_session_logger.py#L164`](tests/session/test_session_logger.py#L164)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_save_interaction_disabled()` | disabled_session_config | `None` | Test that save_interaction returns None when logging is disabled. |
| 🔄 `test_save_interaction_success()` | session_config, mock_vibe_config, mock_tool_manager, mock_agent_profile | `None` | Test that save_interaction successfully saves session data. |
| 🔄 `test_save_interaction_system_prompt_in_metadata()` | session_config, mock_vibe_config, mock_tool_manager, mock_agent_profile | `None` | Test that system prompt is saved in metadata and not in messages. |
| 🔄 `test_save_interaction_with_existing_messages()` | session_config, mock_vibe_config, mock_tool_manager, mock_agent_profile | `None` | Test that save_interaction correctly handles existing messages. |
| 🔄 `test_save_interaction_no_new_messages_is_noop()` | session_config, mock_vibe_config, mock_tool_manager, mock_agent_profile | `None` | Test that save_interaction does nothing when there are no new messages. |
| 🔄 `test_save_interaction_no_user_messages()` | session_config, mock_vibe_config, mock_tool_manager, mock_agent_profile | `None` | Test that save_interaction handles sessions with no user messages. |
| 🔄 `test_save_interaction_long_user_message()` | session_config, mock_vibe_config, mock_tool_manager, mock_agent_profile | `None` | Test that save_interaction truncates long user messages for title. |
| 🔄 `test_save_interaction_throttles_tmp_cleanup()` | session_config, mock_vibe_config, mock_tool_manager, mock_agent_profile | `None` | — |

## `TestSessionLoggerResetSession`

**Source:** [`tests/session/test_session_logger.py#L561`](tests/session/test_session_logger.py#L561)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_reset_session()` | session_config | `None` | Test that reset_session correctly resets session information. |
| `test_reset_session_disabled()` | disabled_session_config | `None` | Test that reset_session does nothing when logging is disabled. |

## `TestSessionLoggerFileOperations`

**Source:** [`tests/session/test_session_logger.py#L600`](tests/session/test_session_logger.py#L600)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_save_folder()` | session_config | `None` | Test that save_folder creates correct folder name. |
| `test_metadata_filepath()` | session_config | `None` | Test that metadata_filepath returns correct path. |
| `test_messages_filepath()` | session_config | `None` | Test that messages_filepath returns correct path. |
| `test_disabled_file_operations_raise_errors()` | disabled_session_config | `None` | Test that file operations raise errors when logging is disabled. |

## `TestSessionLoggerCleanupTmpFiles`

**Source:** [`tests/session/test_session_logger.py#L666`](tests/session/test_session_logger.py#L666)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_cleanup_tmp_files_disabled()` | disabled_session_config | `None` | Test that cleanup_tmp_files returns early when logging is disabled. |
| `test_cleanup_tmp_files_no_tmp_files()` | session_config | `None` | Test that cleanup_tmp_files handles no tmp files gracefully. |
| `test_cleanup_tmp_files_deletes_old_files()` | session_config | `None` | Test that cleanup_tmp_files deletes tmp files older than 5 minutes. |
| `test_cleanup_tmp_files_recursive()` | session_config | `None` | Test that cleanup_tmp_files works recursively in subdirectories. |
| `test_cleanup_tmp_files_handles_exceptions()` | session_config | `None` | Test that cleanup_tmp_files handles exceptions gracefully. |
| `test_maybe_cleanup_tmp_files_throttles_calls()` | session_config | `None` | — |

## `temp_session_dir()`

```python
def temp_session_dir(tmp_path: Path) -> Path
```

Create a temporary directory for session logging tests.

**Source:** [`tests/session/test_session_logger.py#L20`](tests/session/test_session_logger.py#L20)

## `session_config()`

```python
def session_config(temp_session_dir: Path) -> SessionLoggingConfig
```

Create a session logging config for testing.

**Source:** [`tests/session/test_session_logger.py#L28`](tests/session/test_session_logger.py#L28)

## `disabled_session_config()`

```python
def disabled_session_config() -> SessionLoggingConfig
```

Create a disabled session logging config for testing.

**Source:** [`tests/session/test_session_logger.py#L36`](tests/session/test_session_logger.py#L36)

## `mock_agent_profile()`

```python
def mock_agent_profile() -> AgentProfile
```

Create a mock agent profile for testing.

**Source:** [`tests/session/test_session_logger.py#L44`](tests/session/test_session_logger.py#L44)

## `mock_tool_manager()`

```python
def mock_tool_manager() -> ToolManager
```

Create a mock tool manager for testing.

**Source:** [`tests/session/test_session_logger.py#L56`](tests/session/test_session_logger.py#L56)

## `mock_vibe_config()`

```python
def mock_vibe_config() -> VibeConfig
```

Create a mock vibe config for testing.

**Source:** [`tests/session/test_session_logger.py#L64`](tests/session/test_session_logger.py#L64)

## `create_temp_file_ago()`

```python
def create_temp_file_ago(tmp_path: Path, filename: str, minutes_ago: int) -> Path
```

Create a file with a modification time of `minutes_ago` minutes ago.

**Source:** [`tests/session/test_session_logger.py#L657`](tests/session/test_session_logger.py#L657)

