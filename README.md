# 个人知识书库

这是一个由标准 Markdown 驱动的静态知识网站。Obsidian 和 iCloud 负责私人写作与同步；只有主动复制到 `public/` 的内容会进入 Git、搜索索引和公开站点。

- 源码仓库：<https://github.com/zaiguihuashuxia/notes>
- 公开站点：<https://zaiguihuashuxia.github.io/notes/>

## 本地运行

需要 Python 3.9+ 和 [uv](https://docs.astral.sh/uv/)：

```bash
uv sync --frozen
uv run python scripts/site.py serve
```

完整检查与生产构建：

```bash
uv run python scripts/site.py check
```

生成的静态产物位于 `site/`，该目录由构建流程生成且不提交 Git。

新增公开笔记时，使用 `templates/` 中的结构作为参考，把确认可以公开的标准 Markdown 和附件放入 `public/`，运行完整检查与本地预览后再提交并推送。`main` 分支的有效提交会由 GitHub Actions 自动部署到公开站点。
