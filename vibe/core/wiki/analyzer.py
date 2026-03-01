"""Deep static analysis of a Python project — foundation for wiki generation.

Walks every ``*.py`` file under a project root, parses the AST, and builds a
rich :class:`ProjectModel` graph of modules, classes, functions, imports,
class hierarchies, and subsystem clusters.

The ``ProjectModel`` is consumed downstream by:

* ``narrative.py``  — renders MkDocs pages for developers
* ``llm_doc.py``    — renders ``llms.txt`` / ``llms-full.txt`` for LLMs
* ``diagrams.py``   — auto-generates PlantUML from the graph
* ``architecture.py`` — extracts design-pattern knowledge
"""

from __future__ import annotations

import ast
import json
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class FunctionNode:
    """One function or method."""

    name: str
    qualified_name: str
    lineno: int
    end_lineno: int
    docstring: str
    parameters: list[str]
    return_annotation: str
    decorators: list[str]
    is_async: bool
    is_method: bool = False
    is_property: bool = False
    is_classmethod: bool = False
    is_staticmethod: bool = False
    is_abstractmethod: bool = False
    is_private: bool = False

    @property
    def signature(self) -> str:
        prefix = "async " if self.is_async else ""
        params = ", ".join(self.parameters)
        ret = f" -> {self.return_annotation}" if self.return_annotation else ""
        return f"{prefix}def {self.name}({params}){ret}"


@dataclass
class ClassNode:
    """One class definition."""

    name: str
    qualified_name: str
    lineno: int
    end_lineno: int
    docstring: str
    bases: list[str]
    decorators: list[str]
    methods: list[FunctionNode] = field(default_factory=list)
    class_variables: list[str] = field(default_factory=list)
    is_dataclass: bool = False
    is_pydantic: bool = False
    is_enum: bool = False
    is_abstract: bool = False
    is_protocol: bool = False

    @property
    def public_methods(self) -> list[FunctionNode]:
        return [m for m in self.methods if not m.is_private]

    @property
    def private_methods(self) -> list[FunctionNode]:
        return [m for m in self.methods if m.is_private]


@dataclass
class ImportNode:
    """One import statement."""

    module: str
    names: list[str]
    is_relative: bool = False
    level: int = 0


@dataclass
class ModuleNode:
    """One Python file."""

    path: Path
    relative_path: str
    dotted_name: str
    lineno_count: int
    docstring: str
    imports: list[ImportNode] = field(default_factory=list)
    classes: list[ClassNode] = field(default_factory=list)
    functions: list[FunctionNode] = field(default_factory=list)
    constants: list[str] = field(default_factory=list)
    all_exports: list[str] | None = None

    @property
    def is_init(self) -> bool:
        return self.path.name == "__init__.py"


@dataclass
class SubsystemCluster:
    """A logical subsystem grouping (e.g. ``cli``, ``core``, ``acp``)."""

    name: str
    description: str
    modules: list[ModuleNode] = field(default_factory=list)

    @property
    def total_lines(self) -> int:
        return sum(m.lineno_count for m in self.modules)

    @property
    def total_classes(self) -> int:
        return sum(len(m.classes) for m in self.modules)

    @property
    def total_functions(self) -> int:
        return sum(len(m.functions) for m in self.modules)


@dataclass
class DependencyInfo:
    """Project-level dependency metadata from pyproject.toml."""

    name: str
    version_spec: str
    category: str = ""  # e.g. "llm", "tui", "networking", "testing"


