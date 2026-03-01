---
title: "vibe.core.tools.builtins.wiki_diagram"
tldr: "PlantUML diagram generation tool — create and render diagrams as SVG."
tags: [reference, api]
---

# [**vibe.core.tools.builtins.wiki_diagram**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_diagram.py)

PlantUML diagram generation tool — create and render diagrams as SVG.

The agent can use this tool to create custom PlantUML diagrams for the
project wiki.  Diagrams are rendered to SVG and saved alongside their
``.puml`` source.

## [**WikiDiagramArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_diagram.py#L28)

The [**WikiDiagramArgs**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_diagram.py#L28) Pydantic model (extending `BaseModel`). Key fields include `source`, `name`, `title`, `fmt`, `output_dir`.

## [**WikiDiagramResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_diagram.py#L39)

The [**WikiDiagramResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_diagram.py#L39) Pydantic model (extending `BaseModel`). Key fields include `message`, `output_path`, `puml_path`.

## [**WikiDiagramConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_diagram.py#L45)

The [**WikiDiagramConfig**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_diagram.py#L45) Pydantic model (extending `BaseToolConfig`). Key fields include `permission`, `default_output_dir`, `plantuml_server`.

## [**WikiDiagramState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_diagram.py#L51)

The [**WikiDiagramState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_diagram.py#L51) Pydantic model (extending `BaseToolState`).

## [**WikiDiagram**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_diagram.py#L55)

The [**WikiDiagram**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/tools/builtins/wiki_diagram.py#L55) class (extending `BaseTool[WikiDiagramArgs, WikiDiagramResult, WikiDiagramConfig, WikiDiagramState]`, `ToolUIData[WikiDiagramArgs, WikiDiagramResult]`). It exposes `format_call_display()`, `get_result_display()`, `get_status_text()`, `run()`.

**Public API:**

- `def format_call_display()`
- `def get_result_display()`
- `def get_status_text()`
- `async def run()`

