"""Site builder — orchestrates the full wiki generation pipeline.

Pipeline:  ``analyze → architecture → diagrams → narrative + llm_doc → MkDocs site``

Supports **incremental rebuilds**: when a previous build state exists the
pipeline compares the saved commit SHA against HEAD via ``git diff``.  If
no ``.py`` files changed the build is skipped entirely.  PlantUML diagrams
are cached by content-hash so unchanged diagrams are never re-rendered.

Public API
----------
>>> import asyncio
>>> from vibe.core.wiki.site_builder import build_wiki_site
>>> result = asyncio.run(build_wiki_site("."))
>>> print(result.summary)
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass, field
from enum import StrEnum, auto
from pathlib import Path

from vibe.core.wiki.analyzer import ProjectModel, analyze_project, write_json_artefacts
from vibe.core.wiki.architecture import ArchitectureKnowledge, extract_architecture
from vibe.core.wiki.build_state import WikiBuildState, hash_diagram_source
from vibe.core.wiki.diagrams import generate_all_diagrams
from vibe.core.wiki.llm_doc import generate_llms_full_txt, generate_llms_txt
from vibe.core.wiki.narrative import generate_narrative_pages
from vibe.core.wiki.plantuml import render_plantuml
from vibe.core.wiki.source_linker import changed_files_since, detect_commit_sha

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Build mode
# ---------------------------------------------------------------------------

class BuildMode(StrEnum):
    """How much work ``build_wiki_site`` actually did."""

    FULL = auto()        # first build or state missing
    INCREMENTAL = auto() # .py files changed → re-analysed + regenerated
    SKIPPED = auto()     # nothing changed since last build


# ---------------------------------------------------------------------------
# Build result
# ---------------------------------------------------------------------------

@dataclass
class WikiBuildResult:
    """Outcome of a full wiki build."""

    output_dir: Path
    build_mode: BuildMode = BuildMode.FULL
    pages_written: int = 0
    diagrams_rendered: int = 0
    diagrams_cached: int = 0
    diagrams_failed: int = 0
    llm_files_written: int = 0
    json_artefacts_written: int = 0
    changed_files: list[str] = field(default_factory=list)
    model: ProjectModel | None = None
    knowledge: ArchitectureKnowledge | None = None
    errors: list[str] = field(default_factory=list)

    @property
    def summary(self) -> str:
        if self.build_mode is BuildMode.SKIPPED:
            return (
                f"Wiki up-to-date → {self.output_dir}\n"
                "  No .py files changed since last build — skipped."
            )
        mode_label = "incremental" if self.build_mode is BuildMode.INCREMENTAL else "full"
        parts = [
            f"Wiki built ({mode_label}) → {self.output_dir}",
            f"  Pages: {self.pages_written}",
            f"  Diagrams: {self.diagrams_rendered} rendered, "
            f"{self.diagrams_cached} cached, {self.diagrams_failed} failed",
            f"  LLM docs: {self.llm_files_written} (llms.txt + llms-full.txt)",
            f"  JSON artefacts: {self.json_artefacts_written}",
        ]
        if self.changed_files:
            parts.append(f"  Changed files: {len(self.changed_files)}")
            for f in self.changed_files[:10]:
                parts.append(f"    - {f}")
            if len(self.changed_files) > 10:
                parts.append(f"    … and {len(self.changed_files) - 10} more")
        if self.model:
            parts.append(
                f"  Project: {self.model.project_name} v{self.model.version} — "
                f"{len(self.model.modules)} modules, "
                f"{len(self.model.all_classes)} classes, "
                f"{self.model.total_lines:,} lines"
            )
        if self.errors:
            parts.append(f"  Errors: {len(self.errors)}")
            for e in self.errors[:5]:
                parts.append(f"    - {e}")
        return "\n".join(parts)


# ---------------------------------------------------------------------------
# MkDocs configuration
# ---------------------------------------------------------------------------

def _generate_mkdocs_yml(model: ProjectModel, docs_dir: Path) -> str:
    """Generate ``mkdocs.yml`` configuration."""
    return f"""\
site_name: "{model.project_name} Code Wiki"
site_description: "Auto-generated documentation for {model.project_name} v{model.version}"
docs_dir: "{docs_dir}"

