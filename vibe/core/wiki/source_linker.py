"""Git remote detection and source-link generation for wiki documentation.

Provides synchronous helpers that turn ``(relative_path, lineno)`` pairs into
full GitHub / GitLab URLs suitable for embedding in Markdown documentation.

Also exposes commit-based change detection so the wiki pipeline can perform
**incremental rebuilds** — only regenerating pages when ``.py`` files have
actually changed since the last build.

The heavy lifting reuses the same ``gitpython`` + ``giturlparse`` stack that
:mod:`vibe.core.teleport.git` relies on, but avoids the async executor layer
since wiki generation is a batch pipeline.
"""

from __future__ import annotations

import logging
import subprocess
from pathlib import Path

from git import InvalidGitRepositoryError, Repo
from giturlparse import parse as parse_git_url

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Remote detection
# ---------------------------------------------------------------------------

def detect_remote_url(root: Path) -> str | None:
    """Detect the GitHub/GitLab blob base URL for a repository.

    Scans all remotes for a recognised hosting provider and returns a
    permanent URL of the form::

        https://github.com/{owner}/{repo}/blob/{commit_sha}

    Returns ``None`` when *root* is not a git repository, has no remotes,
    or no remote points to a supported host.
    """
    try:
        repo = Repo(root, search_parent_directories=True)
    except (InvalidGitRepositoryError, Exception):
        logger.debug("Not a git repository: %s", root)
        return None

    owner_repo = _find_remote(repo)
    if owner_repo is None:
        logger.debug("No supported remote found for %s", root)
        return None

    owner, repo_name, host = owner_repo

    try:
        commit_sha = repo.head.commit.hexsha
    except (ValueError, TypeError):
        logger.debug("Could not determine HEAD commit for %s", root)
        return None

    return f"https://{host}/{owner}/{repo_name}/blob/{commit_sha}"


# ---------------------------------------------------------------------------
# Link builders
# ---------------------------------------------------------------------------

def source_url(
    remote_base: str | None,
    relative_path: str,
    lineno: int | None = None,
) -> str | None:
    """Build a full source URL for a file (optionally at a line).

    Returns ``None`` when *remote_base* is not available.
    """
    if remote_base is None:
        return None
    url = f"{remote_base}/{relative_path}"
    if lineno:
        url = f"{url}#L{lineno}"
    return url


def source_link_md(
    remote_base: str | None,
    relative_path: str,
    lineno: int | None = None,
    display: str | None = None,
) -> str:
    """Return a Markdown link to a source location.

    When *remote_base* is available the link points to the hosted file::

        [**AgentLoop**](https://github.com/owner/repo/blob/SHA/path.py#L105)

    When no remote is configured, falls back to bold inline code::

        **`AgentLoop`**
    """
    label = display or relative_path
    if url := source_url(remote_base, relative_path, lineno):
        return f"[**{label}**]({url})"
    return f"**`{label}`**"


# ---------------------------------------------------------------------------
# Commit & change detection
# ---------------------------------------------------------------------------

def detect_commit_sha(root: Path) -> str | None:
    """Return the HEAD commit SHA for the repository at *root*.

    Returns ``None`` when *root* is not a git repo or HEAD is detached
    without a valid commit.
    """
    try:
        repo = Repo(root, search_parent_directories=True)
        return repo.head.commit.hexsha
    except (InvalidGitRepositoryError, ValueError, TypeError, Exception):
        return None


def changed_files_since(
    root: Path,
    since_sha: str,
    *,
    suffixes: frozenset[str] = frozenset({".py"}),
) -> list[str] | None:
    """Return paths changed between *since_sha* and HEAD.

    Only files whose suffix is in *suffixes* are included.  Paths are
    relative to the repository root (matching ``ModuleNode.relative_path``).

    Returns ``None`` when the comparison cannot be made (e.g. *since_sha*
    is unreachable after a force-push or shallow clone), signalling the
    caller should fall back to a full rebuild.
    """
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=ACMRD", f"{since_sha}..HEAD"],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            logger.debug("git diff failed (rc=%d): %s", result.returncode, result.stderr.strip())
            return None

        changed: list[str] = []
        for line in result.stdout.strip().splitlines():
            path = line.strip()
            if path and Path(path).suffix in suffixes:
                changed.append(path)
        return changed

    except FileNotFoundError:
        logger.debug("git binary not found")
        return None
    except Exception as exc:
        logger.debug("changed_files_since failed: %s", exc)
        return None


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

_SUPPORTED_HOSTS: frozenset[str] = frozenset({"github.com", "gitlab.com"})


def _find_remote(repo: Repo) -> tuple[str, str, str] | None:
    """Return ``(owner, repo_name, host)`` for the first supported remote."""
    for remote in repo.remotes:
        for url in remote.urls:
            if result := _parse_url(url):
                return result
    return None


def _parse_url(url: str) -> tuple[str, str, str] | None:
    """Parse a git URL and return ``(owner, repo, host)`` if supported."""
    parsed = parse_git_url(url)
    if not parsed.owner or not parsed.repo:
        return None
    # giturlparse exposes .github, .gitlab booleans
    if parsed.github:
        return parsed.owner, parsed.repo, "github.com"
    if parsed.gitlab:
        return parsed.owner, parsed.repo, "gitlab.com"
    # Fallback: check the raw host against our allow-list
    host = getattr(parsed, "host", "") or ""
    if host in _SUPPORTED_HOSTS:
        return parsed.owner, parsed.repo, host
    return None
