"""Auto-generate PlantUML diagrams from a :class:`ProjectModel`.

Each public function returns PlantUML source text (``str``).  The caller
is responsible for rendering to SVG via :mod:`vibe.core.wiki.plantuml`.
"""

from __future__ import annotations

from vibe.core.wiki.analyzer import ClassNode, ProjectModel, SubsystemCluster
from vibe.core.wiki.architecture import ArchitectureKnowledge, PatternKind


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _sanitize(name: str) -> str:
    """Make a name safe for PlantUML identifiers."""
    return name.replace(".", "_").replace("-", "_").replace(" ", "_")


# ---------------------------------------------------------------------------
# 1. Mind map — subsystem overview
# ---------------------------------------------------------------------------

def generate_mindmap(model: ProjectModel) -> str:
    """Project mind-map showing subsystems and their key classes."""
    lines = ["@startmindmap", f"* {model.project_name} v{model.version}"]
    for sub in model.subsystems:
        lines.append(f"** {sub.name}")
        lines.append(f"***_ {sub.total_lines} lines, {sub.total_classes} classes")
        # Show top-5 classes by method count
        all_cls = [c for m in sub.modules for c in m.classes]
        top = sorted(all_cls, key=lambda c: len(c.methods), reverse=True)[:5]
        for cls in top:
            lines.append(f"*** {cls.name}")
    lines.append("@endmindmap")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 2. Component diagram — subsystem boundaries
# ---------------------------------------------------------------------------

def generate_component_diagram(model: ProjectModel) -> str:
    """C4-style component diagram showing subsystem boundaries and links."""
    lines = [
        "@startuml",
        "!theme plain",
        "skinparam componentStyle rectangle",
        "skinparam linetype ortho",
        "",
        'title "Component Overview"',
        "",
    ]

    # Declare packages
    for sub in model.subsystems:
        sid = _sanitize(sub.name)
        lines.append(f'package "{sub.name}" as {sid} {{')
        # Show top-3 modules
        top_mods = sorted(sub.modules, key=lambda m: m.lineno_count, reverse=True)[:3]
        for mod in top_mods:
            mid = _sanitize(mod.dotted_name)
            label = mod.path.stem
            lines.append(f'  component "{label}" as {mid}')
        lines.append("}")
        lines.append("")

    # Add edges from import graph
    drawn: set[tuple[str, str]] = set()
    for src, targets in model.import_graph.items():
        src_sub = _classify_to_subsystem_name(src, model)
        for tgt in targets:
            tgt_sub = _classify_to_subsystem_name(tgt, model)
            if src_sub != tgt_sub:
                edge = (src_sub, tgt_sub)
                if edge not in drawn:
                    drawn.add(edge)
                    lines.append(f"{_sanitize(src_sub)} --> {_sanitize(tgt_sub)}")

    lines.append("@enduml")
    return "\n".join(lines)


def _classify_to_subsystem_name(dotted: str, model: ProjectModel) -> str:
    for sub in model.subsystems:
        if any(m.dotted_name == dotted for m in sub.modules):
            return sub.name
    return "external"


# ---------------------------------------------------------------------------
# 3. Class diagram per subsystem
# ---------------------------------------------------------------------------

def _class_stereotype(cls: ClassNode) -> str:
    if cls.is_protocol:
        return " <<Protocol>>"
    if cls.is_abstract:
        return " <<Abstract>>"
    if cls.is_pydantic:
        return " <<Pydantic>>"
    if cls.is_dataclass:
        return " <<dataclass>>"
    if cls.is_enum:
        return " <<Enum>>"
    return ""


def generate_class_diagram(subsystem: SubsystemCluster, model: ProjectModel) -> str:
    """Class diagram for one subsystem — inheritance + key attributes."""
    lines = [
        "@startuml",
        "!theme plain",
        "skinparam classAttributeIconSize 0",
        f'title "Class Diagram — {subsystem.name}"',
        "",
    ]

    all_classes = [c for m in subsystem.modules for c in m.classes]

    # Limit to 25 classes max for readability
    if len(all_classes) > 25:
        all_classes = sorted(all_classes, key=lambda c: len(c.methods), reverse=True)[:25]

    class_names_in_diagram = {c.name for c in all_classes}

    for cls in all_classes:
        stereo = _class_stereotype(cls)
        kind = "abstract class" if cls.is_abstract or cls.is_protocol else "class"
        if cls.is_enum:
            kind = "enum"

        lines.append(f'{kind} "{cls.name}"{stereo} {{')

        # Show up to 5 class variables
        for cv in cls.class_variables[:5]:
            lines.append(f"  +{cv}")

        # Show public methods (max 8)
        for m in cls.public_methods[:8]:
            prefix = "{abstract} " if m.is_abstractmethod else ""
            static = "{static} " if m.is_staticmethod or m.is_classmethod else ""
            lines.append(f"  {prefix}{static}+{m.name}()")

        # Indicate if more are hidden
        hidden_count = max(0, len(cls.methods) - 8)
        if hidden_count:
            lines.append(f"  .. +{hidden_count} more ..")

        lines.append("}")
        lines.append("")

    # Inheritance edges
    for cls in all_classes:
        for base in cls.bases:
            base_simple = base.split("[")[0].split(".")[-1]
            if base_simple in class_names_in_diagram:
                lines.append(f'"{base_simple}" <|-- "{cls.name}"')

    lines.append("@enduml")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# 4. Sequence diagram — message flow
