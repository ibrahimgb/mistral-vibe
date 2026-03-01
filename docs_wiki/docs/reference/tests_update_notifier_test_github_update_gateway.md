---
title: "tests.update_notifier.test_github_update_gateway"
tldr: "Module tests.update_notifier.test_github_update_gateway"
tags: [reference, api]
---

# `tests.update_notifier.test_github_update_gateway`

**Source:** [`tests/update_notifier/test_github_update_gateway.py`](tests/update_notifier/test_github_update_gateway.py) · 245 lines

## Constants

- `GITHUB_API_URL`

## `_raise_connect_timeout()`

```python
def _raise_connect_timeout(request: httpx.Request) -> httpx.Response
```

**Source:** [`tests/update_notifier/test_github_update_gateway.py#L19`](tests/update_notifier/test_github_update_gateway.py#L19)

## `test_retrieves_latest_version_when_available()`

```python
async def test_retrieves_latest_version_when_available() -> None
```

**Source:** [`tests/update_notifier/test_github_update_gateway.py#L24`](tests/update_notifier/test_github_update_gateway.py#L24)

## `test_strips_uppercase_prefix_from_tag_name()`

```python
async def test_strips_uppercase_prefix_from_tag_name() -> None
```

**Source:** [`tests/update_notifier/test_github_update_gateway.py#L44`](tests/update_notifier/test_github_update_gateway.py#L44)

## `test_considers_no_update_available_when_no_releases_are_found()`

```python
async def test_considers_no_update_available_when_no_releases_are_found() -> None
```

If the repository cannot be accessed (e.g. invalid token), the response will be 404.
But using API 'releases/latest', if no release has been created, the response will ALSO be 404.

This test ensures that we consider no update available when no releases are found.
(And this is why we are using "releases" with a per_page=1 parameter, instead of "releases/latest")

**Source:** [`tests/update_notifier/test_github_update_gateway.py#L63`](tests/update_notifier/test_github_update_gateway.py#L63)

## `test_considers_no_update_available_when_only_drafts_and_prereleases_are_found()`

```python
async def test_considers_no_update_available_when_only_drafts_and_prereleases_are_found() -> None
```

**Source:** [`tests/update_notifier/test_github_update_gateway.py#L85`](tests/update_notifier/test_github_update_gateway.py#L85)

## `test_picks_the_most_recently_published_non_prerelease_and_non_draft()`

```python
async def test_picks_the_most_recently_published_non_prerelease_and_non_draft() -> None
```

**Source:** [`tests/update_notifier/test_github_update_gateway.py#L108`](tests/update_notifier/test_github_update_gateway.py#L108)

## `test_ignores_draft_releases_and_prereleases()`

```python
async def test_ignores_draft_releases_and_prereleases(payload: dict[str, object]) -> None
```

**Source:** [`tests/update_notifier/test_github_update_gateway.py#L165`](tests/update_notifier/test_github_update_gateway.py#L165)

## `test_retrieves_nothing_when_fetching_update_fails()`

```python
async def test_retrieves_nothing_when_fetching_update_fails(handler: Handler, expected_cause: UpdateGatewayCause, expected_custom_message: str | None) -> None
```

**Source:** [`tests/update_notifier/test_github_update_gateway.py#L230`](tests/update_notifier/test_github_update_gateway.py#L230)

