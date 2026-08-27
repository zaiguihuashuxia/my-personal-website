## Context

The account-root and `/my-personal-website/` project-path URLs currently return byte-identical MkDocs output because both repositories publish the knowledge library. The local checkout at `/Users/qiwu/learn/my-personal-website` is logically the knowledge-library working directory, but its default `origin` currently points to `zaiguihuashuxia.github.io`; the project repository that will be renamed from `my-personal-website` to `notes` is retained as `legacy-origin`.

See `proposal.md` for motivation and `specs/personal-homepage-and-knowledge-site-routing/spec.md` for the required final behavior. This design spans two repositories and two independent GitHub Pages deployments.

## Goals / Non-Goals

**Goals:**

- Restore repository identity so this checkout is the canonical knowledge-library checkout.
- Give the knowledge repository the concise, purpose-aligned name `notes` and publish it at `/notes/`.
- Give the account-root repository a small, independently deployable personal homepage.
- Preserve the existing knowledge-library history, validation boundary, search, and project-site deployment.
- Make rollback possible without deleting either repository or rewriting shared history.

**Non-Goals:**

- Moving the knowledge-library source into a subdirectory of the user-site repository.
- Introducing a JavaScript framework, CMS, backend, custom domain, or shared monorepo build.
- Redesigning the MkDocs knowledge-library theme or content architecture.
- Providing elaborate portfolio sections in the first homepage version; the initial page is a focused identity and navigation surface.
- Preserving `https://zaiguihuashuxia.github.io/my-personal-website/` as a compatibility or redirect site after the repository rename.
- Renaming the current local checkout directory as part of the remote repository migration; a later fresh checkout may use `/Users/qiwu/learn/notes`.

## Decisions

### Keep one repository per published site

`zaiguihuashuxia.github.io` will own the account-root personal homepage, while `notes` will own the project-path knowledge library at `/notes/`. GitHub Pages already maps these repository types to the desired URLs, so the knowledge source will not be nested under a `notes/` directory in the user-site repository.

Alternative considered: build both sites from a monorepo and copy the MkDocs output into a subdirectory of one artifact. That requires a coordinated build, creates a second owner for the `/notes/` path unless project Pages is disabled, and couples otherwise independent releases.

### Rename the knowledge repository directly to `notes`

The existing `my-personal-website` repository will be renamed in place to `notes` rather than copied into a newly initialized repository. This keeps its default-branch history and repository metadata together while making the repository name match its role. The canonical Pages address changes to `/notes/`; the old project Pages address is intentionally retired because GitHub does not guarantee redirecting project-site URLs after a repository rename.

Alternative considered: create a new `notes` repository and keep `my-personal-website` as a redirect-only Pages project. That preserves the old site path but leaves an ambiguously named compatibility repository, adds another deployment to maintain, and weakens the two-site boundary the change is intended to establish.

### Restore the current checkout to the knowledge repository

Before changing repository contents or its GitHub name, push the new planning state to `zaiguihuashuxia/my-personal-website`. Rename that GitHub repository to `notes`, then update the current remote relationships so `origin` points to `notes`, `homepage-origin` points to `zaiguihuashuxia.github.io`, and `main` tracks the renamed project repository. Use a separate sibling checkout for homepage work rather than repurposing this directory.

Alternative considered: keep this checkout attached to the user-site repository and create a new knowledge checkout. That conflicts with the directory name and increases the chance of publishing future knowledge changes to the wrong repository.

### Use a dependency-free static homepage

The first personal homepage will use a small explicit public directory containing semantic HTML and CSS. It will identify Wu Qi, provide a short introduction, and link to the knowledge library and GitHub profile. A dedicated Pages workflow will upload only this homepage directory and deploy it to the account root.

Alternative considered: reuse MkDocs or add a frontend framework. Neither is justified for a small personal navigation page, and both would add dependencies and obscure the publication boundary.

### Preserve the knowledge-library build and configure its canonical project URL

The renamed project repository will retain `.github/workflows/site.yml` and `scripts/site.py check`. Its MkDocs configuration will declare `https://zaiguihuashuxia.github.io/notes/` as the production site URL so generated canonical metadata and sitemap locations match the new project path.

Alternative considered: leave the site URL implicit because relative links already work. Explicit configuration reduces ambiguity in generated metadata and documents the restored production location.

### Treat the previous migration as superseded history

The completed `migrate-github-pages-user-site` change records an implemented intermediate state but its unarchived delta requires the knowledge library at the account root. It must not be merged into main specs. After the final two-site behavior is verified, archive that historical change with spec synchronization skipped, then archive this change normally in a separately authorized archive workflow.

## Risks / Trade-offs

- [A commit is pushed to the wrong repository during remote restoration] → Resolve both remote URLs, upstream tracking, and target commit SHAs before every push; keep explicit `origin` and `homepage-origin` names.
- [Replacing the user-site working tree removes knowledge files from its default branch] → Perform the replacement in a separate checkout and commit normally without history rewriting; rollback remains a revert to the last knowledge-site commit.
- [The project-path route temporarily serves stale content] → Deploy and validate the project site before replacing the account-root content, then use cache-bypassing checks against both URLs.
- [Existing links continue to target the retired project Pages URL] → Search homepage content, MkDocs metadata, repository documentation, workflows, and known public references for `my-personal-website`; update all controlled references to `/notes/` and do not claim that GitHub redirects the old Pages URL.
- [The repository rename succeeds but Pages is not yet available at `/notes/`] → Keep the root site unchanged until the renamed repository's workflow completes and representative `/notes/` routes pass acceptance checks.
- [The two sites accidentally share a deployment workflow or artifact] → Give each repository its own workflow and verify each deployment changes only its expected URL.
- [The superseded change introduces conflicting main specs] → Archive it only through an explicit archive operation that skips spec synchronization.
- [The minimal homepage is difficult to use on mobile or with keyboard navigation] → Require semantic links, visible focus styles, readable contrast, and responsive layout checks in acceptance.

## Migration Plan

1. Validate the current knowledge-library build, commit this change's planning artifacts, and push them to `my-personal-website` before changing the remote repository name.
2. Rename `zaiguihuashuxia/my-personal-website` to `zaiguihuashuxia/notes`, update the current checkout's remotes and upstream, and configure the MkDocs production URL as `/notes/`.
3. Deploy the renamed knowledge repository and verify its Actions workflow, homepage, representative article, assets, search, canonical metadata, and sitemap at `/notes/`.
4. Create or refresh a separate sibling checkout of `zaiguihuashuxia.github.io` without deleting or rewriting repository history.
5. Replace the user-site branch's knowledge-library working tree with the minimal homepage public files and its dedicated Pages workflow, link the homepage to `/notes/`, then deploy from `main`.
6. Verify that the root URL presents the personal homepage, `/notes/` presents MkDocs, the retired `/my-personal-website/` URL is not advertised as canonical, and both workflows remain independent.
7. Update operational and acceptance documentation to record both canonical repositories and URLs.

Rollback: before the homepage cutover, rename `notes` back to `my-personal-website` if the new project deployment cannot be made healthy, then restore the previous remote URL and MkDocs site URL. After the homepage cutover, also revert the homepage replacement commit in `zaiguihuashuxia.github.io` or its knowledge link as needed. No rollback rewrites Git history.
