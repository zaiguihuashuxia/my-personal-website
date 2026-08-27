## 1. Foundation and Stack Verification

- [x] 1.1 Verify the current Material for MkDocs stack against required navigation, mixed Chinese/English local search, Markdown extensions, strict validation, and static deployment; record the pinned dependency set and confirm no blocking requirement needs the documented Starlight fallback.
- [x] 1.2 Scaffold the static-site configuration and explicit public source directory, and verify a clean environment can install pinned dependencies and produce a minimal successful build.
- [x] 1.3 Define repository ignore rules and an allowlisted public content/asset boundary, and verify private, draft, Obsidian configuration, and private-asset fixtures do not appear in generated output.
- [x] 1.4 Add documented local preview and production-validation commands, and verify both commands run from a fresh supported environment using the pinned dependencies.

## 2. Markdown Content Contract

- [x] 2.1 Configure the supported standard Markdown, code highlighting, tables, relative images, mathematical notation, and note/warning blocks, and verify a representative fixture renders correctly in the generated site.
- [x] 2.2 Implement validation for required titles and conditional series/order metadata, and verify valid standalone and ordered articles pass while an ordered article without usable order fails.
- [x] 2.3 Preserve semantic URL slugs independently of display order, and verify changing series order does not change an article's public URL.
- [x] 2.4 Configure fatal validation for unresolved internal links and missing public assets, and verify diagnostics identify the source Markdown file and invalid reference.
- [x] 2.5 Document the Obsidian-compatible authoring subset and manual promotion flow from the private iCloud vault to public source, and verify the guide explicitly excludes wikilinks, transclusion, block IDs, and private-asset copying from the supported workflow.

## 3. Knowledge Navigation and Reading Experience

- [x] 3.1 Create the knowledge-map home page and populated-domain discovery model, and verify the home page presents the site's purpose and Java entry point without empty future-domain links or a blog-style chronology.
- [x] 3.2 Implement domain/topic/article navigation with curated index pages, breadcrumbs, sidebar context, and on-page heading outlines, and verify a nested Java article exposes all required navigation context.
- [x] 3.3 Implement ordered-series previous/next links from declared series order, and verify an interior series article receives correct neighbors while a standalone article receives no artificial sequence controls.
- [x] 3.4 Configure light and dark themes and responsive navigation behavior, and verify representative home, topic, and article pages remain readable and navigable at desktop and narrow mobile viewport sizes.

## 4. Local Search

- [x] 4.1 Configure build-time, browser-local search over public titles, descriptions, headings, prose, and relevant code text, and verify representative Chinese terms, English framework names, and Java identifiers return the expected articles.
- [x] 4.2 Verify search result entries provide enough title and hierarchy context to distinguish matches from different modules.
- [x] 4.3 Add a privacy regression check for generated search data, and verify terms that exist only in local-only test fixtures never appear in search indexes or search results.

## 5. Java Revision Library

- [x] 5.1 Create the Java topic home page with the confirmed progression through fundamentals, OOP, Java Web, Spring fundamentals, Spring Boot, and Spring Cloud, and verify all six module entry points are navigable and Spring fundamentals bridges Java Web and Spring Boot.
- [x] 5.2 Create meaningful overview pages for the six Java modules with learning purpose, core-concept map, available public articles, and recommended review order, and verify no overview links to an unavailable article as completed content.
- [x] 5.3 Add a reusable curated-resource pattern covering source link, suitable stage, prerequisites, rationale, and related local notes, and verify at least one author-approved Java resource demonstrates every field that applies.
- [x] 5.4 Add a reusable concept-article pattern for concise conclusion, explanation, minimal example, common pitfalls, self-check questions, and related links, and verify it renders correctly using an author-approved Java note or a non-production validation fixture.
- [x] 5.5 Inventory Java Markdown notes the author approves for publication, migrate only those notes into the matching modules, and verify every migrated page meets metadata, link, asset, and supported-syntax validation.
- [x] 5.6 Add a review outline to every Java module populated with approved concept articles, and verify each outline links its key terms, comparisons, mistakes, and self-check questions back to available detail pages.

## 6. Continuous Integration and Publication

- [x] 6.1 Add continuous integration that installs pinned dependencies and runs metadata, link, asset, privacy-boundary, search, and production-build checks, and verify an intentionally broken fixture prevents the workflow from reaching deployment.
- [x] 6.2 Add the preferred GitHub Pages deployment workflow while keeping the generated static directory provider-neutral, and verify a successful publication-branch run deploys the same artifact produced by local production validation.
- [x] 6.3 Ensure failed validation or generation cannot replace the last successful site, and verify the deployment job is skipped when its validation dependency fails.
- [x] 6.4 Inspect the final static artifact for allowed source, asset, and search content, and verify it contains no private paths, draft names, Obsidian workspace data, or local-only test tokens.

## 7. End-to-End Acceptance and Handoff

- [x] 7.1 Run the complete author flow from promoting a standard Markdown note through local preview, commit-triggered validation, and static deployment, and verify the published page is navigable and searchable at its stable URL.
- [x] 7.2 Run the reader flow across the home knowledge map, Java module navigation, ordered and standalone pages, review links, search, themes, and mobile layout, and record that every scenario in the four delta specs passes.
- [x] 7.3 Document ongoing content addition, public-asset handling, local preview, validation, publication, and rollback, and verify a new article can be added by following the documentation without editing application code.
