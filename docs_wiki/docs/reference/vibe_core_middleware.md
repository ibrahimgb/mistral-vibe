---
title: "vibe.core.middleware"
tldr: "Module vibe.core.middleware"
tags: [reference, api]
---

# [**vibe.core.middleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py)

This module defines the constants `PLAN_AGENT_REMINDER`, `PLAN_AGENT_EXIT`, `CHAT_AGENT_REMINDER`, `CHAT_AGENT_EXIT`.

## [**MiddlewareAction**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L16)

The [**MiddlewareAction**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L16) enum (extending `StrEnum`). Key fields include `CONTINUE`, `STOP`, `COMPACT`, `INJECT_MESSAGE`.

## [**ResetReason**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L23)

The [**ResetReason**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L23) enum (extending `StrEnum`). Key fields include `STOP`, `COMPACT`.

## [**ConversationContext**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L29)

The [**ConversationContext**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L29) dataclass. Key fields include `messages`, `stats`, `config`.

## [**MiddlewareResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L36)

The [**MiddlewareResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L36) dataclass. Key fields include `action`, `message`, `reason`, `metadata`.

## [**ConversationMiddleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L43)

The [**ConversationMiddleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L43) protocol (extending `Protocol`). It exposes `before_turn()`, `reset()`.

**Public API:**

- `async def before_turn()`
- `def reset()`

## [**TurnLimitMiddleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L49)

The [**TurnLimitMiddleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L49) class. It exposes `__init__()`, `before_turn()`, `reset()`.

**Public API:**

- `def __init__()`
- `async def before_turn()`
- `def reset()`

## [**PriceLimitMiddleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L65)

The [**PriceLimitMiddleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L65) class. It exposes `__init__()`, `before_turn()`, `reset()`.

**Public API:**

- `def __init__()`
- `async def before_turn()`
- `def reset()`

## [**AutoCompactMiddleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L81)

The [**AutoCompactMiddleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L81) class. It exposes `__init__()`, `before_turn()`, `reset()`.

**Public API:**

- `def __init__()`
- `async def before_turn()`
- `def reset()`

## [**ContextWarningMiddleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L100)

The [**ContextWarningMiddleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L100) class. It exposes `__init__()`, `before_turn()`, `reset()`.

**Public API:**

- `def __init__()`
- `async def before_turn()`
- `def reset()`

## [**ReadOnlyAgentMiddleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L147)

The [**ReadOnlyAgentMiddleware**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L147) class. It exposes `__init__()`, `before_turn()`, `reset()`.

**Public API:**

- `def __init__()`
- `async def before_turn()`
- `def reset()`

## [**MiddlewarePipeline**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L187)

The [**MiddlewarePipeline**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/middleware.py#L187) class. It exposes `__init__()`, `add()`, `clear()`, `reset()`, `run_before_turn()`.

**Public API:**

- `def __init__()`
- `def add()`
- `def clear()`
- `def reset()`
- `async def run_before_turn()`

