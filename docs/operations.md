# 运行、发布与回滚

## 首次准备

```bash
uv sync --frozen
```

## 写作预览

```bash
uv run python scripts/site.py serve
```

本地地址默认为 `http://127.0.0.1:8000/`。预览只读取 `public/`。

## 发布前检查

```bash
uv run python scripts/site.py check
```

该命令依次运行：

1. 构建工具单元测试。
2. frontmatter、系列顺序、普通 Markdown、内部链接和公开附件校验。
3. MkDocs strict 生产构建。
4. 静态产物、系列导航、搜索内容和隐私哨兵检查。

任何一步失败都不会进入部署。

## 自动发布

`.github/workflows/site.yml` 在 pull request 上执行完整检查，在 `main` 分支 push 上额外上传 `site/` 并通过 GitHub Pages 部署。部署 job 依赖 build job，因此验证失败时不会覆盖上一次成功站点。

首次启用时，需要在 GitHub 仓库的 Pages 设置中把 Source 设为 **GitHub Actions**。如果未来改用其他托管平台，只需上传同一个 `site/` 静态目录。

## 添加文章

1. 从私人 Obsidian Vault 中选择已经确认公开的笔记。
2. 按 `docs/authoring.md` 转换为支持的标准 Markdown。
3. 使用 `templates/concept-note.md` 或 `templates/resource-note.md` 作为结构参考。
4. 放入对应的 `public/<领域>/<主题>/` 目录。
5. 运行完整检查与本地预览。
6. 提交并推送到发布分支。

新增普通文章不需要修改 Python 或主题代码；导航由公开目录和 frontmatter 自动生成。

## 回滚

- 内容错误：revert 对应提交并推送，工作流会重新生成上一版本内容。
- 构建工具错误：恢复上一个可用依赖锁和构建脚本后重新运行工作流。
- 紧急情况：在 GitHub Pages 环境中重新运行最后一次成功部署，或把最后一次成功的 `site/` artifact 上传到任意静态托管。
