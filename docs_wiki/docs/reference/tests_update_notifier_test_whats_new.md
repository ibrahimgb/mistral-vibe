---
title: "tests.update_notifier.test_whats_new"
tldr: "Module tests.update_notifier.test_whats_new"
tags: [reference, api]
---

# `tests.update_notifier.test_whats_new`

**Source:** [`tests/update_notifier/test_whats_new.py`](tests/update_notifier/test_whats_new.py) · 161 lines

## `test_should_show_whats_new_returns_false_when_cache_is_none()`

```python
async def test_should_show_whats_new_returns_false_when_cache_is_none() -> None
```

**Source:** [`tests/update_notifier/test_whats_new.py#L20`](tests/update_notifier/test_whats_new.py#L20)

## `test_should_show_whats_new_returns_true_when_seen_whats_new_version_differs()`

```python
async def test_should_show_whats_new_returns_true_when_seen_whats_new_version_differs() -> None
```

**Source:** [`tests/update_notifier/test_whats_new.py#L29`](tests/update_notifier/test_whats_new.py#L29)

## `test_should_show_whats_new_returns_false_when_seen_whats_new_version_matches()`

```python
async def test_should_show_whats_new_returns_false_when_seen_whats_new_version_matches() -> None
```

**Source:** [`tests/update_notifier/test_whats_new.py#L45`](tests/update_notifier/test_whats_new.py#L45)

## `test_should_show_whats_new_returns_true_when_seen_whats_new_version_is_none()`

```python
async def test_should_show_whats_new_returns_true_when_seen_whats_new_version_is_none() -> None
```

**Source:** [`tests/update_notifier/test_whats_new.py#L61`](tests/update_notifier/test_whats_new.py#L61)

## `test_load_whats_new_content_returns_none_when_file_does_not_exist()`

```python
def test_load_whats_new_content_returns_none_when_file_does_not_exist(tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_whats_new.py#L76`](tests/update_notifier/test_whats_new.py#L76)

## `test_load_whats_new_content_returns_none_when_file_is_empty()`

```python
def test_load_whats_new_content_returns_none_when_file_is_empty(tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_whats_new.py#L85`](tests/update_notifier/test_whats_new.py#L85)

## `test_load_whats_new_content_returns_none_when_file_contains_only_whitespace()`

```python
def test_load_whats_new_content_returns_none_when_file_contains_only_whitespace(tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_whats_new.py#L95`](tests/update_notifier/test_whats_new.py#L95)

## `test_load_whats_new_content_returns_content_when_file_exists()`

```python
def test_load_whats_new_content_returns_content_when_file_exists(tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_whats_new.py#L107`](tests/update_notifier/test_whats_new.py#L107)

## `test_load_whats_new_content_handles_os_error()`

```python
def test_load_whats_new_content_handles_os_error(tmp_path: Path) -> None
```

**Source:** [`tests/update_notifier/test_whats_new.py#L120`](tests/update_notifier/test_whats_new.py#L120)

## `test_mark_version_as_seen_creates_new_cache_when_repository_is_empty()`

```python
async def test_mark_version_as_seen_creates_new_cache_when_repository_is_empty() -> None
```

**Source:** [`tests/update_notifier/test_whats_new.py#L132`](tests/update_notifier/test_whats_new.py#L132)

## `test_mark_version_as_seen_updates_seen_whats_new_version_preserving_other_fields()`

```python
async def test_mark_version_as_seen_updates_seen_whats_new_version_preserving_other_fields() -> None
```

**Source:** [`tests/update_notifier/test_whats_new.py#L146`](tests/update_notifier/test_whats_new.py#L146)

