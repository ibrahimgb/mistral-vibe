"""LLM-optimised renderer — flat Markdown for ``llms.txt`` and ``llms-full.txt``.

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
"""

from __future__ import annotations

from vibe.core.wiki.analyzer import ClassNode, FunctionNode, ModuleNode, ProjectModel
from vibe.core.wiki.architecture import ArchitectureKnowledge
from vibe.core.wiki.source_linker import source_url


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _oneliner(docstring: str) -> str:
    """Extract the first non-empty line from a docstring."""
    for line in docstring.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ""


def _method_sig(m: FunctionNode) -> str:
    async_prefix = "async " if m.is_async else ""
    params = ", ".join(p.split(":")[0].strip() for p in m.parameters if p != "self")
    ret = f" -> {m.return_annotation}" if m.return_annotation else ""
    return f"{async_prefix}def {m.name}({params}){ret}"


def _file_ref(
    remote_base: str | None,
    relative_path: str,
    lineno: int | None = None,
) -> str:
    """Return a source reference — full URL when available, else local path."""
    if url := source_url(remote_base, relative_path, lineno):
        return url
    frag = f"#L{lineno}" if lineno else ""
    return f"{relative_path}{frag}"


def _is_test_module(mod: ModuleNode) -> bool:
    return mod.relative_path.startswith("tests/") or mod.path.name.startswith("test_")


def _is_empty_init(mod: ModuleNode) -> bool:
    return mod.is_init and not mod.classes and not mod.functions


def _is_significant_private(fn: FunctionNode) -> bool:
    """True when a private helper is worth including in the LLM doc."""
    if fn.docstring:
        return True
    return (fn.end_lineno - fn.lineno) > 20


# ---------------------------------------------------------------------------
# llms.txt — short index
# ---------------------------------------------------------------------------

def generate_llms_txt(model: ProjectModel, knowledge: ArchitectureKnowledge) -> str:
    """Generate the short ``llms.txt`` index."""
    lines: list[str] = []

    # Header
    lines.append(f"# {model.project_name}")
    lines.append("")
    lines.append(f"> {model.project_name} v{model.version} is a terminal-based AI coding assistant "
                  "built on Mistral AI.  It features an agent loop with tool use, "
                  "multi-provider LLM backends, session persistence, and a rich TUI.")
    lines.append("")

    # Key entry points
    lines.append("## Entry Points")
    lines.append("")
    lines.append("- CLI: `vibe.cli.entrypoint:main`")
    lines.append("- ACP Server: `vibe.acp.entrypoint:main`")
    lines.append("- Agent Loop: `vibe.core.agent_loop:AgentLoop`")
    lines.append("- Config: `vibe.core.config:VibeConfig`")
    lines.append("- Tool System: `vibe.core.tools.manager:ToolManager`")
    lines.append("")

    # Subsystems
    lines.append("## Subsystems")
    lines.append("")
    for sub in model.subsystems:
        lines.append(f"- **{sub.name}** ({len(sub.modules)} modules, "
                      f"{sub.total_classes} classes, {sub.total_lines:,} lines): "
                      f"{sub.description}")
    lines.append("")

    # Design patterns summary
    lines.append("## Design Patterns")
    lines.append("")
    pattern_kinds = {p.kind.value for p in knowledge.patterns}
    for kind in sorted(pattern_kinds):
        count = sum(1 for p in knowledge.patterns if p.kind.value == kind)
        lines.append(f"- {kind.replace('_', ' ').title()} ({count} instances)")
    lines.append("")

    # Pointer to full doc
    lines.append("## Detailed Documentation")
    lines.append("")
    lines.append("- [llms-full.txt](llms-full.txt): Complete module/class/function reference")
    lines.append("- [symbol_index.json](symbol_index.json): Symbol → file:line mapping")
    lines.append("- [dependency_graph.json](dependency_graph.json): Module import adjacency list")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# llms-full.txt — complete reference
# ---------------------------------------------------------------------------

