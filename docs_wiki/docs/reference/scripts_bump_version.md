---
title: "scripts.bump_version"
tldr: "Version bumping script for semver versioning."
tags: [reference, api]
---

# [**scripts.bump_version**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/bump_version.py)

Version bumping script for semver versioning.

This script increments the version in pyproject.toml based on the specified bump type:
- major: 1.0.0 -> 2.0.0
- minor: 1.0.0 -> 1.1.0
- micro/patch: 1.0.0 -> 1.0.1

This module defines the constants `BUMP_TYPES`.

## [**parse_version()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/bump_version.py#L25)

```python
def parse_version(version_str: str) -> tuple[int, int, int]
```

## [**format_version()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/bump_version.py#L33)

```python
def format_version(major: int, minor: int, patch: int) -> str
```

## [**bump_version()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/bump_version.py#L37)

```python
def bump_version(version: str, bump_type: BumpType) -> str
```

## [**update_hard_values_files()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/bump_version.py#L49)

```python
def update_hard_values_files(filepath: str, patterns: list[tuple[str, str]]) -> None
```

## [**get_current_version()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/bump_version.py#L67)

```python
def get_current_version() -> str
```

## [**update_changelog()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/bump_version.py#L82)

```python
def update_changelog(new_version: str) -> None
```

## [**print_warning()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/bump_version.py#L110)

```python
def print_warning(new_version: str) -> None
```

## [**clean_up_whats_new_message()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/bump_version.py#L125)

```python
def clean_up_whats_new_message() -> None
```

## [**main()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/scripts/bump_version.py#L133)

```python
def main() -> None
```

