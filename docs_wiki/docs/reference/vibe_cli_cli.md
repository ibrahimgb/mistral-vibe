---
title: "vibe.cli.cli"
tldr: "Module vibe.cli.cli"
tags: [reference, api]
---

# [**vibe.cli.cli**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/cli.py)

## [**get_initial_agent_name()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/cli.py#L28)

```python
def get_initial_agent_name(args: argparse.Namespace) -> str
```

## [**get_prompt_from_stdin()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/cli.py#L34)

```python
def get_prompt_from_stdin() -> str | None
```

## [**load_config_or_exit()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/cli.py#L49)

```python
def load_config_or_exit() -> VibeConfig
```

## [**bootstrap_config_files()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/cli.py#L63)

```python
def bootstrap_config_files() -> None
```

## [**load_session()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/cli.py#L78)

```python
def load_session(args: argparse.Namespace, config: VibeConfig) -> tuple[list[LLMMessage], Path] | None
```

## [**run_cli()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/cli.py#L135)

```python
def run_cli(args: argparse.Namespace) -> None
```

