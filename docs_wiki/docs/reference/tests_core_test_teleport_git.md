---
title: "tests.core.test_teleport_git"
tldr: "Module tests.core.test_teleport_git"
tags: [reference, api]
---

# `tests.core.test_teleport_git`

**Source:** [`tests/core/test_teleport_git.py`](tests/core/test_teleport_git.py) · 327 lines

## `TestGitRepositoryParseGithubUrl`

**Source:** [`tests/core/test_teleport_git.py#L44`](tests/core/test_teleport_git.py#L44)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_parse_ssh_url()` |  | `None` | — |
| `test_parse_ssh_url_without_git_suffix()` |  | `None` | — |
| `test_parse_https_url()` |  | `None` | — |
| `test_parse_https_url_without_git_suffix()` |  | `None` | — |
| `test_parse_https_url_with_credentials()` |  | `None` | — |
| `test_parse_non_github_url_returns_none()` |  | `None` | — |
| `test_parse_invalid_url_returns_none()` |  | `None` | — |

## `TestGitRepositoryToHttpsUrl`

**Source:** [`tests/core/test_teleport_git.py#L76`](tests/core/test_teleport_git.py#L76)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `test_converts_to_https_url()` |  | `None` | — |

## `TestGitRepositoryIsSupported`

**Source:** [`tests/core/test_teleport_git.py#L82`](tests/core/test_teleport_git.py#L82)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `repo()` | tmp_path | `GitRepository` | — |
| 🔄 `test_returns_false_when_not_git_repo()` | tmp_path | `None` | — |
| 🔄 `test_returns_false_when_no_remote()` | repo | `None` | — |
| 🔄 `test_returns_false_when_non_github_remote()` | repo | `None` | — |
| 🔄 `test_returns_true_when_github_repo()` | repo | `None` | — |
| 🔄 `test_finds_github_among_multiple_remotes()` | repo | `None` | — |

## `TestGitRepositoryGetInfo`

**Source:** [`tests/core/test_teleport_git.py#L123`](tests/core/test_teleport_git.py#L123)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `repo()` | tmp_path | `GitRepository` | — |
| 🔄 `test_raises_when_not_git_repo()` | tmp_path | `None` | — |
| 🔄 `test_raises_when_no_remote()` | repo | `None` | — |
| 🔄 `test_raises_when_non_github_remote()` | repo | `None` | — |
| 🔄 `test_raises_when_no_commit()` | repo | `None` | — |
| 🔄 `test_returns_info_on_success()` | repo | `None` | — |
| 🔄 `test_handles_detached_head()` | repo | `None` | — |

## `TestGitRepositoryIsCommitPushed`

**Source:** [`tests/core/test_teleport_git.py#L195`](tests/core/test_teleport_git.py#L195)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `repo()` | tmp_path | `GitRepository` | — |
| 🔄 `test_returns_false_when_not_on_remote()` | repo | `None` | — |
| 🔄 `test_returns_true_when_on_remote()` | repo | `None` | — |
| 🔄 `test_checks_correct_remote()` | repo | `None` | — |

## `TestGitRepositoryGetUnpushedCommitCount`

**Source:** [`tests/core/test_teleport_git.py#L223`](tests/core/test_teleport_git.py#L223)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `repo()` | tmp_path | `GitRepository` | — |
| 🔄 `test_raises_when_no_branch()` | repo | `None` | — |
| 🔄 `test_returns_count()` | repo | `None` | — |
| 🔄 `test_fallback_to_default_branch()` | repo | `None` | — |

## `TestGitRepositoryPushCurrentBranch`

**Source:** [`tests/core/test_teleport_git.py#L267`](tests/core/test_teleport_git.py#L267)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `repo()` | tmp_path | `GitRepository` | — |
| 🔄 `test_returns_false_when_no_branch()` | repo | `None` | — |
| 🔄 `test_returns_false_when_push_fails()` | repo | `None` | — |
| 🔄 `test_returns_true_when_push_succeeds()` | repo | `None` | — |

## `TestGitRepositoryGetRemoteDefaultBranch`

**Source:** [`tests/core/test_teleport_git.py#L294`](tests/core/test_teleport_git.py#L294)

### Public Methods

| Method | Parameters | Returns | Description |
|--------|-----------|---------|-------------|
| `repo()` | tmp_path | `GitRepository` | — |
| 🔄 `test_returns_default_branch_when_head_exists()` | repo | `None` | — |
| 🔄 `test_returns_none_when_remote_not_found()` | repo | `None` | — |
| 🔄 `test_returns_none_when_head_ref_missing()` | repo | `None` | — |

## `make_mock_remote()`

```python
def make_mock_remote(url: str) -> MagicMock
```

**Source:** [`tests/core/test_teleport_git.py#L15`](tests/core/test_teleport_git.py#L15)

## `make_mock_repo()`

```python
def make_mock_repo(urls: list[str] | None, commit: str | None, branch: str | None, is_detached: bool, diff: str) -> MagicMock
```

**Source:** [`tests/core/test_teleport_git.py#L21`](tests/core/test_teleport_git.py#L21)