@dataclass
class ProjectModel:
    """Top-level analysis result for the entire project."""

    project_name: str
    version: str
    python_requires: str
    root: Path
    modules: list[ModuleNode] = field(default_factory=list)
    subsystems: list[SubsystemCluster] = field(default_factory=list)
    dependencies: list[DependencyInfo] = field(default_factory=list)
    import_graph: dict[str, list[str]] = field(default_factory=dict)
    class_hierarchy: dict[str, list[str]] = field(default_factory=dict)
    remote_base_url: str | None = None
    commit_sha: str | None = None

    # Convenience ----------------------------------------------------------

    @property
    def total_lines(self) -> int:
        return sum(m.lineno_count for m in self.modules)

    @property
    def all_classes(self) -> list[ClassNode]:
        return [c for m in self.modules for c in m.classes]

    @property
    def all_functions(self) -> list[FunctionNode]:
        return [f for m in self.modules for f in m.functions]

    def module_by_dotted(self, dotted: str) -> ModuleNode | None:
        return next((m for m in self.modules if m.dotted_name == dotted), None)


# ---------------------------------------------------------------------------
# AST helpers
# ---------------------------------------------------------------------------

_PYDANTIC_BASES = frozenset({
    "BaseModel", "BaseSettings", "BaseToolConfig", "BaseToolState",
})

_ENUM_BASES = frozenset({
    "Enum", "StrEnum", "IntEnum", "Flag", "IntFlag",
})

_ABSTRACT_INDICATORS = frozenset({
    "ABC", "ABCMeta", "Protocol",
})


def _decorator_names(node: ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef) -> list[str]:
    names: list[str] = []
    for dec in node.decorator_list:
        match dec:
            case ast.Name(id=n):
                names.append(n)
            case ast.Attribute(attr=a):
                names.append(a)
            case ast.Call(func=ast.Name(id=n)):
                names.append(n)
            case ast.Call(func=ast.Attribute(attr=a)):
                names.append(a)
            case _:
                names.append(ast.dump(dec))
    return names


def _get_annotation(node: ast.expr | None) -> str:
    if node is None:
        return ""
    return ast.unparse(node)


def _extract_function(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
    module_dotted: str,
    *,
    owner_class: str = "",
) -> FunctionNode:
    decorators = _decorator_names(node)
    params: list[str] = []
    for arg in node.args.args:
        ann = _get_annotation(arg.annotation)
        entry = f"{arg.arg}: {ann}" if ann else arg.arg
        params.append(entry)

    qualified = f"{module_dotted}.{owner_class}.{node.name}" if owner_class else f"{module_dotted}.{node.name}"
    return FunctionNode(
        name=node.name,
        qualified_name=qualified,
        lineno=node.lineno,
        end_lineno=node.end_lineno or node.lineno,
        docstring=ast.get_docstring(node) or "",
        parameters=params,
        return_annotation=_get_annotation(node.returns),
        decorators=decorators,
        is_async=isinstance(node, ast.AsyncFunctionDef),
        is_method=bool(owner_class),
        is_property="property" in decorators,
        is_classmethod="classmethod" in decorators,
        is_staticmethod="staticmethod" in decorators,
        is_abstractmethod="abstractmethod" in decorators,
        is_private=node.name.startswith("_") and not node.name.startswith("__"),
    )


def _extract_class(node: ast.ClassDef, module_dotted: str) -> ClassNode:
    bases = [ast.unparse(b) for b in node.bases]
    decorators = _decorator_names(node)

    methods: list[FunctionNode] = []
    class_vars: list[str] = []
    for child in ast.iter_child_nodes(node):
        match child:
            case ast.FunctionDef() | ast.AsyncFunctionDef():
                methods.append(_extract_function(child, module_dotted, owner_class=node.name))
            case ast.AnnAssign(target=ast.Name(id=name)):
                class_vars.append(name)
            case ast.Assign(targets=[ast.Name(id=name)]):
                class_vars.append(name)

    base_names = {b.split("[")[0].split(".")[-1] for b in bases}
    return ClassNode(
        name=node.name,
        qualified_name=f"{module_dotted}.{node.name}",
        lineno=node.lineno,
        end_lineno=node.end_lineno or node.lineno,
        docstring=ast.get_docstring(node) or "",
        bases=bases,
        decorators=decorators,
        methods=methods,
        class_variables=class_vars,
        is_dataclass="dataclass" in decorators,
        is_pydantic=bool(base_names & _PYDANTIC_BASES),
        is_enum=bool(base_names & _ENUM_BASES),
        is_abstract=bool(base_names & _ABSTRACT_INDICATORS),
        is_protocol="Protocol" in base_names,
    )


