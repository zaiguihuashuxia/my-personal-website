## Purpose

Defines a reliable public-only static publication pipeline that can be hosted inexpensively, requires no application backend, and prevents invalid or local-only content from being deployed.

## ADDED Requirements

### Requirement: Static deployable output
The publication process SHALL generate a self-contained static website that can be served by a standard static hosting provider without a database, application server, authentication service, or runtime content API.

#### Scenario: Serve a production build
- **WHEN** a successful production build is deployed to static hosting
- **THEN** readers can navigate articles, use the generated search experience, and load public assets without a running application backend

### Requirement: Public-only build input
Production builds SHALL use an explicit allowlisted public content and asset boundary and SHALL NOT copy private notes, drafts, private assets, or unrelated Obsidian vault files into generated output.

#### Scenario: Build beside local-only notes
- **WHEN** private notes and drafts exist in the author's local Obsidian environment during a production build
- **THEN** no content, metadata, file name, or search token from those notes appears in the build artifacts

### Requirement: Build validation gate
The publication process SHALL fail before deployment when public content contains invalid required metadata, unresolved internal links, missing public assets, or another configured fatal documentation warning.

#### Scenario: Broken internal article link
- **WHEN** a public article links to a missing internal page
- **THEN** the production build fails with a diagnostic that identifies the source article and broken reference

#### Scenario: Valid public content
- **WHEN** all public content and assets satisfy validation
- **THEN** the build produces deployable static output and permits the deployment stage to continue

### Requirement: Automated publication
The project SHALL provide a repeatable automated workflow that validates, builds, and deploys the public site after accepted changes reach the configured publication branch.

#### Scenario: Publish an accepted content change
- **WHEN** a valid public Markdown change reaches the publication branch
- **THEN** the workflow builds and deploys the corresponding static site without requiring manual file upload

#### Scenario: Prevent deployment after failure
- **WHEN** validation or site generation fails
- **THEN** the workflow reports failure and does not replace the last successful deployment

### Requirement: Reproducible local preview
The author SHALL be able to run a documented local preview and production validation using pinned project dependencies before publishing.

#### Scenario: Preview an article before commit
- **WHEN** the author runs the documented local preview with the supported environment
- **THEN** the author can inspect the public site's rendered content and navigation using the same content rules as production
