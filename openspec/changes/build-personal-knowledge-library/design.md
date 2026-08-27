## Context

The repository currently contains OpenSpec planning configuration but no website implementation or existing knowledge-site architecture. The confirmed authoring environment is Obsidian with iCloud synchronization for local notes; only deliberately selected material is intended for the public site. See `proposal.md` for motivation and the four delta specs for observable behavior.

The first version is a single-author static knowledge library, not an online knowledge-management application. Java is the first vertical slice, while the content model must remain capable of adding unrelated domains such as tools or life knowledge later. The site must favor long-term Markdown portability and low operational maintenance over custom application behavior.

## Goals / Non-Goals

**Goals:**

- Make the public repository a safe, portable publication target for selected standard Markdown notes.
- Deliver a documentation/e-book reading experience with strong hierarchy, local search, technical content rendering, and mobile readability.
- Establish one reusable domain/topic/article structure and validate it with the Java learning and review area.
- Make local preview, validation, and static deployment repeatable with pinned dependencies.
- Keep the publication boundary easy to audit: public source enters the repository and local-only source does not.

**Non-Goals:**

- Synchronize Obsidian or iCloud data, move the repository into iCloud, or provide mobile Git operations.
- Implement online editing, authentication, remote access to private notes, a CMS, or a runtime backend.
- Reproduce D2L's executable notebook toolchain or provide PDF/EPUB generation.
- Create a complete Java textbook or fabricate detailed study notes that the author has not written.
- Pre-create empty taxonomies for future knowledge domains.

## Decisions

### 1. Use Material for MkDocs as the first-version site generator

The implementation will start with Material for MkDocs because its default information architecture matches the requested documentation/e-book experience and it provides navigation, on-page outlines, code rendering, local search, responsive layouts, and light/dark themes with limited custom code. Dependencies will be pinned after confirming that the selected versions support the required Markdown extensions, mixed Chinese/English search, navigation behavior, and strict build validation.

Alternatives considered:

- **Astro Starlight:** more flexible for a highly customized personal site, but the confirmed first version does not need that extra frontend surface area.
- **VitePress:** a viable documentation generator, but it offers no clear first-version advantage over the preferred MkDocs documentation workflow.
- **Quartz:** optimized for Obsidian-specific links and graph-style knowledge gardens, which are not part of the confirmed authoring habits or reading model.
- **Docusaurus or a custom application:** adds framework and maintenance cost without a confirmed need for runtime features.

If the compatibility check finds a blocking defect, Starlight is the fallback. Aesthetic preference alone is not a blocker and will not trigger a stack change.

### 2. Treat the repository as the public publication boundary

The website repository will contain the site configuration, public Markdown, and public assets only. Private notes and drafts remain in the author's iCloud-synchronized Obsidian environment and are promoted by copying or moving finished standard Markdown and approved assets into the repository's public source tree.

The production builder will read from an explicit public source directory rather than scanning an entire Obsidian vault. Ignore rules provide defense in depth, but privacy does not depend solely on frontmatter or navigation visibility. The site does not implement or automate iCloud synchronization.

Alternative considered: keeping private, draft, and public notes in one tracked vault and filtering by `visibility` metadata. This was rejected because a filtering mistake could expose private source through repository history, build artifacts, or search data.

### 3. Use a domain/topic/article content tree

The public content tree will use semantic directory and file slugs:

```text
public/
  index.md
  programming/
    index.md
    java/
      index.md
      fundamentals/
      oop/
      java-web/
      spring/
      spring-boot/
      spring-cloud/
```

Each populated directory has an `index.md` that acts as a curated map rather than an automatically generated file dump. Course and resource material lives inside the relevant topic instead of forming a separate global hierarchy. Future domains reuse the same structure but are added only when they have publishable content.

Numeric prefixes will not be part of public slugs. Ordered learning series declare order through metadata, and the generated navigation uses that declared order. Standalone references omit series metadata and sequence controls.

### 4. Keep frontmatter minimal and validate it

All public articles require `title`. `description` and `tags` are optional. Series membership and `order` are required only for ordered content. Git history or build metadata may supply last-updated information; authors are not required to maintain dates manually in the first version.

