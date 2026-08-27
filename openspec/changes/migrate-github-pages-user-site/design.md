## Context

The current public repository is `zaiguihuashuxia/my-personal-website`, whose GitHub Pages deployment succeeds at the project-site URL but cannot satisfy the required account-root URL. The existing GitHub Actions workflow builds a `site/` artifact only after `scripts/site.py check` passes, then deploys it through GitHub Pages. The generated site is not configured with a repository-specific base path, so it is expected to work unchanged when served at the account root.

See `proposal.md` for motivation and `specs/github-pages-user-site-publication/spec.md` for the required observable behavior.

## Goals / Non-Goals

**Goals:**

- Publish the existing knowledge library at the GitHub account root through the dedicated user-site repository.
- Preserve source history and the established validated build-and-deploy workflow.
- Leave a recoverable original repository and make the local checkout point to the new canonical remote after cutover.

**Non-Goals:**

- Redesigning site content, navigation, visual styling, or the MkDocs build pipeline.
- Providing redirects for every previously shared project-site URL beyond GitHub's normal repository redirect behavior.
- Adding a custom domain, DNS configuration, or third-party hosting.

## Decisions

### Create a distinct user-site repository rather than rename the existing repository

Create the public `zaiguihuashuxia.github.io` repository and migrate the existing history and working tree to it. This follows the requested migration model and preserves `my-personal-website` as a non-production reference.

Alternative considered: rename `my-personal-website` to `zaiguihuashuxia.github.io`. That is simpler and also enables a root Pages URL, but it removes the separately retained original repository requested for traceability.

### Preserve Git history while moving the production remote

After creating an empty target repository, push every relevant local branch and tag to it, then change this checkout's `origin` URL to `git@github.com:zaiguihuashuxia/zaiguihuashuxia.github.io.git`. Retain the old URL under a clearly named secondary remote such as `legacy-origin`.

Alternative considered: copy only the current files into a new repository. This would be operationally easy but would lose source history and violate the migration traceability requirement.

### Reuse the existing GitHub Actions Pages workflow

Move `.github/workflows/site.yml` unchanged with the source and use GitHub Pages with the **GitHub Actions** source in the target repository. A push to the target's `main` branch remains the cutover deployment trigger.

Alternative considered: deploy the generated `site/` directory directly to a branch. This would duplicate deployment logic and bypass the existing validation gate.

### Verify deployed URLs instead of assuming base-path compatibility

Use the existing local production check before push, then inspect the successful target workflow and issue HTTP/browser checks against the root homepage, one known article URL, static assets, and generated search after deployment. This confirms that no hidden `/my-personal-website/` prefix remains.

Alternative considered: change MkDocs configuration pre-emptively. No such prefix is currently configured, so changing it without a failing verification result would add unnecessary risk.

## Risks / Trade-offs

- [Target repository is not empty or is created under the wrong account] → Confirm its full name and emptiness before pushing; do not force-push to a non-empty target.
- [Pages source is not set to GitHub Actions] → Configure the target repository's Pages source before triggering or rerun the first deployment.
- [Unnoticed repository-prefixed links break after cutover] → Check generated output and live representative routes before declaring migration complete.
- [DNS/CDN propagation delays make the root URL temporarily unavailable] → Treat a successful deployment and a delayed external response separately; retry verification after GitHub Pages reports completion.
- [Local checkout continues to push to the legacy repository] → Inspect both fetch and push URLs after updating `origin`; keep the old remote under an explicit non-default name.

## Migration Plan

1. Run the existing local validation and confirm the source worktree is clean enough to migrate deliberately.
2. Create the empty, public `zaiguihuashuxia.github.io` repository in the `zaiguihuashuxia` account; confirm its identity before pushing.
3. Push the source history, branches, tags, content, and `.github` workflow to the target repository without deleting the original repository.
4. Configure GitHub Pages in the target repository to use GitHub Actions, then push or dispatch the workflow from `main` to deploy the artifact.
5. Update this checkout's default `origin` remote to the target and retain the old URL as `legacy-origin`.
6. Verify the successful workflow, root homepage, representative article route, static assets, and search. Update documented production URLs if they still name the project-site path.

Rollback: if the target build or root-domain verification fails, stop using the target as production, restore this checkout's `origin` to the legacy remote if it was changed, correct the failing configuration or link, and redeploy only after local validation passes. The original repository remains intact throughout.
