"""Developer-facing renderer — Gemini Code Wiki style narrative Markdown.

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
"""

from __future__ import annotations

from vibe.core.wiki.analyzer import (
    ClassNode,
    FunctionNode,
    ModuleNode,
    ProjectModel,
    SubsystemCluster,
)
from vibe.core.wiki.architecture import ArchitectureKnowledge, PatternInstance
from vibe.core.wiki.source_linker import source_link_md


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _frontmatter(title: str, tldr: str, tags: list[str]) -> str:
    tag_str = ", ".join(tags)
    return (
        "---\n"
        f"title: \"{title}\"\n"
        f"tldr: \"{tldr}\"\n"
        f"tags: [{tag_str}]\n"
        "---\n\n"
    )


def _src(
    remote_base: str | None,
    relative_path: str,
    lineno: int | None = None,
    display: str | None = None,
) -> str:
    """Shorthand for ``source_link_md`` used throughout renderers."""
    return source_link_md(remote_base, relative_path, lineno, display)


def _embed_svg(diagram_name: str) -> str:
    """Return markdown to embed an SVG diagram."""
    return f"![{diagram_name}](../diagrams/{diagram_name}.svg)\n"


_NOISE_SUBSYSTEMS = frozenset({"root", "__init__.py", "scripts"})


def _is_noise_subsystem(sub: SubsystemCluster) -> bool:
    """Subsystems too trivial to warrant their own page."""
    if sub.name in _NOISE_SUBSYSTEMS:
        return True
    return sub.total_classes == 0 and sub.total_lines < 50


def _is_test_module(mod: ModuleNode) -> bool:
    """Return True for test files."""
    return mod.relative_path.startswith("tests/") or mod.path.name.startswith("test_")


def _is_trivial_module(mod: ModuleNode) -> bool:
    """Return True for modules not worth a reference page."""
    if mod.is_init and not mod.classes and not mod.functions:
        return True
    if _is_test_module(mod):
        return True
    if mod.lineno_count < 10 and not mod.classes and not mod.functions:
        return True
    return False


def _is_significant_private(fn: FunctionNode) -> bool:
    """True when a private method is architecturally significant enough to document."""
    if fn.docstring:
        return True
    return (fn.end_lineno - fn.lineno) > 20


def _describe_class(cls: ClassNode, mod: ModuleNode, remote_base: str | None) -> str:
    """Build a narrative prose paragraph for one class.

    Mentions stereo-type, bases, purpose (from docstring first line), and
    key public methods — all woven into flowing text with inline source links.
    """
    link = _src(remote_base, mod.relative_path, cls.lineno, cls.name)
    parts: list[str] = []

    # Opening sentence with stereotype
    stereo = ""
    if cls.is_protocol:
        stereo = "protocol"
    elif cls.is_abstract:
        stereo = "abstract base class"
    elif cls.is_pydantic:
        stereo = "Pydantic model"
    elif cls.is_dataclass:
        stereo = "dataclass"
    elif cls.is_enum:
        stereo = "enum"

    if stereo:
        parts.append(f"The {link} {stereo}")
    else:
        parts.append(f"The {link} class")

    # Bases
    if cls.bases:
        base_names = ", ".join(f"`{b}`" for b in cls.bases)
        parts[-1] += f" (extending {base_names})"

    # Docstring first line as purpose
    if cls.docstring:
        first_line = cls.docstring.split("\n")[0].strip().rstrip(".")
        parts[-1] += f" {first_line.lower()}."
    else:
        parts[-1] += "."

    # Fields for Pydantic / dataclass / enum
    if cls.class_variables and (cls.is_pydantic or cls.is_dataclass or cls.is_enum):
        field_names = ", ".join(f"`{v}`" for v in cls.class_variables[:8])
        suffix = ", …" if len(cls.class_variables) > 8 else ""
        parts.append(f" Key fields include {field_names}{suffix}.")

    # Key public methods — mention up to 5 inline
    notable = [m for m in cls.public_methods if not m.is_property]
    if notable:
        method_mentions = ", ".join(
            f"`{m.name}()`" for m in notable[:5]
        )
        suffix = f" among {len(notable)} public methods" if len(notable) > 5 else ""
        parts.append(f" It exposes {method_mentions}{suffix}.")

    # Significant private methods
    sig_private = [m for m in cls.private_methods if _is_significant_private(m)]
    if sig_private:
        pvt_mentions = ", ".join(f"`{m.name}()`" for m in sig_private[:3])
        parts.append(f" Internally it relies on {pvt_mentions}.")

    return "".join(parts)


