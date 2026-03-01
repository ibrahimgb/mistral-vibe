---
title: "tests.test_agent_backend"
tldr: "Module tests.test_agent_backend"
tags: [reference, api]
---

# `tests.test_agent_backend`

**Source:** [`tests/test_agent_backend.py`](tests/test_agent_backend.py) · 187 lines

## `_two_model_vibe_config()`

```python
def _two_model_vibe_config(active_model: str) -> VibeConfig
```

VibeConfig with two models so we can switch active_model.

**Source:** [`tests/test_agent_backend.py#L20`](tests/test_agent_backend.py#L20)

## `_make_sampling_params()`

```python
def _make_sampling_params() -> CreateMessageRequestParams
```

**Source:** [`tests/test_agent_backend.py#L43`](tests/test_agent_backend.py#L43)

## `test_passes_x_affinity_header_when_asking_an_answer()`

```python
async def test_passes_x_affinity_header_when_asking_an_answer(vibe_config: VibeConfig)
```

**Source:** [`tests/test_agent_backend.py#L55`](tests/test_agent_backend.py#L55)

## `test_passes_x_affinity_header_when_asking_an_answer_streaming()`

```python
async def test_passes_x_affinity_header_when_asking_an_answer_streaming(vibe_config: VibeConfig)
```

**Source:** [`tests/test_agent_backend.py#L69`](tests/test_agent_backend.py#L69)

## `test_updates_tokens_stats_based_on_backend_response()`

```python
async def test_updates_tokens_stats_based_on_backend_response(vibe_config: VibeConfig)
```

**Source:** [`tests/test_agent_backend.py#L87`](tests/test_agent_backend.py#L87)

## `test_updates_tokens_stats_based_on_backend_response_streaming()`

```python
async def test_updates_tokens_stats_based_on_backend_response_streaming(vibe_config: VibeConfig)
```

**Source:** [`tests/test_agent_backend.py#L98`](tests/test_agent_backend.py#L98)

## `test_passes_entrypoint_metadata_to_backend()`

```python
async def test_passes_entrypoint_metadata_to_backend(vibe_config: VibeConfig)
```

**Source:** [`tests/test_agent_backend.py#L115`](tests/test_agent_backend.py#L115)

## `test_mcp_sampling_handler_uses_updated_backend_when_agent_backend_changes()`

```python
async def test_mcp_sampling_handler_uses_updated_backend_when_agent_backend_changes()
```

AgentLoop's MCP sampling handler uses current backend when backend is reassigned.

**Source:** [`tests/test_agent_backend.py#L142`](tests/test_agent_backend.py#L142)

## `test_mcp_sampling_handler_uses_updated_config_when_agent_config_changes()`

```python
async def test_mcp_sampling_handler_uses_updated_config_when_agent_config_changes()
```

**Source:** [`tests/test_agent_backend.py#L169`](tests/test_agent_backend.py#L169)

