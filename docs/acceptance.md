# 首版验收记录

## 自动验证

- `uv sync --frozen` 可以从锁文件安装依赖。
- `uv run python scripts/site.py check` 通过构建工具测试、内容校验、MkDocs strict 构建、隐私检查和搜索检查。
- 故意缺少标题、系列顺序、内部链接或使用 Obsidian wikilink 的测试内容会被拒绝。
- 生成产物只包含 `public/` 中的页面和公开附件；搜索索引不包含本地隐私哨兵。
- 语义文件路径不含顺序编号，调整 frontmatter `order` 只改变阅读顺序，不改变 URL。

## 浏览器验收

已在本地站点完成以下检查：

- 首页展示知识库目的和 Java 入口，没有博客时间线或空的未来领域。
- 1440 × 900 桌面视口显示左侧领域导航、正文、右侧页内目录和面包屑。
- “面向对象”系列页的上一页为“Java 基础”，下一页为“Java Web”；独立领域页没有虚假上一篇/下一篇。
- 深色/浅色主题可以切换。
- 搜索“面向对象”得到模块、Java 基础和相关主题结果，结果包含页面标题、摘要和标签上下文。
- 390 × 844 手机视口正文可读，主导航折叠到菜单，面包屑、代码复制和下一页入口可访问。

## 历史线上发布记录

2026-08-27 曾完成 GitHub Pages 的首次生产发布、完整作者流程验收，以及从项目站点到用户站点的中间迁移：

- 当时的用户站点仓库：<https://github.com/zaiguihuashuxia/zaiguihuashuxia.github.io>
- 当时的根站点地址：<https://zaiguihuashuxia.github.io/>
- 当时的项目仓库名称：`zaiguihuashuxia/my-personal-website`（现已原地改名为 `zaiguihuashuxia/notes`）
- 首次项目站点发布提交：`f68d0de2ddf33866182c86bea183825fd9bba8fa`
- 用户站点迁移基线提交：`2beffd15190d7a93d20bfd9dfebe515d0c37726a`
- 当前发布工作流：<https://github.com/zaiguihuashuxia/zaiguihuashuxia.github.io/actions/workflows/site.yml>
- GitHub Pages source 已设为 GitHub Actions；重新运行后，`build` 与 `deploy` job 均成功，线上 artifact 来自与本地 `scripts/site.py check` 相同的生产构建目录。
- 首页可访问，并展示知识库目的、Java 入口和分层导航。
- 固定链接 `/programming/java/fundamentals/dev-java-learn/` 可直接打开；页面包含面包屑、左侧模块导航、右侧目录与来源链接。
- 在线搜索 `dev.java` 返回 2 个匹配结果，并能定位固定链接页面及 Java 基础索引中的相关内容。

作者流程已从 Markdown 公开提升、严格本地校验、Git 提交与推送、提交触发的 GitHub Actions 验证，贯通到 GitHub Pages 部署及线上导航/搜索验收。首次 workflow 因 Pages 尚未启用而在 Configure Pages 阶段停止，启用 GitHub Actions source 后重跑成功；这也确认构建失败或平台未就绪时不会执行部署。

## `notes` 迁移验收

- 规范知识仓库：<https://github.com/zaiguihuashuxia/notes>
- 规范知识站点：<https://zaiguihuashuxia.github.io/notes/>
- 改名前保全规划与历史的提交：`ba2a2f2f332b7eec198b0ef5aa2fbeb8859ac9da`
- `mkdocs.yml`、canonical 元数据和 sitemap 必须使用 `/notes/`。
- `/notes/` 的 Actions 部署及代表性页面验收完成前，根用户站点不得替换为个人主页。

2026-08-27 已完成双站分离验收：

- 知识站切换提交：`33018c25a66981396a76e0ac5370a26ab54b03fe`；`Knowledge site` workflow run `33075788540` 的 `build` 与 `deploy` 均成功。
- 根主页切换提交：`62cbbd7f6ef515da3445d67c150c0c1b211999b0`；`Personal homepage` workflow run `33076575015` 的 `deploy` 成功。
- 根地址返回 200，标题为“Wu Qi · 个人主页”，并提供 `/notes/` 与 GitHub 入口。
- `/notes/` 返回 200，标题为“个人知识书库”，代表文章、样式资源和搜索索引均返回 200；浏览器搜索 `dev.java` 返回 2 个匹配结果。
- 根主页 HTML 与知识站 HTML 的 SHA-256 不同，两个工作流分别只上传 `public/` 与 `site/`，部署产物边界独立。
- 已退役的 `/my-personal-website/` Pages 地址在最终验收时返回 404，受控站点和文档不将它作为兼容入口。
- 本地知识站检出的 `origin/main` 指向 `zaiguihuashuxia/notes`；独立主页检出的 `origin/main` 指向 `zaiguihuashuxia/zaiguihuashuxia.github.io`。
- 根站替换前提交 `83b6b52af22fb64c813d646f23946a322838682a` 保留在用户站点历史中；可以通过 revert 恢复，不需要重写历史。
- 后续 OpenSpec 归档应先对 `migrate-github-pages-user-site` 跳过规格同步，再正常归档 `separate-homepage-and-knowledge-site`，避免把“知识库占用根地址”的中间要求合入主规格。
