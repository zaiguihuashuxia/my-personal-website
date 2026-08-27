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

生成的静态产物位于 `site/`。详细写作和发布方法见 [`docs/authoring.md`](docs/authoring.md) 与 [`docs/operations.md`](docs/operations.md)。
