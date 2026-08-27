## Purpose

Defines publication of the public knowledge library through the account-level GitHub Pages URL, with repeatable validation and a safe transition away from the project-site URL.

## ADDED Requirements

### Requirement: Account-root GitHub Pages publication
The public knowledge library SHALL be published from the public repository named `zaiguihuashuxia.github.io` and SHALL be reachable at `https://zaiguihuashuxia.github.io/` without a repository-path prefix.

#### Scenario: Open the user-site root URL
- **WHEN** a reader requests `https://zaiguihuashuxia.github.io/` after a successful deployment
- **THEN** GitHub Pages returns the knowledge library homepage rather than a 404 response

### Requirement: Automated user-site deployment
The user-site repository SHALL validate and build the same public-only static output before deploying it to GitHub Pages whenever an accepted change reaches its publication branch.

#### Scenario: Publish a valid change from the user-site repository
- **WHEN** a valid site change reaches the configured publication branch of `zaiguihuashuxia.github.io`
- **THEN** the workflow deploys the generated site to the account-root URL

#### Scenario: Reject an invalid change
- **WHEN** validation or static-site generation fails in the user-site repository
- **THEN** the deployment does not replace the last successful account-root site

### Requirement: Root-domain navigation compatibility
The deployed account-root site SHALL make its homepage, public static assets, generated search, and documented representative article URLs reachable from `https://zaiguihuashuxia.github.io/`.

#### Scenario: Navigate a representative article from the root-domain site
- **WHEN** a reader opens the homepage and follows a navigation link to a published article
- **THEN** the article and its required static assets load without a `/my-personal-website/` URL prefix

#### Scenario: Search the root-domain site
- **WHEN** a reader uses the generated search interface at the account-root URL
- **THEN** matching published content is returned and can be opened successfully

### Requirement: Preserved source and migration traceability
The migration SHALL preserve the knowledge-library source, publication workflow, and Git history in the user-site repository, while retaining the original `my-personal-website` repository as a non-production migration reference.

#### Scenario: Inspect the migrated user-site repository
- **WHEN** an author clones `zaiguihuashuxia.github.io`
- **THEN** the repository contains the current knowledge-library source, its Pages workflow, and the pre-migration commit history needed to continue publication