theme:
  name: material
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: deep purple
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: deep purple
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.instant
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.highlight
    - search.suggest
    - content.code.copy
    - content.tabs.link

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - attr_list
  - md_in_html
  - tables
  - toc:
      permalink: true

plugins:
  - search

extra_css:
  - css/custom.css
"""


_CUSTOM_CSS = """\
/* Code Wiki custom styles */
img[alt*="diagram"], img[alt*="overview"], img[alt*="flow"],
img[alt*="context"], img[alt*="pattern"],
img[alt*="classes_"], img[alt*="mindmap"], img[alt*="component"],
img[alt*="sequence"] {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1em auto;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 8px;
  padding: 8px;
  background: var(--md-default-bg-color);
}

.md-typeset table {
  font-size: 0.85em;
}

.md-typeset h3 code {
  font-size: 0.9em;
}
"""


# ---------------------------------------------------------------------------
# Diagram rendering
# ---------------------------------------------------------------------------

async def _render_all_diagrams(
    diagram_sources: dict[str, str],
    diagrams_dir: Path,
    prev_hashes: dict[str, str] | None = None,
) -> tuple[int, int, int, list[str], dict[str, str]]:
    """Render PlantUML diagrams to SVG, skipping unchanged ones.

    Returns ``(rendered, cached, failed, errors, new_hashes)``.
    """
    diagrams_dir.mkdir(parents=True, exist_ok=True)
    rendered = 0
    cached = 0
    failed = 0
    errors: list[str] = []
    new_hashes: dict[str, str] = {}
    prev = prev_hashes or {}

    for name, source in diagram_sources.items():
        content_hash = hash_diagram_source(source)
        new_hashes[name] = content_hash

        # Save .puml source regardless
        (diagrams_dir / f"{name}.puml").write_text(source, encoding="utf-8")

        # Skip render if hash matches and SVG already exists
        svg_path = diagrams_dir / f"{name}.svg"
        if prev.get(name) == content_hash and svg_path.exists():
            cached += 1
            continue

        try:
            await render_plantuml(source, diagrams_dir / name, fmt="svg")
            rendered += 1
        except Exception as exc:
            failed += 1
            errors.append(f"Diagram '{name}': {exc}")
            logger.warning("Failed to render diagram %s: %s", name, exc)
            _write_placeholder_svg(svg_path, name)

    return rendered, cached, failed, errors, new_hashes


def _write_placeholder_svg(path: Path, name: str) -> None:
    """Write a minimal placeholder SVG when rendering fails."""
    svg = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="100">'
        '<rect width="400" height="100" fill="#f5f5f5" stroke="#ccc"/>'
        f'<text x="200" y="55" text-anchor="middle" fill="#999" font-size="14">'
        f'Diagram: {name} (render failed)</text>'
        '</svg>'
    )
    path.write_text(svg, encoding="utf-8")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

async def build_wiki_site(
    project_root: str | Path,
    output_dir: str | Path | None = None,
    *,
    force: bool = False,
) -> WikiBuildResult:
    """Run the wiki generation pipeline with incremental rebuild support.

    Parameters
    ----------
    project_root:
        Path to the repository root.
    output_dir:
        Where to write the wiki.  Defaults to ``<project_root>/docs_wiki``.
    force:
        When ``True`` skip change detection and do a full rebuild regardless.

    Returns
    -------
    WikiBuildResult:
        Summary of what was generated.
    """
    root = Path(project_root).resolve()
    out = Path(output_dir).resolve() if output_dir else root / "docs_wiki"
    docs_dir = out / "docs"
    diagrams_dir = docs_dir / "diagrams"
    css_dir = docs_dir / "css"

    result = WikiBuildResult(output_dir=out)

    # ------------------------------------------------------------------
    # 0. Load previous build state & decide build mode
    # ------------------------------------------------------------------
    prev_state = WikiBuildState.load(out) if not force else None
    head_sha = detect_commit_sha(root)

    if prev_state and head_sha:
        if prev_state.commit_sha == head_sha:
            # Exact same commit — nothing to do
            result.build_mode = BuildMode.SKIPPED
            logger.info("Wiki up-to-date (commit %s…) — skipping.", head_sha[:12])
            return result

        # Different commit — check what actually changed
        diff = changed_files_since(root, prev_state.commit_sha)
        if diff is not None and len(diff) == 0:
            # Commits exist but no .py files changed (docs, configs, etc.)
            result.build_mode = BuildMode.SKIPPED
            logger.info("No .py files changed since %s… — skipping.", prev_state.commit_sha[:12])
            return result

        # .py files changed → incremental rebuild
        result.build_mode = BuildMode.INCREMENTAL
        result.changed_files = diff or []
        logger.info(
            "Incremental rebuild: %s .py file(s) changed since %s…",
            len(result.changed_files) if diff else "unknown",
            prev_state.commit_sha[:12],
        )
    else:
        result.build_mode = BuildMode.FULL
        logger.info("Full wiki build (no previous state).")

    # ------------------------------------------------------------------
    # 1. Analyse
    # ------------------------------------------------------------------
    logger.info("Analysing project at %s …", root)
    model = analyze_project(root)
    result.model = model
    logger.info("Found %d modules, %d classes", len(model.modules), len(model.all_classes))

    # ------------------------------------------------------------------
    # 2. Extract architecture knowledge
    # ------------------------------------------------------------------
    knowledge = extract_architecture(model)
    result.knowledge = knowledge
    logger.info("Detected %d design patterns", len(knowledge.patterns))

    # ------------------------------------------------------------------
    # 3. Generate + render diagrams (with caching)
    # ------------------------------------------------------------------
    diagram_sources = generate_all_diagrams(model, knowledge)
    prev_hashes = prev_state.diagram_hashes if prev_state else None
    rendered, cached, failed, errors, new_hashes = await _render_all_diagrams(
        diagram_sources, diagrams_dir, prev_hashes,
    )
    result.diagrams_rendered = rendered
    result.diagrams_cached = cached
    result.diagrams_failed = failed
    result.errors.extend(errors)
    logger.info("Diagrams: %d rendered, %d cached, %d failed", rendered, cached, failed)

    # ------------------------------------------------------------------
    # 4. Generate narrative pages (developer docs)
    # ------------------------------------------------------------------
    pages = generate_narrative_pages(model, knowledge)
    for rel_path, content in pages.items():
        page_path = docs_dir / rel_path
        page_path.parent.mkdir(parents=True, exist_ok=True)
        page_path.write_text(content, encoding="utf-8")
        result.pages_written += 1
    logger.info("Wrote %d narrative pages", result.pages_written)

    # ------------------------------------------------------------------
    # 5. Generate LLM docs
    # ------------------------------------------------------------------
    llms_txt = generate_llms_txt(model, knowledge)
    (out / "llms.txt").write_text(llms_txt, encoding="utf-8")

    llms_full = generate_llms_full_txt(model, knowledge)
    (out / "llms-full.txt").write_text(llms_full, encoding="utf-8")
    result.llm_files_written = 2
    logger.info("Wrote llms.txt + llms-full.txt")

    # ------------------------------------------------------------------
    # 6. Write JSON artefacts
    # ------------------------------------------------------------------
    write_json_artefacts(model, out)
    result.json_artefacts_written = 2

    # ------------------------------------------------------------------
    # 7. Write MkDocs config + CSS
    # ------------------------------------------------------------------
    mkdocs_yml = _generate_mkdocs_yml(model, docs_dir)
    (out / "mkdocs.yml").write_text(mkdocs_yml, encoding="utf-8")

    css_dir.mkdir(parents=True, exist_ok=True)
    (css_dir / "custom.css").write_text(_CUSTOM_CSS, encoding="utf-8")

    # ------------------------------------------------------------------
    # 8. Save build state for next incremental run
    # ------------------------------------------------------------------
    if head_sha:
        state = WikiBuildState.create(
            commit_sha=head_sha,
            project_version=model.version,
            modules_count=len(model.modules),
            diagram_hashes=new_hashes,
        )
        state.save(out)
        logger.info("Saved build state (commit %s…).", head_sha[:12])

    logger.info("Wiki build complete: %s", out)
    return result
