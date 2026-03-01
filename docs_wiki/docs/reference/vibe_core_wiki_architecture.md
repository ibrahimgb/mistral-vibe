---
title: "vibe.core.wiki.architecture"
tldr: "Extract design-pattern knowledge from a :class:`ProjectModel`."
tags: [reference, api]
---

# [**vibe.core.wiki.architecture**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py)

Extract design-pattern knowledge from a :class:`ProjectModel`.

Scans the analysis results for well-known structural patterns in the AST
metadata (base-class names, decorators, naming conventions) and emits a
catalog of :class:`PatternInstance` records.  The output feeds into the
narrative renderer and the LLM doc renderer.

This module defines the constants `_TRIVIAL_RETURNS`.

## [**PatternKind**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L21)

The [**PatternKind**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L21) enum (extending `StrEnum`) well-known software design patterns we detect. Key fields include `PROTOCOL_ADAPTER`, `TEMPLATE_METHOD`, `FACTORY`, `MIDDLEWARE_PIPELINE`, `OBSERVER_STREAMING`, `AUTODISCOVERY`, `CONFIG_AS_CODE`.

## [**PatternInstance**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L34)

The [**PatternInstance**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L34) dataclass one occurrence of a pattern in the codebase. Key fields include `kind`, `title`, `description`, `files`, `classes`, `rationale`.

## [**ArchitectureKnowledge**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L46)

The [**ArchitectureKnowledge**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L46) dataclass collected design-pattern knowledge for the project. Key fields include `patterns`.

## [**_is_test_module()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L56)

```python
def _is_test_module(mod: ModuleNode) -> bool
```

Return ``True`` if a module lives under ``tests/`` or is a test file.

## [**_detect_protocol_adapter()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L65)

```python
def _detect_protocol_adapter(model: ProjectModel) -> list[PatternInstance]
```

Find Protocol classes and their concrete implementations.

## [**_detect_template_method()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L116)

```python
def _detect_template_method(model: ProjectModel) -> list[PatternInstance]
```

Find ABCs with a mix of abstract and concrete methods.

## [**_is_factory_return()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L149)

```python
def _is_factory_return(annotation: str) -> bool
```

Return ``True`` if *annotation* looks like a class instantiation.

Rejects primitives, built-in containers, and optional/union wrappers
around primitives.  Accepts anything whose core name starts uppercase
(e.g. ``AgentLoop``, ``VibeConfig``, ``BaseTool[…]``).

## [**_detect_factory()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L166)

```python
def _detect_factory(model: ProjectModel) -> list[PatternInstance]
```

Find factory functions/methods that return non-trivial class instances.

## [**_detect_middleware()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L205)

```python
def _detect_middleware(model: ProjectModel) -> list[PatternInstance]
```

Find middleware-pattern classes (chain/pipeline).

## [**_detect_streaming()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L235)

```python
def _detect_streaming(model: ProjectModel) -> list[PatternInstance]
```

Find AsyncGenerator-based streaming patterns.

## [**_detect_autodiscovery()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L270)

```python
def _detect_autodiscovery(model: ProjectModel) -> list[PatternInstance]
```

Find plugin/tool auto-discovery by filesystem scanning.

## [**_detect_config_as_code()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L296)

```python
def _detect_config_as_code(model: ProjectModel) -> list[PatternInstance]
```

Find Pydantic Settings / config patterns.

## [**extract_architecture()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/architecture.py#L323)

```python
def extract_architecture(model: ProjectModel) -> ArchitectureKnowledge
```

Run all pattern detectors and return collected knowledge.

Parameters
----------
model:
    A fully-populated :class:`ProjectModel` from :func:`analyze_project`.

Returns
-------
ArchitectureKnowledge:
    Design patterns found and technology choices catalogued.