def _describe_function(fn: FunctionNode, mod: ModuleNode, remote_base: str | None) -> str:
    """Build a one-line prose description of a top-level function."""
    link = _src(remote_base, mod.relative_path, fn.lineno, f"{fn.name}()")
    prefix = "The async function" if fn.is_async else "The function"
    if fn.docstring:
        purpose = fn.docstring.split("\n")[0].strip().rstrip(".")
        return f"{prefix} {link} {purpose.lower()}."
    return f"{prefix} {link} is defined in {_src(remote_base, mod.relative_path, display=mod.path.name)}."


# ---------------------------------------------------------------------------
# Page generators — Overview
# ---------------------------------------------------------------------------

def render_index_page(model: ProjectModel) -> tuple[str, str]:
    """Generate the wiki index / landing page."""
    rb = model.remote_base_url
    tldr = (
        f"{model.project_name} v{model.version} — "
        f"{len(model.modules)} modules, {len(model.all_classes)} classes "
        f"across {len(model.subsystems)} subsystems."
    )

    lines = [_frontmatter(f"{model.project_name} Code Wiki", tldr, ["overview", "index"])]
    lines.append(f"# {model.project_name} Code Wiki\n\n")

    # Narrative overview paragraph
    lines.append(
        f"{model.project_name} v{model.version} is a Python {model.python_requires} "
        f"project comprising {model.total_lines:,} lines of code organised into "
        f"{len(model.modules)} modules and {len(model.all_classes)} classes. "
        f"The codebase is structured around {len(model.subsystems)} subsystems "
        f"described below.\n\n"
    )

    lines.append("## Architecture Overview\n\n")
    lines.append(_embed_svg("c4_context"))
    lines.append("\n## Subsystem Map\n\n")
    lines.append(_embed_svg("mindmap_overview"))

    # Subsystems as a descriptive table — name + description only
    lines.append("\n## Subsystems\n\n")
    lines.append("| Subsystem | Description |\n")
    lines.append("|-----------|-------------|\n")
    for sub in model.subsystems:
        if _is_noise_subsystem(sub):
            continue
        lines.append(
            f"| [{sub.name}](subsystems/{sub.name}.md) | "
            f"{sub.description} "
            f"({len(sub.modules)} modules, {sub.total_classes} classes) |\n"
        )

    lines.append("\n## Quick Navigation\n\n")
    lines.append("- [Architecture & Patterns](architecture/patterns.md)\n")
    lines.append("- [Component Overview](architecture/components.md)\n")
    lines.append("- [Data Flow](architecture/data_flow.md)\n")
    lines.append("- [API Reference](reference/index.md)\n")

    return "index.md", "".join(lines)


# ---------------------------------------------------------------------------
# Page generators — Subsystem guides (How-To / Explanation)
# ---------------------------------------------------------------------------

