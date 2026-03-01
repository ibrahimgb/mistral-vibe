"""Code Wiki — dual-output documentation generator for Mistral Vibe.

Produces two outputs from a single code-analysis pass:
- **Developer docs**: Rich MkDocs site with embedded PlantUML SVG diagrams
- **LLM docs**: Flat ``llms.txt`` + ``llms-full.txt`` optimised for prompt windows

Public API
----------
>>> from vibe.core.wiki.analyzer import analyze_project
>>> from vibe.core.wiki.site_builder import build_wiki_site
"""

from __future__ import annotations
