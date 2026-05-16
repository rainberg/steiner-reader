# .docx 导入流程

基于 GA083 和 GA074 的 .docx 导入经验提炼的通用工具。

## 脚本说明

### 主导入脚本（每本书一份）

| 脚本 | 用途 |
|------|------|
| `import_ga083.py` | GA083 导入（10讲+前言） |
| `import_ga074.py` | GA074 导入（3讲+附录） |

新书导入时，复制最近的脚本，修改以下配置即可：
- `BOOK_ID` — 数据库中的 book.id
- `DOCX_PATH` — .docx 文件路径
- `LECTURE_TITLES` — 标题映射（VORTRAG key → (title_de, title_zh)）
- `HEADER_KEYS` — 标题关键字列表
- `SUBTITLE_PREFIXES` — 副标题前缀（用于识别标题块中的副标题行）

### 正文合并脚本

| 脚本 | 用途 |
|------|------|
| `merge_headers.py` | 只合并标题块（标题 + 副标题 + 日期 → 多行段落） |
| `merge_paragraphs.py` | 两阶段合并：先合标题块，再合并正文（跳过标题） |

### 翻译恢复脚本

| 脚本 | 用途 |
|------|------|
| `restore_translations_pass1.py` | 三遍匹配：精确匹配 → 去连字符匹配 → 前缀匹配 |
| `restore_translations_substring.py` | 子串匹配（用于前3遍之后的补充） |

## .docx 导入关键教训

1. **标题变音** — "FÜNFTER"（带 umlaut）≠ "FUNFTER"（不带 umlaut），HEADER_KEYS 必须用正确拼写
2. **副标题前缀** — 用最短可区分前缀，如 "DIE ZEIT UND IHRE SOZIAL" 比 "DIE ZEIT UND IHRE SOZIALEN" 更通用
3. **副标题和日期常在同一行** — `extract_date_from_subtitle()` 处理此情况
4. **正文合并必须在分句之前** — 先合并段落，再切分句子
5. **标题块不参与分句** — `is_header_ordinal()` 判断是否标题，跳过标题段落的分句
6. **翻译恢复需要多遍匹配** — 旧导入的句子边界与新导入不同，需要精确+模糊+前缀+子串四种匹配
7. **翻译恢复用 CSV** — 从旧备份导出翻译到 CSV（Python csv 模块），导入时加载匹配，避免数据库跨库查询

## 完整工作流程

```
1. 复制最近的 import_gaXXX.py → import_gaNEW.py
2. 修改 BOOK_ID, DOCX_PATH, LECTURE_TITLES 等配置
3. 从备份导出翻译: export_trans.py → CSV
4. 运行导入: python3 import_gaNEW.py
5. 运行翻译恢复: python3 restore_translations_pass1.py; python3 restore_translations_substring.py
6. 更新标题翻译: 应用 translation_fixes 替换规则
7. 验证: 检查标题块结构、翻译覆盖率
```