def render_subsystem_page(
    sub: SubsystemCluster,
    model: ProjectModel,
    knowledge: ArchitectureKnowledge,
) -> tuple[str, str]:
    """Render a Gemini-style narrative subsystem guide page."""
    rb = model.remote_base_url

    # Filter out test modules entirely
    prod_modules = [m for m in sub.modules if not _is_test_module(m)]
    class_count = sum(len(m.classes) for m in prod_modules)
    fn_count = sum(len(m.functions) for m in prod_modules)
    total_lines = sum(m.lineno_count for m in prod_modules)

    tldr = f"{sub.name}: {sub.description} ({len(prod_modules)} modules, {class_count} classes)"

    lines = [_frontmatter(f"Subsystem — {sub.name}", tldr, ["subsystem", sub.name])]
    lines.append(f"# {sub.name}\n\n")

    # Opening narrative paragraph (instead of metrics table)
    lines.append(
        f"The **{sub.name}** subsystem {sub.description.lower().rstrip('.')}. "
        f"It contains {len(prod_modules)} modules with {class_count} classes, "
        f"{fn_count} functions, and approximately {total_lines:,} lines of code.\n\n"
    )

    # Embed class diagram if we have classes
    if class_count > 0:
        diagram_name = f"classes_{sub.name}"
        lines.append("## Class Diagram\n\n")
        lines.append(_embed_svg(diagram_name))
        lines.append("\n")

    # Key components as narrative prose paragraphs
    all_classes = [
        (cls, mod)
        for mod in prod_modules
        for cls in mod.classes
    ]
    top_classes = sorted(all_classes, key=lambda pair: len(pair[0].methods), reverse=True)[:10]

    if top_classes:
        lines.append("## Key Components\n\n")
        for cls, mod in top_classes:
            lines.append(f"{_describe_class(cls, mod, rb)}\n\n")

    # Design patterns found in this subsystem — weave into prose
    sub_patterns = [
        p for p in knowledge.patterns
        if any(
            f.startswith(f"vibe/{sub.name}/") or f"/{sub.name}/" in f
            for f in p.files
        )
    ]
    if sub_patterns:
        lines.append("## Design Patterns\n\n")
        for p in sub_patterns:
            file_links = ", ".join(
                _src(rb, f, display=f.rsplit("/", 1)[-1])
                for f in p.files[:3]
            )
            lines.append(
                f"**{p.title}** — {p.description} "
                f"See {file_links}."
            )
            if p.rationale:
                lines.append(f" {p.rationale}")
            lines.append("\n\n")

    # Module listing — compact, one line per module with inline source links
    lines.append("## Modules\n\n")
    for mod in sorted(prod_modules, key=lambda m: m.relative_path):
        link = _src(rb, mod.relative_path, display=mod.relative_path)
        doc_suffix = ""
        if mod.docstring:
            doc_suffix = f" — {mod.docstring.split(chr(10))[0]}"
        lines.append(f"- {link}{doc_suffix}\n")

    return f"subsystems/{sub.name}.md", "".join(lines)


# ---------------------------------------------------------------------------
# Page generators — Architecture pages (Explanation)
# ---------------------------------------------------------------------------

def render_patterns_page(
    knowledge: ArchitectureKnowledge,
    remote_base: str | None = None,
) -> tuple[str, str]:
    """Render the design patterns catalog as narrative prose."""
    rb = remote_base
    tldr = f"{len(knowledge.patterns)} design patterns detected across the codebase."
    lines = [_frontmatter("Design Patterns", tldr, ["architecture", "patterns"])]
    lines.append("# Design Patterns\n\n")
    lines.append(_embed_svg("design_patterns"))
    lines.append("\n")

    # Group by kind
    grouped: dict[str, list[PatternInstance]] = {}
    for p in knowledge.patterns:
        grouped.setdefault(p.kind.value, []).append(p)

    for kind_name, patterns in sorted(grouped.items()):
        pretty = kind_name.replace("_", " ").title()
        lines.append(f"## {pretty}\n\n")
        for p in patterns:
            lines.append(f"**{p.title}**\n\n")
            lines.append(f"{p.description}")
            if p.files:
                file_links = ", ".join(
                    _src(rb, f, display=f.rsplit("/", 1)[-1])
                    for f in p.files[:5]
                )
                lines.append(f" This pattern is implemented in {file_links}.")
            if p.rationale:
                lines.append(f" {p.rationale}")
            lines.append("\n\n")

    return "architecture/patterns.md", "".join(lines)


