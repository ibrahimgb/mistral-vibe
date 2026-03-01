---
title: "vibe.core.wiki.narrative"
tldr: "Developer-facing renderer — Gemini Code Wiki style narrative Markdown."
tags: [reference, api]
---

# [**vibe.core.wiki.narrative**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py)

Developer-facing renderer — Gemini Code Wiki style narrative Markdown.

Generates prose-based documentation with inline bold source links pointing
to the hosted repository (GitHub/GitLab).  Every class, function, or module
mention becomes a clickable ``[**Name**](url#Lnn)`` link.

Style targets:
- Narrative flowing paragraphs (not tables of metrics or "—" placeholders)
- Tables used sparingly, only for genuinely tabular data
- Cross-references between sections via anchor links
- Test modules excluded entirely
- Private helpers included only when architecturally significant

Each page retains YAML frontmatter with ``tldr`` and ``tags`` for MkDocs.

This module defines the constants `_NOISE_SUBSYSTEMS`.

## [**_src()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L45)

```python
def _src(remote_base: str | None, relative_path: str, lineno: int | None, display: str | None) -> str
```

Shorthand for ``source_link_md`` used throughout renderers.

## [**_embed_svg()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L55)

```python
def _embed_svg(diagram_name: str) -> str
```

Return markdown to embed an SVG diagram.

## [**_is_noise_subsystem()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L63)

```python
def _is_noise_subsystem(sub: SubsystemCluster) -> bool
```

Subsystems too trivial to warrant their own page.

## [**_is_test_module()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L70)

```python
def _is_test_module(mod: ModuleNode) -> bool
```

Return True for test files.

## [**_is_trivial_module()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L75)

```python
def _is_trivial_module(mod: ModuleNode) -> bool
```

Return True for modules not worth a reference page.

## [**_is_significant_private()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L86)

```python
def _is_significant_private(fn: FunctionNode) -> bool
```

True when a private method is architecturally significant enough to document.

## [**_describe_class()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L93)

```python
def _describe_class(cls: ClassNode, mod: ModuleNode, remote_base: str | None) -> str
```

Build a narrative prose paragraph for one class.

Mentions stereo-type, bases, purpose (from docstring first line), and
key public methods — all woven into flowing text with inline source links.

## [**_describe_function()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L156)

```python
def _describe_function(fn: FunctionNode, mod: ModuleNode, remote_base: str | None) -> str
```

Build a one-line prose description of a top-level function.

## [**render_index_page()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L170)

```python
def render_index_page(model: ProjectModel) -> tuple[str, str]
```

Generate the wiki index / landing page.

## [**render_subsystem_page()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L222)

```python
def render_subsystem_page(sub: SubsystemCluster, model: ProjectModel, knowledge: ArchitectureKnowledge) -> tuple[str, str]
```

Render a Gemini-style narrative subsystem guide page.

## [**render_patterns_page()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L307)

```python
def render_patterns_page(knowledge: ArchitectureKnowledge, remote_base: str | None) -> tuple[str, str]
```

Render the design patterns catalog as narrative prose.

## [**render_components_page()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L343)

```python
def render_components_page(model: ProjectModel) -> tuple[str, str]
```

Render the component overview as narrative prose.

## [**render_data_flow_page()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L377)

```python
def render_data_flow_page() -> tuple[str, str]
```

Render the data flow page with narrative descriptions.

## [**render_module_reference()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L415)

```python
def render_module_reference(mod: ModuleNode, remote_base: str | None) -> tuple[str, str]
```

Render narrative API reference for one module.

## [**render_reference_index()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L474)

```python
def render_reference_index(model: ProjectModel) -> tuple[str, str]
```

Render the API reference index page.

## [**generate_narrative_pages()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/narrative.py#L505)

```python
def generate_narrative_pages(model: ProjectModel, knowledge: ArchitectureKnowledge) -> dict[str, str]
```

Generate all MkDocs Markdown pages.

Returns
-------
dict[str, str]:
    Mapping ``relative_path → markdown_content``.  Paths are relative
    to the MkDocs ``docs/`` directory.

