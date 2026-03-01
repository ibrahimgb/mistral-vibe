---
title: "tests.update_notifier.test_update_use_case"
tldr: "Module tests.update_notifier.test_update_use_case"
tags: [reference, api]
---

# `tests.update_notifier.test_update_use_case`

**Source:** [`tests/update_notifier/test_update_use_case.py`](tests/update_notifier/test_update_use_case.py) · 302 lines

## `current_timestamp()`

```python
def current_timestamp() -> int
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L19`](tests/update_notifier/test_update_use_case.py#L19)

## `test_retrieves_the_latest_update_when_available()`

```python
async def test_retrieves_the_latest_update_when_available() -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L24`](tests/update_notifier/test_update_use_case.py#L24)

## `test_retrieves_nothing_when_the_current_version_is_the_latest()`

```python
async def test_retrieves_nothing_when_the_current_version_is_the_latest() -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L39`](tests/update_notifier/test_update_use_case.py#L39)

## `test_retrieves_nothing_when_the_current_version_is_greater_than_the_latest()`

```python
async def test_retrieves_nothing_when_the_current_version_is_greater_than_the_latest() -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L54`](tests/update_notifier/test_update_use_case.py#L54)

## `test_retrieves_nothing_when_no_version_is_available()`

```python
async def test_retrieves_nothing_when_no_version_is_available() -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L71`](tests/update_notifier/test_update_use_case.py#L71)

## `test_retrieves_nothing_when_latest_version_is_invalid()`

```python
async def test_retrieves_nothing_when_latest_version_is_invalid() -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L84`](tests/update_notifier/test_update_use_case.py#L84)

## `test_replaces_hyphens_with_plus_signs_in_latest_version_to_conform_with_PEP_440()`

```python
async def test_replaces_hyphens_with_plus_signs_in_latest_version_to_conform_with_PEP_440() -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L97`](tests/update_notifier/test_update_use_case.py#L97)

## `test_retrieves_nothing_when_current_version_is_invalid()`

```python
async def test_retrieves_nothing_when_current_version_is_invalid() -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L116`](tests/update_notifier/test_update_use_case.py#L116)

## `test_raises_update_error()`

```python
async def test_raises_update_error(cause: UpdateGatewayCause, expected_message_substring: str) -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L142`](tests/update_notifier/test_update_use_case.py#L142)

## `test_notifies_and_updates_cache_when_repository_is_empty()`

```python
async def test_notifies_and_updates_cache_when_repository_is_empty(current_timestamp: int) -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L158`](tests/update_notifier/test_update_use_case.py#L158)

## `test_does_not_notify_when_an_available_update_has_been_recently_cached()`

```python
async def test_does_not_notify_when_an_available_update_has_been_recently_cached(current_timestamp: int) -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L181`](tests/update_notifier/test_update_use_case.py#L181)

## `test_retrieves_nothing_when_the_recently_cached_update_is_the_one_currently_in_use()`

```python
async def test_retrieves_nothing_when_the_recently_cached_update_is_the_one_currently_in_use(current_timestamp: int) -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L205`](tests/update_notifier/test_update_use_case.py#L205)

## `test_retrieves_fresh_update_and_notifies_and_updates_cache_when_cache_is_not_fresh()`

```python
async def test_retrieves_fresh_update_and_notifies_and_updates_cache_when_cache_is_not_fresh(current_timestamp: int) -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L227`](tests/update_notifier/test_update_use_case.py#L227)

## `test_updates_cache_timestamp_with_current_version_when_no_update_is_available()`

```python
async def test_updates_cache_timestamp_with_current_version_when_no_update_is_available(current_timestamp: int) -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L254`](tests/update_notifier/test_update_use_case.py#L254)

## `test_updates_cache_timestamp_with_current_version_when_gateway_errors()`

```python
async def test_updates_cache_timestamp_with_current_version_when_gateway_errors(current_timestamp: int) -> None
```

**Source:** [`tests/update_notifier/test_update_use_case.py#L279`](tests/update_notifier/test_update_use_case.py#L279)