def _extract_imports(tree: ast.Module) -> list[ImportNode]:
    imports: list[ImportNode] = []
    for node in ast.walk(tree):
        match node:
            case ast.Import(names=aliases):
                for alias in aliases:
                    imports.append(ImportNode(
                        module=alias.name,
                        names=[alias.asname or alias.name],
                    ))
            case ast.ImportFrom(module=mod, names=aliases, level=lvl):
                imports.append(ImportNode(
                    module=mod or "",
                    names=[a.name for a in aliases],
                    is_relative=bool(lvl),
                    level=lvl or 0,
                ))
    return imports


def _extract_constants(tree: ast.Module) -> list[str]:
    """Top-level UPPER_CASE assignments."""
    consts: list[str] = []
    for node in ast.iter_child_nodes(tree):
        match node:
            case ast.Assign(targets=[ast.Name(id=name)]) if name.isupper():
                consts.append(name)
            case ast.AnnAssign(target=ast.Name(id=name)) if name.isupper():
                consts.append(name)
    return consts


def _extract_all_exports(tree: ast.Module) -> list[str] | None:
    for node in ast.iter_child_nodes(tree):
        match node:
            case ast.Assign(targets=[ast.Name(id="__all__")], value=val):
                match val:
                    case ast.List(elts=elts) | ast.Tuple(elts=elts):
                        return [
                            e.value for e in elts
                            if isinstance(e, ast.Constant) and isinstance(e.value, str)
                        ]
    return None


# ---------------------------------------------------------------------------
# Module parsing
# ---------------------------------------------------------------------------

def parse_module(path: Path, project_root: Path) -> ModuleNode | None:
    """Parse a single Python file into a :class:`ModuleNode`.

    Returns ``None`` when the file cannot be parsed.
    """
    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError:
        return None

    relative = path.relative_to(project_root)
    parts = list(relative.with_suffix("").parts)
    if parts and parts[-1] == "__init__":
        parts.pop()
    dotted = ".".join(parts)

    classes: list[ClassNode] = []
    functions: list[FunctionNode] = []

    for node in ast.iter_child_nodes(tree):
        match node:
            case ast.ClassDef():
                classes.append(_extract_class(node, dotted))
            case ast.FunctionDef() | ast.AsyncFunctionDef():
                functions.append(_extract_function(node, dotted))

    return ModuleNode(
        path=path,
        relative_path=str(relative),
        dotted_name=dotted,
        lineno_count=len(source.splitlines()),
        docstring=ast.get_docstring(tree) or "",
        imports=_extract_imports(tree),
        classes=classes,
        functions=functions,
        constants=_extract_constants(tree),
        all_exports=_extract_all_exports(tree),
    )


# ---------------------------------------------------------------------------
# Project-level analysis
# ---------------------------------------------------------------------------

_SUBSYSTEM_DESCRIPTIONS: dict[str, str] = {
    "cli": "Command-line interface, TUI, autocompletion, and user-facing commands.",
    "core": "Core agent loop, configuration, LLM backends, middleware, and orchestration.",
    "acp": "Agent Client Protocol — session management, ACP tools, and server integration.",
    "tools": "Built-in tool implementations, MCP integrations, and tool management.",
    "setup": "Onboarding, first-run setup, and trusted-folder management.",
    "wiki": "Code wiki documentation generator (this system).",
    "voice": "Voice recording and transcription.",
}


