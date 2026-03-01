---
title: "tests.skills.conftest"
tldr: "Module tests.skills.conftest"
tags: [reference, api]
---

# `tests.skills.conftest`

**Source:** [`tests/skills/conftest.py`](tests/skills/conftest.py) · 62 lines

## `skills_dir()`

```python
def skills_dir(tmp_path: Path) -> Path
```

Create a temporary skills directory.

**Source:** [`tests/skills/conftest.py#L13`](tests/skills/conftest.py#L13)

## `skill_config()`

```python
def skill_config(skills_dir: Path) -> VibeConfig
```

**Source:** [`tests/skills/conftest.py#L21`](tests/skills/conftest.py#L21)

## `create_skill()`

```python
def create_skill(skills_dir: Path, name: str, description: str) -> Path
```

**Source:** [`tests/skills/conftest.py#L29`](tests/skills/conftest.py#L29)

