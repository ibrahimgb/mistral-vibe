---
title: "vibe.core.proxy_setup"
tldr: "Module vibe.core.proxy_setup"
tags: [reference, api]
---

# [**vibe.core.proxy_setup**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/proxy_setup.py)

This module defines the constants `SUPPORTED_PROXY_VARS`.

## [**ProxySetupError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/proxy_setup.py#L17)

The [**ProxySetupError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/proxy_setup.py#L17) class (extending `Exception`).

## [**get_current_proxy_settings()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/proxy_setup.py#L21)

```python
def get_current_proxy_settings() -> dict[str, str | None]
```

## [**set_proxy_var()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/proxy_setup.py#L32)

```python
def set_proxy_var(key: str, value: str) -> None
```

## [**unset_proxy_var()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/proxy_setup.py#L43)

```python
def unset_proxy_var(key: str) -> None
```

## [**parse_proxy_command()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/proxy_setup.py#L56)

```python
def parse_proxy_command(args: str) -> tuple[str, str | None]
```

