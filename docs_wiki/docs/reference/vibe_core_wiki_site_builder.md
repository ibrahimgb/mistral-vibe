---
title: "vibe.core.wiki.site_builder"
tldr: "Site builder — orchestrates the full wiki generation pipeline."
tags: [reference, api]
---

# [**vibe.core.wiki.site_builder**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/site_builder.py)

Site builder — orchestrates the full wiki generation pipeline.

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

This module defines the constants `_CUSTOM_CSS`.

## [**BuildMode**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/site_builder.py#L42)

The [**BuildMode**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/site_builder.py#L42) enum (extending `StrEnum`) how much work ``build_wiki_site`` actually did. Key fields include `FULL`, `INCREMENTAL`, `SKIPPED`.

## [**WikiBuildResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/site_builder.py#L55)

The [**WikiBuildResult**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/site_builder.py#L55) dataclass outcome of a full wiki build. Key fields include `output_dir`, `build_mode`, `pages_written`, `diagrams_rendered`, `diagrams_cached`, `diagrams_failed`, `llm_files_written`, `json_artefacts_written`, ….

**Public API:**

- `def summary()`

## [**_generate_mkdocs_yml()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/site_builder.py#L111)

```python
def _generate_mkdocs_yml(model: ProjectModel, docs_dir: Path) -> str
```

Generate ``mkdocs.yml`` configuration.

## [**_render_all_diagrams()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/site_builder.py#L196)

```python
async def _render_all_diagrams(diagram_sources: dict[str, str], diagrams_dir: Path, prev_hashes: dict[str, str] | None) -> tuple[int, int, int, list[str], dict[str, str]]
```

Render PlantUML diagrams to SVG, skipping unchanged ones.

Returns ``(rendered, cached, failed, errors, new_hashes)``.

## [**_write_placeholder_svg()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/site_builder.py#L238)

```python
def _write_placeholder_svg(path: Path, name: str) -> None
```

Write a minimal placeholder SVG when rendering fails.

## [**build_wiki_site()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/site_builder.py#L255)

```python
async def build_wiki_site(project_root: str | Path, output_dir: str | Path | None) -> WikiBuildResult
```

Run the wiki generation pipeline with incremental rebuild support.

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

