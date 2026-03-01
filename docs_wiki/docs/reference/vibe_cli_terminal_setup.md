---
title: "vibe.cli.terminal_setup"
tldr: "Module vibe.cli.terminal_setup"
tags: [reference, api]
---

# [**vibe.cli.terminal_setup**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/terminal_setup.py)

## [**Terminal**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/terminal_setup.py#L13)

The [**Terminal**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/terminal_setup.py#L13) enum (extending `Enum`). Key fields include `VSCODE`, `VSCODE_INSIDERS`, `CURSOR`, `JETBRAINS`, `ITERM2`, `WEZTERM`, `GHOSTTY`, `UNKNOWN`.

## [**SetupResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/terminal_setup.py#L25)

The [**SetupResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/terminal_setup.py#L25) dataclass. Key fields include `success`, `terminal`, `message`, `requires_restart`.

## [**detect_terminal()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/terminal_setup.py#L64)

```python
def detect_terminal() -> Terminal
```

## [**_setup_vscode_like_terminal()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/terminal_setup.py#L137)

```python
def _setup_vscode_like_terminal(terminal: Terminal) -> SetupResult
```

Setup keybindings for VS Code or Cursor.

## [**_setup_iterm2()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/terminal_setup.py#L209)

```python
def _setup_iterm2() -> SetupResult
```

## [**setup_terminal()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/cli/terminal_setup.py#L306)

```python
def setup_terminal() -> SetupResult
```

