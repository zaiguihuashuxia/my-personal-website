## Why

The project needs a low-maintenance personal knowledge website that turns selected Markdown notes into a structured, searchable public learning library. The first version should support the author's current Java studies and revision workflow without exposing private Obsidian notes or introducing a dynamic knowledge-management platform.

## What Changes

- Establish a Markdown-first content workflow in which notes are authored in Obsidian, synchronized privately through iCloud, and explicitly promoted into a public content area before publication.
- Create a static documentation-style website with a knowledge-map home page, domain/topic/article hierarchy, section navigation, on-page table of contents, breadcrumbs, full-text search, responsive reading, and light/dark themes.
- Introduce Java as the first content area, covering Java fundamentals, object-oriented programming, Java Web, Spring fundamentals, Spring Boot, and Spring Cloud without claiming textbook-level completeness.
- Support both ordered learning series and standalone reference articles, with module overviews, concept-focused notes, review outlines, self-check questions, and curated learning resources.
- Automate static-site build and deployment after public content is committed, while validating internal links and excluding private notes, drafts, and private assets.
- Use Material for MkDocs as the preferred first-version implementation unless an implementation-time compatibility check identifies a blocker for the confirmed Markdown, navigation, search, or publication requirements.
- Exclude research notes, online editing, accounts, remote private-note access, databases, comments, collaboration, knowledge graphs, executable notebooks, progress tracking, and AI features from the first version.

## Capabilities

### New Capabilities

- `markdown-knowledge-content`: Defines the portable Markdown content model, public/private boundary, content hierarchy, ordered-series support, and supported technical content.
- `knowledge-navigation-and-search`: Defines the public reading experience, knowledge map, hierarchical navigation, article structure, and local full-text discovery.
- `java-review-library`: Defines the first-version Java learning area, its modules, resource curation, concept notes, and revision-oriented content.
- `static-site-publication`: Defines static generation, validation, public-only build input, and automated deployment behavior.

### Modified Capabilities

None.

## Impact

- Introduces the initial static-site project structure, documentation theme configuration, Markdown content directories, and deployment workflow.
- Establishes an Obsidian-compatible authoring convention and a strict boundary between local-only material and publishable content.
- Adds build-time search indexing and internal-link validation, but no runtime server, database, authentication system, or external search service.
- Uses Java content as the first vertical slice while leaving room for later domains such as computing, AI, tools, and life knowledge without implementing those domains in this change.
