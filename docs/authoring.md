# Obsidian 写作与公开流程

## 边界

私人笔记和草稿继续保存在 iCloud 同步的 Obsidian Vault 中。网站仓库不是整个 Vault 的镜像；只有主动放进 `public/` 的 Markdown 和附件才会进入 Git、构建产物和搜索索引。

推荐流程：

1. 在私人 Vault 中学习和记录。
2. 整理为可以公开的独立笔记，并删除隐私信息。
3. 把 Markdown 复制到 `public/<领域>/<主题>/`。
4. 把它引用的公开附件复制到 `public/assets/` 或相邻公开目录。
5. 将 Obsidian 内部链接改为普通 Markdown 相对链接。
6. 运行 `uv run python scripts/site.py check`。
7. 本地预览确认后再提交 Git。

## 支持的 Markdown

- YAML frontmatter
- 标题、列表、链接、表格和图片
- fenced code block
- 数学公式
- Material admonition，例如 `!!! note`

首版明确不支持：

- `[[Obsidian wikilink]]`
- `![[Obsidian transclusion]]`
- `^block-id`
- 依赖 Obsidian 图谱的元数据
- 从 `private-assets/` 直接引用附件

每篇公开文章必须提供 `title`。只有加入有序系列时才需要同时提供 `series` 和整数 `order`；文件名使用稳定的语义 slug，不添加顺序编号。
