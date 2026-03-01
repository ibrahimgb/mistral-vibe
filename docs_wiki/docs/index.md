---
title: "mistral-vibe Code Wiki"
tldr: "mistral-vibe v2.3.0 — 323 modules, 671 classes across 10 subsystems."
tags: [overview, index]
---

# mistral-vibe Code Wiki

mistral-vibe v2.3.0 is a Python >=3.12 project comprising 57,075 lines of code organised into 323 modules and 671 classes. The codebase is structured around 10 subsystems described below.

## Architecture Overview

![c4_context](../diagrams/c4_context.svg)

## Subsystem Map

![mindmap_overview](../diagrams/mindmap_overview.svg)

## Subsystems

| Subsystem | Description |
|-----------|-------------|
| [acp](subsystems/acp.md) | Agent Client Protocol — session management, ACP tools, and server integration. (13 modules, 19 classes) |
| [cli](subsystems/cli.md) | Command-line interface, TUI, autocompletion, and user-facing commands. (66 modules, 106 classes) |
| [core](subsystems/core.md) | Core agent loop, configuration, LLM backends, middleware, and orchestration. (58 modules, 158 classes) |
| [setup](subsystems/setup.md) | Onboarding, first-run setup, and trusted-folder management. (6 modules, 7 classes) |
| [tests](subsystems/tests.md) | The tests subsystem. (143 modules, 281 classes) |
| [tools](subsystems/tools.md) | Built-in tool implementations, MCP integrations, and tool management. (21 modules, 86 classes) |
| [voice](subsystems/voice.md) | Voice recording and transcription. (3 modules, 1 classes) |
| [wiki](subsystems/wiki.md) | Code wiki documentation generator (this system). (10 modules, 13 classes) |

## Quick Navigation

- [Architecture & Patterns](architecture/patterns.md)
- [Component Overview](architecture/components.md)
- [Data Flow](architecture/data_flow.md)
- [API Reference](reference/index.md)
