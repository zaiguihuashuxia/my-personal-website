## Purpose

Defines distinct public responsibilities and stable navigation between the account-level personal homepage and the project-level knowledge library, while allowing each site to be published independently.

## ADDED Requirements

### Requirement: Personal homepage at the account root
The account-level GitHub Pages site SHALL present a personal homepage at `https://zaiguihuashuxia.github.io/` that is visibly distinct from the knowledge-library homepage.

#### Scenario: Open the account-root URL
- **WHEN** a visitor requests `https://zaiguihuashuxia.github.io/`
- **THEN** the response identifies the site owner and presents personal navigation rather than the MkDocs knowledge-library interface

### Requirement: Homepage navigation to public destinations
The personal homepage SHALL provide accessible links to the public knowledge library and the owner's GitHub profile.

#### Scenario: Enter the knowledge library from the homepage
- **WHEN** a visitor activates the knowledge-library entry on the personal homepage
- **THEN** the browser opens `https://zaiguihuashuxia.github.io/notes/`

#### Scenario: Open the owner's GitHub profile
- **WHEN** a visitor activates the GitHub profile entry on the personal homepage
- **THEN** the browser opens `https://github.com/zaiguihuashuxia`

### Requirement: Knowledge library at the project path
The public knowledge library SHALL be published from the `zaiguihuashuxia/notes` project repository at `https://zaiguihuashuxia.github.io/notes/`.

#### Scenario: Open the project-site URL
- **WHEN** a reader requests `https://zaiguihuashuxia.github.io/notes/`
- **THEN** the response presents the MkDocs knowledge-library homepage with its navigation and search experience

#### Scenario: Open an existing knowledge article
- **WHEN** a reader requests a documented article below `/notes/`
- **THEN** the article and its required static assets load without redirecting to the personal homepage

### Requirement: Canonical knowledge-library identity
The published sites, repository metadata, and operational documentation SHALL identify `zaiguihuashuxia/notes` and `https://zaiguihuashuxia.github.io/notes/` as the canonical knowledge-library repository and URL, without depending on the retired project Pages path for redirection.

#### Scenario: Inspect a published or documented knowledge-library link
- **WHEN** a visitor or maintainer follows a knowledge-library link exposed by the homepage, MkDocs metadata, repository documentation, or operational guidance
- **THEN** the link targets `https://zaiguihuashuxia.github.io/notes/` rather than `https://zaiguihuashuxia.github.io/my-personal-website/`

#### Scenario: Complete the repository rename
- **WHEN** the knowledge repository is renamed
- **THEN** its canonical GitHub repository URL is `https://github.com/zaiguihuashuxia/notes` and its existing default-branch history remains available

### Requirement: Independent publication boundaries
The personal homepage and knowledge library SHALL use separate source repositories and publication workflows so that publishing either site does not replace the other site's content.

#### Scenario: Publish a personal-homepage change
- **WHEN** an accepted homepage change is deployed from `zaiguihuashuxia.github.io`
- **THEN** the account-root homepage changes while the project-path knowledge library remains available

#### Scenario: Publish a knowledge-library change
- **WHEN** an accepted knowledge-library change is deployed from `notes`
- **THEN** the project-path knowledge library changes while the account-root personal homepage remains available

### Requirement: Validated knowledge-library deployment
The knowledge-library project repository SHALL continue to validate and build its public-only static output before deploying an accepted change.

#### Scenario: Knowledge-library validation fails
- **WHEN** knowledge content or the production build fails validation
- **THEN** the failed change does not replace the last successful project-path deployment
