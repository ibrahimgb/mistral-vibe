Build and manage the project Code Wiki — a dual-output documentation system that generates both a rich MkDocs developer site and LLM-optimised flat markdown files.

## How it works

The wiki tool runs a multi-stage pipeline:

1. **Analyse** — AST-parse all Python files, build import graphs, class hierarchies, and subsystem clusters
2. **Extract** — detect design patterns (Protocol/Adapter, Template Method, Factory, Middleware, etc.)
3. **Diagram** — auto-generate PlantUML diagrams (mind maps, component diagrams, class diagrams, sequence diagrams) and render to SVG
4. **Render** — produce two parallel outputs:
   - MkDocs pages with embedded SVG diagrams, cross-references, and YAML frontmatter (for developers)
   - `llms.txt` + `llms-full.txt` with dense symbol→file mappings (for LLMs)

## Actions

- `build` — Run the full pipeline. Generates docs_wiki/ with MkDocs site + llms.txt + llms-full.txt + JSON artefacts
- `analyze` — Run analysis only. Returns project stats (module count, class count, etc.)
- `list_pages` — List all generated wiki pages (requires a prior build)

## When to Use This Tool

**Use proactively when:**
- The user asks for project documentation, code wiki, or architecture overview
- The user wants to understand the project structure or design patterns
- The user asks "generate docs" or "build wiki"
- The user needs LLM-friendly project context (llms.txt)

**Skip this tool for:**
- Writing individual documentation files (use write_file instead)
- Answering questions about specific code (use read_file/grep instead)

## Examples

### Build the full wiki
```json
{
  "action": "build",
  "project_root": ".",
  "output_dir": "docs_wiki"
}
```

### Analyse project without building
```json
{
  "action": "analyze",
  "project_root": "."
}
```

### List generated pages
```json
{
  "action": "list_pages"
}
```

## Output Structure

After `build`, the `docs_wiki/` directory contains:

```
docs_wiki/
├── mkdocs.yml              # MkDocs configuration
├── llms.txt                # LLM short index
├── llms-full.txt           # LLM complete reference
├── symbol_index.json       # symbol → file:line mapping
├── dependency_graph.json   # module import adjacency list
└── docs/
    ├── index.md            # Landing page with architecture overview
    ├── css/custom.css
    ├── diagrams/           # SVG + .puml source files
    ├── subsystems/         # Per-subsystem guides
    ├── architecture/       # Patterns, tech choices, components, data flow
    └── reference/          # Per-module API reference
```
