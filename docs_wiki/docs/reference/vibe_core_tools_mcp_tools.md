---
title: "vibe.core.tools.mcp.tools"
tldr: "Module vibe.core.tools.mcp.tools"
tags: [reference, api]
---

# [**vibe.core.tools.mcp.tools**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py)

## [**_OpenArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L62)

The [**_OpenArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L62) Pydantic model (extending `BaseModel`). Key fields include `model_config`.

## [**MCPToolResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L66)

The [**MCPToolResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L66) Pydantic model (extending `BaseModel`). Key fields include `ok`, `server`, `tool`, `text`, `structured`.

## [**RemoteTool**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L74)

The [**RemoteTool**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L74) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `name`, `description`, `input_schema`.

## [**_MCPContentBlock**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L111)

The [**_MCPContentBlock**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L111) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `text`.

## [**_MCPResultIn**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L116)

The [**_MCPResultIn**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L116) Pydantic model (extending `BaseModel`). Key fields include `model_config`, `structuredContent`, `content`.

## [**list_tools_http()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L149)

```python
async def list_tools_http(url: str) -> list[RemoteTool]
```

## [**call_tool_http()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L163)

```python
async def call_tool_http(url: str, tool_name: str, arguments: dict[str, Any]) -> MCPToolResult
```

## [**create_mcp_http_proxy_tool_class()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L191)

```python
def create_mcp_http_proxy_tool_class() -> type[BaseTool[_OpenArgs, MCPToolResult, BaseToolConfig, BaseToolState]]
```

## [**list_tools_stdio()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L276)

```python
async def list_tools_stdio(command: list[str]) -> list[RemoteTool]
```

## [**call_tool_stdio()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L294)

```python
async def call_tool_stdio(command: list[str], tool_name: str, arguments: dict[str, Any]) -> MCPToolResult
```

## [**create_mcp_stdio_proxy_tool_class()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/mcp/tools.py#L326)

```python
def create_mcp_stdio_proxy_tool_class() -> type[BaseTool[_OpenArgs, MCPToolResult, BaseToolConfig, BaseToolState]]
```

