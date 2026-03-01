"""Extract design-pattern knowledge from a :class:`ProjectModel`.

Scans the analysis results for well-known structural patterns in the AST
metadata (base-class names, decorators, naming conventions) and emits a
catalog of :class:`PatternInstance` records.  The output feeds into the
narrative renderer and the LLM doc renderer.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum, auto

from vibe.core.wiki.analyzer import ClassNode, ModuleNode, ProjectModel


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

class PatternKind(StrEnum):
    """Well-known software design patterns we detect."""

    PROTOCOL_ADAPTER = auto()       # Protocol / Ports & Adapters
    TEMPLATE_METHOD = auto()        # ABC with abstract + concrete methods
    FACTORY = auto()                # Factory function / dict
    MIDDLEWARE_PIPELINE = auto()     # Chained middleware / hooks
    OBSERVER_STREAMING = auto()     # AsyncGenerator / event-driven streaming
    AUTODISCOVERY = auto()          # Plugin auto-loading via filesystem scan
    CONFIG_AS_CODE = auto()         # Pydantic settings / TOML config


@dataclass
class PatternInstance:
    """One occurrence of a pattern in the codebase."""

    kind: PatternKind
    title: str
    description: str
    files: list[str] = field(default_factory=list)     # relative paths
    classes: list[str] = field(default_factory=list)    # qualified names
    rationale: str = ""


@dataclass
class ArchitectureKnowledge:
    """Collected design-pattern knowledge for the project."""

    patterns: list[PatternInstance] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _is_test_module(mod: ModuleNode) -> bool:
    """Return ``True`` if a module lives under ``tests/`` or is a test file."""
    return mod.relative_path.startswith("tests/") or mod.path.name.startswith("test_")


# ---------------------------------------------------------------------------
# Pattern detectors
# ---------------------------------------------------------------------------

def _detect_protocol_adapter(model: ProjectModel) -> list[PatternInstance]:
    """Find Protocol classes and their concrete implementations."""
    protocols: list[ClassNode] = []
    protocol_names: set[str] = set()
    instances: list[PatternInstance] = []

    for mod in model.modules:
        if _is_test_module(mod):
            continue
        for cls in mod.classes:
            if cls.is_protocol or "Protocol" in cls.bases:
                protocols.append(cls)
                protocol_names.add(cls.name)

    if not protocols:
        return []

    # Find implementations — classes whose bases reference a protocol name
    for protocol in protocols:
        implementors: list[str] = []
        impl_files: list[str] = []
        for mod in model.modules:
            if _is_test_module(mod):
                continue
            for cls in mod.classes:
                base_names = {b.split("[")[0].split(".")[-1] for b in cls.bases}
                if protocol.name in base_names and cls.name != protocol.name:
                    implementors.append(cls.qualified_name)
                    impl_files.append(mod.relative_path)

        if implementors:
            pmod = next(
                (m for m in model.modules if any(c.name == protocol.name for c in m.classes)),
                None,
            )
            files = list(dict.fromkeys([pmod.relative_path] + impl_files)) if pmod else impl_files
            instances.append(PatternInstance(
                kind=PatternKind.PROTOCOL_ADAPTER,
                title=f"Protocol / Adapter — {protocol.name}",
                description=(
                    f"`{protocol.name}` defines a port with "
                    f"{len(implementors)} adapter(s): "
                    f"{', '.join(f'`{i.split('.')[-1]}`' for i in implementors)}."
                ),
                files=files,
                classes=[protocol.qualified_name, *implementors],
            ))

    return instances


def _detect_template_method(model: ProjectModel) -> list[PatternInstance]:
    """Find ABCs with a mix of abstract and concrete methods."""
    instances: list[PatternInstance] = []
    for mod in model.modules:
        if _is_test_module(mod):
            continue
        for cls in mod.classes:
            if not cls.is_abstract:
                continue
            abstract_methods = [m for m in cls.methods if m.is_abstractmethod]
            concrete_methods = [m for m in cls.methods if not m.is_abstractmethod and not m.is_private]
            if abstract_methods and concrete_methods:
                instances.append(PatternInstance(
                    kind=PatternKind.TEMPLATE_METHOD,
                    title=f"Template Method — {cls.name}",
                    description=(
                        f"`{cls.name}` defines {len(abstract_methods)} abstract hook(s) "
                        f"({', '.join(f'`{m.name}`' for m in abstract_methods[:4])}) "
                        f"with {len(concrete_methods)} concrete method(s) providing the template."
                    ),
                    files=[mod.relative_path],
                    classes=[cls.qualified_name],
                ))
    return instances


# Return types that are too trivial to count as a factory product.
_TRIVIAL_RETURNS = frozenset({
    "str", "int", "float", "bool", "None", "list", "dict", "tuple",
    "set", "bytes", "Path", "Any",
})


def _is_factory_return(annotation: str) -> bool:
    """Return ``True`` if *annotation* looks like a class instantiation.

    Rejects primitives, built-in containers, and optional/union wrappers
    around primitives.  Accepts anything whose core name starts uppercase
    (e.g. ``AgentLoop``, ``VibeConfig``, ``BaseTool[…]``).
    """
    if not annotation:
        return False
    # Strip Optional[], | None, list[], etc.
    core = annotation.split("[")[0].split("|")[0].strip().split(".")[-1]
    if core in _TRIVIAL_RETURNS:
        return False
    # Must start with an uppercase letter (class name convention)
    return core[:1].isupper()


def _detect_factory(model: ProjectModel) -> list[PatternInstance]:
    """Find factory functions/methods that return non-trivial class instances."""
    instances: list[PatternInstance] = []
    factory_prefixes = ("create_", "build_", "make_")

    for mod in model.modules:
        if _is_test_module(mod):
            continue
        for fn in mod.functions:
            if (any(fn.name.startswith(p) for p in factory_prefixes)
                    and _is_factory_return(fn.return_annotation)):
                instances.append(PatternInstance(
                    kind=PatternKind.FACTORY,
                    title=f"Factory — {fn.name}()",
                    description=(
                        f"`{fn.name}()` in `{mod.dotted_name}` "
                        f"creates `{fn.return_annotation}`."
                    ),
                    files=[mod.relative_path],
                    classes=[fn.qualified_name],
                ))
        for cls in mod.classes:
            for method in cls.methods:
                if (any(method.name.startswith(p) for p in factory_prefixes)
                        and (method.is_classmethod or method.is_staticmethod)
                        and _is_factory_return(method.return_annotation)):
                    instances.append(PatternInstance(
                        kind=PatternKind.FACTORY,
                        title=f"Factory — {cls.name}.{method.name}()",
                        description=(
                            f"`{cls.name}.{method.name}()` creates "
                            f"`{method.return_annotation}`."
                        ),
                        files=[mod.relative_path],
                        classes=[method.qualified_name],
                    ))
    return instances


def _detect_middleware(model: ProjectModel) -> list[PatternInstance]:
    """Find middleware-pattern classes (chain/pipeline)."""
    instances: list[PatternInstance] = []
    middleware_indicators = {"middleware", "Middleware", "pipeline", "Pipeline", "chain", "Chain"}

    for mod in model.modules:
        if _is_test_module(mod):
            continue
        if any(kw in mod.dotted_name for kw in ("middleware", "pipeline")):
            instances.append(PatternInstance(
                kind=PatternKind.MIDDLEWARE_PIPELINE,
                title=f"Middleware Pipeline — {mod.dotted_name}",
                description=f"Module `{mod.dotted_name}` implements a middleware pipeline.",
                files=[mod.relative_path],
                classes=[c.qualified_name for c in mod.classes],
            ))
            continue

        for cls in mod.classes:
            if any(kw in cls.name for kw in middleware_indicators):
                instances.append(PatternInstance(
                    kind=PatternKind.MIDDLEWARE_PIPELINE,
                    title=f"Middleware — {cls.name}",
                    description=f"`{cls.name}` in `{mod.dotted_name}` acts as a middleware component.",
                    files=[mod.relative_path],
                    classes=[cls.qualified_name],
                ))
    return instances


def _detect_streaming(model: ProjectModel) -> list[PatternInstance]:
    """Find AsyncGenerator-based streaming patterns."""
    instances: list[PatternInstance] = []
    for mod in model.modules:
        if _is_test_module(mod):
            continue
        for cls in mod.classes:
            streaming_methods = [
                m for m in cls.methods
                if m.is_async and "AsyncGenerator" in m.return_annotation
            ]
            if streaming_methods:
                instances.append(PatternInstance(
                    kind=PatternKind.OBSERVER_STREAMING,
                    title=f"Async Streaming — {cls.name}",
                    description=(
                        f"`{cls.name}` uses AsyncGenerator streaming in "
                        f"{len(streaming_methods)} method(s): "
                        f"{', '.join(f'`{m.name}`' for m in streaming_methods[:4])}."
                    ),
                    files=[mod.relative_path],
                    classes=[cls.qualified_name],
                ))
        for fn in mod.functions:
            if fn.is_async and "AsyncGenerator" in fn.return_annotation:
                instances.append(PatternInstance(
                    kind=PatternKind.OBSERVER_STREAMING,
                    title=f"Async Streaming — {fn.name}()",
                    description=f"`{fn.name}()` in `{mod.dotted_name}` yields an async stream.",
                    files=[mod.relative_path],
                    classes=[fn.qualified_name],
                ))
    return instances


def _detect_autodiscovery(model: ProjectModel) -> list[PatternInstance]:
    """Find plugin/tool auto-discovery by filesystem scanning."""
    instances: list[PatternInstance] = []
    for mod in model.modules:
        if _is_test_module(mod):
            continue
        if "manager" in mod.path.stem:
            for cls in mod.classes:
                discovery_methods = [
                    m for m in cls.methods
                    if any(kw in m.name for kw in ("discover", "scan", "_iter", "_load", "register"))
                ]
                if discovery_methods:
                    instances.append(PatternInstance(
                        kind=PatternKind.AUTODISCOVERY,
                        title=f"Auto-Discovery — {cls.name}",
                        description=(
                            f"`{cls.name}` auto-discovers plugins via "
                            f"{', '.join(f'`{m.name}()`' for m in discovery_methods[:3])}."
                        ),
                        files=[mod.relative_path],
                        classes=[cls.qualified_name],
                    ))
    return instances


def _detect_config_as_code(model: ProjectModel) -> list[PatternInstance]:
    """Find Pydantic Settings / config patterns."""
    instances: list[PatternInstance] = []
    for mod in model.modules:
        if _is_test_module(mod):
            continue
        for cls in mod.classes:
            if cls.is_pydantic and any(
                kw in cls.name.lower() for kw in ("config", "settings", "options")
            ):
                instances.append(PatternInstance(
                    kind=PatternKind.CONFIG_AS_CODE,
                    title=f"Config-as-Code — {cls.name}",
                    description=(
                        f"`{cls.name}` in `{mod.dotted_name}` uses Pydantic for "
                        f"typed configuration with {len(cls.class_variables)} field(s)."
                    ),
                    files=[mod.relative_path],
                    classes=[cls.qualified_name],
                ))
    return instances


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def extract_architecture(model: ProjectModel) -> ArchitectureKnowledge:
    """Run all pattern detectors and return collected knowledge.

    Parameters
    ----------
    model:
        A fully-populated :class:`ProjectModel` from :func:`analyze_project`.

    Returns
    -------
    ArchitectureKnowledge:
        Design patterns found and technology choices catalogued.
    """
    patterns: list[PatternInstance] = []
    for detector in (
        _detect_protocol_adapter,
        _detect_template_method,
        _detect_factory,
        _detect_middleware,
        _detect_streaming,
        _detect_autodiscovery,
        _detect_config_as_code,
    ):
        patterns.extend(detector(model))

    return ArchitectureKnowledge(patterns=patterns)