# ---------------------------------------------------------------------------

def generate_agent_flow_sequence(model: ProjectModel) -> str:
    """Sequence diagram for the core agent loop → LLM → tool call flow."""
    return """@startuml
!theme plain
title "Agent Loop — Message Flow"

actor User
participant "VibeApp\\n(TUI)" as TUI
participant "AgentLoop" as Agent
participant "LLMBackend" as LLM
participant "ToolManager" as Tools
participant "SessionLogger" as Session

User -> TUI : type message
TUI -> Agent : act(user_message)
activate Agent

Agent -> Agent : _build_messages()
Agent -> LLM : chat(messages)
activate LLM
LLM --> Agent : stream chunks
deactivate LLM

alt tool_calls present
    Agent -> Tools : invoke(tool_call)
    activate Tools
    Tools --> Agent : tool_result
    deactivate Tools
    Agent -> Agent : _conversation_loop()
    Agent -> LLM : chat(messages + tool_result)
    LLM --> Agent : final response
end

Agent -> Session : log_turn()
Agent --> TUI : stream response
deactivate Agent
TUI --> User : render markdown

@enduml"""


# ---------------------------------------------------------------------------
# 5. C4 Context diagram
# ---------------------------------------------------------------------------

def generate_c4_context(model: ProjectModel) -> str:
    """Top-level C4 context diagram showing external actors."""
    return f"""@startuml
!theme plain
title "C4 Context — {model.project_name}"

actor "Developer" as dev
rectangle "{model.project_name} v{model.version}" as vibe {{
  component "CLI / TUI" as cli
  component "Agent Loop" as agent
  component "Tool System" as tools
}}

cloud "LLM Providers" as llm {{
  component "Mistral AI" as mistral
  component "Anthropic" as anthropic
  component "Vertex AI" as vertex
}}

database "File System" as fs
rectangle "MCP Servers" as mcp

dev --> cli : commands & prompts
cli --> agent : user messages
agent --> llm : API calls
agent --> tools : tool invocations
tools --> fs : read/write files
tools --> mcp : MCP protocol
agent --> agent : conversation loop

@enduml"""


# ---------------------------------------------------------------------------
# 6. Data flow diagram
# ---------------------------------------------------------------------------

def generate_data_flow(model: ProjectModel) -> str:
    """Data flow diagram showing how messages traverse the system."""
    return """@startuml
!theme plain
title "Data Flow — Message Lifecycle"

start

:User types message;

:VibeApp captures input;

:Build system prompt\\n+ conversation history;

:Middleware pre-processing;

:Send to LLM Backend;

if (Response has tool calls?) then (yes)
  :ToolManager dispatches\\ntool invocations;

  :Tools execute\\n(bash, read_file, etc.);

  :Tool results appended\\nto conversation;

  :Re-send to LLM;
else (no)
endif

:Stream response tokens;

:Middleware post-processing;

:Render in TUI\\n(Markdown → Rich);

:Log to session file;

stop

@enduml"""


# ---------------------------------------------------------------------------
# 7. Design pattern diagram
# ---------------------------------------------------------------------------

def generate_pattern_diagram(knowledge: ArchitectureKnowledge) -> str:
    """Mind map of detected design patterns and where they appear."""
    lines = ["@startmindmap", "* Design Patterns"]

    grouped: dict[PatternKind, list[str]] = {}
    for p in knowledge.patterns:
        grouped.setdefault(p.kind, []).append(p.title)

    for kind, titles in grouped.items():
        lines.append(f"** {kind.value.replace('_', ' ').title()}")
        for title in titles[:6]:
            lines.append(f"*** {title}")
        if len(titles) > 6:
            lines.append(f"***_ +{len(titles) - 6} more")

    lines.append("@endmindmap")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Public API — generate all diagrams
# ---------------------------------------------------------------------------

def generate_all_diagrams(
    model: ProjectModel,
    knowledge: ArchitectureKnowledge,
) -> dict[str, str]:
    """Generate all PlantUML diagram sources.

    Returns
    -------
    dict[str, str]:
        Mapping of ``diagram_name → plantuml_source``.  Keys are used
        as filenames (without extension) in the output directory.
    """
    diagrams: dict[str, str] = {
        "mindmap_overview": generate_mindmap(model),
        "component_overview": generate_component_diagram(model),
        "agent_flow_sequence": generate_agent_flow_sequence(model),
        "c4_context": generate_c4_context(model),
        "data_flow": generate_data_flow(model),
        "design_patterns": generate_pattern_diagram(knowledge),
    }

    # Per-subsystem class diagrams
    for sub in model.subsystems:
        if sub.total_classes > 0:
            diagrams[f"classes_{sub.name}"] = generate_class_diagram(sub, model)

    return diagrams
