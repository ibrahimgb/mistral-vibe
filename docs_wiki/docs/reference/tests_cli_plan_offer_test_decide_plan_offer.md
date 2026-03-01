---
title: "tests.cli.plan_offer.test_decide_plan_offer"
tldr: "Module tests.cli.plan_offer.test_decide_plan_offer"
tags: [reference, api]
---

# `tests.cli.plan_offer.test_decide_plan_offer`

**Source:** [`tests/cli/plan_offer/test_decide_plan_offer.py`](tests/cli/plan_offer/test_decide_plan_offer.py) · 182 lines

## `mistral_api_key_env()`

```python
def mistral_api_key_env() -> Generator[str, None, None]
```

**Source:** [`tests/cli/plan_offer/test_decide_plan_offer.py#L21`](tests/cli/plan_offer/test_decide_plan_offer.py#L21)

## `test_proposes_upgrade_without_call_when_api_key_is_empty()`

```python
async def test_proposes_upgrade_without_call_when_api_key_is_empty() -> None
```

**Source:** [`tests/cli/plan_offer/test_decide_plan_offer.py#L34`](tests/cli/plan_offer/test_decide_plan_offer.py#L34)

## `test_proposes_an_action_based_on_current_plan_status()`

```python
async def test_proposes_an_action_based_on_current_plan_status(response: WhoAmIResponse, expected_action: PlanOfferAction, expected_plan_type: PlanType) -> None
```

**Source:** [`tests/cli/plan_offer/test_decide_plan_offer.py#L83`](tests/cli/plan_offer/test_decide_plan_offer.py#L83)

## `test_proposes_nothing_when_nothing_is_suggested()`

```python
async def test_proposes_nothing_when_nothing_is_suggested() -> None
```

**Source:** [`tests/cli/plan_offer/test_decide_plan_offer.py#L97`](tests/cli/plan_offer/test_decide_plan_offer.py#L97)

## `test_proposes_upgrade_when_api_key_is_unauthorized()`

```python
async def test_proposes_upgrade_when_api_key_is_unauthorized() -> None
```

**Source:** [`tests/cli/plan_offer/test_decide_plan_offer.py#L114`](tests/cli/plan_offer/test_decide_plan_offer.py#L114)

## `test_proposes_none_and_logs_warning_when_gateway_error_occurs()`

```python
async def test_proposes_none_and_logs_warning_when_gateway_error_occurs(caplog: pytest.LogCaptureFixture) -> None
```

**Source:** [`tests/cli/plan_offer/test_decide_plan_offer.py#L124`](tests/cli/plan_offer/test_decide_plan_offer.py#L124)

## `test_resolve_api_key_for_plan_with_mistral_backend()`

```python
def test_resolve_api_key_for_plan_with_mistral_backend(mistral_api_key_env: str) -> None
```

**Source:** [`tests/cli/plan_offer/test_decide_plan_offer.py#L137`](tests/cli/plan_offer/test_decide_plan_offer.py#L137)

## `test_resolve_api_key_for_plan_with_non_mistral_backend()`

```python
def test_resolve_api_key_for_plan_with_non_mistral_backend(mistral_api_key_env: str) -> None
```

**Source:** [`tests/cli/plan_offer/test_decide_plan_offer.py#L153`](tests/cli/plan_offer/test_decide_plan_offer.py#L153)

## `test_resolve_api_key_for_plan_with_missing_env_var()`

```python
def test_resolve_api_key_for_plan_with_missing_env_var() -> None
```

**Source:** [`tests/cli/plan_offer/test_decide_plan_offer.py#L167`](tests/cli/plan_offer/test_decide_plan_offer.py#L167)

