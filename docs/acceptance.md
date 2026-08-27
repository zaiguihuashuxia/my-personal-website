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

## 线上发布验收

2026-08-27 已完成 GitHub Pages 的首次生产发布和完整作者流程验收：

- 仓库：<https://github.com/zaiguihuashuxia/my-personal-website>
- 生产站点：<https://zaiguihuashuxia.github.io/my-personal-website/>
- 首次发布提交：`f68d0de2ddf33866182c86bea183825fd9bba8fa`
- 验收工作流：<https://github.com/zaiguihuashuxia/my-personal-website/actions/runs/33056160388>
- GitHub Pages source 已设为 GitHub Actions；重新运行后，`build` 与 `deploy` job 均成功，线上 artifact 来自与本地 `scripts/site.py check` 相同的生产构建目录。
- 首页可访问，并展示知识库目的、Java 入口和分层导航。
- 固定链接 `/programming/java/fundamentals/dev-java-learn/` 可直接打开；页面包含面包屑、左侧模块导航、右侧目录与来源链接。
- 在线搜索 `dev.java` 返回 2 个匹配结果，并能定位固定链接页面及 Java 基础索引中的相关内容。

作者流程已从 Markdown 公开提升、严格本地校验、Git 提交与推送、提交触发的 GitHub Actions 验证，贯通到 GitHub Pages 部署及线上导航/搜索验收。首次 workflow 因 Pages 尚未启用而在 Configure Pages 阶段停止，启用 GitHub Actions source 后重跑成功；这也确认构建失败或平台未就绪时不会执行部署。
