---
title: "vibe.cli.plan_offer.decide_plan_offer"
tldr: "Module vibe.cli.plan_offer.decide_plan_offer"
tags: [reference, api]
---

# [**vibe.cli.plan_offer.decide_plan_offer**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/decide_plan_offer.py)

This module defines the constants `CONSOLE_CLI_URL`, `UPGRADE_URL`, `SWITCH_TO_PRO_KEY_URL`, `ACTION_TO_URL`.

## [**PlanOfferAction**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/decide_plan_offer.py#L22)

The [**PlanOfferAction**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/decide_plan_offer.py#L22) enum (extending `StrEnum`). Key fields include `NONE`, `UPGRADE`, `SWITCH_TO_PRO_KEY`.

## [**PlanType**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/decide_plan_offer.py#L34)

The [**PlanType**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/decide_plan_offer.py#L34) enum (extending `StrEnum`). Key fields include `FREE`, `PRO`, `UNKNOWN`.

## [**decide_plan_offer()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/decide_plan_offer.py#L40)

```python
async def decide_plan_offer(api_key: str | None, gateway: WhoAmIGateway) -> tuple[PlanOfferAction, PlanType]
```

## [**resolve_api_key_for_plan()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/decide_plan_offer.py#L69)

```python
def resolve_api_key_for_plan(provider: ProviderConfig) -> str | None
```

## [**plan_offer_cta()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/decide_plan_offer.py#L78)

```python
def plan_offer_cta(action: PlanOfferAction) -> str | None
```