def _classify_subsystem(relative_path: str) -> str:
    """Map a module relative path to a subsystem name."""
    parts = Path(relative_path).parts
    if len(parts) < 2:
        return "root"

    # vibe/<subsystem>/...
    subsystem = parts[1] if parts[0] == "vibe" else parts[0]

    # core/tools → "tools", core/llm → "core", etc.
    if subsystem == "core" and len(parts) > 2:
        sub2 = parts[2]
        if sub2 in ("tools", "voice", "wiki"):
            return sub2
    return subsystem


def _build_import_graph(modules: list[ModuleNode]) -> dict[str, list[str]]:
    """Build a directed adjacency list: module → [modules it imports]."""
    known = {m.dotted_name for m in modules}
    graph: dict[str, list[str]] = defaultdict(list)

    for mod in modules:
        for imp in mod.imports:
            target = imp.module
            # Resolve relative imports
            if imp.is_relative and imp.level > 0:
                parts = mod.dotted_name.split(".")
                base = ".".join(parts[: max(0, len(parts) - imp.level)])
                target = f"{base}.{target}" if target else base

            # Check if target or its parent package is in our project
            if target in known:
                graph[mod.dotted_name].append(target)
            else:
                # Try the first component match (vibe.core.config → vibe.core)
                for prefix_len in range(len(target.split(".")), 0, -1):
                    prefix = ".".join(target.split(".")[:prefix_len])
                    if prefix in known:
                        graph[mod.dotted_name].append(prefix)
                        break

    return dict(graph)


def _build_class_hierarchy(modules: list[ModuleNode]) -> dict[str, list[str]]:
    """Build base → [child, …] hierarchy mapping using qualified names."""
    hierarchy: dict[str, list[str]] = defaultdict(list)
    name_to_qualified: dict[str, str] = {}

    for mod in modules:
        for cls in mod.classes:
            name_to_qualified[cls.name] = cls.qualified_name

    for mod in modules:
        for cls in mod.classes:
            for base in cls.bases:
                base_simple = base.split("[")[0].split(".")[-1]
                base_qualified = name_to_qualified.get(base_simple, base_simple)
                hierarchy[base_qualified].append(cls.qualified_name)

    return dict(hierarchy)


def _parse_pyproject(project_root: Path) -> tuple[str, str, str, list[DependencyInfo]]:
    """Extract project metadata and dependencies from pyproject.toml."""
    toml_path = project_root / "pyproject.toml"
    if not toml_path.exists():
        return "unknown", "0.0.0", ">=3.12", []

    import tomllib
    data = tomllib.loads(toml_path.read_text(encoding="utf-8"))

    project = data.get("project", {})
    name = project.get("name", "unknown")
    version = project.get("version", "0.0.0")
    python_req = project.get("requires-python", ">=3.12")

    # Categorise dependencies
    dep_categories: dict[str, str] = {
        "mistralai": "llm", "anthropic": "llm", "google-cloud-aiplatform": "llm",
        "openai": "llm",
        "textual": "tui", "rich": "tui", "prompt-toolkit": "tui",
        "httpx": "networking", "mcp": "networking",
        "pydantic": "data", "pydantic-settings": "data",
        "pytest": "testing", "pytest-asyncio": "testing",
        "tree-sitter": "parsing",
        "sounddevice": "audio", "soundfile": "audio", "numpy": "audio",
    }

    deps: list[DependencyInfo] = []
    for dep_str in project.get("dependencies", []):
        # "mistralai>=1.12.4" → name="mistralai", spec=">=1.12.4"
        for sep in (">=", "<=", "==", "~=", "!=", ">", "<"):
            if sep in dep_str:
                pkg_name, version_spec = dep_str.split(sep, 1)
                pkg_name = pkg_name.strip().lower()
                version_spec = f"{sep}{version_spec.strip()}"
                break
        else:
            pkg_name = dep_str.strip().lower()
            version_spec = ""

        # Lookup category by prefix match
        category = ""
        for prefix, cat in dep_categories.items():
            if pkg_name.startswith(prefix.lower()):
                category = cat
                break

        deps.append(DependencyInfo(name=pkg_name, version_spec=version_spec, category=category))

    return name, version, python_req, deps


