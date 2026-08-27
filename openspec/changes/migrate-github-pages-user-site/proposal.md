## Why

当前知识库由项目仓库 `my-personal-website` 发布，只能通过包含仓库名的项目站点 URL 访问；用户根域 `https://zaiguihuashuxia.github.io/` 返回 404。将站点迁移至 GitHub 用户站点专用仓库可提供预期的根域入口，同时延续现有的自动校验与 Pages 部署流程。

## What Changes

- 新建名为 `zaiguihuashuxia.github.io` 的公开 GitHub 用户站点仓库。
- 将当前 `my-personal-website` 的完整站点源码、GitHub Pages 工作流和版本历史迁移到该仓库，并使本地工作目录跟踪新远程仓库。
- 将 GitHub Pages 的发布入口从项目站点 URL 切换为 `https://zaiguihuashuxia.github.io/`。
- 验证根域首页、站内固定链接、搜索和静态资源均能从新入口正常访问。
- 保留原 `my-personal-website` 仓库作为迁移后的归档/重定向来源，不再将其作为生产 Pages 站点。

## Capabilities

### New Capabilities

- `github-pages-user-site-publication`: 将知识库作为 GitHub 用户站点在账户根域发布，并规定迁移与验收行为。

### Modified Capabilities

- 无。

## Impact

- 受影响系统：GitHub 仓库、GitHub Actions、GitHub Pages 和本地 Git remote。
- 站点构建实现（MkDocs、公开内容边界和 `scripts/site.py`）预期保持不变；现有 `.github/workflows/site.yml` 将在新仓库继续执行。
- 旧项目站点 URL 不再是正式生产入口，任何指向它的外部链接需要后续更新或依赖 GitHub 的仓库重定向。
