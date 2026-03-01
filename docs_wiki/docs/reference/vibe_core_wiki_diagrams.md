---
title: "vibe.core.wiki.diagrams"
tldr: "Auto-generate PlantUML diagrams from a :class:`ProjectModel`."
tags: [reference, api]
---

# [**vibe.core.wiki.diagrams**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/diagrams.py)

Auto-generate PlantUML diagrams from a :class:`ProjectModel`.

Each public function returns PlantUML source text (``str``).  The caller
is responsible for rendering to SVG via :mod:`vibe.core.wiki.plantuml`.

## [**_sanitize()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/diagrams.py#L17)

```python
def _sanitize(name: str) -> str
```

Make a name safe for PlantUML identifiers.

## [**generate_mindmap()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/diagrams.py#L26)

```python
def generate_mindmap(model: ProjectModel) -> str
```

Project mind-map showing subsystems and their key classes.

## [**generate_component_diagram()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/diagrams.py#L45)

```python
def generate_component_diagram(model: ProjectModel) -> str
```

C4-style component diagram showing subsystem boundaries and links.

## [**generate_class_diagram()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/diagrams.py#L111)

```python
def generate_class_diagram(subsystem: SubsystemCluster, model: ProjectModel) -> str
```

Class diagram for one subsystem — inheritance + key attributes.

## [**generate_agent_flow_sequence()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/diagrams.py#L170)

```python
def generate_agent_flow_sequence(model: ProjectModel) -> str
```

Sequence diagram for the core agent loop → LLM → tool call flow.

## [**generate_c4_context()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/diagrams.py#L215)

```python
def generate_c4_context(model: ProjectModel) -> str
```

Top-level C4 context diagram showing external actors.

## [**generate_data_flow()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/diagrams.py#L252)

```python
def generate_data_flow(model: ProjectModel) -> str
```

Data flow diagram showing how messages traverse the system.

## [**generate_pattern_diagram()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/diagrams.py#L298)

```python
def generate_pattern_diagram(knowledge: ArchitectureKnowledge) -> str
```

Mind map of detected design patterns and where they appear.

## [**generate_all_diagrams()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/diagrams.py#L321)

```python
def generate_all_diagrams(model: ProjectModel, knowledge: ArchitectureKnowledge) -> dict[str, str]
```

Generate all PlantUML diagram sources.

Returns
-------
dict[str, str]:
    Mapping of ``diagram_name → plantuml_source``.  Keys are used
    as filenames (without extension) in the output directory.