def render_components_page(model: ProjectModel) -> tuple[str, str]:
    """Render the component overview as narrative prose."""
    rb = model.remote_base_url
    tldr = f"Component overview of {model.project_name} — {len(model.subsystems)} subsystems."
    lines = [_frontmatter("Component Overview", tldr, ["architecture", "components"])]
    lines.append("# Component Overview\n\n")
    lines.append(_embed_svg("component_overview"))
    lines.append("\n")

    lines.append(
        f"The {model.project_name} system is organised into "
        f"{len(model.subsystems)} subsystems that interact through "
        f"well-defined import boundaries.\n\n"
    )

    lines.append("## Subsystem Interactions\n\n")
    for sub in model.subsystems:
        sub_modules = {m.dotted_name for m in sub.modules}
        deps: set[str] = set()
        for mod_name in sub_modules:
            for target in model.import_graph.get(mod_name, []):
                target_sub = next(
                    (s.name for s in model.subsystems if any(m.dotted_name == target for m in s.modules)),
                    None,
                )
                if target_sub and target_sub != sub.name:
                    deps.add(target_sub)
        if deps:
            dep_list = ", ".join(f"**{d}**" for d in sorted(deps))
            lines.append(f"The **{sub.name}** subsystem depends on {dep_list}.\n\n")

    return "architecture/components.md", "".join(lines)


def render_data_flow_page() -> tuple[str, str]:
    """Render the data flow page with narrative descriptions."""
    lines = [_frontmatter("Data Flow", "How messages traverse the Vibe system.", ["architecture", "data-flow"])]
    lines.append("# Data Flow\n\n")

    lines.append(
        "This section describes the lifecycle of a user message as it flows "
        "through the Vibe system, from initial input to final response.\n\n"
    )

    lines.append("## Message Lifecycle\n\n")
    lines.append(_embed_svg("data_flow"))
    lines.append("\n## Agent Loop Sequence\n\n")
    lines.append(_embed_svg("agent_flow_sequence"))

    lines.append("\n## Key Stages\n\n")
    lines.append(
        "The message lifecycle proceeds through eight stages. "
        "First, **user input** is captured by the Textual TUI. "
        "The **system prompt** is then assembled from conversation history and "
        "system instructions. **Middleware pre-processing** transforms the "
        "messages before the **LLM invocation**, which streams the request to "
        "the configured backend (Mistral, Anthropic, etc.). "
        "If the response contains tool calls, the **tool dispatch** phase "
        "hands them to `ToolManager` for execution. "
        "The **conversation loop** feeds tool results back to the LLM for "
        "continued reasoning. Finally, **response rendering** displays the "
        "Markdown via Rich in the TUI, and **session logging** persists the "
        "full turn to the session JSONL file.\n"
    )

    return "architecture/data_flow.md", "".join(lines)


# ---------------------------------------------------------------------------
# Page generators — API Reference
# ---------------------------------------------------------------------------