The Markdown contract favors standard links, relative public asset paths, fenced code, tables, and YAML frontmatter. A small documented extension set will cover mathematics and note/warning blocks. Obsidian wikilinks, block IDs, transclusion, graph metadata, and other proprietary syntax are outside the contract.

### 5. Curate navigation from content rather than exposing the filesystem directly

The home page lists only populated domains. Domain and topic index pages provide the human-authored learning map. The sidebar reflects the domain/topic/article hierarchy, while ordered-series metadata controls chapter order and previous/next links. The implementation may use a compatible navigation plugin or a generated navigation manifest, selected during the stack compatibility check; it must not require numeric file-name prefixes.

### 6. Build search into the static output

Search will be generated at build time and run in the browser. The initial configuration will enable Chinese and English language handling and will verify queries for Chinese prose, English framework names, and Java identifiers. Only public rendered content feeds the search index; no external indexing service is introduced.

### 7. Use Java as a representative vertical slice, not a completeness promise

The Java area includes six confirmed module entry points: fundamentals, OOP, Java Web, Spring fundamentals, Spring Boot, and Spring Cloud. Spring fundamentals is kept as the conceptual bridge between Java Web and Spring Boot.

Each populated module includes an overview and review outline. The implementation will create the content structure, reusable authoring patterns, and representative seed pages needed to validate the end-to-end experience. Detailed Java prose must come from author-approved notes; unwritten curriculum items are omitted rather than published as empty pages.

### 8. Validate before deploying to static hosting

Local and continuous-integration builds use the same pinned dependency set and fatal-warning policy. Required metadata, internal links, public assets, navigation references, and production generation are validated before deployment. Deployment runs only after validation succeeds and preserves the last successful site on failure.

GitHub Actions with GitHub Pages is the preferred default because it fits the Git-driven static workflow. The generated site remains provider-neutral so another static host can be selected without changing content or specifications.

## Risks / Trade-offs

- **[Risk] Mixed Chinese/English search may rank or tokenize some Java terms poorly** -> Add representative Chinese, English, and identifier search cases during implementation and tune supported language/tokenization settings without adding a hosted search service.
- **[Risk] MkDocs and navigation plugins can introduce compatibility or maintenance issues** -> Pin the smallest viable dependency set, verify it before content migration, and fall back to explicit generated navigation or Starlight only for a documented blocker.
- **[Risk] Obsidian rendering may differ from the website** -> Document the supported Markdown subset and include representative rendering fixtures for links, images, code, math, and callouts.
- **[Risk] A private attachment could be copied with a public note** -> Require an explicit public asset location, validate referenced assets, and review the generated artifact boundary in automated tests.
- **[Risk] Topic hierarchies may grow too deeply as new domains appear** -> Keep domain/topic/article as the default depth and use curated index pages or optional series instead of adding global classification dimensions.
- **[Trade-off] Manual promotion from the iCloud vault adds one publishing step** -> Accept the explicit step because it creates an auditable privacy boundary and avoids synchronizing the whole private vault with the site repository.
- **[Trade-off] Representative Java seed content will not be a complete reference** -> Display only finished content and let the library grow through normal study rather than publishing empty promises.

## Migration Plan

1. Confirm the Material for MkDocs dependency set and required feature compatibility before building content structure.
2. Scaffold the public-only site source, supported Markdown conventions, and local preview/validation commands.
3. Add the knowledge-map home page and Java domain/topic/module indexes with representative content and review flow.
4. Validate privacy boundaries, navigation, rendering, search, links, and mobile layouts locally and in continuous integration.
5. Deploy to a preview or project URL, verify the generated artifact contains only approved public material, and then enable publication from the configured branch.

There is no existing production site to migrate. Rollback consists of redeploying the last successful static artifact or reverting the publication commit.

## Open Questions

- **Site title, visual branding, and custom domain:** defer until implementation review; use a neutral working title and default theme customization initially.
- **Final hosting provider:** default to GitHub Pages, while keeping the static output portable if repository or domain constraints favor another provider.
- **Initial Java note volume:** create the six module entry points and representative revision flow, then include only author-approved notes available during implementation; do not invent a complete curriculum.
