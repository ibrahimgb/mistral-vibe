"""PlantUML diagram generation tool — create and render diagrams as SVG.

The agent can use this tool to create custom PlantUML diagrams for the
project wiki.  Diagrams are rendered to SVG and saved alongside their
``.puml`` source.
"""

from __future__ import annotations

from collections.abc import AsyncGenerator
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


class WikiDiagramArgs(BaseModel):
    source: str = Field(description="PlantUML source text (including @startuml/@enduml).")
    name: str = Field(description="Diagram file name (without extension), e.g. 'class_overview'.")
    title: str = Field(default="", description="Human-readable diagram title.")
    fmt: str = Field(default="svg", description="Output format: 'svg' or 'png'.")
    output_dir: str | None = Field(
        default=None,
        description="Output directory. Defaults to docs_wiki/docs/diagrams/.",
    )


class WikiDiagramResult(BaseModel):
    message: str
    output_path: str
    puml_path: str


class WikiDiagramConfig(BaseToolConfig):
    permission: ToolPermission = ToolPermission.ALWAYS
    default_output_dir: str = "docs_wiki/docs/diagrams"
    plantuml_server: str = "https://www.plantuml.com/plantuml"


class WikiDiagramState(BaseToolState):
    pass


class WikiDiagram(
    BaseTool[WikiDiagramArgs, WikiDiagramResult, WikiDiagramConfig, WikiDiagramState],
    ToolUIData[WikiDiagramArgs, WikiDiagramResult],
):
    description: ClassVar[str] = (
        "Render a PlantUML diagram to SVG or PNG. "
        "Accepts PlantUML source text and produces a rendered image file "
        "alongside the .puml source. Supports class diagrams, sequence diagrams, "
        "mind maps, component diagrams, and more."
    )

    @classmethod
    def format_call_display(cls, args: WikiDiagramArgs) -> ToolCallDisplay:
        title = args.title or args.name
        return ToolCallDisplay(summary=f"Rendering diagram: {title}")

    @classmethod
    def get_result_display(cls, event: ToolResultEvent) -> ToolResultDisplay:
        if isinstance(event.result, WikiDiagramResult):
            return ToolResultDisplay(success=True, message=event.result.message)
        return ToolResultDisplay(success=True, message="Diagram rendered")

    @classmethod
    def get_status_text(cls) -> str:
        return "Rendering PlantUML diagram"

    async def run(
        self, args: WikiDiagramArgs, ctx: InvokeContext | None = None,
    ) -> AsyncGenerator[ToolStreamEvent | WikiDiagramResult, None]:
        from vibe.core.wiki.plantuml import render_plantuml

        # Validate source
        if "@startuml" not in args.source and "@startmindmap" not in args.source:
            raise ToolError(
                "PlantUML source must contain @startuml/@enduml or "
                "@startmindmap/@endmindmap markers."
            )

        out_dir = Path(args.output_dir or self.config.default_output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)

        # Save .puml source
        puml_path = out_dir / f"{args.name}.puml"
        puml_path.write_text(args.source, encoding="utf-8")

        # Render
        try:
            rendered_path = await render_plantuml(
                args.source,
                out_dir / args.name,
                fmt=args.fmt,
            )
        except Exception as exc:
            raise ToolError(f"Failed to render diagram: {exc}") from exc

        yield WikiDiagramResult(
            message=f"Diagram '{args.name}' rendered to {rendered_path}",
            output_path=str(rendered_path),
            puml_path=str(puml_path),
        )
