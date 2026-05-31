# Tasks

- [x] Task 1: 新增数据库模型 — TranslationPublication 和 UserTranslationJob
  - [x] 1.1: 在 models.py 中新增 TranslationPublication 模型（book_id, lecture_id, scope, status, first_contributor_user_id, published_at, error_message, created_at, updated_at），user_id 使用 String(36) 兼容 UUID
  - [x] 1.2: 在 models.py 中新增 UserTranslationJob 模型（user_id String(36), book_id, lecture_id, mode, status, total_sentences, completed_sentences, error_message, created_at, updated_at）
  - [x] 1.3: 扩展 Contribution 模型，新增 book_id(Integer), cost(Integer, default=0), grants_download(Boolean, default=False) 字段
  - [x] 1.4: 确保后端启动时 create_all 能创建新表

- [x] Task 2: 新增 content_access 服务
  - [x] 2.1: 创建 backend/app/services/content_access.py
  - [x] 2.2: 实现 get_publication_for_lecture(db, book_id, lecture_id) — 查询 published 状态的 publication
  - [x] 2.3: 实现 ensure_translation_publication(db, book_id, lecture_id, user_id, status) — 创建或更新 publication
  - [x] 2.4: 实现 publish_lecture_translation(db, book_id, lecture_id) — 将 status 更新为 published
  - [x] 2.5: 实现 add_contribution(db, user_id, book_id, lecture_id, contribution_type, cost, grants_download) — 写贡献记录
  - [x] 2.6: 实现 can_download_lecture(db, user_id, book_id, lecture_id) — 检查下载权限
  - [x] 2.7: 实现 get_contributors(db, book_id, lecture_id) — 获取贡献者列表
  - [x] 2.8: 实现 get_lecture_book_id(db, lecture_id) — 获取讲座所属书籍 ID

- [x] Task 3: 重构 translate.py — 翻译任务持久化
  - [x] 3.1: 移除 _running_tasks 和 _running_task_tokens 内存变量
  - [x] 3.2: 重构 translate_lecture 端点：使用 translation_publications 检查状态，使用 user_translation_jobs 创建任务
  - [x] 3.3: 重构 translation-status 端点：优先从 user_translation_jobs 读取进度，增加 status/mode/translation_published/is_running 字段
  - [x] 3.4: 重构 translation-cost 端点：增加 translation_published/download_cost/translated_in_database 等字段
  - [x] 3.5: 重构 _do_translate_lecture 后台任务：从数据库读取 job，更新 job 进度，完成后 publish
  - [x] 3.6: 实现后端模拟翻译 _simulate_existing_translation：更新 user_translation_jobs 进度
  - [x] 3.7: 新增 purchase-download 端点
  - [x] 3.8: 新增 download-pdf 端点（reportlab 生成德中对照 PDF）
  - [x] 3.9: 新增 PUT /sentences/{id}/translation 和 PUT /sentences/{id}/source 端点
  - [x] 3.10: 新增孤儿任务检测：translation-status 中检查 running 超过 30 分钟的任务标记为 failed

- [x] Task 4: 修改 lectures.py — 翻译可见性由 publication 表控制
  - [x] 4.1: get_lecture_paragraphs 中使用 get_publication_for_lecture 替代 Lecture.is_published 判断
  - [x] 4.2: get_lecture_simple 中返回 translation_published, first_contributor, contributors, can_download_pdf, can_edit, download_notice 字段
  - [x] 4.3: 保留 is_published 字段兼容，但主要逻辑切换到 publication 表

- [x] Task 5: 前端 API 层适配
  - [x] 5.1: 更新 TranslationStatus 接口：增加 status, mode, translation_published 字段
  - [x] 5.2: 更新 TranslationCost 接口：增加 translation_published, download_cost 等字段
  - [x] 5.3: 更新 Lecture 接口：增加 translation_published, first_contributor, contributors, can_download_pdf, can_edit, download_notice
  - [x] 5.4: 新增 Contributor 接口
  - [x] 5.5: 新增 MutationResult 接口
  - [x] 5.6: 新增 purchaseLectureDownload, downloadLecturePdf, editSentenceTranslation, editSentenceSource 函数
  - [x] 5.7: 更新 getTranslationStatus 使用 authFetch

- [x] Task 6: 前端阅读页适配
  - [x] 6.1: is_published → translation_published 适配
  - [x] 6.2: 移除前端 simulateProgress，改为纯轮询后端 translation-status
  - [x] 6.3: 新增贡献者展示区域
  - [x] 6.4: 新增下载区域（有权限显示下载按钮+提醒，无权限显示购买按钮）
  - [x] 6.5: 新增句子编辑功能（改译/改原按钮，编辑弹窗，确认扣点）
  - [x] 6.6: 翻译进度条由后端数据驱动

- [x] Task 7: 数据迁移与部署
  - [x] 7.1: 编写迁移脚本：将现有 lecture_access 中 translate 类型的记录同步到 translation_publications
  - [x] 7.2: 将现有 is_published=true 的讲座同步到 translation_publications
  - [x] 7.3: 在生产服务器执行迁移
  - [x] 7.4: 构建前端并部署
  - [x] 7.5: 重启后端服务
  - [x] 7.6: 验证功能正常

# Task Dependencies
- Task 2 depends on Task 1
- Task 3 depends on Task 1, Task 2
- Task 4 depends on Task 2
- Task 5 depends on Task 3, Task 4
- Task 6 depends on Task 5
- Task 7 depends on Task 6
