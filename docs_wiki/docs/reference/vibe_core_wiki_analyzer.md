---
title: "vibe.core.wiki.analyzer"
tldr: "Deep static analysis of a Python project — foundation for wiki generation."
tags: [reference, api]
---

# [**vibe.core.wiki.analyzer**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py)

Deep static analysis of a Python project — foundation for wiki generation.

Walks every ``*.py`` file under a project root, parses the AST, and builds a
rich :class:`ProjectModel` graph of modules, classes, functions, imports,
class hierarchies, and subsystem clusters.

The ``ProjectModel`` is consumed downstream by:

* ``narrative.py``  — renders MkDocs pages for developers
* ``llm_doc.py``    — renders ``llms.txt`` / ``llms-full.txt`` for LLMs
* ``diagrams.py``   — auto-generates PlantUML from the graph
* ``architecture.py`` — extracts design-pattern knowledge

This module defines the constants `_PYDANTIC_BASES`, `_ENUM_BASES`, `_ABSTRACT_INDICATORS`, `_SUBSYSTEM_DESCRIPTIONS`.

## [**FunctionNode**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L29)

The [**FunctionNode**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L29) dataclass one function or method. Key fields include `name`, `qualified_name`, `lineno`, `end_lineno`, `docstring`, `parameters`, `return_annotation`, `decorators`, ….

**Public API:**

- `def signature()`

## [**ClassNode**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L57)

The [**ClassNode**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L57) dataclass one class definition. Key fields include `name`, `qualified_name`, `lineno`, `end_lineno`, `docstring`, `bases`, `decorators`, `methods`, ….

**Public API:**

- `def public_methods()`
- `def private_methods()`

## [**ImportNode**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L85)

The [**ImportNode**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L85) dataclass one import statement. Key fields include `module`, `names`, `is_relative`, `level`.

## [**ModuleNode**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L95)

The [**ModuleNode**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L95) dataclass one python file. Key fields include `path`, `relative_path`, `dotted_name`, `lineno_count`, `docstring`, `imports`, `classes`, `functions`, ….

**Public API:**

- `def is_init()`

## [**SubsystemCluster**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L115)

The [**SubsystemCluster**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L115) dataclass a logical subsystem grouping (e.g. ``cli``, ``core``, ``acp``). Key fields include `name`, `description`, `modules`.

**Public API:**

- `def total_lines()`
- `def total_classes()`
- `def total_functions()`

## [**DependencyInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L136)

The [**DependencyInfo**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L136) dataclass project-level dependency metadata from pyproject.toml. Key fields include `name`, `version_spec`, `category`.

## [**ProjectModel**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L145)

The [**ProjectModel**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L145) dataclass top-level analysis result for the entire project. Key fields include `project_name`, `version`, `python_requires`, `root`, `modules`, `subsystems`, `dependencies`, `import_graph`, …. It exposes `module_by_dotted()`.

**Public API:**

- `def total_lines()`
- `def all_classes()`
- `def all_functions()`
- `def module_by_dotted()`

## [**_extract_function()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L218)

```python
def _extract_function(node: ast.FunctionDef | ast.AsyncFunctionDef, module_dotted: str) -> FunctionNode
```

## [**_extract_class()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L251)

```python
def _extract_class(node: ast.ClassDef, module_dotted: str) -> ClassNode
```

## [**_extract_constants()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L305)

```python
def _extract_constants(tree: ast.Module) -> list[str]
```

Top-level UPPER_CASE assignments.

## [**parse_module()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L334)

```python
def parse_module(path: Path, project_root: Path) -> ModuleNode | None
```

Parse a single Python file into a :class:`ModuleNode`.

Returns ``None`` when the file cannot be parsed.

## [**_classify_subsystem()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L394)

```python
def _classify_subsystem(relative_path: str) -> str
```

Map a module relative path to a subsystem name.

## [**_build_import_graph()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L411)

```python
def _build_import_graph(modules: list[ModuleNode]) -> dict[str, list[str]]
```

Build a directed adjacency list: module → [modules it imports].

## [**_build_class_hierarchy()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L439)

```python
def _build_class_hierarchy(modules: list[ModuleNode]) -> dict[str, list[str]]
```

Build base → [child, …] hierarchy mapping using qualified names.

## [**_parse_pyproject()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L458)

```python
def _parse_pyproject(project_root: Path) -> tuple[str, str, str, list[DependencyInfo]]
```

Extract project metadata and dependencies from pyproject.toml.

## [**analyze_project()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L509)

```python
def analyze_project(project_root: str | Path) -> ProjectModel
```

Analyse a full Python project and return a :class:`ProjectModel`.

Parameters
----------
project_root:
    Path to the repository root (the directory containing ``pyproject.toml``
    and the ``vibe/`` package).

Returns
-------
ProjectModel:
    Complete analysis result ready for downstream renderers.

## [**generate_symbol_index()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L583)

```python
def generate_symbol_index(model: ProjectModel) -> dict[str, str]
```

Return ``{qualified_name: "relative/path.py#L<line>", …}``.

## [**generate_dependency_graph()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L596)

```python
def generate_dependency_graph(model: ProjectModel) -> dict[str, list[str]]
```

Return the module-level import adjacency list.

## [**write_json_artefacts()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/analyzer.py#L601)

```python
def write_json_artefacts(model: ProjectModel, output_dir: Path) -> None
```

Write ``symbol_index.json`` and ``dependency_graph.json`` to *output_dir*.

