"""Persistent build state for incremental wiki rebuilds.

Stores the last-built commit SHA and diagram content hashes so that
subsequent ``build_wiki_site()`` calls can skip unchanged work.

The state file lives at ``<wiki_output_dir>/.wiki_build_state.json``.
"""

from __future__ import annotations

import hashlib
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)

_STATE_FILENAME = ".wiki_build_state.json"


class WikiBuildState(BaseModel):
    """Serialisable snapshot of the last successful wiki build."""

    commit_sha: str = Field(description="HEAD commit SHA at build time.")
    build_timestamp: str = Field(description="ISO-8601 UTC timestamp of the build.")
    project_version: str = Field(default="", description="Project version string.")
    modules_count: int = Field(default=0, description="Number of modules analysed.")
    diagram_hashes: dict[str, str] = Field(
        default_factory=dict,
        description="Mapping diagram_name → SHA-256 of .puml source.",
    )

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self, output_dir: Path) -> None:
        """Write state to ``<output_dir>/.wiki_build_state.json``."""
        path = output_dir / _STATE_FILENAME
        path.write_text(self.model_dump_json(indent=2), encoding="utf-8")
        logger.debug("Saved build state to %s", path)

    @classmethod
    def load(cls, output_dir: Path) -> WikiBuildState | None:
        """Load previously saved state, or return ``None`` if missing / corrupt."""
        path = output_dir / _STATE_FILENAME
        if not path.exists():
            return None
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            return cls.model_validate(data)
        except Exception as exc:
            logger.warning("Could not load build state from %s: %s", path, exc)
            return None

    # ------------------------------------------------------------------
    # Factory
    # ------------------------------------------------------------------

    @classmethod
    def create(
        cls,
        commit_sha: str,
        project_version: str,
        modules_count: int,
        diagram_hashes: dict[str, str] | None = None,
    ) -> WikiBuildState:
        """Build a fresh state snapshot for the current build."""
        return cls(
            commit_sha=commit_sha,
            build_timestamp=datetime.now(timezone.utc).isoformat(),
            project_version=project_version,
            modules_count=modules_count,
            diagram_hashes=diagram_hashes or {},
        )


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def hash_diagram_source(source: str) -> str:
    """Return a hex SHA-256 digest of a PlantUML source string."""
    return hashlib.sha256(source.encode("utf-8")).hexdigest()
