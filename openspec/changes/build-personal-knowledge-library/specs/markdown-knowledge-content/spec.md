## Purpose

Defines a portable Markdown content contract and a deliberate publication boundary so knowledge can be written in Obsidian, kept maintainable over time, and published without exposing local-only material.

## ADDED Requirements

### Requirement: Portable Markdown source
The system SHALL treat ordinary Markdown files with YAML frontmatter as the canonical public content source, and public articles SHALL remain editable in Obsidian without requiring proprietary Obsidian syntax.

#### Scenario: Edit a public article in Obsidian
- **WHEN** the author opens a public article in Obsidian and edits standard Markdown content
- **THEN** the same source file remains valid input for the website build without a conversion step

### Requirement: Explicit public content boundary
The content model SHALL distinguish publishable content and public assets from private notes, drafts, and private assets, and only material explicitly placed in the public content boundary SHALL be eligible for publication.

#### Scenario: Keep a private note local
- **WHEN** a note or attachment remains outside the public content boundary
- **THEN** it is absent from generated pages, navigation, search data, and deployment artifacts

#### Scenario: Promote a finished note
- **WHEN** the author moves a finished note and its public assets into the public content boundary
- **THEN** the note becomes eligible for validation and publication on the next build

### Requirement: Domain-topic-article hierarchy
The public library SHALL organize knowledge primarily as domains containing topics and articles, while allowing a topic to contain optional course or learning-series groupings.

#### Scenario: Browse a topic
- **WHEN** a reader enters a topic from its domain
- **THEN** the reader can find the topic overview, its published articles, and any published series or curated resources belonging to that topic

### Requirement: Ordered and standalone content
The content model SHALL support both ordered learning series and standalone reference articles without forcing standalone articles into an artificial sequence.

#### Scenario: Publish an ordered series
- **WHEN** published articles declare membership and order within a learning series
- **THEN** the website preserves that reading order independently of file-name sorting

#### Scenario: Publish a standalone reference
- **WHEN** a published article does not belong to an ordered series
- **THEN** it remains navigable and searchable without requiring previous or next article metadata

### Requirement: Minimal content metadata
Every public article SHALL declare a title, MAY declare a description and tags, and SHALL declare an explicit order when it participates in an ordered series. Display order SHALL NOT require numeric prefixes in public URL slugs.

#### Scenario: Validate ordered content metadata
- **WHEN** an article belongs to an ordered series but has no usable order value
- **THEN** validation reports the article as invalid before publication

### Requirement: Technical learning content
Public articles SHALL support headings, links, lists, tables, images, fenced code blocks with syntax highlighting, mathematical notation, and visually distinct note or warning blocks.

#### Scenario: Render a technical article
- **WHEN** a public Markdown article contains code, mathematical notation, a table, an image, and a warning block
- **THEN** the generated article renders each element in a readable form without requiring a runtime backend
