## 1. Pre-migration checks

- [x] 1.1 Run `uv run python scripts/site.py check` from the current checkout and verify the production build completes before any remote migration.
- [x] 1.2 Inspect `git status`, the current `origin` fetch/push URLs, and the target repository name; verify that `zaiguihuashuxia/zaiguihuashuxia.github.io` is an empty public repository and that `my-personal-website` remains available as the legacy source.
- [x] 1.3 Search the generated site and published-content configuration for `/my-personal-website/` URLs; record any explicit links that require updating after cutover and verify the current deployment workflow remains present.

## 2. Repository migration

- [x] 2.1 Create the public GitHub repository `zaiguihuashuxia/zaiguihuashuxia.github.io` without initializing conflicting content, and verify its full name and default branch.
- [ ] 2.2 Push the knowledge-library history, relevant branches, tags, source files, and `.github/workflows/site.yml` to the new repository; verify that the target `main` commit matches the legacy repository's migration commit.
- [ ] 2.3 Rename the current checkout's old `origin` remote to `legacy-origin` and configure `origin` to the new user-site repository; verify both fetch and push URLs and confirm no default push targets the legacy repository.

## 3. User-site deployment

- [ ] 3.1 Set the target repository's GitHub Pages source to GitHub Actions and trigger the `main` deployment; verify the build and deploy jobs complete successfully.
- [ ] 3.2 Confirm the deployment reports `https://zaiguihuashuxia.github.io/` as its Pages URL and verify the root request returns the knowledge-library homepage rather than 404.

## 4. Post-cutover validation and documentation

- [ ] 4.1 Verify from the root-domain deployment that a representative article, its static assets, and generated search open successfully with no `/my-personal-website/` prefix.
- [ ] 4.2 Update repository-facing operational and acceptance documentation to identify the root-domain URL and new canonical repository; verify no production instructions still direct authors to the legacy repository.
- [ ] 4.3 Retain `my-personal-website` as a non-production reference, review the final remote configuration and public URLs, and verify the migration rollback information remains usable.
