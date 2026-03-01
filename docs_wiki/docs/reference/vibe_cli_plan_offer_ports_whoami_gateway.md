---
title: "vibe.cli.plan_offer.ports.whoami_gateway"
tldr: "Module vibe.cli.plan_offer.ports.whoami_gateway"
tags: [reference, api]
---

# [**vibe.cli.plan_offer.ports.whoami_gateway**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/ports/whoami_gateway.py)

## [**WhoAmIResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/ports/whoami_gateway.py#L8)

The [**WhoAmIResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/ports/whoami_gateway.py#L8) dataclass. Key fields include `is_pro_plan`, `advertise_pro_plan`, `prompt_switching_to_pro_plan`.

## [**WhoAmIGatewayUnauthorized**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/ports/whoami_gateway.py#L14)

The [**WhoAmIGatewayUnauthorized**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/ports/whoami_gateway.py#L14) class (extending `Exception`).

## [**WhoAmIGatewayError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/ports/whoami_gateway.py#L18)

The [**WhoAmIGatewayError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/ports/whoami_gateway.py#L18) class (extending `Exception`).

## [**WhoAmIGateway**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/ports/whoami_gateway.py#L22)

The [**WhoAmIGateway**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/plan_offer/ports/whoami_gateway.py#L22) protocol (extending `Protocol`). It exposes `whoami()`.

**Public API:**

- `async def whoami()`

