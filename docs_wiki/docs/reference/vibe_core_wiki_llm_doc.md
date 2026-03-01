---
title: "vibe.core.wiki.llm_doc"
tldr: "LLM-optimised renderer — flat Markdown for ``llms.txt`` and ``llms-full.txt``."
tags: [reference, api]
---

# [**vibe.core.wiki.llm_doc**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/llm_doc.py)

LLM-optimised renderer — flat Markdown for ``llms.txt`` and ``llms-full.txt``.

Follows the `llmstxt.org <https://llmstxt.org>`_ convention:

* **``llms.txt``** — short index with project summary, key entry points, and
  section links.  Fits in ~2 K tokens.
* **``llms-full.txt``** — complete reference with every production module,
  class, and function.  Dense, flat, no images, no HTML.  Designed for
  pasting into a prompt window.

Both files are generated from the same :class:`ProjectModel` produced by
:func:`vibe.core.wiki.analyzer.analyze_project`.

Test modules and empty ``__init__.py`` files are excluded.  When a remote
base URL is available, file references become full GitHub/GitLab URLs.

## [**_oneliner()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/llm_doc.py#L29)

```python
def _oneliner(docstring: str) -> str
```

Extract the first non-empty line from a docstring.

## [**_file_ref()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/llm_doc.py#L45)

```python
def _file_ref(remote_base: str | None, relative_path: str, lineno: int | None) -> str
```

Return a source reference — full URL when available, else local path.

## [**_is_significant_private()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/llm_doc.py#L65)

```python
def _is_significant_private(fn: FunctionNode) -> bool
```

True when a private helper is worth including in the LLM doc.

## [**generate_llms_txt()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/llm_doc.py#L76)

```python
def generate_llms_txt(model: ProjectModel, knowledge: ArchitectureKnowledge) -> str
```

Generate the short ``llms.txt`` index.

## [**_render_class_block()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/llm_doc.py#L131)

```python
def _render_class_block(cls: ClassNode, mod: ModuleNode, remote_base: str | None) -> list[str]
```

Render one class for llms-full.txt.

## [**_render_function_block()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/llm_doc.py#L175)

```python
def _render_function_block(fn: FunctionNode, mod: ModuleNode, remote_base: str | None) -> list[str]
```

Render one top-level function for llms-full.txt.

## [**generate_llms_full_txt()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/llm_doc.py#L191)

```python
def generate_llms_full_txt(model: ProjectModel, knowledge: ArchitectureKnowledge) -> str
```

Generate the complete ``llms-full.txt`` reference.

Test modules and empty ``__init__.py`` files are excluded.

