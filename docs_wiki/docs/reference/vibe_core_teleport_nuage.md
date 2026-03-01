---
title: "vibe.core.teleport.nuage"
tldr: "Module vibe.core.teleport.nuage"
tags: [reference, api]
---

# [**vibe.core.teleport.nuage**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py)

## [**GitRepoConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L14)

The [**GitRepoConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L14) Pydantic model (extending `BaseModel`). Key fields include `url`, `branch`, `commit`.

## [**VibeSandboxConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L20)

The [**VibeSandboxConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L20) Pydantic model (extending `BaseModel`). Key fields include `git_repo`.

## [**VibeNewSandbox**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L24)

The [**VibeNewSandbox**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L24) Pydantic model (extending `BaseModel`). Key fields include `type`, `config`, `teleported_diffs`.

## [**TeleportSession**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L30)

The [**TeleportSession**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L30) Pydantic model (extending `BaseModel`). Key fields include `metadata`, `messages`.

## [**WorkflowParams**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L35)

The [**WorkflowParams**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L35) Pydantic model (extending `BaseModel`). Key fields include `prompt`, `sandbox`, `session`.

## [**WorkflowExecuteResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L41)

The [**WorkflowExecuteResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L41) Pydantic model (extending `BaseModel`). Key fields include `execution_id`.

## [**PublicKeyResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L45)

The [**PublicKeyResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L45) Pydantic model (extending `BaseModel`). Key fields include `public_key`.

## [**QueryResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L49)

The [**QueryResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L49) Pydantic model (extending `BaseModel`). Key fields include `result`.

## [**CreateLeChatThreadInput**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L53)

The [**CreateLeChatThreadInput**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L53) Pydantic model (extending `BaseModel`). Key fields include `encrypted_api_key`, `user_message`, `project_name`.

## [**CreateLeChatThreadOutput**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L59)

The [**CreateLeChatThreadOutput**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L59) Pydantic model (extending `BaseModel`). Key fields include `chat_url`.

## [**UpdateResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L63)

The [**UpdateResponse**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L63) Pydantic model (extending `BaseModel`). Key fields include `result`.

## [**NuageClient**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L67)

The [**NuageClient**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/teleport/nuage.py#L67) class. It exposes `__init__()`, `__aenter__()`, `__aexit__()`, `start_workflow()`, `send_github_token()` among 6 public methods.

**Public API:**

- `def __init__()`
- `async def __aenter__()`
- `async def __aexit__()`
- `async def start_workflow()`
- `async def send_github_token()`
- `async def create_le_chat_thread()`