def render_module_reference(
    mod: ModuleNode,
    remote_base: str | None = None,
) -> tuple[str, str]:
    """Render narrative API reference for one module."""
    rb = remote_base
    first_doc_line = mod.docstring.split("\n")[0] if mod.docstring else f"Module {mod.dotted_name}"
    tldr = first_doc_line[:120]

    lines = [_frontmatter(mod.dotted_name, tldr, ["reference", "api"])]

    mod_link = _src(rb, mod.relative_path, display=mod.dotted_name)
    lines.append(f"# {mod_link}\n\n")

    if mod.docstring:
        lines.append(f"{mod.docstring}\n\n")

    if mod.constants:
        const_names = ", ".join(f"`{c}`" for c in mod.constants)
        lines.append(f"This module defines the constants {const_names}.\n\n")

    # Classes — narrative paragraphs
    for cls in mod.classes:
        lines.append(f"## {_src(rb, mod.relative_path, cls.lineno, cls.name)}\n\n")

        lines.append(f"{_describe_class(cls, mod, rb)}\n\n")

        # Public methods — compact reference list
        if cls.public_methods:
            lines.append("**Public API:**\n\n")
            for m in cls.public_methods:
                prefix = "async " if m.is_async else ""
                sig = f"`{prefix}def {m.name}()`"
                doc = f" — {m.docstring.split(chr(10))[0]}" if m.docstring else ""
                lines.append(f"- {sig}{doc}\n")
            lines.append("\n")

        # Significant private methods only
        sig_private = [m for m in cls.private_methods if _is_significant_private(m)]
        if sig_private:
            lines.append("**Internal helpers:**\n\n")
            for m in sig_private:
                doc = f" — {m.docstring.split(chr(10))[0]}" if m.docstring else ""
                lines.append(f"- `{m.name}()`{doc}\n")
            lines.append("\n")

    # Top-level functions — narrative
    for fn in mod.functions:
        if fn.is_private and not _is_significant_private(fn):
            continue
        lines.append(f"## {_src(rb, mod.relative_path, fn.lineno, f'{fn.name}()')}\n\n")
        lines.append(f"```python\n{fn.signature}\n```\n\n")
        if fn.docstring:
            lines.append(f"{fn.docstring}\n\n")

    ref_path = mod.relative_path.replace("/", "_").replace(".py", ".md")
    return f"reference/{ref_path}", "".join(lines)


def render_reference_index(model: ProjectModel) -> tuple[str, str]:
    """Render the API reference index page."""
    rb = model.remote_base_url
    tldr = f"API reference for {len(model.modules)} modules."
    lines = [_frontmatter("API Reference", tldr, ["reference", "index"])]
    lines.append("# API Reference\n\n")

    for sub in model.subsystems:
        if _is_noise_subsystem(sub):
            continue
        prod_mods = [m for m in sub.modules if not _is_test_module(m)]
        if not prod_mods:
            continue
        lines.append(f"## {sub.name}\n\n")
        for mod in sorted(prod_mods, key=lambda m: m.dotted_name):
            if _is_trivial_module(mod):
                continue
            ref_path = mod.relative_path.replace("/", "_").replace(".py", ".md")
            link = _src(rb, mod.relative_path, display=mod.dotted_name)
            first_line = mod.docstring.split("\n")[0][:60] if mod.docstring else ""
            doc_suffix = f" — {first_line}" if first_line else ""
            lines.append(f"- [{mod.dotted_name}]({ref_path}){doc_suffix}\n")
        lines.append("\n")

    return "reference/index.md", "".join(lines)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def generate_narrative_pages(
    model: ProjectModel,
    knowledge: ArchitectureKnowledge,
) -> dict[str, str]:
    """Generate all MkDocs Markdown pages.

    Returns
    -------
    dict[str, str]:
        Mapping ``relative_path → markdown_content``.  Paths are relative
        to the MkDocs ``docs/`` directory.
    """
    rb = model.remote_base_url
    pages: dict[str, str] = {}

    # Index / landing
    path, content = render_index_page(model)
    pages[path] = content

    # Subsystem guides (skip noise subsystems)
    for sub in model.subsystems:
        if _is_noise_subsystem(sub):
            continue
        path, content = render_subsystem_page(sub, model, knowledge)
        pages[path] = content

    # Architecture pages
    path, content = render_patterns_page(knowledge, rb)
    pages[path] = content

    path, content = render_components_page(model)
    pages[path] = content

    path, content = render_data_flow_page()
    pages[path] = content

    # API reference index
    path, content = render_reference_index(model)
    pages[path] = content

    # Per-module reference pages — skip trivial / test modules
    for mod in model.modules:
        if _is_trivial_module(mod):
            continue
        path, content = render_module_reference(mod, rb)
        pages[path] = content

    return pages
