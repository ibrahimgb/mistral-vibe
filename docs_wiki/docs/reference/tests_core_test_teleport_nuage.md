---
title: "tests.core.test_teleport_nuage"
tldr: "Module tests.core.test_teleport_nuage"
tags: [reference, api]
---

# `tests.core.test_teleport_nuage`

**Source:** [`tests/core/test_teleport_nuage.py`](tests/core/test_teleport_nuage.py) · 337 lines

## `TestNuageModels`

**Source:** [`tests/core/test_teleport_nuage.py#L20`](tests/core/test_teleport_nuage.py#L20)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_git_repo_config_defaults()` |  | `None` | — |
| `test_git_repo_config_with_values()` |  | `None` | — |
| `test_vibe_sandbox_config_defaults()` |  | `None` | — |
| `test_vibe_new_sandbox_defaults()` |  | `None` | — |
| `test_workflow_params_serialization()` |  | `None` | — |
| `test_create_le_chat_thread_input()` |  | `None` | — |

## `TestNuageClientContextManager`

**Source:** [`tests/core/test_teleport_nuage.py#L77`](tests/core/test_teleport_nuage.py#L77)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_creates_client_on_enter()` |  | `None` | — |
| 🔄 `test_uses_provided_client()` |  | `None` | — |

## `TestNuageClientStartWorkflow`

**Source:** [`tests/core/test_teleport_nuage.py#L98`](tests/core/test_teleport_nuage.py#L98)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `mock_client()` |  | `MagicMock` | — |
| `nuage()` | mock_client | `NuageClient` | — |
| 🔄 `test_start_workflow_success()` | nuage, mock_client | `None` | — |
| 🔄 `test_start_workflow_failure()` | nuage, mock_client | `None` | — |
| 🔄 `test_start_workflow_unauthorized_hint()` | nuage, mock_client | `None` | — |

## `TestNuageClientSendGithubToken`

**Source:** [`tests/core/test_teleport_nuage.py#L154`](tests/core/test_teleport_nuage.py#L154)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `mock_client()` |  | `MagicMock` | — |
| `nuage()` | mock_client | `NuageClient` | — |
| 🔄 `test_send_github_token_success()` | nuage, mock_client, monkeypatch | `None` | — |
| 🔄 `test_query_public_key_failure()` | nuage, mock_client | `None` | — |
| 🔄 `test_signal_encrypted_token_failure()` | nuage, mock_client | `None` | — |

## `TestNuageClientCreateLeChatThread`

**Source:** [`tests/core/test_teleport_nuage.py#L234`](tests/core/test_teleport_nuage.py#L234)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `mock_client()` |  | `MagicMock` | — |
| `nuage()` | mock_client | `NuageClient` | — |
| 🔄 `test_create_le_chat_thread_success()` | nuage, mock_client, monkeypatch | `None` | — |
| 🔄 `test_create_le_chat_thread_failure()` | nuage, mock_client, monkeypatch | `None` | — |

## `TestNuageClientHeaders`

**Source:** [`tests/core/test_teleport_nuage.py#L332`](tests/core/test_teleport_nuage.py#L332)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_headers_include_auth()` |  | `None` | — |

