---
title: "vibe.acp.acp_agent_loop"
tldr: "Module vibe.acp.acp_agent_loop"
tags: [reference, api]
---

# [**vibe.acp.acp_agent_loop**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/acp_agent_loop.py)

## [**AcpSessionLoop**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/acp_agent_loop.py#L113)

The [**AcpSessionLoop**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/acp_agent_loop.py#L113) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `id`, `agent_loop`, `task`.

## [**VibeAcpAgentLoop**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/acp_agent_loop.py#L120)

The [**VibeAcpAgentLoop**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/acp_agent_loop.py#L120) class (extending `AcpAgent`). It exposes `__init__()`, `initialize()`, `authenticate()`, `new_session()`, `load_session()` among 16 public methods. Internally it relies on `_create_approval_callback()`, `_replay_conversation_history()`, `_handle_proxy_setup_command()`.

**Public API:**

- `def __init__()`
- `async def initialize()`
- `async def authenticate()`
- `async def new_session()`
- `async def load_session()`
- `async def set_session_mode()`
- `async def set_session_model()`
- `async def set_config_option()`
- `async def list_sessions()`
- `async def prompt()`
- `async def cancel()`
- `async def fork_session()`
- `async def resume_session()`
- `async def ext_method()`
- `async def ext_notification()`
- `def on_connect()`

**Internal helpers:**

- `_create_approval_callback()`
- `_replay_conversation_history()`
- `_handle_proxy_setup_command()`
- `_build_text_prompt()`
- `_run_agent_loop()`

## [**run_acp_server()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/acp/acp_agent_loop.py#L801)

```python
def run_acp_server() -> None
```

