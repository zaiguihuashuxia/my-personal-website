# 技术栈兼容性记录

首版采用以下直接依赖，并由 `uv.lock` 固定完整依赖图：

- Python 3.9+
- MkDocs 1.6.1
- Material for MkDocs 9.7.7
- jieba 0.42.1
- PyYAML 6.0.3

验证范围包括静态构建、Material 导航和面包屑、浅色/深色主题、代码块、数学公式、提示块、浏览器本地搜索以及中英文混合搜索。

`mkdocs-awesome-nav` 当前要求 Python 3.10+，因此首版没有引入它。项目使用 `scripts/site.py` 从公开 Markdown frontmatter 生成导航，并使用 MkDocs hook 配置系列文章的上一篇/下一篇。这减少了依赖，同时保留 Python 3.9 兼容性。

如 Material for MkDocs 的锁定版本无法满足已确认的行为要求，Astro Starlight 才作为回退方案；目前没有发现阻塞项。
