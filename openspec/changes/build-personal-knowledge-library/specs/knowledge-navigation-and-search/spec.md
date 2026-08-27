## Purpose

Defines how readers discover, navigate, search, and read the public knowledge library across structured learning material and independent reference notes.

## ADDED Requirements

### Requirement: Knowledge-map home page
The website SHALL provide a home page that explains the library and presents entry points to published knowledge domains and highlighted learning areas, rather than a reverse-chronological blog feed.

#### Scenario: Enter the library
- **WHEN** a reader opens the home page
- **THEN** the reader can understand the site's purpose and navigate directly to the currently published domains and featured topics

### Requirement: Hierarchical navigation context
Every published article SHALL expose its location through domain/topic navigation and breadcrumbs, and article headings SHALL be available through an on-page table of contents when the article contains multiple sections.

#### Scenario: Read a nested Java article
- **WHEN** a reader opens an article nested under the Java topic
- **THEN** the page shows its domain and topic context, the surrounding section navigation, and links to its visible headings

### Requirement: Ordered-series navigation
Articles in an ordered learning series SHALL expose previous and next navigation according to the declared series order, while standalone articles SHALL omit misleading sequence controls.

#### Scenario: Move through a learning series
- **WHEN** a reader reaches an interior article in an ordered series
- **THEN** the page links to the immediately preceding and following published articles in that series

#### Scenario: Read a standalone article
- **WHEN** a reader opens a standalone reference article
- **THEN** the page does not present unrelated articles as previous or next chapters

### Requirement: Local full-text search
The website SHALL provide search without a runtime search service and SHALL index the titles, descriptions, headings, prose, and relevant code text of published articles. Search SHALL support mixed Chinese, English, and technical identifiers used by the library.

#### Scenario: Search mixed-language knowledge
- **WHEN** a reader searches for a Chinese term, an English framework name, or a technical identifier that appears in published content
- **THEN** matching public articles are returned with enough title and location context to identify the result

#### Scenario: Search excludes local-only material
- **WHEN** a search term occurs only in a private note or draft
- **THEN** the public search returns no result derived from that material

### Requirement: Responsive and theme-aware reading
The public website SHALL remain readable and navigable on desktop and mobile viewports and SHALL provide light and dark visual themes.

#### Scenario: Read on a phone
- **WHEN** a reader opens an article on a narrow mobile viewport
- **THEN** the article remains readable and the navigation and table of contents remain accessible without covering the main content permanently

### Requirement: No empty future taxonomy
Navigation and the home-page knowledge map SHALL expose only published domains, topics, series, and articles, even though the content model permits future domains.

#### Scenario: Future domain has no published content
- **WHEN** a planned domain contains no public material
- **THEN** the public website does not display an empty navigation entry for that domain
