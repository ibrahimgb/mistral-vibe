---
title: "tests.update_notifier.test_filesystem_update_cache_repository"
tldr: "Module tests.update_notifier.test_filesystem_update_cache_repository"
tags: [reference, api]
---

# `tests.update_notifier.test_filesystem_update_cache_repository`

**Source:** [`tests/update_notifier/test_filesystem_update_cache_repository.py`](tests/update_notifier/test_filesystem_update_cache_repository.py) · 119 lines

## `test_reads_cache_from_file_when_present()`

```python
async def test_reads_cache_from_file_when_present(tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_filesystem_update_cache_repository.py#L15`](tests/update_notifier/test_filesystem_update_cache_repository.py#L15)

## `test_returns_none_when_cache_file_is_missing()`

```python
async def test_returns_none_when_cache_file_is_missing(tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_filesystem_update_cache_repository.py#L31`](tests/update_notifier/test_filesystem_update_cache_repository.py#L31)

## `test_returns_none_when_cache_file_is_corrupted()`

```python
async def test_returns_none_when_cache_file_is_corrupted(tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_filesystem_update_cache_repository.py#L40`](tests/update_notifier/test_filesystem_update_cache_repository.py#L40)

## `test_overwrites_existing_cache()`

```python
async def test_overwrites_existing_cache(tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_filesystem_update_cache_repository.py#L52`](tests/update_notifier/test_filesystem_update_cache_repository.py#L52)

## `test_reads_cache_with_seen_whats_new_version()`

```python
async def test_reads_cache_with_seen_whats_new_version(tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_filesystem_update_cache_repository.py#L70`](tests/update_notifier/test_filesystem_update_cache_repository.py#L70)

## `test_writes_cache_with_seen_whats_new_version()`

```python
async def test_writes_cache_with_seen_whats_new_version(tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_filesystem_update_cache_repository.py#L90`](tests/update_notifier/test_filesystem_update_cache_repository.py#L90)

## `test_silently_ignores_errors_when_writing_cache_fails()`

```python
async def test_silently_ignores_errors_when_writing_cache_fails(tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_filesystem_update_cache_repository.py#L109`](tests/update_notifier/test_filesystem_update_cache_repository.py#L109)

