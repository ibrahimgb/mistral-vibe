---
title: "tests.core.test_teleport_service"
tldr: "Module tests.core.test_teleport_service"
tags: [reference, api]
---

# `tests.core.test_teleport_service`

**Source:** [`tests/core/test_teleport_service.py`](tests/core/test_teleport_service.py) · 418 lines

## `TestTeleportServiceCompressDiff`

**Source:** [`tests/core/test_teleport_service.py#L41`](tests/core/test_teleport_service.py#L41)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `service()` | tmp_path | `TeleportService` | — |
| `test_returns_none_for_empty_diff()` | service | `None` | — |
| `test_compresses_and_encodes_diff()` | service | `None` | — |
| `test_raises_when_diff_too_large()` | service | `None` | — |

## `TestTeleportServiceBuildSandbox`

**Source:** [`tests/core/test_teleport_service.py#L71`](tests/core/test_teleport_service.py#L71)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `service()` | tmp_path | `TeleportService` | — |
| `test_builds_sandbox_from_git_info()` | service | `None` | — |
| `test_includes_compressed_diff()` | service | `None` | — |

## `TestTeleportServiceValidateConfig`

**Source:** [`tests/core/test_teleport_service.py#L115`](tests/core/test_teleport_service.py#L115)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_raises_when_no_api_key()` | tmp_path | `None` | — |
| `test_passes_when_api_key_set()` | tmp_path | `None` | — |

## `TestTeleportServiceCheckSupported`

**Source:** [`tests/core/test_teleport_service.py#L142`](tests/core/test_teleport_service.py#L142)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `service()` | tmp_path | `TeleportService` | — |
| 🔄 `test_check_supported_calls_git_info()` | service | `None` | — |
| 🔄 `test_check_supported_raises_when_not_supported()` | service | `None` | — |

## `TestTeleportServiceIsSupported`

**Source:** [`tests/core/test_teleport_service.py#L182`](tests/core/test_teleport_service.py#L182)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `service()` | tmp_path | `TeleportService` | — |
| 🔄 `test_is_supported_returns_true()` | service | `None` | — |
| 🔄 `test_is_supported_returns_false()` | service | `None` | — |

## `TestTeleportServiceExecute`

**Source:** [`tests/core/test_teleport_service.py#L205`](tests/core/test_teleport_service.py#L205)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `service()` | tmp_path | `TeleportService` | — |
| `git_info()` |  | `GitRepoInfo` | — |
| 🔄 `test_execute_happy_path_commit_pushed_with_token()` | service, git_info | `None` | — |
| 🔄 `test_execute_requires_push_and_user_approves()` | service, git_info | `None` | — |
| 🔄 `test_execute_requires_push_and_user_declines()` | service, git_info | `None` | — |
| 🔄 `test_execute_requires_auth_flow()` | service, git_info | `None` | — |
| 🔄 `test_execute_uses_default_prompt_when_none()` | service, git_info | `None` | — |

## `TestTeleportServiceContextManager`

**Source:** [`tests/core/test_teleport_service.py#L377`](tests/core/test_teleport_service.py#L377)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_creates_client_on_enter()` | tmp_path | `None` | — |

## `TestTeleportAvailability`

**Source:** [`tests/core/test_teleport_service.py#L396`](tests/core/test_teleport_service.py#L396)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_teleport_available_is_false_when_git_not_installed()` |  | `None` | — |
| `test_teleport_service_raises_error_when_git_not_available()` |  | `None` | — |
| `test_teleport_available_is_true_when_git_installed()` | tmp_path | `None` | — |

## `_reimport_agent_loop()`

```python
def _reimport_agent_loop() -> Any
```

**Source:** [`tests/core/test_teleport_service.py#L34`](tests/core/test_teleport_service.py#L34)

