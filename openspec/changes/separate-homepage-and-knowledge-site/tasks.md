## 1. 建立迁移基线

- [x] 1.1 在当前知识站点检出中运行 `uv run python scripts/site.py check`，检查分支、工作区、远程仓库和两个线上地址；确认本地构建通过，并记录根地址与旧 `/my-personal-website/` 项目地址当前仍发布同一知识站点的基线结果。
- [x] 1.2 将本变更的 OpenSpec 规划文件提交到 `main`，并以非强制推送方式把同一提交同步到 `zaiguihuashuxia/my-personal-website`；确认项目仓库的 `main` 保留既有历史并包含完整规划文件。

## 2. 重命名并恢复知识站点仓库边界

- [x] 2.1 在 GitHub 上将 `zaiguihuashuxia/my-personal-website` 原地重命名为 `zaiguihuashuxia/notes`，不新建空仓库且不重写历史；确认新仓库地址可访问、默认分支仍为 `main`，并验证重命名前的规划提交与既有提交历史完整保留。
- [x] 2.2 调整当前检出的 Git 远程：让 `origin` 指向 `zaiguihuashuxia/notes`，让 `homepage-origin` 指向 `zaiguihuashuxia/zaiguihuashuxia.github.io`，并让本地 `main` 跟踪 `origin/main`；分别验证 fetch URL、push URL 和上游分支，不依赖旧仓库地址的 Git 重定向。
- [x] 2.3 在知识站点中把 MkDocs 生产 `site_url` 设置为 `https://zaiguihuashuxia.github.io/notes/`，同步更新仓库描述、README、相关运维与验收文档中的仓库名和正式地址；运行完整 `uv run python scripts/site.py check`，并确认 canonical 元数据和 sitemap 使用 `/notes/` 地址。
- [ ] 2.4 提交并推送知识站点变更到 `notes`，确认该仓库的 GitHub Actions 构建与 Pages 部署成功；验证 `/notes/`、一个代表性文章地址、静态资源和搜索功能均可正常访问，然后才能开始替换根站点内容。

## 3. 建立独立个人主页

- [ ] 3.1 从用户站点仓库建立或刷新独立的同级检出 `/Users/qiwu/learn/zaiguihuashuxia.github.io`；确认它位于干净的 `main`，且替换前发布知识站点的提交仍可通过历史记录恢复。
- [ ] 3.2 在用户站点仓库中用明确的静态公开目录替换现有知识站点工作树，创建依赖最少的语义化 HTML/CSS 个人主页，包含身份信息、简短介绍、指向 `https://zaiguihuashuxia.github.io/notes/` 的知识库链接和 GitHub 主页链接；验证页面不含 MkDocs 导航内容，并完成键盘操作、移动端布局和基础可访问性检查。
- [ ] 3.3 为用户站点仓库配置只上传个人主页公开目录的专用 Pages 工作流，并移除或替换其中用于知识站点的发布工作流；验证新工作流不会调用 `scripts/site.py`，也不会上传知识站点构建产物。
- [ ] 3.4 以普通提交和非强制推送方式发布个人主页，确认用户站点仓库的 GitHub Actions 构建与 Pages 部署成功，并验证 `https://zaiguihuashuxia.github.io/` 展示个人主页。

## 4. 验证分离结果并交接

- [ ] 4.1 验证根地址与 `/notes/` 项目地址均返回成功状态，且页面标题、主要内容和内容摘要明显不同；确认根主页能够跳转到 `/notes/` 知识库和 GitHub 主页，同时知识库文章、资源和搜索仍然可用。
- [ ] 4.2 确认根主页部署版本来自 `zaiguihuashuxia.github.io` 的提交与工作流，项目知识站点部署版本来自 `notes` 的提交与工作流，并验证任一部署产物都不包含另一个站点的源代码树。
- [ ] 4.3 搜索两个受控仓库的主页内容、MkDocs 配置与生成元数据、README、工作流和运维文档，确认它们不再把 `my-personal-website` 仓库或 `/my-personal-website/` Pages 路径作为正式知识库入口；记录旧 Pages 地址的实际响应，但不依赖 GitHub 对它进行重定向。
- [ ] 4.4 完成运维、远程仓库和回滚说明的最终交接；确认知识站点检出的 `origin`/上游为 `notes`、个人主页同级检出的 `origin` 为用户站点仓库、替换前的根站点提交仍可恢复，且文档清楚区分根个人主页与 `/notes/` 知识库。
- [ ] 4.5 记录后续归档顺序：先在单独授权的归档流程中以跳过规格同步的方式归档已被取代的 `migrate-github-pages-user-site`，再正常归档本变更；验证主规格中没有合入“知识库必须占用根地址”的过时要求。
