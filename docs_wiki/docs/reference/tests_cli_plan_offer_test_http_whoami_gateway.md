---
title: "tests.cli.plan_offer.test_http_whoami_gateway"
tldr: "Module tests.cli.plan_offer.test_http_whoami_gateway"
tags: [reference, api]
---

# `tests.cli.plan_offer.test_http_whoami_gateway`

**Source:** [`tests/cli/plan_offer/test_http_whoami_gateway.py`](tests/cli/plan_offer/test_http_whoami_gateway.py) · 122 lines

## `test_returns_plan_flags()`

```python
async def test_returns_plan_flags(respx_mock: respx.MockRouter) -> None
```

**Source:** [`tests/cli/plan_offer/test_http_whoami_gateway.py#L16`](tests/cli/plan_offer/test_http_whoami_gateway.py#L16)

## `test_raises_on_unauthorized()`

```python
async def test_raises_on_unauthorized(respx_mock: respx.MockRouter, status_code: int) -> None
```

**Source:** [`tests/cli/plan_offer/test_http_whoami_gateway.py#L41`](tests/cli/plan_offer/test_http_whoami_gateway.py#L41)

## `test_raises_on_non_success()`

```python
async def test_raises_on_non_success(respx_mock: respx.MockRouter) -> None
```

**Source:** [`tests/cli/plan_offer/test_http_whoami_gateway.py#L55`](tests/cli/plan_offer/test_http_whoami_gateway.py#L55)

## `test_incomplete_payload_defaults_missing_flags_to_false()`

```python
async def test_incomplete_payload_defaults_missing_flags_to_false(respx_mock: respx.MockRouter) -> None
```

**Source:** [`tests/cli/plan_offer/test_http_whoami_gateway.py#L67`](tests/cli/plan_offer/test_http_whoami_gateway.py#L67)

## `test_wraps_request_error()`

```python
async def test_wraps_request_error(respx_mock: respx.MockRouter) -> None
```

**Source:** [`tests/cli/plan_offer/test_http_whoami_gateway.py#L82`](tests/cli/plan_offer/test_http_whoami_gateway.py#L82)

## `test_parses_boolean_strings()`

```python
async def test_parses_boolean_strings(respx_mock: respx.MockRouter) -> None
```

**Source:** [`tests/cli/plan_offer/test_http_whoami_gateway.py#L94`](tests/cli/plan_offer/test_http_whoami_gateway.py#L94)

## `test_raises_on_invalid_boolean_string()`

```python
async def test_raises_on_invalid_boolean_string(respx_mock: respx.MockRouter) -> None
```

**Source:** [`tests/cli/plan_offer/test_http_whoami_gateway.py#L114`](tests/cli/plan_offer/test_http_whoami_gateway.py#L114)

