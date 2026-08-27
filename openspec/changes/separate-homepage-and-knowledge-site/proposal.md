## Why

当前用户站点根路径和项目站点路径都发布同一套知识库，无法区分个人主页与知识笔记入口；同时，`my-personal-website` 容易被理解为根个人主页仓库，与其实际承载的笔记和知识内容不符。将两类站点恢复为 GitHub Pages 原生的用户站点和项目站点结构，并把知识仓库改名为 `notes`，可以让根路径承担个人介绍与导航职责，让知识库在语义清晰、简短稳定的 `/notes/` 路径独立演进。

## What Changes

- **BREAKING** 将 `https://zaiguihuashuxia.github.io/` 的内容从知识库首页替换为独立个人主页。
- **BREAKING** 将知识仓库从 `zaiguihuashuxia/my-personal-website` 重命名为 `zaiguihuashuxia/notes`，并把 MkDocs 生产地址改为 `https://zaiguihuashuxia.github.io/notes/`；旧项目 Pages 地址不作为重定向或兼容入口继续维护。
- 恢复重命名后的 `zaiguihuashuxia/notes` 作为知识库的规范源码仓库和生产发布源。
- 保留 `zaiguihuashuxia/zaiguihuashuxia.github.io` 作为个人主页仓库，只发布个人介绍和站点入口，不在其中嵌套知识库源码目录。
- 在个人主页提供指向 `/notes/` 的清晰知识库入口，并链接到 GitHub 个人资料。
- 为两个仓库分别保留独立的构建、部署和本地工作目录，避免一次发布覆盖另一个站点。
- 将已完成但尚未归档的 `migrate-github-pages-user-site` 视为被本 change 取代的历史迁移；其“知识库占用根路径”delta 不应合并进主规格。

## Capabilities

### New Capabilities

- `personal-homepage-and-knowledge-site-routing`: 定义个人主页与知识库在两个 GitHub Pages 站点之间的职责、URL 和导航关系。

### Modified Capabilities

- 无。当前 `openspec/specs/` 中尚无已归档的相关 capability；本 change 通过新的最终状态 capability 取代未归档的旧迁移 delta。

## Impact

- 受影响系统：知识仓库名称、两个 GitHub 仓库、两个 GitHub Pages 发布源、本地 Git remote 与本地 checkout 布局。
- 知识库的 MkDocs 内容、公开内容边界、搜索和校验逻辑预期保持不变，但其正式 URL 改为 `https://zaiguihuashuxia.github.io/notes/`。
- 旧 `https://zaiguihuashuxia.github.io/my-personal-website/` 项目 Pages 地址不会被视为自动重定向入口；主页链接、站点元数据、文档和已知内部引用需要迁移到新地址。
- 用户站点仓库需要独立的轻量个人主页和发布流程。
- 旧迁移 change 需要在后续归档时使用跳过规格合并的历史归档方式，避免产生与本 change 冲突的主规格。
