---
title: "vibe.core.wiki.plantuml"
tldr: "PlantUML rendering utilities — local binary or public server fallback."
tags: [reference, api]
---

# [**vibe.core.wiki.plantuml**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/plantuml.py)

PlantUML rendering utilities — local binary or public server fallback.

Provides :func:`render_plantuml` which takes PlantUML source text and
returns SVG (or PNG) bytes.  Prefers a locally-installed ``plantuml``
binary; falls back to the public PlantUML server.

This module defines the constants `_B64_CHARS`, `_DEFAULT_SERVER`.

## [**plantuml_text_encode()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/plantuml.py#L35)

```python
def plantuml_text_encode(text: str) -> str
```

Encode PlantUML source into the URL-safe format used by the server.

## [**has_local_plantuml()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/plantuml.py#L56)

```python
def has_local_plantuml() -> bool
```

Return ``True`` if a ``plantuml`` binary is on ``$PATH``.

## [**render_plantuml_local()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/plantuml.py#L61)

```python
async def render_plantuml_local(source: str, output_path: Path, fmt: str) -> Path
```

Render via the local ``plantuml`` CLI.

Raises
------
FileNotFoundError
    If ``plantuml`` is not installed.
RuntimeError
    If the plantuml process exits non-zero.

## [**render_plantuml_server()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/plantuml.py#L94)

```python
async def render_plantuml_server(source: str, output_path: Path, fmt: str, server: str) -> Path
```

Render via the public PlantUML server (HTTP GET).

Raises
------
RuntimeError
    If the server returns a non-200 status.

## [**render_plantuml()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/plantuml.py#L122)

```python
async def render_plantuml(source: str, output_path: Path, fmt: str, server: str) -> Path
```

Render PlantUML source to a file, preferring local binary.

Parameters
----------
source:
    PlantUML diagram source text (including ``@startuml``/``@enduml``).
output_path:
    Desired output path (extension will be replaced with *fmt*).
fmt:
    Output format — ``"svg"`` (default) or ``"png"``.
server:
    PlantUML server URL used as fallback.

Returns
-------
Path:
    The path to the rendered file.

