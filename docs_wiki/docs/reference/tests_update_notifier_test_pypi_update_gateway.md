---
title: "tests.update_notifier.test_pypi_update_gateway"
tldr: "Module tests.update_notifier.test_pypi_update_gateway"
tags: [reference, api]
---

# `tests.update_notifier.test_pypi_update_gateway`

**Source:** [`tests/update_notifier/test_pypi_update_gateway.py`](tests/update_notifier/test_pypi_update_gateway.py) · 155 lines

## Constants

- `PYPI_API_URL`

## `test_retrieves_nothing_when_no_versions_are_available()`

```python
async def test_retrieves_nothing_when_no_versions_are_available() -> None
```

**Source:** [`tests/update_notifier/test_pypi_update_gateway.py#L21`](tests/update_notifier/test_pypi_update_gateway.py#L21)

## `test_retrieves_the_latest_non_yanked_version()`

```python
async def test_retrieves_the_latest_non_yanked_version() -> None
```

**Source:** [`tests/update_notifier/test_pypi_update_gateway.py#L36`](tests/update_notifier/test_pypi_update_gateway.py#L36)

## `test_retrieves_nothing_when_only_yanked_versions_are_available()`

```python
async def test_retrieves_nothing_when_only_yanked_versions_are_available() -> None
```

**Source:** [`tests/update_notifier/test_pypi_update_gateway.py#L67`](tests/update_notifier/test_pypi_update_gateway.py#L67)

## `test_does_not_match_versions_by_substring()`

```python
async def test_does_not_match_versions_by_substring() -> None
```

**Source:** [`tests/update_notifier/test_pypi_update_gateway.py#L88`](tests/update_notifier/test_pypi_update_gateway.py#L88)

## `_raise_connect_timeout()`

```python
def _raise_connect_timeout(request: httpx.Request) -> httpx.Response
```

**Source:** [`tests/update_notifier/test_pypi_update_gateway.py#L111`](tests/update_notifier/test_pypi_update_gateway.py#L111)

## `test_retrieves_nothing_when_fetching_update_fails()`

```python
async def test_retrieves_nothing_when_fetching_update_fails(handler: Callable[[httpx.Request], httpx.Response], expected_cause: UpdateGatewayCause, expected_message: str | None) -> None
```

**Source:** [`tests/update_notifier/test_pypi_update_gateway.py#L142`](tests/update_notifier/test_pypi_update_gateway.py#L142)

