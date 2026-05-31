# Steiner Reader Web — Code Wiki

> **版本:** 0.1.0  
> **最后更新:** 2026-05-31  
> **生产域名:** https://steiner.3mudi.com

---

## 目录

1. [项目概述](#1-项目概述)
2. [技术栈与依赖](#2-技术栈与依赖)
3. [项目架构](#3-项目架构)
4. [数据库设计](#4-数据库设计)
5. [认证系统](#5-认证系统)
6. [积分系统](#6-积分系统)
7. [后端模块详解](#7-后端模块详解)
8. [前端模块详解](#8-前端模块详解)
9. [API 接口文档](#9-api-接口文档)
10. [数据流与核心流程](#10-数据流与核心流程)
11. [部署与运维](#11-部署与运维)
12. [测试](#12-测试)
13. [脚本工具集](#13-脚本工具集)
14. [已知问题与待办](#14-已知问题与待办)

---

## 1. 项目概述

**Steiner Reader** 是一个鲁道夫·施泰纳（Rudolf Steiner）德语著作的在线阅读平台，提供德中双语对照阅读、AI 翻译、积分付费、PDF 下载、句子修订等功能。

### 核心功能

| 功能 | 说明 |
|------|------|
| 文献导入 | PDF/EPUB/DOCX 上传，自动解析为 书→章节→段落→句子 层级结构 |
| 德中翻译 | Google Translate 逐句翻译，后台异步任务，10 积分/讲座 |
| 多模式阅读 | 德中对照、仅德语、仅中文三种阅读模式 |
| 翻译付费墙 | 用户消费积分才能看到翻译内容；`is_published=true` 时免费可见 |
| 积分系统 | reserve/settle/refund 原子操作，冻结积分机制，充值审核流程 |
| PDF 下载 | reportlab 中德双语 PDF 生成，翻译贡献者自动获得下载权限 |
| 句子修订 | 用户可消费积分修改译文，支持投票机制 |
| 语义搜索 | 通过 Qdrant API 进行语义搜索 |
| 用户管理 | 独立 auth-service JWT 认证，管理员后台 |

### 核心用户流程

```
用户上传 PDF/EPUB/DOCX → 系统自动解析结构（免费）
    │
    ▼
用户浏览书籍/章节 → 仅德语可读
    │
    ▼
用户触发翻译（消耗积分）
    ├── reserve 积分 → 后台翻译 → settle 积分
    ├── 翻译完成 → is_published=true → 发布翻译
    └── 翻译失败 → refund 积分
    │
    ▼
用户阅读德中对照 / 仅中文 / 仅德语
    │
    ▼
用户可下载 PDF / 修订译文
```

---

## 2. 技术栈与依赖

### 后端

| 类别 | 技术 | 版本 |
|------|------|------|
| Web 框架 | FastAPI | 0.115.6 |
| ASGI 服务器 | Uvicorn | 0.34.0 |
| ORM | SQLAlchemy | 2.0.36 |
| 异步驱动 | asyncpg | 0.30.0 |
| 数据库迁移 | Alembic | 1.14.0 |
| PDF 解析 | pdfplumber | 0.11.4 |
| 德语 NLP | spaCy (de_core_news_sm) | 3.8.3 |
| 翻译 | deep-translator (GoogleTranslator) | 1.11.4 |
| HTTP 客户端 | httpx | — |
| PDF 生成 | reportlab | — |
| 数据验证 | Pydantic / pydantic-settings | 2.10.3 / 2.7.0 |
| 数据库 | PostgreSQL | 16 |

### 前端

| 类别 | 技术 | 版本 |
|------|------|------|
| 框架 | Next.js (App Router, Turbopack) | 16.2.4 |
| UI 库 | React | 19.2.4 |
| CSS | Tailwind CSS | 4.x |
| 语言 | TypeScript | 5.x |

### 基础设施

| 类别 | 技术 |
|------|------|
| 认证服务 | 独立 auth-service (https://auth.3mudi.com) |
| CDN | Cloudflare |
| 反向代理 | Nginx (Alpine) |
| 容器化 | Docker Compose |
| 进程管理 | systemd (生产环境) |
| 数据库 | PostgreSQL 16 |

---

## 3. 项目架构

### 3.1 整体架构图

```
用户 ──HTTPS──▶ Cloudflare CDN
                    │
                    ▼
              Nginx (:80) ─── Origin: 66.154.112.162
                    │
                    ├── /api/* ──▶ FastAPI (:8000)
                    │                 │
                    │                 ├── SQLAlchemy ──▶ PostgreSQL (:5432)
                    │                 ├── httpx ───────▶ Auth Service (auth.3mudi.com)
                    │                 ├── translator ──▶ Google Translate API
                    │                 └── pdf_generator ──▶ reportlab
                    │
                    └── /* ──────▶ Next.js (:3000)
                                      │
                                      └── api.ts ──▶ /api/* (rewrites → FastAPI)
```

### 3.2 目录结构

```
Steiner_Reader_Web/
├── backend/                        # Python 后端服务
│   ├── app/
│   │   ├── main.py                 # FastAPI 应用入口（11 个路由）
│   │   ├── config.py               # 配置管理（含 AUTH_SERVICE_URL）
│   │   ├── db/
│   │   │   ├── database.py         # 异步数据库连接与会话
│   │   │   └── models.py           # 16 个 ORM 模型
│   │   ├── models/
│   │   │   └── schemas.py          # Pydantic 请求/响应模型
│   │   ├── routers/
│   │   │   ├── auth.py             # 认证代理（auth-service JWT 验证）
│   │   │   ├── books.py            # 书籍/讲座/下载权限
│   │   │   ├── lectures.py         # 讲座段落/句子
│   │   │   ├── paragraphs.py       # 段落句子列表
│   │   │   ├── translate.py        # 翻译（核心：扣费/任务/发布）
│   │   │   ├── downloads.py        # PDF 下载/购买权限
│   │   │   ├── edits.py            # 句子修订/投票
│   │   │   ├── recharge.py         # 充值请求/审核
│   │   │   ├── admin.py            # 管理员（用户/积分/重翻/标题）
│   │   │   ├── images.py           # 图片服务
│   │   │   ├── search.py           # 语义搜索（Qdrant）
│   │   │   └── upload.py           # PDF 上传/解析
│   │   └── services/
│   │       ├── auth_client.py      # auth-service 客户端（向后兼容层）
│   │       ├── credit_service.py   # 积分服务（reserve/settle/refund/贡献/访问）
│   │       ├── translation_service.py  # 翻译服务（job 持久化/孤儿检测/发布状态）
│   │       ├── pdf_generator.py    # 双语 PDF 生成（reportlab）
│   │       ├── pdf_parser.py       # PDF 结构解析
│   │       └── translator.py       # 翻译服务（Google Translate）
│   ├── tests/                      # pytest 测试（30 个）
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/                       # Next.js 前端
│   ├── app/
│   │   ├── layout.tsx              # 根布局
│   │   ├── page.tsx                # 首页（4 种视图模式）
│   │   ├── globals.css             # 全局样式 + 设计系统
│   │   ├── components/
│   │   │   ├── Header.tsx          # 全局导航（积分/管理/搜索）
│   │   │   ├── HomeClient.tsx      # 首页客户端组件
│   │   │   ├── GroupedBooksView.tsx # 分组视图（GA 十年分组）
│   │   │   ├── PaginatedBooksView.tsx # 分页网格视图
│   │   │   ├── SearchBooksView.tsx # 搜索视图（防抖）
│   │   │   ├── SearchModal.tsx     # 语义搜索模态框
│   │   │   └── WaterfallBooksView.tsx # 瀑布流视图
│   │   ├── login/page.tsx          # 登录/注册
│   │   ├── profile/page.tsx        # 个人中心（密码/邮箱/积分记录）
│   │   ├── recharge/page.tsx       # 充值页面
│   │   ├── upload/page.tsx         # 文件上传
│   │   ├── admin/page.tsx          # 管理员面板
│   │   └── books/[bookId]/
│   │       ├── page.tsx            # 书籍详情（目录树）
│   │       └── lectures/[lectureId]/
│   │           └── page.tsx        # 阅读器（核心页面）
│   ├── lib/api.ts                  # API 客户端
│   └── next.config.ts              # Next.js 配置
│
├── scripts/                        # 数据导入脚本（300+）
├── deploy/systemd/                 # systemd 服务配置
├── docs/                           # 文档与数据分析
├── docker-compose.yml              # Docker Compose 编排
├── nginx.conf                      # Nginx 配置
├── init.sql                        # 数据库初始化 SQL
├── .env.example                    # 环境变量模板
├── CLAUDE.md                       # Claude Code 指南
├── HANDOVER.md                     # 交接文档
└── PLAN.md                         # 实施计划
```

---

## 4. 数据库设计

### 4.1 完整表清单（19 表）

| 表名 | 说明 | 关键字段 |
|------|------|---------|
| `books` | 书籍 | `id`, `ga_number`, `title_de`, `title_zh` |
| `lectures` | 讲座/章节 | `id`, `book_id`, `is_published`, `is_translating`, `translate_progress`, `translate_total` |
| `paragraphs` | 段落 | `id`, `lecture_id`, `order_index` |
| `sentences` | 句子 | `id`, `paragraph_id`, `text_de`, `text_zh` |
| `lecture_images` | 讲座图片 | `id`, `lecture_id`, `filename`, `after_sentence_id` |
| `translation_jobs` | 翻译任务（旧，按书） | `id`, `book_id`, `status` |
| **`translation_publications`** | **翻译发布状态（新）** | `id`, `lecture_id`, `book_id`, `status`(translating/published/failed), `first_contributor_user_id`, `published_at` |
| **`user_translation_jobs`** | **用户翻译任务（新）** | `id`, `user_id`(UUID), `lecture_id`, `status`(pending/running/completed/failed), `total_sentences`, `completed_sentences` |
| `credit_settings` | 积分价格配置 | `action`, `price` |
| `contributions` | 贡献记录 | `user_id`(UUID), `lecture_id`, `contribution_type`, `display_name`, `cost`, `grants_download` |
| `lecture_access` | 访问权限 | `user_id`(UUID), `lecture_id`, `access_type` |
| `edit_audit_log` | 编辑审计日志 | `user_id`, `sentence_id`, `field_changed`, `old_value`, `new_value` |
| `sentence_revisions` | 句子修订 | `sentence_id`, `new_value`, `user_id`, `status`, `vote_count` |
| `revision_votes` | 修订投票 | `revision_id`, `user_id` |
| `translation_fixes` | 翻译修正规则 | `pattern`, `replacement`, `enabled` |
| `recharge_requests` | 充值请求 | `user_id`(UUID), `amount`, `coefficient`, `payment_image`, `status`(pending/approved/rejected) |

### 4.2 ER 关系图

```
┌──────────┐     ┌──────────────┐     ┌──────────────┐     ┌───────────┐
│  books   │────▶│  lectures    │────▶│  paragraphs  │────▶│ sentences │
│          │ 1:N │              │ 1:N │              │ 1:N │           │
└──────────┘     │ is_published │     └──────────────┘     │ text_de   │
     │           │ is_translating│                          │ text_zh   │
     │           │ parent_id    │──── 自引用（层级结构）    └───────────┘
     │           └──────┬───────┘
     │                  │
     │     ┌────────────┼────────────────┐
     │     │ 1:N        │ 1:N            │ 1:N
     │     ▼            ▼                ▼
     │ ┌────────────┐ ┌──────────────┐ ┌────────────────────────┐
     │ │lecture_    │ │translation_  │ │user_translation_jobs   │
     │ │images      │ │publications  │ │(持久化翻译任务)         │
     │ └────────────┘ │(三态发布)     │ │ status: running/       │
     │                └──────────────┘ │ completed/failed       │
     │                                 └────────────────────────┘
     │ 1:N
     ▼
┌──────────────────┐
│translation_jobs  │  (旧版，按书级别)
└──────────────────┘

┌──────────────┐     ┌──────────────┐     ┌──────────────────┐
│contributions │     │lecture_access│     │recharge_requests │
│ user_id(UUID)│     │ user_id(UUID)│     │ user_id(UUID)    │
│ grants_down  │     │ access_type  │     │ status: pending/ │
└──────────────┘     └──────────────┘     │ approved/rejected│
                                          └──────────────────┘

┌──────────────────┐     ┌──────────────┐     ┌──────────────┐
│sentence_revisions│────▶│revision_votes│     │credit_settings│
│ status: active   │ 1:N │ user_id      │     │ action→price │
│ vote_count       │     └──────────────┘     └──────────────┘
└──────────────────┘
```

### 4.3 关键设计点

- **`user_id` 类型**：`String(36)` (UUID)，因为 auth-service 使用 UUID
- **`lectures.parent_id`**：自引用实现树形目录（部分→章节→演讲）
- **`lectures.is_published`**：当前与 `translation_publications` 双写，未来将完全迁移到后者
- **`translation_publications.status`**：三态（translating/published/failed），替代 `is_published` 布尔字段
- **`user_translation_jobs`**：替代内存 `_running_tasks`，翻译状态持久化到数据库
- **`contributions.grants_download`**：翻译贡献者自动获得下载权限

---

## 5. 认证系统

### 5.1 架构

```
前端 ──▶ auth.3mudi.com (独立服务)
              │
              ├── POST /api/auth/login     → 登录
              ├── POST /api/auth/register  → 注册
              ├── GET  /api/auth/verify    → 验证 Token（不返回 display_name）
              └── GET  /api/auth/me        → 完整用户信息（含 credits, credits_reserved）

后端 ──▶ auth.3mudi.com (HTTP 代理)
              │
              ├── GET  /api/auth/verify    → 验证 JWT
              ├── GET  /api/auth/me        → 获取 display_name fallback
              ├── POST /api/credits/reserve → 预扣积分
              ├── POST /api/credits/settle  → 确认扣费
              ├── POST /api/credits/refund  → 退还积分
              └── POST /api/credits/topup   → 充值
```

### 5.2 认证流程

1. 前端直接调用 auth-service 登录/注册，获取 JWT Token
2. Token 存储在 `localStorage.access_token` 和 `localStorage.auth_user`
3. 后续请求通过 `Authorization: Bearer <token>` 携带
4. 后端 `auth.py` 调用 auth-service `/verify` 验证 Token
5. 若 `/verify` 不返回 `display_name`，fallback 调用 `/me` 获取

### 5.3 AuthUser 模型

```python
class AuthUser(BaseModel):
    id: str              # UUID
    display_name: str
    email: Optional[str]
    role: str            # "user" 或 "admin"
    credits: float
    is_active: bool
    raw_token: str       # 原始 JWT，用于调用 auth-service
```

### 5.4 依赖注入

| 函数 | 说明 |
|------|------|
| `get_current_user(token)` | 从 JWT 解析用户，返回 `AuthUser` 或 `None` |
| `require_user(user)` | 要求已登录，否则 401 |
| `require_admin(user)` | 要求 `role == "admin"`，否则 403 |

---

## 6. 积分系统

### 6.1 积分操作

| 操作 | 说明 | reference_id 规则 |
|------|------|-------------------|
| `reserve` | 预扣（冻结）积分 | `translate-lecture-{id}-{uuid}` |
| `settle` | 确认扣费 | `{ref_id}-settle` |
| `refund` | 退还积分 | `{ref_id}-refund` |
| `topup` | 充值 | 无需 reference_id |

**关键设计**：auth-service 的 `credit_logs` 表对 `reference_id` 有全局唯一约束，因此 reserve/settle/refund 必须使用不同的 reference_id（通过后缀区分）。

### 6.2 积分计算

- **总积分**: `credits`（auth-service 返回）
- **冻结积分**: `credits_reserved`（翻译 reserve 后冻结）
- **可用积分**: `credits - credits_reserved`（前端统一显示此值）

### 6.3 atomic_deduct_credits 流程

```
1. reserve_credits(ref_id) 
   ├── 成功 → settle_credits(ref_id-settle)
   │         ├── 成功 → 返回成功
   │         └── 失败 → 积分保持冻结（不丢失）
   └── 409 (ref_id 已存在) → settle_credits(ref_id-settle)
                              ├── 成功 → 返回成功
                              └── 409 → 视为已处理（幂等）
```

### 6.4 积分价格

| 操作 | 价格 | 配置来源 |
|------|------|---------|
| 翻译单个讲座 | 10 点 | `credit_settings.translate_per_lecture` |
| 下载单个讲座 | 5 点 | `credit_settings.download_per_lecture` |

---

## 7. 后端模块详解

### 7.1 应用入口 — main.py

注册 **11 个路由模块**：

```python
app.include_router(books.router)       # /api/books
app.include_router(translate.router)    # /api/lectures/{id}/translate
app.include_router(images.router)       # /api/images/*
app.include_router(auth.router)         # /api/auth
app.include_router(admin.router)        # /api/admin
app.include_router(lectures.router)     # /api/lectures
app.include_router(paragraphs.router)   # /api/paragraphs
app.include_router(recharge.router)     # /api/recharge
app.include_router(downloads.router)    # /api/downloads
app.include_router(edits.router)        # /api/edits
app.include_router(search.router)       # /api/search
```

### 7.2 配置管理 — config.py

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| `DATABASE_URL` | `postgresql+asyncpg://steiner:change_me@localhost:5432/steiner_reader` | 数据库连接串 |
| `AUTH_SERVICE_URL` | `https://auth.3mudi.com` | 认证服务地址 |
| `AUTH_APP_NAME` | `steiner` | 认证应用名 |
| `TRANSLATION_ENGINE` | `google` | 翻译引擎 |
| `UPLOAD_DIR` | `/opt/steiner-reader/uploads` | 上传目录 |
| `APP_NAME` | `Steiner Reader` | 应用名称 |
| `DEBUG` | `False` | 调试模式 |

### 7.3 路由模块

#### auth.py — 认证代理 (`/api/auth`)

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/auth/me` | GET | 代理获取用户信息（含 credits, credits_reserved） |

**关键函数**：`_verify_token()`, `_fetch_user_info()`, `get_current_user()`, `require_user()`, `require_admin()`

#### translate.py — 翻译路由 (`/api`)

| 端点 | 方法 | 说明 | 认证 |
|------|------|------|------|
| `/api/lectures/{id}/translate` | POST | 触发翻译 | 必需 |
| `/api/lectures/{id}/translation-cost` | GET | 翻译费用 | 可选 |
| `/api/lectures/{id}/translation-status` | GET | 翻译进度 | 无 |

**翻译流程**：
1. `detect_orphan_jobs()` — 检测超过 30 分钟的孤儿任务
2. `is_lecture_running()` — 检查是否已在翻译
3. 已翻译未发布 → 检查 Contribution 记录，已付费则直接发布
4. 未翻译 → `reserve_credits()` → `start_translation_job()` → `asyncio.create_task()`
5. 后台任务：每 20 句提交一次 → `complete_translation_job()` → `settle_credits()`
6. 失败 → `fail_translation_job()` → `refund_credits()`

#### downloads.py — 下载路由 (`/api/downloads`)

| 端点 | 方法 | 说明 | 认证 |
|------|------|------|------|
| `/api/downloads/{lecture_id}/purchase` | POST | 购买下载权限 | 必需 |
| `/api/downloads/{lecture_id}/pdf` | GET | 下载双语 PDF | 必需 |
| `/api/downloads/{lecture_id}/check` | GET | 检查下载权限 | 必需 |

#### edits.py — 修订路由 (`/api/edits`)

| 端点 | 方法 | 说明 | 认证 |
|------|------|------|------|
| `/api/edits/{sentence_id}/revise` | POST | 提交修订 | 必需 |
| `/api/edits/{revision_id}/vote` | POST | 投票 | 必需 |
| `/api/edits/{revision_id}/reject` | POST | 拒绝修订 | 管理员 |
| `/api/edits/sentence/{sentence_id}` | GET | 获取修订列表 | 无 |
| `/api/edits/sentence/{sentence_id}/history` | GET | 编辑历史 | 无 |

#### recharge.py — 充值路由 (`/api/recharge`)

| 端点 | 方法 | 说明 | 认证 |
|------|------|------|------|
| `/api/recharge/request` | POST | 提交充值请求 | 必需 |
| `/api/recharge/my` | GET | 我的充值记录 | 必需 |
| `/api/recharge/upload-receipt` | POST | 上传支付凭证 | 必需 |
| `/api/recharge/pending` | GET | 待审核列表 | 管理员 |
| `/api/recharge/{id}/review` | POST | 审核充值 | 管理员 |

#### search.py — 语义搜索 (`/api/search`)

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/search` | GET | 语义搜索（Qdrant API） |

#### upload.py — 上传路由 (`/api/books`)

| 端点 | 方法 | 说明 | 认证 |
|------|------|------|------|
| `/api/books/upload` | POST | 上传 PDF 并解析 | 必需 |

#### books.py — 书籍路由 (`/api/books`)

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/books/summary` | GET | 书籍摘要（CTE 优化） |
| `/api/books/groups` | GET | 按 GA 十年分组 |
| `/api/books` | GET | 完整书籍列表 |
| `/api/books/{id}` | GET | 书籍详情 |
| `/api/books/{book_id}/lectures/{lecture_id}` | GET | 讲座完整内容 |

#### admin.py — 管理员路由 (`/api/admin`)

| 端点 | 方法 | 说明 | 认证 |
|------|------|------|------|
| `/api/admin/users` | GET | 用户列表 | 管理员 |
| `/api/admin/users/{id}/credits` | PUT | 设置积分 | 管理员 |
| `/api/admin/users/{id}/add-credits` | POST | 增加积分 | 管理员 |
| `/api/admin/lectures/{id}/retranslate` | POST | 重翻译 | 管理员 |
| `/api/admin/lectures/{id}/translation-stats` | GET | 翻译统计 | 管理员 |

### 7.4 服务层

#### credit_service.py — 积分服务

| 函数 | 说明 |
|------|------|
| `compute_price(db, action, default)` | 从 `credit_settings` 表查询价格 |
| `seed_default_settings(db)` | 初始化默认积分设置 |
| `_call_auth(method, path, token, payload)` | auth-service HTTP 调用底层 |
| `get_balance(token)` | 查询积分余额 |
| `reserve_credits(token, amount, ref_id)` | 预扣积分 |
| `settle_credits(token, reserved, actual, ref_id)` | 确认扣费 |
| `refund_credits(token, amount, ref_id)` | 退还积分 |
| `topup_credits(token, amount)` | 充值 |
| `atomic_deduct_credits(token, amount, ref_id)` | 原子扣费（reserve + settle） |
| `add_contribution(db, user_id, lecture_id, ...)` | 记录贡献 |
| `grant_access(db, user_id, lecture_id, type)` | 授予访问权限 |
| `check_download_access(db, user_id, lecture_id)` | 检查下载权限（LectureAccess + Contribution 兜底） |
| `get_contributions(db, lecture_id)` | 获取贡献列表 |

#### translation_service.py — 翻译服务

| 函数 | 说明 |
|------|------|
| `is_lecture_running(db, lecture_id)` | 检查讲座是否在翻译中 |
| `start_translation_job(db, lecture_id, user_id, book_id)` | 创建翻译任务 |
| `complete_translation_job(db, lecture_id)` | 完成翻译任务 |
| `fail_translation_job(db, lecture_id, error)` | 标记翻译失败 |
| `detect_orphan_jobs(db, timeout_minutes=30)` | 检测孤儿任务（超时自动标记 failed） |
| `get_publication_status(db, lecture_id)` | 获取发布状态 |
| `set_publication_status(db, lecture_id, book_id, status, user_id)` | 设置发布状态 |

#### pdf_generator.py — PDF 生成

| 函数 | 说明 |
|------|------|
| `generate_bilingual_pdf(lecture_data)` | 生成中德双语 PDF（reportlab） |
| `_register_fonts()` | 注册中文字体（WenQuanYiMicroHei / 微软雅黑 fallback） |

#### translator.py — 翻译服务

| 函数 | 说明 |
|------|------|
| `translate_sentence_sync(text_de)` | 同步翻译单句 |
| `translate_sentence_async(text_de)` | 异步包装 |
| `translate_lecture_sentences(sentences)` | 批量翻译，300ms 限速 |

---

## 8. 前端模块详解

### 8.1 页面路由

| 路由 | 文件 | 说明 |
|------|------|------|
| `/` | `page.tsx` | 首页（4 种视图：瀑布流/分组/网格/搜索） |
| `/books/[bookId]` | `books/[bookId]/page.tsx` | 书籍详情（目录树） |
| `/books/[bookId]/lectures/[lectureId]` | `lectures/[lectureId]/page.tsx` | 阅读器（核心页面） |
| `/login` | `login/page.tsx` | 登录/注册 |
| `/profile` | `profile/page.tsx` | 个人中心 |
| `/recharge` | `recharge/page.tsx` | 充值页面 |
| `/upload` | `upload/page.tsx` | 文件上传 |
| `/admin` | `admin/page.tsx` | 管理员面板 |

### 8.2 组件

| 组件 | 说明 |
|------|------|
| `Header.tsx` | 全局导航（积分/管理/搜索/语言切换） |
| `HomeClient.tsx` | 首页客户端渲染（搜索+卡片） |
| `GroupedBooksView.tsx` | GA 十年分组视图（手风琴展开） |
| `PaginatedBooksView.tsx` | 分页网格视图（24/页，排序） |
| `SearchBooksView.tsx` | 搜索视图（300ms 防抖） |
| `SearchModal.tsx` | 语义搜索模态框 |
| `WaterfallBooksView.tsx` | 瀑布流视图（无限滚动） |

### 8.3 API 客户端 — lib/api.ts

**认证机制**：
- Token 存储在 `localStorage.access_token`
- 用户信息在 `localStorage.auth_user`
- `authFetch()` 自动附加 Authorization header
- 12 秒请求超时
- 登录/登出时派发 `auth-changed` 事件

**关键 API 函数**：

| 函数 | 端点 | 认证 |
|------|------|------|
| `fetchBooks()` | GET /api/books | 无 |
| `fetchBookSummaries()` | GET /api/books/summary | 无 |
| `fetchBookGroups()` | GET /api/books/groups | 无 |
| `fetchBook(id)` | GET /api/books/{id} | 无 |
| `fetchLecture(id)` / `fetchLecture(bid, lid)` | GET /api/lectures/{id} | authFetch |
| `fetchParagraphs(lid)` | GET /api/lectures/{id}/paragraphs | authFetch |
| `translateLecture(lid)` | POST /api/lectures/{id}/translate | 必需 |
| `getTranslationCost(lid)` | GET /api/lectures/{id}/translation-cost | 可选 |
| `getTranslationStatus(lid)` | GET /api/lectures/{id}/translation-status | 无 |
| `downloadLecturePdf(lid)` | GET /api/downloads/{id}/pdf | 必需 |
| `fetchContributions(lid)` | GET /api/... | 必需 |
| `fetchMyTransactions()` | GET /api/... | 必需 |

**前端 API URL 配置**：
- 生产环境：`NEXT_PUBLIC_API_URL` 必须为空（通过 Nginx 代理）
- 开发环境：`next.config.ts` rewrites 代理到 `127.0.0.1:8000`

### 8.4 阅读器页面 — lectures/[lectureId]/page.tsx

核心阅读页面，功能最复杂：

- **三种阅读模式**：`de-zh`（德中对照）、`de-only`（仅德语）、`zh-only`（仅中文）
- **翻译付费墙**：未发布翻译时显示翻译按钮，消耗积分
- **翻译进度轮询**：3 秒间隔，`is_running` 状态驱动
- **PDF 下载**：翻译贡献者自动获得下载权限
- **图片展示**：`ImageView` 组件支持点击放大
- **句子交互**：点击/双击切换中文翻译显示
- **错误处理**：加载失败显示错误信息而非自动跳转

---

## 9. API 接口文档

### 完整接口列表

#### 认证

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | `/api/auth/me` | 获取用户信息（含 credits_reserved） | 必需 |

#### 书籍

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | `/api/books/summary` | 书籍摘要 | 无 |
| GET | `/api/books/groups` | GA 十年分组 | 无 |
| GET | `/api/books` | 完整书籍列表 | 无 |
| GET | `/api/books/{id}` | 书籍详情 | 无 |
| GET | `/api/books/{bid}/lectures/{lid}` | 讲座内容 | 无 |
| POST | `/api/books/upload` | 上传 PDF | 必需 |

#### 章节与段落

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | `/api/lectures/{id}` | 讲座信息 | 无 |
| GET | `/api/lectures/{id}/paragraphs` | 段落列表 | authFetch |
| GET | `/api/paragraphs/{id}/sentences` | 句子列表 | 无 |

#### 翻译

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/api/lectures/{id}/translate` | 触发翻译 | 必需 |
| GET | `/api/lectures/{id}/translation-cost` | 翻译费用 | 可选 |
| GET | `/api/lectures/{id}/translation-status` | 翻译进度 | 无 |

#### 下载

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/api/downloads/{id}/purchase` | 购买下载权限 | 必需 |
| GET | `/api/downloads/{id}/pdf` | 下载 PDF | 必需 |
| GET | `/api/downloads/{id}/check` | 检查权限 | 必需 |

#### 修订

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/api/edits/{sid}/revise` | 提交修订 | 必需 |
| POST | `/api/edits/{rid}/vote` | 投票 | 必需 |
| POST | `/api/edits/{rid}/reject` | 拒绝修订 | 管理员 |
| GET | `/api/edits/sentence/{sid}` | 修订列表 | 无 |
| GET | `/api/edits/sentence/{sid}/history` | 编辑历史 | 无 |

#### 充值

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| POST | `/api/recharge/request` | 提交充值 | 必需 |
| GET | `/api/recharge/my` | 我的充值记录 | 必需 |
| POST | `/api/recharge/upload-receipt` | 上传凭证 | 必需 |
| GET | `/api/recharge/pending` | 待审核列表 | 管理员 |
| POST | `/api/recharge/{id}/review` | 审核 | 管理员 |

#### 搜索

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | `/api/search` | 语义搜索 | 无 |

#### 图片

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | `/api/books/{id}/images` | 书籍图片 | 无 |
| GET | `/api/lectures/{id}/images` | 讲座图片 | 无 |
| GET | `/api/images/{ga_dir}/{filename}` | 图片文件 | 无 |

#### 管理员

| 方法 | 路径 | 说明 | 认证 |
|------|------|------|------|
| GET | `/api/admin/users` | 用户列表 | 管理员 |
| PUT | `/api/admin/users/{id}/credits` | 设置积分 | 管理员 |
| POST | `/api/admin/users/{id}/add-credits` | 增加积分 | 管理员 |
| POST | `/api/admin/lectures/{id}/retranslate` | 重翻译 | 管理员 |
| GET | `/api/admin/lectures/{id}/translation-stats` | 翻译统计 | 管理员 |

#### 系统

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/` | 应用信息 |
| GET | `/health` | 健康检查 |

---

## 10. 数据流与核心流程

### 10.1 翻译流程（核心）

```
用户点击"翻译本章"
    │
    ▼
POST /api/lectures/{id}/translate
    │
    ├── detect_orphan_jobs() — 清理超时任务
    ├── is_lecture_running() — 防重复
    │
    ├── [已翻译未发布]
    │   ├── 检查 Contribution 记录
    │   │   ├── 已付费 → 直接发布（不扣费）
    │   │   └── 未付费 → atomic_deduct_credits → 发布
    │   └── 返回 already_translated
    │
    └── [未翻译]
        ├── get_credits_balance() — 检查可用积分
        ├── reserve_credits(ref_id) — 预扣 10 点
        ├── start_translation_job() — 创建 DB 任务
        ├── set_publication_status("translating")
        └── asyncio.create_task(_do_translate_lecture)
            │
            ├── 每 20 句批量翻译 + db.commit()
            ├── complete_translation_job()
            ├── set_publication_status("published")
            ├── add_contribution() + grant_access("download")
            └── settle_credits(ref_id-settle)
                │
                [失败时]
                ├── fail_translation_job()
                ├── set_publication_status("failed")
                └── refund_credits(ref_id-refund)
```

### 10.2 认证流程

```
前端 → auth.3mudi.com/login → JWT Token
    │
    ▼
localStorage: access_token + auth_user
    │
    ▼
后端 auth.py: _verify_token() → _fetch_user_info() fallback
    │
    ▼
AuthUser(id=UUID, display_name, credits, raw_token)
```

### 10.3 充值流程

```
用户上传支付截图 → POST /api/recharge/request
    │
    ▼
recharge_requests 表 (status=pending)
    │
    ▼
管理员审核 → POST /api/recharge/{id}/review
    │
    ├── approved → auth-service topup_credits
    └── rejected → 更新状态
```

---

## 11. 部署与运维

### 11.1 环境信息

| | 生产环境 | 开发环境 |
|------|----------|----------|
| **服务商** | CloudCone | Oracle Frankfurt |
| **IP** | `66.154.112.162` | `89.168.93.94` |
| **用户** | `root` | `ubuntu` |
| **域名** | `steiner.3mudi.com` (Cloudflare CDN) | — |
| **认证方式** | 密码 | SSH Key |
| **部署方式** | systemd 裸机 | — |
| **auth-service** | auth.3mudi.com (外部) | 本机 PostgreSQL 14 |

### 11.2 生产服务

| 服务 | systemd 单元 | 端口 | 工作目录 |
|------|-------------|------|----------|
| Nginx | 系统服务 | 80 | — |
| Frontend | `steiner-frontend` | 3000 (127.0.0.1) | `/opt/steiner-reader/frontend` |
| Backend | `steiner-backend` | 8000 (127.0.0.1) | `/opt/steiner-reader/backend` |
| PostgreSQL | 系统服务 | 5432 | — |

### 11.3 部署命令

```bash
# 推荐：git pull 方式
plink -ssh root@66.154.112.162 -pw "PASSWORD" \
  "cd /opt/steiner-reader && git fetch origin && git reset --hard origin/main && \
   systemctl restart steiner-backend.service && \
   cd frontend && npm run build && systemctl restart steiner-frontend.service"

# 备用：rsync 方式
rsync -avz --exclude='__pycache__' backend/app root@66.154.112.162:/opt/steiner-reader/backend/
ssh root@66.154.112.162 "systemctl restart steiner-backend.service"
rsync -avz --exclude='node_modules' frontend/app root@66.154.112.162:/opt/steiner-reader/frontend/
ssh root@66.154.112.162 "cd /opt/steiner-reader/frontend && npm run build && systemctl restart steiner-frontend.service"
```

### 11.4 日志

| 日志 | 路径 |
|------|------|
| 后端 stdout | `/var/log/steiner-reader/backend.log` |
| 后端 stderr | `/var/log/steiner-reader/backend-error.log` |
| systemd 日志 | `journalctl -u steiner-backend` / `journalctl -u steiner-frontend` |

### 11.5 数据库

| 项目 | 值 |
|------|-----|
| 用户 | `steiner` |
| 数据库 | `steiner_reader` |
| 规模 | 19 表，316 本书，5367 讲座，415 MB |
| 备份 | `/var/backups/steiner-reader/`（保留 14 天） |
| 开发环境备份 | `ubuntu@89.168.93.94:/tmp/steiner_reader_backup_20250531.sql.gz` (142 MB) |

### 11.6 磁盘 ⚠️

- 20GB 磁盘，当前使用约 **92%**
- 需定期清理 `/tmp/` 下的旧备份文件
- 曾因磁盘 100% 满导致全站宕机

### 11.7 开发环境启动

```bash
# 后端
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# 前端
cd frontend
npm install
npm run dev    # 端口 3000，自动代理 /api → localhost:8000
```

---

## 12. 测试

### 12.1 运行测试

```bash
cd backend
python -m pytest tests/ -v
```

### 12.2 测试覆盖

| 测试文件 | 测试数 | 覆盖内容 |
|----------|--------|---------|
| `test_credit_service.py` | 5 | `compute_price` 默认值回退、`add_contribution` |
| `test_translation_models.py` | 7 | `TranslationPublication`/`UserTranslationJob` 模型 |
| `test_translation_service.py` | 13 | job 持久化、孤儿检测、发布状态 |
| `test_pdf_generator.py` | 3 | PDF 生成（正常/缺中文/空讲座） |
| `test_recharge.py` | 2 | datetime 序列化 |

### 12.3 测试基础设施

- `pytest.ini`: `asyncio_mode = auto`
- `conftest.py`: SQLite 内存数据库 fixture
- 所有测试独立运行，不依赖外部服务

---

## 13. 脚本工具集

`scripts/` 目录包含 300+ 个数据导入和批处理脚本：

| 目录 | 说明 | 数量 |
|------|------|------|
| `scripts/individual/all_189/` | 每本书独立导入脚本 | ~180 |
| `scripts/epub/` | EPUB 格式导入 | ~120 |
| `scripts/bdn_import/` | BDN 批量导入 | 4 |
| `scripts/docx_import/` | DOCX 导入模板 | — |

核心工具：`import_ga_generic.py`, `epub_importer.py`, `batch_import.py`, `smart_import.py`, `download_pdfs.sh`, `backup_database.sh`

---

## 14. 已知问题与待办

### 🔴 高优先级

| # | 问题 | 说明 |
|---|------|------|
| 1 | **translation_publications 完全替代 is_published** | 当前双写状态，前端仍从 `Lecture.is_published` 判断 |
| 2 | **翻译进度由 job 表驱动** | `user_translation_jobs.completed_sentences` 未在翻译中更新 |
| 3 | **display_name 回填** | 旧贡献记录 `display_name` 可能为空 |
| 4 | **生产磁盘 92%** | 需定期清理 `/tmp/` 或扩容 |

### 🟡 中优先级

| # | 问题 | 说明 |
|---|------|------|
| 5 | **translation-cost 接口扩展** | 缺少 `translation_published`/`download_cost` 等字段 |
| 6 | **充值审核性能** | 逐个用户查询 auth-service，批量时慢 |
| 7 | **前端翻译失败状态** | 未区分"翻译中"和"翻译失败"，缺重试按钮 |

### 🟢 低优先级

| # | 问题 | 说明 |
|---|------|------|
| 8 | **CORS 未限制** | `allow_origins=["*"]`，生产环境需限制 |
| 9 | **清理临时文件** | `.bak`/`.backup` 文件应清理 |
| 10 | **贡献者聚合显示** | 多用户贡献同一讲座时应聚合 |
| 11 | **前端/后端上传格式不匹配** | 前端接受 `.epub,.docx`，后端 `upload.py` 仅处理 `.pdf` |
| 12 | **book_images 表** | `images.py` 查询 `book_images` 表，但 ORM 中未定义 |

### ⚠️ 注意事项

- **Next.js 16**：非常新的版本，API 可能与旧版不同
- **reference_id 全局唯一**：reserve/settle/refund 必须使用不同 reference_id
- **前端 API URL**：生产环境 `NEXT_PUBLIC_API_URL` 必须为空
- **Anki 冻结积分**：ooJerry 用户 309.30 积分被 Anki 应用冻结