def analyze_project(project_root: str | Path) -> ProjectModel:
    """Analyse a full Python project and return a :class:`ProjectModel`.

    Parameters
    ----------
    project_root:
        Path to the repository root (the directory containing ``pyproject.toml``
        and the ``vibe/`` package).

    Returns
    -------
    ProjectModel:
        Complete analysis result ready for downstream renderers.
    """
    root = Path(project_root).resolve()

    # 1. Parse pyproject.toml
    name, version, python_req, deps = _parse_pyproject(root)

    # 2. Discover and parse all Python files
    skip_dirs = {"__pycache__", ".venv", ".git", "node_modules", ".mypy_cache", ".ruff_cache"}
    modules: list[ModuleNode] = []

    for py_file in sorted(root.rglob("*.py")):
        if any(part in skip_dirs for part in py_file.parts):
            continue
        if not str(py_file).startswith(str(root)):
            continue
        if (mod := parse_module(py_file, root)) is not None:
            modules.append(mod)

    # 3. Build import graph & class hierarchy
    import_graph = _build_import_graph(modules)
    class_hierarchy = _build_class_hierarchy(modules)

    # 4. Cluster into subsystems
    clusters: dict[str, list[ModuleNode]] = defaultdict(list)
    for mod in modules:
        subsystem = _classify_subsystem(mod.relative_path)
        clusters[subsystem].append(mod)

    subsystems = [
        SubsystemCluster(
            name=name,
            description=_SUBSYSTEM_DESCRIPTIONS.get(name, f"The {name} subsystem."),
            modules=mods,
        )
        for name, mods in sorted(clusters.items())
    ]

    # 5. Detect remote source URL and commit SHA
    from vibe.core.wiki.source_linker import detect_commit_sha, detect_remote_url
    remote_base = detect_remote_url(root)
    sha = detect_commit_sha(root)

    return ProjectModel(
        project_name=name,
        version=version,
        python_requires=python_req,
        root=root,
        modules=modules,
        subsystems=subsystems,
        dependencies=deps,
        import_graph=import_graph,
        class_hierarchy=class_hierarchy,
        remote_base_url=remote_base,
        commit_sha=sha,
    )


# ---------------------------------------------------------------------------
# JSON artefact generation
# ---------------------------------------------------------------------------

def generate_symbol_index(model: ProjectModel) -> dict[str, str]:
    """Return ``{qualified_name: "relative/path.py#L<line>", …}``."""
    index: dict[str, str] = {}
    for mod in model.modules:
        for cls in mod.classes:
            index[cls.qualified_name] = f"{mod.relative_path}#L{cls.lineno}"
            for method in cls.methods:
                index[method.qualified_name] = f"{mod.relative_path}#L{method.lineno}"
        for fn in mod.functions:
            index[fn.qualified_name] = f"{mod.relative_path}#L{fn.lineno}"
    return index


def generate_dependency_graph(model: ProjectModel) -> dict[str, list[str]]:
    """Return the module-level import adjacency list."""
    return model.import_graph


def write_json_artefacts(model: ProjectModel, output_dir: Path) -> None:
    """Write ``symbol_index.json`` and ``dependency_graph.json`` to *output_dir*."""
    output_dir.mkdir(parents=True, exist_ok=True)

    si = generate_symbol_index(model)
    (output_dir / "symbol_index.json").write_text(
        json.dumps(si, indent=2, sort_keys=True), encoding="utf-8",
    )

    dg = generate_dependency_graph(model)
    (output_dir / "dependency_graph.json").write_text(
        json.dumps(dg, indent=2, sort_keys=True), encoding="utf-8",
    )
