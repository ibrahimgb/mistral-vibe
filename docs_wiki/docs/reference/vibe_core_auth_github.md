---
title: "vibe.core.auth.github"
tldr: "Module vibe.core.auth.github"
tags: [reference, api]
---

# [**vibe.core.auth.github**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/github.py)

This module defines the constants `GITHUB_CLIENT_ID`, `_SERVICE_NAME`, `_KEYRING_USERNAME`, `_DEVICE_CODE_URL`, `_TOKEN_URL`, `_VALIDATE_URL`, `_SCOPES`.

## [**GitHubAuthError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/github.py#L22)

The [**GitHubAuthError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/github.py#L22) class (extending `Exception`).

## [**DeviceFlowInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/github.py#L27)

The [**DeviceFlowInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/github.py#L27) dataclass. Key fields include `user_code`, `verification_uri`.

## [**DeviceFlowHandle**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/github.py#L33)

The [**DeviceFlowHandle**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/github.py#L33) dataclass. Key fields include `device_code`, `expires_in`, `info`.

## [**GitHubAuthProvider**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/github.py#L39)

The [**GitHubAuthProvider**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/auth/github.py#L39) class. It exposes `__init__()`, `__aenter__()`, `__aexit__()`, `get_token()`, `has_token()` among 9 public methods. Internally it relies on `_poll_for_token()`.

**Public API:**

- `def __init__()`
- `async def __aenter__()`
- `async def __aexit__()`
- `def get_token()`
- `def has_token()`
- `def delete_token()`
- `async def get_valid_token()`
- `async def start_device_flow()`
- `async def wait_for_token()`

**Internal helpers:**

- `_poll_for_token()`

