"""Wiki documentation tool — build, manage, and query the Code Wiki.

Provides actions:
- ``build``  — run the full analysis + generation pipeline
- ``list_pages`` — list generated wiki pages
- ``analyze`` — run analysis only, return project stats
"""

from __future__ import annotations

from collections.abc import AsyncGenerator
from enum import StrEnum, auto
from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, Field

from vibe.core.tools.base import (
    BaseTool,
    BaseToolConfig,
    BaseToolState,
    InvokeContext,
    ToolError,
    ToolPermission,
)
from vibe.core.tools.ui import ToolCallDisplay, ToolResultDisplay, ToolUIData
from vibe.core.types import ToolResultEvent, ToolStreamEvent


class WikiAction(StrEnum):
    BUILD = auto()
    UPDATE = auto()
    LIST_PAGES = auto()
    ANALYZE = auto()


class WikiDocArgs(BaseModel):
    action: WikiAction = Field(description="Action to perform: 'build', 'update', 'list_pages', or 'analyze'.")
    project_root: str | None = Field(
        default=None,
        description="Path to the project root. Defaults to current working directory.",
    )
    output_dir: str | None = Field(
        default=None,
        description="Output directory for the wiki. Defaults to <project_root>/docs_wiki.",
    )
    force: bool = Field(
        default=False,
        description="Force a full rebuild, ignoring incremental cache.",
    )


class WikiDocResult(BaseModel):
    message: str
    build_mode: str = Field(default="", description="'full', 'incremental', or 'skipped'.")
    pages: list[str] = Field(default_factory=list)
    changed_files: list[str] = Field(default_factory=list)
    stats: dict[str, int] = Field(default_factory=dict)


class WikiDocConfig(BaseToolConfig):
    permission: ToolPermission = ToolPermission.ALWAYS


class WikiDocState(BaseToolState):
    last_output_dir: str | None = None


class WikiDoc(
    BaseTool[WikiDocArgs, WikiDocResult, WikiDocConfig, WikiDocState],
    ToolUIData[WikiDocArgs, WikiDocResult],
):
    description: ClassVar[str] = (
        "Build and manage the project Code Wiki. "
        "Generates dual-output documentation: a rich MkDocs site for developers "
        "and flat llms.txt/llms-full.txt for LLM consumption. "
        "Includes auto-generated PlantUML diagrams, design pattern catalog, "
        "and API reference."
    )

    @classmethod
    def format_call_display(cls, args: WikiDocArgs) -> ToolCallDisplay:
        match args.action:
            case WikiAction.BUILD:
                return ToolCallDisplay(summary="Building Code Wiki (full)")
            case WikiAction.UPDATE:
                return ToolCallDisplay(summary="Updating Code Wiki (incremental)")
            case WikiAction.LIST_PAGES:
                return ToolCallDisplay(summary="Listing wiki pages")
            case WikiAction.ANALYZE:
                return ToolCallDisplay(summary="Analyzing project")
            case _:
                return ToolCallDisplay(summary=f"Wiki: {args.action}")

    @classmethod
    def get_result_display(cls, event: ToolResultEvent) -> ToolResultDisplay:
        if isinstance(event.result, WikiDocResult):
            return ToolResultDisplay(success=True, message=event.result.message)
        return ToolResultDisplay(success=True, message="Done")

    @classmethod
    def get_status_text(cls) -> str:
        return "Building Code Wiki"

    async def run(
        self, args: WikiDocArgs, ctx: InvokeContext | None = None,
    ) -> AsyncGenerator[ToolStreamEvent | WikiDocResult, None]:
        match args.action:
            case WikiAction.BUILD:
                yield await self._build(args, force=True)
            case WikiAction.UPDATE:
                yield await self._build(args, force=False)
            case WikiAction.LIST_PAGES:
                yield self._list_pages()
            case WikiAction.ANALYZE:
                yield await self._analyze(args)
            case _:
                raise ToolError(f"Unknown action: {args.action}")

    async def _build(self, args: WikiDocArgs, *, force: bool) -> WikiDocResult:
        from vibe.core.wiki.site_builder import build_wiki_site

        root = args.project_root or "."
        result = await build_wiki_site(root, args.output_dir, force=force or args.force)
        self.state.last_output_dir = str(result.output_dir)

        return WikiDocResult(
            message=result.summary,
            build_mode=result.build_mode.value,
            changed_files=result.changed_files,
            stats={
                "pages": result.pages_written,
                "diagrams_rendered": result.diagrams_rendered,
                "diagrams_cached": result.diagrams_cached,
                "diagrams_failed": result.diagrams_failed,
                "llm_files": result.llm_files_written,
                "json_artefacts": result.json_artefacts_written,
            },
        )

    def _list_pages(self) -> WikiDocResult:
        if not self.state.last_output_dir:
            return WikiDocResult(message="No wiki built yet. Use action='build' first.")

        docs_dir = Path(self.state.last_output_dir) / "docs"
        if not docs_dir.exists():
            return WikiDocResult(message=f"Wiki docs directory not found: {docs_dir}")

        pages = sorted(str(p.relative_to(docs_dir)) for p in docs_dir.rglob("*.md"))
        return WikiDocResult(
            message=f"Found {len(pages)} pages in {docs_dir}",
            pages=pages,
            stats={"pages": len(pages)},
        )

    async def _analyze(self, args: WikiDocArgs) -> WikiDocResult:
        from vibe.core.wiki.analyzer import analyze_project

        root = args.project_root or "."
        model = analyze_project(root)

        return WikiDocResult(
            message=(
                f"Project: {model.project_name} v{model.version}\n"
                f"Modules: {len(model.modules)}\n"
                f"Classes: {len(model.all_classes)}\n"
                f"Functions: {len(model.all_functions)}\n"
                f"Subsystems: {len(model.subsystems)}\n"
                f"Total lines: {model.total_lines:,}"
            ),
            stats={
                "modules": len(model.modules),
                "classes": len(model.all_classes),
                "functions": len(model.all_functions),
                "subsystems": len(model.subsystems),
                "total_lines": model.total_lines,
            },
        )
