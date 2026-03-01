---
title: "vibe.core.wiki.source_linker"
tldr: "Git remote detection and source-link generation for wiki documentation."
tags: [reference, api]
---

# [**vibe.core.wiki.source_linker**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/source_linker.py)

Git remote detection and source-link generation for wiki documentation.

Provides synchronous helpers that turn ``(relative_path, lineno)`` pairs into
full GitHub / GitLab URLs suitable for embedding in Markdown documentation.

Also exposes commit-based change detection so the wiki pipeline can perform
**incremental rebuilds** — only regenerating pages when ``.py`` files have
actually changed since the last build.

The heavy lifting reuses the same ``gitpython`` + ``giturlparse`` stack that
:mod:`vibe.core.teleport.git` relies on, but avoids the async executor layer
since wiki generation is a batch pipeline.

This module defines the constants `_SUPPORTED_HOSTS`.

## [**detect_remote_url()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/source_linker.py#L31)

```python
def detect_remote_url(root: Path) -> str | None
```

Detect the GitHub/GitLab blob base URL for a repository.

Scans all remotes for a recognised hosting provider and returns a
permanent URL of the form::

    https://github.com/{owner}/{repo}/blob/{commit_sha}

Returns ``None`` when *root* is not a git repository, has no remotes,
or no remote points to a supported host.

## [**source_url()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/source_linker.py#L68)

```python
def source_url(remote_base: str | None, relative_path: str, lineno: int | None) -> str | None
```

Build a full source URL for a file (optionally at a line).

Returns ``None`` when *remote_base* is not available.

## [**source_link_md()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/source_linker.py#L85)

```python
def source_link_md(remote_base: str | None, relative_path: str, lineno: int | None, display: str | None) -> str
```

Return a Markdown link to a source location.

When *remote_base* is available the link points to the hosted file::

    [**AgentLoop**](https://github.com/owner/repo/blob/SHA/path.py#L105)

When no remote is configured, falls back to bold inline code::

    **`AgentLoop`**

## [**detect_commit_sha()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/source_linker.py#L111)

```python
def detect_commit_sha(root: Path) -> str | None
```

Return the HEAD commit SHA for the repository at *root*.

Returns ``None`` when *root* is not a git repo or HEAD is detached
without a valid commit.

## [**changed_files_since()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/source_linker.py#L124)

```python
def changed_files_since(root: Path, since_sha: str) -> list[str] | None
```

Return paths changed between *since_sha* and HEAD.

Only files whose suffix is in *suffixes* are included.  Paths are
relative to the repository root (matching ``ModuleNode.relative_path``).

Returns ``None`` when the comparison cannot be made (e.g. *since_sha*
is unreachable after a force-push or shallow clone), signalling the
caller should fall back to a full rebuild.

## [**_find_remote()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/source_linker.py#L173)

```python
def _find_remote(repo: Repo) -> tuple[str, str, str] | None
```

Return ``(owner, repo_name, host)`` for the first supported remote.

## [**_parse_url()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/source_linker.py#L182)

```python
def _parse_url(url: str) -> tuple[str, str, str] | None
```

Parse a git URL and return ``(owner, repo, host)`` if supported.

