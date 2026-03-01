---
title: "scripts.prepare_release"
tldr: "Module scripts.prepare_release"
tags: [reference, api]
---

# [**scripts.prepare_release**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py)

## [**run_git_command()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py#L12)

```python
def run_git_command() -> subprocess.CompletedProcess[str]
```

Run a git command and return the result.

## [**ensure_public_remote()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py#L22)

```python
def ensure_public_remote() -> None
```

## [**switch_to_tag()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py#L36)

```python
def switch_to_tag(version: str) -> None
```

## [**get_version_from_pyproject()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py#L50)

```python
def get_version_from_pyproject() -> str
```

## [**get_latest_version()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py#L63)

```python
def get_latest_version() -> str
```

## [**parse_version()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py#L105)

```python
def parse_version(version_str: str) -> tuple[int, int, int]
```

## [**create_release_branch()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py#L113)

```python
def create_release_branch(version: str) -> None
```

## [**cherry_pick_commits()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py#L133)

```python
def cherry_pick_commits(previous_version: str, current_version: str) -> None
```

## [**get_commits_summary()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py#L154)

```python
def get_commits_summary(previous_version: str, current_version: str) -> str
```

## [**get_changelog_entry()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py#L164)

```python
def get_changelog_entry(version: str) -> str
```

## [**print_summary()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py#L180)

```python
def print_summary(current_version: str, previous_version: str, commits_summary: str, changelog_entry: str) -> None
```

## [**main()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/prepare_release.py#L227)

```python
def main() -> None
```

