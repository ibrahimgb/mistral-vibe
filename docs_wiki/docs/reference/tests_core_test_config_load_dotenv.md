---
title: "tests.core.test_config_load_dotenv"
tldr: "Module tests.core.test_config_load_dotenv"
tags: [reference, api]
---

# `tests.core.test_config_load_dotenv`

**Source:** [`tests/core/test_config_load_dotenv.py`](tests/core/test_config_load_dotenv.py) · 81 lines

## `_write_env_file()`

```python
def _write_env_file(path: Path, content: str) -> None
```

**Source:** [`tests/core/test_config_load_dotenv.py#L10`](tests/core/test_config_load_dotenv.py#L10)

## `test_skips_missing_file()`

```python
def test_skips_missing_file(tmp_path: Path) -> None
```

**Source:** [`tests/core/test_config_load_dotenv.py#L14`](tests/core/test_config_load_dotenv.py#L14)

## `test_sets_and_overrides_values()`

```python
def test_sets_and_overrides_values(tmp_path: Path) -> None
```

**Source:** [`tests/core/test_config_load_dotenv.py#L23`](tests/core/test_config_load_dotenv.py#L23)

## `test_ignores_empty_values()`

```python
def test_ignores_empty_values(tmp_path: Path) -> None
```

**Source:** [`tests/core/test_config_load_dotenv.py#L52`](tests/core/test_config_load_dotenv.py#L52)

## `test_reads_from_fifo()`

```python
def test_reads_from_fifo(tmp_path: Path) -> None
```

**Source:** [`tests/core/test_config_load_dotenv.py#L66`](tests/core/test_config_load_dotenv.py#L66)

