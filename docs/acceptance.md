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

## 尚需外部环境确认

GitHub Pages workflow 已实现并在本地检查其构建依赖、artifact 路径和 `deploy.needs: build` 关系。仓库尚未配置可用的 GitHub remote 和 Pages 环境，因此实际远程 workflow/deployment run 需要在连接仓库后确认。
