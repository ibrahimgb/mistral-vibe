---
title: "vibe.cli.update_notifier.ports.update_gateway"
tldr: "Module vibe.cli.update_notifier.ports.update_gateway"
tags: [reference, api]
---

# [**vibe.cli.update_notifier.ports.update_gateway**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_gateway.py)

This module defines the constants `DEFAULT_GATEWAY_MESSAGES`.

## [**Update**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_gateway.py#L9)

The [**Update**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_gateway.py#L9) dataclass. Key fields include `latest_version`.

## [**UpdateGatewayCause**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_gateway.py#L13)

The [**UpdateGatewayCause**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_gateway.py#L13) enum (extending `StrEnum`). Key fields include `TOO_MANY_REQUESTS`, `FORBIDDEN`, `NOT_FOUND`, `REQUEST_FAILED`, `ERROR_RESPONSE`, `INVALID_RESPONSE`, `UNKNOWN`.

## [**UpdateGatewayError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_gateway.py#L40)

The [**UpdateGatewayError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_gateway.py#L40) class (extending `Exception`). It exposes `__init__()`.

**Public API:**

- `def __init__()`

## [**UpdateGateway**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_gateway.py#L52)

The [**UpdateGateway**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/update_notifier/ports/update_gateway.py#L52) protocol (extending `Protocol`). It exposes `fetch_update()`.

**Public API:**

- `async def fetch_update()`

