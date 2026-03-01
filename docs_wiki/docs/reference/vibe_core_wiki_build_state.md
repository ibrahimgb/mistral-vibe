---
title: "vibe.core.wiki.build_state"
tldr: "Persistent build state for incremental wiki rebuilds."
tags: [reference, api]
---

# [**vibe.core.wiki.build_state**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/build_state.py)

Persistent build state for incremental wiki rebuilds.

Stores the last-built commit SHA and diagram content hashes so that
subsequent ``build_wiki_site()`` calls can skip unchanged work.

The state file lives at ``<wiki_output_dir>/.wiki_build_state.json``.

This module defines the constants `_STATE_FILENAME`.

## [**WikiBuildState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/build_state.py#L24)

The [**WikiBuildState**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/build_state.py#L24) Pydantic model (extending `BaseModel`) serialisable snapshot of the last successful wiki build. Key fields include `commit_sha`, `build_timestamp`, `project_version`, `modules_count`, `diagram_hashes`. It exposes `save()`, `load()`, `create()`.

**Public API:**

- `def save()` — Write state to ``<output_dir>/.wiki_build_state.json``.
- `def load()` — Load previously saved state, or return ``None`` if missing / corrupt.
- `def create()` — Build a fresh state snapshot for the current build.

## [**hash_diagram_source()**](https://github.com/ibrahimgb/mistral-vibe/blob/87fd92fb12b535b705a6f815cddb938721e9215d/vibe/core/wiki/build_state.py#L85)

```python
def hash_diagram_source(source: str) -> str
```

Return a hex SHA-256 digest of a PlantUML source string.

