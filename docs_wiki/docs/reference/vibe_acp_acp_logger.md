---
title: "vibe.acp.acp_logger"
tldr: "Module vibe.acp.acp_logger"
tags: [reference, api]
---

# [**vibe.acp.acp_logger**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/acp_logger.py)

This module defines the constants `ACP_LOG_DIR`, `ACP_LOG_FILE`, `MAX_LOG_SIZE_BYTES`, `BACKUP_COUNT`, `ACP_LOGGING_ENABLED_KEY`.

## [**JsonLineFormatter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/acp_logger.py#L33)

The [**JsonLineFormatter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/acp_logger.py#L33) class (extending `logging.Formatter`). It exposes `format()`.

**Public API:**

- `def format()`

## [**is_acp_logging_enabled()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/acp_logger.py#L29)

```python
def is_acp_logging_enabled() -> bool
```

## [**_get_logger()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/acp_logger.py#L38)

```python
def _get_logger() -> logging.Logger
```

## [**acp_message_observer()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/acp_logger.py#L68)

```python
def acp_message_observer(event: StreamEvent) -> None
```