def _render_class_block(
    cls: ClassNode,
    mod: ModuleNode,
    remote_base: str | None,
) -> list[str]:
    """Render one class for llms-full.txt."""
    lines: list[str] = []
    stereo = ""
    if cls.is_protocol:
        stereo = " [Protocol]"
    elif cls.is_abstract:
        stereo = " [Abstract]"
    elif cls.is_pydantic:
        stereo = " [Pydantic]"
    elif cls.is_enum:
        stereo = " [Enum]"
    elif cls.is_dataclass:
        stereo = " [dataclass]"

    lines.append(f"### class: {cls.name}{stereo}")
    lines.append(f"  source: {_file_ref(remote_base, mod.relative_path, cls.lineno)}")
    if cls.bases:
        lines.append(f"  bases: {', '.join(cls.bases)}")
    if cls.docstring:
        lines.append(f"  summary: {_oneliner(cls.docstring)}")

    if cls.class_variables:
        lines.append(f"  fields: {', '.join(cls.class_variables[:15])}")

    for m in cls.public_methods:
        lines.append(f"    {_method_sig(m)}")
        if m.docstring:
            lines.append(f"      {_oneliner(m.docstring)}")

    # Significant private methods — not just names
    sig_private = [m for m in cls.private_methods if _is_significant_private(m)]
    if sig_private:
        private_names = ", ".join(m.name for m in sig_private[:10])
        lines.append(f"  notable_private: {private_names}")

    lines.append("")
    return lines


def _render_function_block(
    fn: FunctionNode,
    mod: ModuleNode,
    remote_base: str | None,
) -> list[str]:
    """Render one top-level function for llms-full.txt."""
    lines: list[str] = []
    lines.append(f"### function: {fn.name}()")
    lines.append(f"  source: {_file_ref(remote_base, mod.relative_path, fn.lineno)}")
    lines.append(f"  signature: {_method_sig(fn)}")
    if fn.docstring:
        lines.append(f"  summary: {_oneliner(fn.docstring)}")
    lines.append("")
    return lines


def generate_llms_full_txt(model: ProjectModel, knowledge: ArchitectureKnowledge) -> str:
    """Generate the complete ``llms-full.txt`` reference.

    Test modules and empty ``__init__.py`` files are excluded.
    """
    rb = model.remote_base_url
    lines: list[str] = []

    # Header
    lines.append(f"# {model.project_name} — Full Reference")
    lines.append("")
    lines.append(f"Version: {model.version}")
    lines.append(f"Python: {model.python_requires}")
    lines.append(f"Modules: {len(model.modules)}")
    lines.append(f"Classes: {len(model.all_classes)}")
    lines.append(f"Functions: {len(model.all_functions)}")
    lines.append(f"Total lines: {model.total_lines:,}")
    if rb:
        lines.append(f"Repository: {rb.rsplit('/blob/', 1)[0]}")
    lines.append("")

    # ---- Design Patterns ----
    lines.append("# Design Patterns")
    lines.append("")
    for p in knowledge.patterns:
        lines.append(f"- {p.title}: {p.description}")
        if p.files:
            file_refs = ", ".join(
                _file_ref(rb, f) for f in p.files[:5]
            )
            lines.append(f"  files: {file_refs}")
    lines.append("")

    # ---- Per-subsystem modules ----
    for sub in model.subsystems:
        # Filter out test modules and empty inits
        prod_modules = [
            m for m in sub.modules
            if not _is_test_module(m) and not _is_empty_init(m)
        ]
        if not prod_modules:
            continue

        prod_classes = sum(len(m.classes) for m in prod_modules)
        prod_fns = sum(len(m.functions) for m in prod_modules)
        prod_lines = sum(m.lineno_count for m in prod_modules)

        lines.append(f"# subsystem: {sub.name}")
        lines.append(f"  description: {sub.description}")
        lines.append(f"  modules: {len(prod_modules)}, classes: {prod_classes}, "
                      f"functions: {prod_fns}, lines: {prod_lines:,}")
        lines.append("")

        for mod in sorted(prod_modules, key=lambda m: m.dotted_name):
            lines.append(f"## module: {mod.dotted_name}")
            lines.append(f"  source: {_file_ref(rb, mod.relative_path)} ({mod.lineno_count} lines)")
            if mod.docstring:
                lines.append(f"  summary: {_oneliner(mod.docstring)}")

            if mod.constants:
                lines.append(f"  constants: {', '.join(mod.constants[:10])}")

            lines.append("")

            for cls in mod.classes:
                lines.extend(_render_class_block(cls, mod, rb))

            for fn in mod.functions:
                if fn.is_private and not _is_significant_private(fn):
                    continue
                lines.extend(_render_function_block(fn, mod, rb))

    return "\n".join(lines)
