# 翻译公开与贡献体系 Spec

## Why

当前生产环境使用 `Lecture.is_published` 布尔字段和 `lecture_access` 表控制翻译可见性，存在三个核心问题：
1. `is_published` 无法表达"翻译中"和"翻译失败"状态，导致孤儿任务无法被检测
2. `_running_tasks` 内存变量重启后丢失，翻译任务变成孤儿
3. 缺少贡献者记录和下载权限管理，无法实现设计文档要求的贡献展示和 PDF 下载权益

## What Changes

- 新增 `translation_publications` 表，替代 `Lecture.is_published` 布尔字段，支持 translating/published/failed 三态
- 新增 `user_translation_jobs` 表，替代 `_running_tasks` 内存变量，翻译任务持久化
- 扩展 `contributions` 表，增加 `book_id`、`cost`、`grants_download` 字段
- 后端 `translate.py` 重构：翻译任务由数据库驱动，模拟翻译由后端推进进度
- 后端 `lectures.py` 修改：翻译可见性由 `translation_publications` 表判断
- 前端阅读页适配新字段：`translation_published` 替代 `is_published`，贡献者展示，下载区域
- 新增 `purchase-download` 和 `download-pdf` 接口
- 新增句子修订接口

## Impact

- Affected code:
  - `backend/app/db/models.py` — 新增 2 个模型，修改 1 个模型
  - `backend/app/routers/translate.py` — 重构
  - `backend/app/routers/lectures.py` — 修改可见性逻辑
  - `backend/app/services/content_access.py` — 新增
  - `backend/app/services/credit_service.py` — 修改
  - `frontend/lib/api.ts` — 新增接口和类型
  - `frontend/app/books/[bookId]/lectures/[lectureId]/page.tsx` — 适配新字段

## ADDED Requirements

### Requirement: 翻译公开状态管理

系统 SHALL 使用 `translation_publications` 表管理翻译公开状态，支持 translating/published/failed 三态。

#### Scenario: 用户贡献点数翻译
- **WHEN** 用户点击"贡献点数翻译本讲"
- **THEN** 系统创建 `translation_publications` 记录（status=translating），创建 `user_translation_jobs` 记录（status=running），扣减点数，记录贡献

#### Scenario: 翻译完成
- **WHEN** 翻译任务（模拟或网络）完成
- **THEN** `translation_publications.status` 更新为 published，`user_translation_jobs.status` 更新为 completed

#### Scenario: 翻译失败
- **WHEN** 翻译任务失败
- **THEN** `translation_publications.status` 更新为 failed，`user_translation_jobs.status` 更新为 failed，保留错误信息

### Requirement: 翻译任务持久化

系统 SHALL 将翻译任务存储在 `user_translation_jobs` 表中，而非内存变量。

#### Scenario: 后端重启后恢复任务状态
- **WHEN** 后端重启
- **THEN** 前端轮询 `translation-status` 时，从数据库读取任务状态，`is_running` 字段基于 `user_translation_jobs.status=running` 判断

#### Scenario: 孤儿任务检测
- **WHEN** 存在 status=running 的任务但超过 30 分钟无进度更新
- **THEN** 系统将任务标记为 failed

### Requirement: 翻译可见性由 publication 表控制

系统 SHALL 根据 `translation_publications` 表判断翻译是否可见，而非 `Lecture.is_published` 字段。

#### Scenario: 未公开讲座
- **WHEN** 讲座没有 published 状态的 publication 记录
- **THEN** 后端返回段落时将所有 `text_zh` 置为 null，前端显示"贡献点数翻译本讲"

#### Scenario: 已公开讲座
- **WHEN** 讲座有 published 状态的 publication 记录
- **THEN** 所有用户可阅读中文译文，无需付费

### Requirement: 贡献者记录与展示

系统 SHALL 记录并展示翻译贡献者。

#### Scenario: 首次贡献者
- **WHEN** 用户首次贡献点数翻译某讲
- **THEN** `translation_publications.first_contributor_user_id` 记录该用户，前端展示"本讲翻译由 XXX 贡献点数解锁"

#### Scenario: 贡献者列表
- **WHEN** 讲座已公开
- **THEN** 前端展示所有贡献者（翻译、修订、下载购买）

### Requirement: PDF 下载权限

系统 SHALL 基于贡献记录判断下载权限。

#### Scenario: 翻译贡献者下载
- **WHEN** 用户对该讲有 grants_download=true 的贡献记录
- **THEN** 用户可下载 PDF

#### Scenario: 购买下载权限
- **WHEN** 用户消费点数购买下载权限
- **THEN** 创建 grants_download=true 的贡献记录，用户可下载 PDF

#### Scenario: 无权限用户
- **WHEN** 用户没有下载权限
- **THEN** 显示"消耗 X 点下载 PDF"按钮

### Requirement: 句子修订

系统 SHALL 支持用户消费点数修改译文或原文。

#### Scenario: 修改译文
- **WHEN** 用户修改一句中文译文并确认
- **THEN** 扣减点数，更新句子文本，写入修订记录和贡献记录，授予下载权限

#### Scenario: 无变化不扣点
- **WHEN** 用户提交的文本与现有文本相同
- **THEN** 不扣减点数，返回"内容没有变化"

## MODIFIED Requirements

### Requirement: translation-status 接口

接口 SHALL 优先返回当前用户最近一次任务进度；若无任务，返回数据库翻译数量与公开状态。

返回字段增加：
- `status`: running/completed/failed/pending
- `mode`: simulate/mixed/network/published
- `translation_published`: boolean
- `is_running`: boolean（基于 user_translation_jobs 表判断）

### Requirement: translation-cost 接口

返回字段增加：
- `translation_published`: boolean
- `download_cost`: number
- `translated_in_database`: number
- `missing_translations`: number
- `requires_network_translation`: boolean

### Requirement: 阅读页前端

- `is_published` → `translation_published`
- 新增贡献者展示区域
- 新增下载区域（有权限/无权限两种状态）
- 新增下载提醒文案
- 翻译进度由后端 `user_translation_jobs` 驱动，不再前端模拟

## REMOVED Requirements

### Requirement: Lecture.is_published 布尔字段
**Reason**: 被 `translation_publications` 表的三态状态替代
**Migration**: 保留 `is_published` 字段但不再作为主要判断依据，后续迁移时同步

### Requirement: _running_tasks 内存变量
**Reason**: 被 `user_translation_jobs` 表替代
**Migration**: 完全移除 `_running_tasks` 和 `_running_task_tokens`

### Requirement: 前端 simulateProgress
**Reason**: 模拟翻译进度由后端 `user_translation_jobs` 驱动
**Migration**: 前端仅轮询 translation-status 接口展示进度
