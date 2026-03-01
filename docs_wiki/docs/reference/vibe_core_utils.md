---
title: "vibe.core.utils"
tldr: "Module vibe.core.utils"
tags: [reference, api]
---

# [**vibe.core.utils**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py)

This module defines the constants `CANCELLATION_TAG`, `TOOL_ERROR_TAG`, `VIBE_STOP_EVENT_TAG`, `VIBE_WARNING_TAG`, `KNOWN_TAGS`.

## [**TaggedText**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L29)

The [**TaggedText**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L29) class. It exposes `__init__()`, `__str__()`, `from_string()`.

**Public API:**

- `def __init__()`
- `def __str__()`
- `def from_string()`

## [**CancellationReason**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L65)

The [**CancellationReason**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L65) enum (extending `Enum`). Key fields include `OPERATION_CANCELLED`, `TOOL_INTERRUPTED`, `TOOL_NO_RESPONSE`, `TOOL_SKIPPED`.

## [**ConversationLimitException**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L242)

The [**ConversationLimitException**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L242) class (extending `Exception`).

## [**AsyncExecutor**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L297)

The [**AsyncExecutor**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L297) class run sync functions in a thread pool with timeout. supports async context manager. It exposes `__init__()`, `__aenter__()`, `__aexit__()`, `run()`, `shutdown()`.

**Public API:**

- `def __init__()`
- `async def __aenter__()`
- `async def __aexit__()`
- `async def run()`
- `def shutdown()`

## [**get_user_cancellation_message()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L72)

```python
def get_user_cancellation_message(cancellation_reason: CancellationReason, tool_name: str | None) -> TaggedText
```

## [**is_user_cancellation_event()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L90)

```python
def is_user_cancellation_event(event: BaseEvent) -> bool
```

## [**is_dangerous_directory()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L99)

```python
def is_dangerous_directory(path: Path | str) -> tuple[bool, str]
```

Check if the current directory is a dangerous folder that would cause
issues if we were to run the tool there.

Args:
    path: Path to check (defaults to current directory)

Returns:
    tuple[bool, str]: (is_dangerous, reason) where reason explains why it's dangerous

## [**get_user_agent()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L138)

```python
def get_user_agent(backend: Backend | None) -> str
```

## [**async_retry()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L152)

```python
def async_retry(tries: int, delay_seconds: float, backoff_factor: float, is_retryable: Callable[[Exception], bool]) -> Callable[[Callable[P, Awaitable[T]]], Callable[P, Awaitable[T]]]
```

Args:
    tries: Number of retry attempts
    delay_seconds: Initial delay between retries in seconds
    backoff_factor: Multiplier for delay on each retry
    is_retryable: Function to determine if an exception should trigger a retry
                 (defaults to checking for retryable HTTP errors from both urllib and httpx)

Returns:
    Decorated function with retry logic

## [**async_generator_retry()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L194)

```python
def async_generator_retry(tries: int, delay_seconds: float, backoff_factor: float, is_retryable: Callable[[Exception], bool]) -> Callable[[Callable[P, AsyncGenerator[T]]], Callable[P, AsyncGenerator[T]]]
```

Retry decorator for async generators.

Args:
    tries: Number of retry attempts
    delay_seconds: Initial delay between retries in seconds
    backoff_factor: Multiplier for delay on each retry
    is_retryable: Function to determine if an exception should trigger a retry
                 (defaults to checking for retryable HTTP errors from both urllib and httpx)

Returns:
    Decorated async generator function with retry logic

## [**run_sync()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L246)

```python
def run_sync(coro: Coroutine[Any, Any, T]) -> T
```

Run an async coroutine synchronously, handling nested event loops.

If called from within an async context (running event loop), runs the
coroutine in a thread pool executor. Otherwise, uses asyncio.run().

This mirrors the pattern used by ToolManager for MCP integration.

## [**is_windows()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L263)

```python
def is_windows() -> bool
```

## [**name_matches()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L275)

```python
def name_matches(name: str, patterns: list[str]) -> bool
```

Check if a name matches any of the provided patterns.

Supports two forms (case-insensitive):
- Glob wildcards using fnmatch (e.g., 'serena_*')
- Regex when prefixed with 're:' (e.g., 're:serena.*')

## [**compact_reduction_display()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L328)

```python
def compact_reduction_display(old_tokens: int | None, new_tokens: int | None) -> str
```

## [**utc_now()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/utils.py#L340)

```python
def utc_now() -> datetime
```

