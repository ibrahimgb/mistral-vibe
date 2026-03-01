---
title: "vibe.core.config"
tldr: "Module vibe.core.config"
tags: [reference, api]
---

# [**vibe.core.config**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py)

This module defines the constants `DEFAULT_MISTRAL_API_ENV_KEY`, `DEFAULT_PROVIDERS`, `DEFAULT_MODELS`.

## [**MissingAPIKeyError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L48)

The [**MissingAPIKeyError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L48) class (extending `RuntimeError`). It exposes `__init__()`.

**Public API:**

- `def __init__()`

## [**MissingPromptFileError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L57)

The [**MissingPromptFileError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L57) class (extending `RuntimeError`). It exposes `__init__()`.

**Public API:**

- `def __init__()`

## [**WrongBackendError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L74)

The [**WrongBackendError**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L74) class (extending `RuntimeError`). It exposes `__init__()`.

**Public API:**

- `def __init__()`

## [**TomlFileSettingsSource**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L84)

The [**TomlFileSettingsSource**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L84) class (extending `PydanticBaseSettingsSource`). It exposes `__init__()`, `get_field_value()`, `__call__()`.

**Public API:**

- `def __init__()`
- `def get_field_value()`
- `def __call__()`

## [**ProjectContextConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L110)

The [**ProjectContextConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L110) Pydantic model (extending `BaseSettings`). Key fields include `max_chars`, `default_commit_count`, `max_doc_bytes`, `truncation_buffer`, `max_depth`, `max_files`, `max_dirs_per_level`, `timeout_seconds`.

## [**SessionLoggingConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L121)

The [**SessionLoggingConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L121) Pydantic model (extending `BaseSettings`). Key fields include `save_dir`, `session_prefix`, `enabled`. It exposes `set_default_save_dir()`, `expand_save_dir()`.

**Public API:**

- `def set_default_save_dir()`
- `def expand_save_dir()`

## [**Backend**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L139)

The [**Backend**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L139) enum (extending `StrEnum`). Key fields include `MISTRAL`, `GENERIC`.

## [**ProviderConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L144)

The [**ProviderConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L144) Pydantic model (extending `BaseModel`). Key fields include `name`, `api_base`, `api_key_env_var`, `api_style`, `backend`, `reasoning_field_name`, `project_id`, `region`.

## [**_MCPBase**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L155)

The [**_MCPBase**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L155) Pydantic model (extending `BaseModel`). Key fields include `name`, `prompt`, `startup_timeout_sec`, `tool_timeout_sec`, `sampling_enabled`. It exposes `normalize_name()`.

**Public API:**

- `def normalize_name()`

## [**_MCPHttpFields**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L181)

The [**_MCPHttpFields**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L181) Pydantic model (extending `BaseModel`). Key fields include `url`, `headers`, `api_key_env`, `api_key_header`, `api_key_format`. It exposes `http_headers()`.

**Public API:**

- `def http_headers()`

## [**MCPHttp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L222)

The [**MCPHttp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L222) class (extending `_MCPBase`, `_MCPHttpFields`).

## [**MCPStreamableHttp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L226)

The [**MCPStreamableHttp**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L226) class (extending `_MCPBase`, `_MCPHttpFields`).

## [**MCPStdio**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L230)

The [**MCPStdio**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L230) class (extending `_MCPBase`). It exposes `argv()`.

**Public API:**

- `def argv()`

## [**ModelConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L253)

The [**ModelConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L253) Pydantic model (extending `BaseModel`). Key fields include `name`, `provider`, `alias`, `temperature`, `input_price`, `output_price`, `thinking`.

## [**VibeConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L313)

The [**VibeConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L313) Pydantic model (extending `BaseSettings`). Key fields include `active_model`, `vim_keybindings`, `disable_welcome_banner_animation`, `autocopy_to_clipboard`, `file_watcher_for_autocomplete`, `displayed_workdir`, `auto_compact_threshold`, `context_warnings`, …. It exposes `get_active_model()`, `get_provider_for_model()`, `settings_customise_sources()`, `save_updates()`, `dump_config()` among 7 public methods.

**Public API:**

- `def nuage_api_key()`
- `def system_prompt()`
- `def get_active_model()`
- `def get_provider_for_model()`
- `def settings_customise_sources()` — Define the priority of settings sources.
- `def save_updates()`
- `def dump_config()`
- `def load()`
- `def create_default()`

## [**load_dotenv_values()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/config.py#L33)

```python
def load_dotenv_values(env_path: Path, environ: MutableMapping[str, str]) -> None
```

