Render PlantUML diagrams to SVG or PNG files. Use this tool to create visual documentation for the project wiki.

## Supported Diagram Types

- **Class diagrams** — show class hierarchies, fields, and methods
- **Sequence diagrams** — show message flow between components
- **Component diagrams** — show system architecture and dependencies
- **Mind maps** — show hierarchical topic overviews
- **Activity diagrams** — show workflows and data flow
- **Use case diagrams** — show actor interactions

## When to Use This Tool

**Use when:**
- Creating architecture diagrams for the project wiki
- Visualising class hierarchies or component relationships
- Documenting workflows or message flows
- The user asks for a diagram or visual representation

**Skip this tool for:**
- Generating the full wiki (use wiki_doc with action='build' instead — it auto-generates diagrams)
- Text-only documentation (use write_file instead)

## Examples

### Class diagram
```json
{
  "source": "@startuml\n!theme plain\nclass AgentLoop {\n  +act(message)\n  +compact()\n  -_conversation_loop()\n}\nclass ToolManager {\n  +get_tool(name)\n  +get_available_tools()\n}\nAgentLoop --> ToolManager\n@enduml",
  "name": "agent_tools",
  "title": "Agent Loop and Tool Manager",
  "fmt": "svg"
}
```

### Sequence diagram
```json
{
  "source": "@startuml\n!theme plain\nactor User\nparticipant TUI\nparticipant AgentLoop\nparticipant LLM\nUser -> TUI: message\nTUI -> AgentLoop: act()\nAgentLoop -> LLM: chat()\nLLM --> AgentLoop: response\nAgentLoop --> TUI: stream\n@enduml",
  "name": "message_flow",
  "title": "Message Flow",
  "fmt": "svg"
}
```

### Mind map
```json
{
  "source": "@startmindmap\n* Project\n** Core\n*** Agent Loop\n*** Config\n** CLI\n*** TUI\n*** Commands\n** Tools\n*** Built-in\n*** MCP\n@endmindmap",
  "name": "project_overview",
  "title": "Project Mind Map",
  "fmt": "svg"
}
```

## Tips

- Always include `@startuml`/`@enduml` (or `@startmindmap`/`@endmindmap`) markers
- Use `!theme plain` for clean, readable diagrams
- Keep diagrams focused — max ~20 elements for readability
- Use `skinparam linetype ortho` for cleaner connection lines
- The tool prefers a local `plantuml` binary but falls back to the public server
