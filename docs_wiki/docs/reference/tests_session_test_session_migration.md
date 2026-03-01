---
title: "tests.session.test_session_migration"
tldr: "Module tests.session.test_session_migration"
tags: [reference, api]
---

# `tests.session.test_session_migration`

**Source:** [`tests/session/test_session_migration.py`](tests/session/test_session_migration.py) · 177 lines

## `TestSessionMigration`

**Source:** [`tests/session/test_session_migration.py#L53`](tests/session/test_session_migration.py#L53)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_migrate_sessions_disabled_config()` | disabled_session_config | `None` | Test that migration does nothing when config is disabled. |
| 🔄 `test_migrate_sessions_no_save_dir()` | session_config | `None` | Test that migration handles missing save_dir gracefully. |
| 🔄 `test_migrate_sessions_no_old_files()` | session_config | `None` | Test that migration handles no old session files gracefully. |
| 🔄 `test_migrate_sessions_successful_migration()` | session_config, old_session_data | `None` | Test successful migration of old session files. |
| 🔄 `test_migrate_sessions_multiple_files()` | session_config, old_session_data | `None` | Test migration of multiple old session files. |
| 🔄 `test_migrate_sessions_error_handling()` | session_config | `None` | Test that migration handles errors gracefully and continues. |

## `temp_session_dir()`

```python
def temp_session_dir(tmp_path: Path) -> Path
```

**Source:** [`tests/session/test_session_migration.py#L13`](tests/session/test_session_migration.py#L13)

## `session_config()`

```python
def session_config(temp_session_dir: Path) -> SessionLoggingConfig
```

**Source:** [`tests/session/test_session_migration.py#L20`](tests/session/test_session_migration.py#L20)

## `disabled_session_config()`

```python
def disabled_session_config() -> SessionLoggingConfig
```

**Source:** [`tests/session/test_session_migration.py#L27`](tests/session/test_session_migration.py#L27)

## `old_session_data()`

```python
def old_session_data() -> dict
```

**Source:** [`tests/session/test_session_migration.py#L34`](tests/session/test_session_migration.py#L34)

