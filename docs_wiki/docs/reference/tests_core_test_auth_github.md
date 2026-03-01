---
title: "tests.core.test_auth_github"
tldr: "Module tests.core.test_auth_github"
tags: [reference, api]
---

# `tests.core.test_auth_github`

**Source:** [`tests/core/test_auth_github.py`](tests/core/test_auth_github.py) · 286 lines

## `TestDeviceFlowModels`

**Source:** [`tests/core/test_auth_github.py#L16`](tests/core/test_auth_github.py#L16)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_device_flow_info()` |  | `None` | — |
| `test_device_flow_handle()` |  | `None` | — |

## `TestGitHubAuthProviderContextManager`

**Source:** [`tests/core/test_auth_github.py#L34`](tests/core/test_auth_github.py#L34)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| 🔄 `test_creates_client_on_enter()` |  | `None` | — |
| 🔄 `test_uses_provided_client()` |  | `None` | — |

## `TestGitHubAuthProviderGetToken`

**Source:** [`tests/core/test_auth_github.py#L53`](tests/core/test_auth_github.py#L53)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_token_from_keyring()` |  | `None` | — |
| `test_returns_none_on_keyring_error()` |  | `None` | — |
| `test_returns_none_when_no_token()` |  | `None` | — |

## `TestGitHubAuthProviderHasToken`

**Source:** [`tests/core/test_auth_github.py#L79`](tests/core/test_auth_github.py#L79)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_returns_true_when_token_exists()` |  | `None` | — |
| `test_returns_false_when_no_token()` |  | `None` | — |

## `TestGitHubAuthProviderStartDeviceFlow`

**Source:** [`tests/core/test_auth_github.py#L93`](tests/core/test_auth_github.py#L93)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `mock_client()` |  | `MagicMock` | — |
| `provider()` | mock_client | `GitHubAuthProvider` | — |
| 🔄 `test_start_device_flow_success()` | provider, mock_client | `None` | — |
| 🔄 `test_start_device_flow_without_browser()` | provider, mock_client | `None` | — |
| 🔄 `test_start_device_flow_failure()` | provider, mock_client | `None` | — |

## `TestGitHubAuthProviderPollForToken`

**Source:** [`tests/core/test_auth_github.py#L155`](tests/core/test_auth_github.py#L155)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `mock_client()` |  | `MagicMock` | — |
| `provider()` | mock_client | `GitHubAuthProvider` | — |
| 🔄 `test_poll_returns_token_on_success()` | provider, mock_client | `None` | — |
| 🔄 `test_poll_handles_slow_down()` | provider, mock_client | `None` | — |
| 🔄 `test_poll_raises_on_expired_token()` | provider, mock_client | `None` | — |
| 🔄 `test_poll_raises_on_access_denied()` | provider, mock_client | `None` | — |
| 🔄 `test_poll_raises_on_timeout()` | provider, mock_client | `None` | — |

## `TestGitHubAuthProviderSaveToken`

**Source:** [`tests/core/test_auth_github.py#L239`](tests/core/test_auth_github.py#L239)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_save_token_success()` |  | `None` | — |
| `test_save_token_raises_on_keyring_error()` |  | `None` | — |

## `TestGitHubAuthProviderWaitForToken`

**Source:** [`tests/core/test_auth_github.py#L259`](tests/core/test_auth_github.py#L259)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `mock_client()` |  | `MagicMock` | — |
| `provider()` | mock_client | `GitHubAuthProvider` | — |
| 🔄 `test_wait_for_token_polls_and_saves()` | provider, mock_client | `None` | — |

