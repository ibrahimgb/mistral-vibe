---
title: "vibe.core.llm.backend.vertex"
tldr: "Module vibe.core.llm.backend.vertex"
tags: [reference, api]
---

# [**vibe.core.llm.backend.vertex**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/vertex.py)

## [**VertexCredentials**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/vertex.py#L34)

The [**VertexCredentials**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/vertex.py#L34) class. It exposes `__init__()`.

**Public API:**

- `def __init__()`
- `def access_token()`

## [**VertexAnthropicAdapter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/vertex.py#L57)

The [**VertexAnthropicAdapter**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/vertex.py#L57) class (extending `AnthropicAdapter`) vertex ai adapter — inherits all streaming/parsing from anthropicadapter. It exposes `__init__()`, `prepare_request()`.

**Public API:**

- `def __init__()`
- `def prepare_request()`

## [**build_vertex_base_url()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/vertex.py#L18)

```python
def build_vertex_base_url(region: str) -> str
```

## [**build_vertex_endpoint()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/llm/backend/vertex.py#L24)

```python
def build_vertex_endpoint(region: str, project_id: str, model: str, streaming: bool) -> str
```

