# Steiner Reader Web — Code Wiki

> **版本:** 0.1.0  
> **最后更新:** 2026-05-27

---

## 目录

1. [项目概述](#1-项目概述)
2. [技术栈与依赖](#2-技术栈与依赖)
3. [项目架构](#3-项目架构)
4. [数据库设计](#4-数据库设计)
5. [后端模块详解](#5-后端模块详解)
6. [前端模块详解](#6-前端模块详解)
7. [API 接口文档](#7-api-接口文档)
8. [数据流与核心流程](#8-数据流与核心流程)
9. [部署与运维](#9-部署与运维)
10. [脚本工具集](#10-脚本工具集)
11. [关键设计决策](#11-关键设计决策)

---

## 1. 项目概述

**Steiner Reader** 是一个用于阅读和翻译鲁道夫·施泰纳（Rudolf Steiner）人智学著作的 Web 平台。项目以施泰纳全集（Gesamtausgabe, GA 系列）为核心数据源，提供以下核心功能：

- **PDF/EPUB/DOCX 上传与自动解析**：上传文献后自动解析为 书 → 章节 → 段落 → 句子 的层级结构
- **句子级德中翻译**：基于 Google Translate（免费）的德语→中文逐句翻译，支持异步后台任务
- **多模式阅读**：德中对照、仅德语、仅中文三种阅读模式
- **用户系统**：注册/登录、积分制翻译付费、管理员后台
- **图片管理**：支持讲座配图的存储与展示
- **树形目录**：支持"部分→章节→演讲"多级层级结构的递归渲染

### 核心用户流程

```
用户上传 PDF/EPUB/DOCX
    │
    ▼
系统自动解析结构
    ├── 识别章节/段落/句子
    ├── 存储德语原文
    └── 向用户展示：仅德语可读
    │
    ▼
用户触发翻译（消耗积分）
    │
    ▼
系统逐句翻译（异步后台任务）
    ├── 翻译完成，存入数据库
    └── 用户可读德中对照 / 仅中文 / 仅德语
```

---

## 2. 技术栈与依赖

### 后端技术栈

| 类别 | 技术 | 版本 |
|------|------|------|
| Web 框架 | FastAPI | 0.115.6 |
| ASGI 服务器 | Uvicorn | 0.34.0 |
| ORM | SQLAlchemy | 2.0.36 |
| 异步 PostgreSQL 驱动 | asyncpg | 0.30.0 |
| 数据库迁移 | Alembic | 1.14.0 |
| PDF 解析 | pdfplumber | 0.11.4 |
| 德语 NLP | spaCy (de_core_news_sm) | 3.8.3 |
| 翻译 | deep-translator (Google Translate) | 1.11.4 |
| OpenAI 兼容接口 | openai | 1.58.1 |
| 数据验证 | Pydantic / pydantic-settings | 2.10.3 / 2.7.0 |
| JWT 认证 | python-jose (via passlib) | — |
| 密码哈希 | passlib[bcrypt] | — |
| 同步 PostgreSQL 驱动 | psycopg2-binary | 2.9.10 |
| 数据库 | PostgreSQL | 16 |

### 前端技术栈

| 类别 | 技术 | 版本 |
|------|------|------|
| 框架 | Next.js (App Router) | 16.2.4 |
| UI 库 | React | 19.2.4 |
| CSS | Tailwind CSS | 4.x |
| 语言 | TypeScript | 5.x |

### 基础设施

| 类别 | 技术 |
|------|------|
| 容器化 | Docker + Docker Compose |
| 反向代理 | Nginx (Alpine) |
| 进程管理 | systemd (裸机部署) |
| 数据库 | PostgreSQL 16 |

---

## 3. 项目架构

### 3.1 整体架构图

```
                    ┌─────────────────────────────────────┐
                    │              VPS / 本地              │
                    │                                     │
  用户 ──HTTP──▶    │  Nginx (:80)                        │
                    │    ├── /       → Next.js (:3000)    │
                    │    ├── /api/*  → FastAPI (:8000)    │
                    │    └── /health → FastAPI (:8000)    │
                    │                                     │
                    │  ┌──────────┐  ┌──────────────────┐ │
                    │  │ Frontend │  │    Backend        │ │
                    │  │ Next.js  │  │    FastAPI        │ │
                    │  │ :3000    │  │    :8000          │ │
                    │  └──────────┘  └────────┬─────────┘ │
                    │                         │            │
                    │                ┌────────▼─────────┐  │
                    │                │   PostgreSQL     │  │
                    │                │   :5432          │  │
                    │                └──────────────────┘  │
                    └─────────────────────────────────────┘
```

### 3.2 目录结构

```
Steiner_Reader_Web/
├── backend/                        # Python 后端服务
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py                 # FastAPI 应用入口
│   │   ├── config.py               # 配置管理 (pydantic-settings)
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── database.py         # 数据库连接与会话管理
│   │   │   └── models.py           # SQLAlchemy ORM 模型
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── schemas.py          # Pydantic 请求/响应模型
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py             # 认证路由 (注册/登录/JWT)
│   │   │   ├── books.py            # 书籍路由 (列表/详情/章节)
│   │   │   ├── lectures.py         # 章节路由 (段落/句子)
│   │   │   ├── paragraphs.py       # 段落路由 (句子列表)
│   │   │   ├── images.py           # 图片路由 (服务/查询)
│   │   │   ├── translate.py        # 翻译路由 (触发/状态/费用)
│   │   │   ├── admin.py            # 管理员路由 (用户/积分/重翻)
│   │   │   └── admin_translation_utils.py  # 管理员翻译工具函数
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── pdf_parser.py       # PDF 结构解析服务
│   │       └── translator.py       # 翻译服务 (Google Translate)
│   ├── Dockerfile
│   ├── requirements.txt
│   └── parse_docx_v*.py            # DOCX 解析脚本 (多版本迭代)
│
├── frontend/                       # Next.js 前端
│   ├── app/
│   │   ├── layout.tsx              # 根布局
│   │   ├── page.tsx                # 首页 (书籍列表)
│   │   ├── globals.css             # 全局样式 + 设计系统
│   │   ├── components/
│   │   │   └── Header.tsx          # 全局导航栏
│   │   ├── login/
│   │   │   └── page.tsx            # 登录/注册页
│   │   ├── upload/
│   │   │   └── page.tsx            # 文件上传页
│   │   ├── admin/
│   │   │   └── page.tsx            # 管理员面板
│   │   └── books/
│   │       └── [bookId]/
│   │           ├── page.tsx        # 书籍详情 (目录树)
│   │           └── lectures/
│   │               └── [lectureId]/
│   │                   └── page.tsx # 阅读器页面
│   ├── lib/
│   │   └── api.ts                  # API 客户端 (类型+请求)
│   ├── next.config.ts              # Next.js 配置 (API 代理)
│   ├── package.json
│   └── tsconfig.json
│
├── scripts/                        # 数据导入脚本
│   ├── individual/all_189/         # 189 本书的独立导入脚本
│   ├── epub/                       # EPUB 格式导入脚本
│   ├── single/                     # 单本书导入脚本
│   └── bdn_import/                 # BDN 批量导入脚本
│
├── deploy/
│   └── systemd/                    # systemd 服务配置
│       ├── steiner-backend.service
│       └── steiner-frontend.service
│
├── docs/                           # 文档与数据分析
├── docker-compose.yml              # Docker Compose 编排
├── nginx.conf                      # Nginx 反向代理配置
├── init.sql                        # 数据库初始化 SQL
├── .env.example                    # 环境变量模板
└── PLAN.md                         # 项目实施计划
```

### 3.3 请求流转

```
浏览器请求
    │
    ▼
Nginx (:80)
    │
    ├── /api/* ──────────▶ FastAPI (:8000)
    │                         │
    │                         ├── SQLAlchemy ORM ──▶ PostgreSQL (:5432)
    │                         ├── pdf_parser ──▶ PDF 解析
    │                         └── translator ──▶ Google Translate API
    │
    └── /* ──────────────▶ Next.js (:3000)
                              │
                              └── api.ts ──▶ /api/* (rewrites → FastAPI)
```

---

## 4. 数据库设计

### 4.1 ER 关系图

```
┌──────────┐     ┌──────────────┐     ┌──────────────┐     ┌───────────┐
│  books   │────▶│  lectures    │────▶│  paragraphs  │────▶│ sentences │
│          │ 1:N │              │ 1:N │              │ 1:N │           │
│ id (PK)  │     │ id (PK)      │     │ id (PK)      │     │ id (PK)   │
│ ga_number│     │ book_id (FK) │     │ lecture_id   │     │ para_id   │
│ title_de │     │ title_de     │     │ order_index  │     │ order_idx │
│ title_zh │     │ title_zh     │     └──────────────┘     │ text_de   │
│ pdf_file │     │ lecture_date │                           │ text_zh   │
│ cover_url│     │ location     │                           └───────────┘
└──────────┘     │ order_index  │
     │           │ parent_id(FK)│──── 自引用 (层级结构)
     │           │ level        │
     │           └──────────────┘
     │                │
     │                │ 1:N
     │                ▼
     │           ┌───────────────┐
     │           │lecture_images │
     │           │               │
     │           │ id (PK)       │
     │           │ lecture_id(FK)│
     │           │ filename      │
     │           │ page_number   │
     │           │ after_sent_id │
     │           └───────────────┘
     │
     │ 1:N
     ▼
┌──────────────────┐     ┌──────────┐
│translation_jobs  │     │  users   │
│                  │     │          │
│ id (PK)          │     │ id (PK)  │
│ book_id (FK)     │     │ username │
│ status           │     │ email    │
│ total_sentences  │     │ pwd_hash │
│ translated_count │     │ credits  │
│ error_message    │     │ is_admin │
└──────────────────┘     └──────────┘
```

### 4.2 表结构详情

#### books — 书籍表

| 字段 | 类型 | 说明 |
|------|------|------|
| id | SERIAL PK | 自增主键 |
| ga_number | VARCHAR(20) | GA 编号，如 "GA 115"，有索引 |
| title_de | TEXT NOT NULL | 德语书名 |
| title_zh | TEXT | 中文书名（可选） |
| pdf_filename | TEXT NOT NULL | 原始 PDF 文件名 |
| cover_url | TEXT | 封面图 URL |
| created_at | TIMESTAMP | 创建时间 |

#### lectures — 章节/演讲表

| 字段 | 类型 | 说明 |
|------|------|------|
| id | SERIAL PK | 自增主键 |
| book_id | INTEGER FK | 所属书籍，CASCADE 删除 |
| title_de | TEXT | 德语标题 |
| title_zh | VARCHAR(200) | 中文标题 |
| lecture_date | DATE | 演讲日期 |
| location | VARCHAR(200) | 演讲地点 |
| order_index | INTEGER NOT NULL | 排序序号 |
| parent_id | INTEGER FK | 父章节 ID（自引用，支持层级结构） |
| level | VARCHAR(10) | 层级标识，如 "lecture"、"heading" |
| created_at | TIMESTAMP | 创建时间 |

**关键设计**：`lectures` 表通过 `parent_id` 自引用实现树形层级结构，支持"部分→章节→演讲"等多级目录。

#### paragraphs — 段落表

| 字段 | 类型 | 说明 |
|------|------|------|
| id | SERIAL PK | 自增主键 |
| lecture_id | INTEGER FK | 所属章节，CASCADE 删除 |
| order_index | INTEGER NOT NULL | 排序序号 |
| created_at | TIMESTAMP | 创建时间 |

#### sentences — 句子表

| 字段 | 类型 | 说明 |
|------|------|------|
| id | SERIAL PK | 自增主键 |
| paragraph_id | INTEGER FK | 所属段落，CASCADE 删除 |
| order_index | INTEGER NOT NULL | 排序序号 |
| text_de | TEXT NOT NULL | 德语原文 |
| text_zh | TEXT | 中文翻译（NULL = 未翻译） |
| created_at | TIMESTAMP | 创建时间 |

**关键设计**：`text_zh` 为 NULL 表示未翻译，这是翻译状态判断的核心字段。

#### lecture_images — 讲座图片表

| 字段 | 类型 | 说明 |
|------|------|------|
| id | SERIAL PK | 自增主键 |
| lecture_id | INTEGER FK | 所属讲座 |
| filename | VARCHAR(255) NOT NULL | 文件名 |
| page_number | INTEGER NOT NULL | PDF 页码 |
| width / height | INTEGER | 图片尺寸 |
| caption | TEXT | 图片说明 |
| order_index | INTEGER | 排序序号 |
| after_paragraph_id | INTEGER FK | 插入位置：段落后 |
| after_sentence_id | INTEGER FK | 插入位置：句子后 |

#### translation_jobs — 翻译任务表

| 字段 | 类型 | 说明 |
|------|------|------|
| id | SERIAL PK | 自增主键 |
| book_id | INTEGER FK | 所属书籍 |
| status | VARCHAR(20) | 状态：pending / running / completed / failed |
| total_sentences | INTEGER | 总句子数 |
| translated_count | INTEGER | 已翻译数 |
| error_message | TEXT | 错误信息 |
| created_at / updated_at | TIMESTAMP | 时间戳 |

#### users — 用户表

| 字段 | 类型 | 说明 |
|------|------|------|
| id | SERIAL PK | 自增主键 |
| username | VARCHAR(50) UNIQUE | 用户名，有索引 |
| email | VARCHAR(255) UNIQUE | 邮箱，有索引 |
| password_hash | VARCHAR(255) | bcrypt 密码哈希 |
| credits | INTEGER | 积分余额（默认 100） |
| is_admin | INTEGER | 管理员标识（0=普通，1=管理员） |
| created_at | TIMESTAMP | 注册时间 |

---

## 5. 后端模块详解

### 5.1 应用入口 — `backend/app/main.py`

FastAPI 应用入口，负责：

- 创建 FastAPI 实例，设置标题和描述
- 配置 CORS 中间件（当前允许所有来源，生产环境需限制）
- 注册 7 个路由模块
- 提供 `/` 和 `/health` 健康检查端点

```python
app = FastAPI(title=settings.APP_NAME, version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], ...)
app.include_router(books.router)      # /api/books
app.include_router(translate.router)   # /api/lectures/{id}/translate
app.include_router(images.router)      # /api/images/*
app.include_router(auth.router)        # /api/auth/*
app.include_router(admin.router)       # /api/admin/*
app.include_router(lectures.router)    # /api/lectures/*
app.include_router(paragraphs.router)  # /api/paragraphs/*
```

### 5.2 配置管理 — `backend/app/config.py`

使用 `pydantic-settings` 的 `BaseSettings` 从环境变量加载配置，支持 `.env` 文件。

| 配置项 | 默认值 | 说明 |
|--------|--------|------|
| DATABASE_URL | `postgresql+asyncpg://steiner:change_me@localhost:5432/steiner_reader` | 异步 PostgreSQL 连接串 |
| TRANSLATION_ENGINE | `google` | 翻译引擎（google / deepseek） |
| JWT_SECRET_KEY | `change-me-in-env` | JWT 签名密钥 |
| JWT_ALGORITHM | `HS256` | JWT 算法 |
| ACCESS_TOKEN_EXPIRE_MINUTES | `10080` (7天) | Token 过期时间 |
| UPLOAD_DIR | `/opt/steiner-reader/uploads` | 上传文件目录 |
| APP_NAME | `Steiner Reader` | 应用名称 |
| DEBUG | `False` | 调试模式 |

### 5.3 数据库层 — `backend/app/db/`

#### database.py — 连接与会话管理

- **`engine`**：基于 `create_async_engine` 的异步引擎，使用 asyncpg 驱动
- **`async_session`**：`async_sessionmaker` 工厂，生成 `AsyncSession` 实例
- **`Base`**：SQLAlchemy `DeclarativeBase`，所有 ORM 模型的基类
- **`get_db()`**：FastAPI 依赖注入函数，提供自动提交/回滚的数据库会话

```python
async def get_db():
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
```

#### models.py — ORM 模型

6 个 SQLAlchemy ORM 模型，与数据库表一一对应：

| 模型 | 表名 | 关键关系 |
|------|------|----------|
| `Book` | books | → lectures (1:N), → translation_jobs (1:N) |
| `Lecture` | lectures | → book (N:1), → paragraphs (1:N), → images (1:N), 自引用 parent/children |
| `Paragraph` | paragraphs | → lecture (N:1), → sentences (1:N) |
| `Sentence` | sentences | → paragraph (N:1) |
| `LectureImage` | lecture_images | → lecture (N:1) |
| `User` | users | 独立表 |

**关键设计点**：
- `Lecture.parent_id` 自引用实现树形目录结构
- `Lecture.level` 字段区分 "heading"（标题节点）和 "lecture"（内容节点）
- 所有外键设置 `CASCADE` 删除，确保数据一致性
- `LectureImage.after_sentence_id` 实现图片在句子间的精确定位

### 5.4 数据模型 — `backend/app/models/schemas.py`

Pydantic V2 模型，用于 API 请求/响应验证。采用分层设计：

**句子层**：
- `SentenceBase` → `SentenceCreate` / `SentenceResponse`

**段落层**：
- `ParagraphBase` → `ParagraphResponse`（包含嵌套 sentences 列表）

**章节层**：
- `LectureBase` → `LectureCreate` / `LectureResponse`（完整内容，含段落）
- `LectureListItem`（轻量，用于目录页，含统计数）
- `LectureSummary`（摘要，含段落数/句子数/图片数/翻译数）

**书籍层**：
- `BookBase` → `BookCreate` / `BookResponse`（含 lecture 摘要）
- `BookSummary`（首页紧凑展示，含统计数）
- `BookDetail`（目录页，含 LectureListItem 列表）

**翻译层**：
- `TranslationJobResponse` / `TranslateRequest`

**性能优化设计**：
- `BookSummary` 使用原生 SQL CTE 查询，避免 N+1 问题
- `LectureListItem` 不包含段落/句子数据，仅含统计计数
- `LectureResponse` 才包含完整段落和句子数据（仅阅读页使用）

### 5.5 路由模块 — `backend/app/routers/`

#### auth.py — 认证路由 (`/api/auth`)

| 端点 | 方法 | 说明 | 认证 |
|------|------|------|------|
| `/api/auth/register` | POST | 用户注册 | 无 |
| `/api/auth/login` | POST | 用户登录 | 无 |
| `/api/auth/me` | GET | 获取当前用户信息 | 必需 |

**关键函数**：

| 函数 | 说明 |
|------|------|
| `create_token(data)` | 生成 JWT Token，设置过期时间 |
| `get_current_user(token, db)` | 从 JWT 解析用户，返回 `User` 或 `None` |
| `require_user(user)` | 要求已登录，否则 401 |
| `require_admin(user)` | 要求管理员权限，否则 403 |

**认证流程**：
1. 用户注册/登录 → 返回 JWT Token + 用户信息
2. 前端存储 Token 到 `localStorage`
3. 后续请求通过 `Authorization: Bearer <token>` 携带
4. `OAuth2PasswordBearer` 自动提取 Token

#### books.py — 书籍路由 (`/api/books`)

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/books/summary` | GET | 首页书籍摘要（CTE 优化查询） |
| `/api/books` | GET | 完整书籍列表（含讲座摘要） |
| `/api/books/{book_id}` | GET | 书籍详情（含讲座列表+翻译统计） |
| `/api/books/{book_id}/lectures/{lecture_id}` | GET | 讲座完整内容（含段落+句子+图片） |

**关键设计**：
- `/summary` 使用 4 个 CTE（lecture_counts, sentence_counts, translated_counts, image_counts）一次性聚合统计，避免 N+1 查询
- 讲座内容端点同时查询 `lecture_images` 表，构建 `sentence_id → image_url` 映射，实现图片与句子的关联展示

#### lectures.py — 章节路由 (`/api/lectures`)

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/lectures/{lecture_id}/paragraphs` | GET | 获取讲座所有段落（含句子+图片） |
| `/api/lectures/{lecture_id}` | GET | 获取讲座基本信息（无段落） |

**关键函数**：

| 函数 | 说明 |
|------|------|
| `_build_paragraph_response(para, image_map)` | 构建 `ParagraphResponse`，包含句子列表、内容拼接、图片映射 |

#### paragraphs.py — 段落路由 (`/api/paragraphs`)

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/paragraphs/{paragraph_id}/sentences` | GET | 获取段落的所有句子 |

#### translate.py — 翻译路由 (`/api`)

| 端点 | 方法 | 说明 | 认证 |
|------|------|------|------|
| `/api/lectures/{lecture_id}/translate` | POST | 触发讲座翻译 | 必需（消耗积分） |
| `/api/lectures/{lecture_id}/translation-cost` | GET | 查询翻译费用 | 可选 |
| `/api/lectures/{lecture_id}/translation-status` | GET | 查询翻译进度 | 无 |

**翻译流程**：
1. 检查是否已在翻译中（`_running_tasks` 集合防重复）
2. 计算未翻译句子数
3. 检查用户积分（每讲座 10 点）
4. 扣除积分
5. 使用 `asyncio.create_task` 启动后台翻译
6. 后台任务每 20 句提交一次数据库（防止崩溃丢失）
7. 前端通过 `/translation-status` 轮询进度

**关键函数**：

| 函数 | 说明 |
|------|------|
| `_do_translate_lecture(lecture_id)` | 后台翻译任务，批量翻译+批量提交 |

#### images.py — 图片路由 (`/api`)

| 端点 | 方法 | 说明 |
|------|------|------|
| `/api/books/{book_id}/images` | GET | 获取书籍图片列表 |
| `/api/lectures/{lecture_id}/images` | GET | 获取讲座图片列表 |
| `/api/images/{ga_dir}/{filename}` | GET | 静态图片文件服务 |

**关键函数**：

| 函数 | 说明 |
|------|------|
| `_resolve_image_path(ga_dir, filename)` | 解析图片路径，支持文件名模糊匹配 |
| `get_ga_dir(ga_number)` | 将 GA 编号转为目录名（如 "225" → "GA225"） |

#### admin.py — 管理员路由 (`/api/admin`)

| 端点 | 方法 | 说明 | 认证 |
|------|------|------|------|
| `/api/admin/users` | GET | 获取用户列表 | 管理员 |
| `/api/admin/users/{user_id}/credits` | PUT | 设置用户积分 | 管理员 |
| `/api/admin/users/{user_id}/add-credits` | POST | 增加用户积分 | 管理员 |
| `/api/admin/lectures/{lecture_id}/retranslate` | POST | 重新翻译讲座 | 管理员 |
| `/api/admin/lectures/{lecture_id}/translation-stats` | GET | 翻译统计 | 管理员 |

**管理员翻译工具** — `backend/app/routers/admin_translation_utils.py`：

| 函数 | 说明 |
|------|------|
| `get_lecture_sentences(db, lecture_id, clear_existing)` | 获取待翻译句子，可选清除已有翻译 |
| `translate_sentences_batch(sentences, german_texts)` | 批量翻译并更新数据库 |
| `admin_retranslate_lecture(db, lecture_id, clear_existing, force_all)` | 管理员重翻译主函数 |

### 5.6 服务层 — `backend/app/services/`

#### translator.py — 翻译服务

基于 `deep-translator` 库的 Google Translate 免费接口。

| 函数 | 说明 |
|------|------|
| `translate_sentence_sync(text_de)` | 同步翻译单句（德→中） |
| `translate_sentence_async(text_de)` | 异步包装，使用 `run_in_executor` |
| `translate_lecture_sentences(sentences, batch_size)` | 批量翻译，逐句调用，300ms 限速 |

**设计特点**：
- 使用 `run_in_executor` 避免阻塞事件循环
- 逐句翻译（非批量 API），每句间隔 300ms 防止被限速
- 翻译失败时返回原文作为 fallback

#### pdf_parser.py — PDF 解析服务

将 PDF 解析为 `Book → Lecture → Paragraph → Sentence` 层级结构。

**数据模型**（dataclass）：

| 类 | 说明 |
|------|------|
| `Sentence` | 德语句子文本 + 序号 |
| `Paragraph` | 句子列表 + 序号 |
| `Lecture` | 标题/日期/地点 + 段落列表 + 序号 |
| `Book` | 标题/GA号 + 讲座列表 |

**核心函数**：

| 函数 | 说明 |
|------|------|
| `parse_pdf(pdf_path, progress_callback)` | 主解析函数，逐页处理，内存优化 |
| `split_into_sentences(text)` | 德语句子分割（spaCy 或正则 fallback） |
| `split_into_paragraphs(text)` | 按双换行分割段落 |
| `clean_text(text)` | 清理 PDF 提取文本（去脚注、连字符修复） |
| `detect_lecture_header_from_text(text)` | 检测讲座标题（德语序数词+日期+地点） |
| `book_to_dict(book)` | 序列化为字典 |
| `get_stats(book)` | 获取解析统计 |

**正则模式**：

| 模式 | 用途 |
|------|------|
| `DATE_LOCATION_RE` | 匹配德语日期+地点（如 "Berlin, 15. Januar 1910"） |
| `LECTURE_ORDINAL_RE` | 匹配德语序数词讲座标题（如 "ERSTER VORTRAG"） |
| `GA_RE` | 匹配 GA 编号 |
| `PAGE_NUM_RE` | 过滤纯页码行 |
| `FOOTNOTE_RE` | 过滤脚注标记 |

**内存优化**：
- 逐页处理，处理完一页立即释放
- 每 10 页触发 `gc.collect()`
- 跳过前 5 页（前言部分）
- 仅提取文本，不保留字符级数据
- spaCy 已禁用（`get_nlp()` 返回 None），使用正则 fallback 以节省内存

---

## 6. 前端模块详解

### 6.1 页面路由

| 路由 | 文件 | 说明 |
|------|------|------|
| `/` | `app/page.tsx` | 首页 — 书籍列表 + 搜索 |
| `/books/[bookId]` | `app/books/[bookId]/page.tsx` | 书籍详情 — 目录树 |
| `/books/[bookId]/lectures/[lectureId]` | `app/books/[bookId]/lectures/[lectureId]/page.tsx` | 阅读器 — 段落/句子展示 |
| `/login` | `app/login/page.tsx` | 登录/注册 |
| `/upload` | `app/upload/page.tsx` | 文件上传 |
| `/admin` | `app/admin/page.tsx` | 管理员面板 |

### 6.2 页面详解

#### 首页 (`/`) — `app/page.tsx`

- 调用 `fetchBookSummaries()` 获取书籍摘要列表
- 支持按 GA 编号、德语书名、中文书名搜索过滤（`useMemo` 优化）
- 展示统计信息：总书籍数、总章节数、总句子数
- `BookCard` 组件展示每本书的摘要信息（GA编号标签、书名、章节数/句子数/图片数）
- 加载中显示 shimmer 骨架屏动画

#### 书籍详情页 (`/books/[bookId]`) — `app/books/[bookId]/page.tsx`

- 调用 `fetchBook(bookId)` 获取书籍详情和讲座列表
- **树形目录**：`buildTree()` 函数将扁平讲座列表转为树形结构
  ```typescript
  function buildTree(lectures: Lecture[]): TreeLecture[] {
    const map = new Map<number, TreeLecture>();
    const roots: TreeLecture[] = [];
    for (const lecture of lectures) {
      map.set(lecture.id, { ...lecture, children: [] });
    }
    for (const lecture of lectures) {
      const node = map.get(lecture.id)!;
      if (lecture.parent_id && map.has(lecture.parent_id)) {
        map.get(lecture.parent_id)!.children.push(node);
      } else {
        roots.push(node);
      }
    }
    return roots;
  }
  ```
- `LectureNode` 组件递归渲染树节点，区分 heading 和 lecture 类型
- heading 节点使用 `section-heading` / `sub-heading` 样式
- lecture 节点可点击跳转到阅读器，显示句子数/图片数/翻译进度

#### 阅读器页 (`/books/[bookId]/lectures/[lectureId]`) — `app/books/[bookId]/lectures/[lectureId]/page.tsx`

核心阅读页面，功能最复杂：

- **三种阅读模式**：`de-zh`（德中对照）、`de-only`（仅德语）、`zh-only`（仅中文）
- **翻译触发**：未翻译时显示翻译按钮，消耗积分
- **翻译进度轮询**：3 秒间隔轮询 `/translation-status`，完成后自动刷新
- **句子交互**：
  - 点击显示/隐藏中文翻译
  - 双击切换翻译显示
  - 德语模式下悬停显示"译"标记
- **图片展示**：`ImageView` 组件支持点击放大查看（全屏遮罩层）
- `SentenceView` 组件根据模式渲染不同布局
- 段落编号显示（§1, §1.1 格式）

**关键组件**：

| 组件 | 说明 |
|------|------|
| `LecturePage` | 主页面组件，管理数据加载、翻译状态、阅读模式 |
| `SentenceView` | 句子渲染组件，根据模式切换德语/中文/对照显示 |
| `ImageView` | 图片查看组件，支持缩略图+全屏放大 |
| `LoadingSkeleton` | 加载骨架屏 |

#### 登录页 (`/login`) — `app/login/page.tsx`

- 登录/注册双模式切换（Tab 切换 UI）
- 注册赠送 100 积分
- 认证成功后存储 Token 到 `localStorage`
- 触发 `auth-changed` 自定义事件通知 Header 更新

#### 上传页 (`/upload`) — `app/upload/page.tsx`

- 支持拖拽和点击上传 EPUB/DOCX 文件
- 多文件批量上传
- 上传后显示解析结果（GA 编号、章节数）
- 文件列表管理（添加/移除）

#### 管理员页 (`/admin`) — `app/admin/page.tsx`

- 用户列表展示（用户名、邮箱、积分、角色、注册时间）
- 积分管理：设置（PUT）和充值（POST）
- 需要管理员权限（`is_admin = 1`）
- 无权限时自动跳转登录页

### 6.3 API 客户端 — `frontend/lib/api.ts`

集中管理所有后端 API 调用，包含：

**TypeScript 接口定义**：

| 接口 | 对应后端模型 |
|------|-------------|
| `Sentence` | `SentenceResponse` |
| `Paragraph` | `ParagraphResponse` |
| `Lecture` | `LectureResponse` / `LectureListItem` |
| `Book` | `BookResponse` |
| `BookSummary` | `BookSummary` |
| `User` | `UserResponse` |
| `AuthResponse` | `TokenResponse` |
| `TranslationCost` | 翻译费用响应 |
| `TranslationStatus` | 翻译状态响应 |
| `TranslateResult` | 翻译触发响应 |
| `LectureImage` | 讲座图片 |

**API 函数**：

| 函数 | 端点 | 认证 |
|------|------|------|
| `fetchBooks()` | GET /api/books | 无 |
| `fetchBookSummaries()` | GET /api/books/summary | 无 |
| `fetchBook(bookId)` | GET /api/books/{id} | 无 |
| `fetchLecture(id)` / `fetchLecture(bookId, lectureId)` | GET /api/lectures/{id} 或 /api/books/{bid}/lectures/{lid} | 无 |
| `fetchParagraphs(lectureId)` | GET /api/lectures/{id}/paragraphs | 无 |
| `fetchSentences(paragraphId)` | GET /api/paragraphs/{id}/sentences | 无 |
| `uploadPdf(file)` | POST /api/books/upload | 必需 |
| `register(username, email, password)` | POST /api/auth/register | 无 |
| `login(username, password)` | POST /api/auth/login | 无 |
| `fetchMe()` | GET /api/auth/me | 必需 |
| `getTranslationCost(lectureId)` | GET /api/lectures/{id}/translation-cost | 可选 |
| `getTranslationStatus(lectureId)` | GET /api/lectures/{id}/translation-status | 无 |
| `translateLecture(lectureId)` | POST /api/lectures/{id}/translate | 必需 |
| `fetchLectureImages(lectureId)` | GET /api/lectures/{id}/images | 无 |

**认证机制**：
- `getToken()`：从 `localStorage` 读取 JWT Token
- `authHeaders()`：构建带 Authorization 的请求头
- `authFetch()`：自动附加认证头的 fetch 封装
- `saveAuth(data)`：存储 Token 和用户信息
- `clearAuth()`：清除认证信息
- `getStoredUser()`：从 localStorage 读取缓存的用户信息

**API 基础 URL**：
- 通过 `NEXT_PUBLIC_API_BASE` 或 `NEXT_PUBLIC_API_URL` 环境变量配置
- 开发环境由 Next.js rewrites 代理到 `http://127.0.0.1:8000`
- 生产环境由 Nginx 统一代理

### 6.4 全局组件

#### Header.tsx — 导航栏

- 品牌标识 "Steiner Reader" + 副标题 "施泰纳著作"
- 登录状态显示：用户名 + 积分（琥珀色标签）
- 管理员入口（仅 `is_admin` 用户可见，紫色样式）
- 上传入口
- 登录/退出按钮
- 初始化时通过 `fetchMe()` 验证 Token 有效性，失败则清除认证

### 6.5 设计系统 — `frontend/app/globals.css`

基于 Tailwind CSS 4 的自定义设计系统：

| 类名 | 用途 |
|------|------|
| `.page-container` | 页面容器（max-w-5xl 居中） |
| `.card` | 卡片组件（白底圆角阴影，hover 增强） |
| `.section-heading` | 章节标题（indigo→blue 渐变背景） |
| `.sub-heading` | 子标题（sky→cyan 浅色渐变，左缩进） |
| `.btn-primary` | 主按钮（indigo 色，hover/active/focus 状态） |
| `.btn-secondary` | 次按钮（白色边框） |
| `.reader-german` | 德语阅读排版（深色、宽松行距） |
| `.reader-chinese` | 中文阅读排版（浅色、小字号） |
| `.shimmer` | 加载骨架屏动画（2s 循环渐变） |

**色彩系统**：
- 品牌色：Steiner Slate（slate 灰阶 50-900）
- 强调色：Indigo（按钮/交互）、Gold（高亮）
- 语义色：Success（绿）、Warning（琥珀）、Danger（红）

**字体系统**：
- Sans: "Inter", "Noto Sans SC", system-ui
- Serif: "Lora", "Noto Serif SC", Georgia

### 6.6 Next.js 配置 — `frontend/next.config.ts`

```typescript
async rewrites() {
  return [{
    source: '/api/:path*',
    destination: 'http://127.0.0.1:8000/api/:path*',
  }];
}
```

开发环境下将 `/api/*` 请求代理到 FastAPI 后端，解决跨域问题。

---

## 7. API 接口文档

### 7.1 完整接口列表

#### 认证接口

| 方法 | 路径 | 说明 | 请求体 | 响应 |
|------|------|------|--------|------|
| POST | `/api/auth/register` | 用户注册 | `{username, email, password}` | `{access_token, user}` |
| POST | `/api/auth/login` | 用户登录 | `{username, password}` | `{access_token, user}` |
| GET | `/api/auth/me` | 当前用户 | — | `{id, username, email, credits, is_admin}` |

#### 书籍接口

| 方法 | 路径 | 说明 | 响应 |
|------|------|------|------|
| GET | `/api/books/summary` | 书籍摘要列表 | `BookSummary[]` |
| GET | `/api/books` | 完整书籍列表 | `BookResponse[]` |
| GET | `/api/books/{book_id}` | 书籍详情 | `BookDetail` |
| GET | `/api/books/{book_id}/lectures/{lecture_id}` | 讲座完整内容 | `{id, paragraphs, ...}` |

#### 章节接口

| 方法 | 路径 | 说明 | 响应 |
|------|------|------|------|
| GET | `/api/lectures/{lecture_id}` | 讲座基本信息 | `{id, title_de, ...}` |
| GET | `/api/lectures/{lecture_id}/paragraphs` | 段落列表（含句子） | `ParagraphResponse[]` |

#### 段落接口

| 方法 | 路径 | 说明 | 响应 |
|------|------|------|------|
| GET | `/api/paragraphs/{paragraph_id}/sentences` | 句子列表 | `SentenceResponse[]` |

#### 翻译接口

| 方法 | 路径 | 说明 | 认证 | 响应 |
|------|------|------|------|------|
| POST | `/api/lectures/{lecture_id}/translate` | 触发翻译 | 必需 | `{status, cost, credits}` |
| GET | `/api/lectures/{lecture_id}/translation-cost` | 翻译费用 | 可选 | `{total, cost, can_afford}` |
| GET | `/api/lectures/{lecture_id}/translation-status` | 翻译进度 | 无 | `{total, translated, completed}` |

#### 图片接口

| 方法 | 路径 | 说明 | 响应 |
|------|------|------|------|
| GET | `/api/books/{book_id}/images` | 书籍图片列表 | `[{id, filename, url}]` |
| GET | `/api/lectures/{lecture_id}/images` | 讲座图片列表 | `[{id, filename, url}]` |
| GET | `/api/images/{ga_dir}/{filename}` | 图片文件 | `FileResponse` |

#### 管理员接口

| 方法 | 路径 | 说明 | 认证 | 响应 |
|------|------|------|------|------|
| GET | `/api/admin/users` | 用户列表 | 管理员 | `{users, total}` |
| PUT | `/api/admin/users/{id}/credits` | 设置积分 | 管理员 | `{success, new_credits}` |
| POST | `/api/admin/users/{id}/add-credits` | 增加积分 | 管理员 | `{success, added, new_credits}` |
| POST | `/api/admin/lectures/{id}/retranslate` | 重翻译 | 管理员 | `{newly_translated, action_taken}` |
| GET | `/api/admin/lectures/{id}/translation-stats` | 翻译统计 | 管理员 | `{total, translated, ratio}` |

#### 系统接口

| 方法 | 路径 | 说明 | 响应 |
|------|------|------|------|
| GET | `/` | 应用信息 | `{app, status}` |
| GET | `/health` | 健康检查 | `{status: "ok"}` |

---

## 8. 数据流与核心流程

### 8.1 文献导入流程

```
PDF/EPUB/DOCX 文件
    │
    ├── [scripts/] 离线导入脚本
    │   ├── individual/all_189/GA*_import.py   # 每本书独立脚本
    │   ├── epub/GA*_import.py                 # EPUB 格式导入
    │   └── bdn_import/                        # BDN 批量导入
    │
    └── [前端上传] /upload 页面
        │
        ▼
    POST /api/books/upload (FormData)
        │
        ▼
    pdf_parser.parse_pdf() 或 DOCX 解析
        │
        ├── 识别 GA 编号、书名
        ├── 检测讲座标题（德语序数词+日期+地点）
        ├── 分割段落（双换行）
        ├── 分割句子（正则 fallback）
        │
        ▼
    写入数据库: Book → Lectures → Paragraphs → Sentences
```

### 8.2 翻译流程

```
用户点击"翻译本章"
    │
    ▼
POST /api/lectures/{id}/translate
    │
    ├── 检查重复（_running_tasks）
    ├── 计算未翻译句子数
    ├── 检查积分（10 点/讲座）
    ├── 扣除积分
    │
    ▼
asyncio.create_task(_do_translate_lecture)
    │
    ├── 加载讲座+段落+句子
    ├── 筛选 text_zh IS NULL 的句子
    │
    ▼
逐批翻译（每 20 句一批）
    │
    ├── translate_lecture_sentences(batch)
    │   ├── 逐句调用 Google Translate
    │   ├── 300ms 限速
    │   └── 失败返回原文
    │
    ├── 更新 sentence.text_zh
    └── db.commit()（每批提交）
    │
    ▼
前端轮询 GET /api/lectures/{id}/translation-status
    │
    └── completed=true → 刷新页面
```

### 8.3 认证流程

```
注册/登录
    │
    ▼
POST /api/auth/register 或 /api/auth/login
    │
    ├── 验证用户名/密码
    ├── bcrypt 密码验证
    │
    ▼
生成 JWT Token (HS256, 7天有效)
    │
    ▼
返回 {access_token, user}
    │
    ▼
前端存储到 localStorage:
    ├── steiner_token → JWT Token
    └── steiner_user → 用户信息 JSON
    │
    ▼
后续请求: Authorization: Bearer <token>
    │
    ▼
get_current_user() 解析 Token → 查询用户
```

### 8.4 前端状态管理

项目采用 React 原生 `useState` + `useEffect` 管理状态，无全局状态管理库。

**认证状态**：
- `localStorage.steiner_token`：JWT Token
- `localStorage.steiner_user`：用户信息 JSON
- `Header` 组件通过 `getStoredUser()` + `fetchMe()` 初始化
- Token 失效时自动清除认证信息

**页面数据**：
- 每个页面组件独立获取数据（`useEffect` + `fetch`）
- 无缓存策略（`cache: 'no-store'`）

**翻译状态**：
- `translating` 布尔值控制 UI 状态
- `setInterval` 轮询翻译进度（3 秒间隔）
- 完成后 `clearInterval` 并刷新数据
- `useRef` 存储 interval 引用，组件卸载时清理

**阅读模式**：
- `ReadingMode` 类型：`'de-zh' | 'de-only' | 'zh-only'`
- `showTranslation` Set 记录用户手动展开翻译的句子 ID
- `SentenceView` 组件根据 mode 和 showZh 状态渲染不同布局

---

## 9. 部署与运维

### 9.1 Docker Compose 部署

```bash
# 设置环境变量
cp .env.example .env
# 编辑 .env 设置 DB_PASSWORD, JWT_SECRET_KEY 等

# 启动所有服务
docker-compose up -d

# 服务端口
# Nginx: 80
# Frontend: 3000 (内部)
# Backend: 8000 (内部)
# PostgreSQL: 5432 (内部)
```

**Docker Compose 服务**：

| 服务 | 镜像 | 端口 | 依赖 |
|------|------|------|------|
| nginx | nginx:alpine | 80:80 | frontend, backend |
| frontend | 自建 (Next.js) | 3000 (内部) | — |
| backend | 自建 (FastAPI) | 8000 (内部) | db |
| db | postgres:16 | 5432 (内部) | — |

**数据卷**：
- `pgdata`：PostgreSQL 数据持久化
- `uploads`：上传文件持久化

**数据库初始化**：
- `init.sql` 通过 Docker volume 挂载到 `/docker-entrypoint-initdb.d/`
- 首次启动时自动执行，创建基础表结构

### 9.2 裸机部署 (systemd)

后端服务配置 — `deploy/systemd/steiner-backend.service`：

```ini
[Unit]
Description=Steiner Reader FastAPI backend
After=network-online.target postgresql.service

[Service]
Type=simple
WorkingDirectory=/opt/steiner-reader/backend
ExecStart=/usr/bin/python3 -m uvicorn app.main:app --host 127.0.0.1 --port 8000
Restart=always
RestartSec=5
StandardOutput=append:/var/log/steiner-reader/backend.log
StandardError=append:/var/log/steiner-reader/backend-error.log
```

前端服务配置 — `deploy/systemd/steiner-frontend.service`：

```ini
[Unit]
Description=Steiner Reader Next.js frontend
After=network-online.target steiner-backend.service

[Service]
Type=simple
WorkingDirectory=/opt/steiner-reader/frontend
Environment=NODE_ENV=production
ExecStart=/usr/bin/npm start -- --hostname 127.0.0.1 --port 3000
Restart=always
RestartSec=5
StandardOutput=append:/var/log/steiner-reader/frontend.log
StandardError=append:/var/log/steiner-reader/frontend-error.log
```

### 9.3 Nginx 配置

关键路由规则：

| 路径 | 代理目标 | 说明 |
|------|----------|------|
| `/api/` | `http://backend:8000` | API 请求 |
| `/health` | `http://backend:8000` | 健康检查 |
| `/` | `http://frontend:3000` | 前端页面 |

- 最大上传大小：50MB（`client_max_body_size 50m`）
- 支持 WebSocket 升级（Next.js HMR）
- 代理头设置：Host, X-Real-IP, X-Forwarded-For, X-Forwarded-Proto

### 9.4 环境变量

| 变量 | 必需 | 说明 |
|------|------|------|
| `DATABASE_URL` | 是 | PostgreSQL 连接串 |
| `DB_PASSWORD` | 是 (Docker) | 数据库密码 |
| `JWT_SECRET_KEY` | 是 | JWT 签名密钥 |
| `JWT_ALGORITHM` | 否 | JWT 算法（默认 HS256） |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | 否 | Token 过期时间（默认 10080 = 7天） |
| `UPLOAD_DIR` | 否 | 上传目录（默认 /opt/steiner-reader/uploads） |
| `TRANSLATION_PROVIDER` | 否 | 翻译提供商（mock/openai/deepl/libretranslate） |
| `TRANSLATION_BATCH_SIZE` | 否 | 翻译批大小（默认 8） |
| `TRANSLATION_SLEEP_SECONDS` | 否 | 翻译请求间隔（默认 1.0s） |
| `DEEPSEEK_API_KEY` | 否 | DeepSeek 翻译 API Key |
| `DEEPSEEK_BASE_URL` | 否 | DeepSeek API 地址 |
| `OPENAI_API_KEY` | 否 | OpenAI 翻译 API Key |
| `OPENAI_TRANSLATION_MODEL` | 否 | OpenAI 翻译模型 |
| `DEEPL_API_KEY` | 否 | DeepL API Key |
| `DEEPL_API_URL` | 否 | DeepL API 地址 |
| `LIBRETRANSLATE_URL` | 否 | LibreTranslate 自托管地址 |
| `LIBRETRANSLATE_API_KEY` | 否 | LibreTranslate API Key |

### 9.5 开发环境启动

```bash
# 后端
cd backend
pip install -r requirements.txt
python -m spacy download de_core_news_sm
uvicorn app.main:app --reload --port 8000

# 前端
cd frontend
npm install
npm run dev    # 默认端口 3000，自动代理 /api → localhost:8000
```

---

## 10. 脚本工具集

`scripts/` 目录包含大量数据导入和批处理脚本，用于将施泰纳著作数据导入数据库。

### 10.1 导入脚本分类

| 目录 | 说明 | 数量 |
|------|------|------|
| `scripts/individual/all_189/` | 每本书的独立导入脚本（GA001-GA354） | ~180 个 |
| `scripts/epub/` | EPUB 格式导入脚本 | ~120 个 |
| `scripts/single/` | 单本书特殊处理脚本 | 3 个 |
| `scripts/bdn_import/` | BDN 批量导入（首批/图片/PDF/修复） | 4 个 |

### 10.2 核心工具脚本

| 脚本 | 说明 |
|------|------|
| `batch_import.py` | 通用批量导入 |
| `batch_translate.py` / `v2` / `v3` | 批量翻译（多版本迭代，v3 使用 ThreadPoolExecutor 并发） |
| `smart_import.py` / `v3` | 智能导入（自动检测格式：Heading样式/全大写标题/TOC目录） |
| `download_pdfs.py` / `.sh` / `_v2.sh` | PDF 下载工具 |
| `pdf_lecture_parser.py` / `_v2.py` | PDF 讲座解析器（多版本） |
| `lecture_parser.py` / `_v2.py` | 通用讲座解析器 |
| `docx_analyzer.py` | DOCX 文件分析器 |
| `epub_import_generator.py` | EPUB 导入脚本生成器 |
| `import_script_generator.py` | 导入脚本生成器 |
| `analyze_books.py` / `_v2.py` | 书籍数据分析 |
| `toc_parser.py` | 目录解析器 |
| `translate_titles.py` | 标题翻译 |
| `translate_worker.py` | 翻译工作进程（按 ID 范围处理，支持多进程并行） |
| `finish_translation.py` | 完成翻译任务 |
| `fix_translation_*.py` | 翻译修复脚本 |
| `resume_translation.py` | 恢复中断的翻译任务 |
| `patch_sentence_splitter.py` | 句子分割器补丁 |
| `backup_database.sh` | 数据库备份 |

### 10.3 后端解析脚本

| 脚本 | 说明 |
|------|------|
| `backend/parse_docx_v2.py` ~ `v5.py` | DOCX 解析器（多版本迭代） |
| `backend/parse_standalone.py` | 独立解析脚本 |

### 10.4 翻译脚本架构

批量翻译脚本经历了多个版本迭代：

- **v1** (`batch_translate.py`)：基础顺序翻译
- **v2** (`batch_translate_v2.py`)：改进的批量处理
- **v3** (`batch_translate_v3.py`)：使用 `ThreadPoolExecutor` 并发翻译，8 个 worker，每个 worker 0.4s 限速
- **translate_worker.py**：独立工作进程，按句子 ID 范围处理，支持多进程并行部署

---

## 11. 关键设计决策

1. **异步优先**：后端全面使用 `async/await` + `asyncpg`，确保高并发性能
2. **层级目录**：`lectures` 表自引用实现树形结构，支持"部分→章节→演讲"多级目录
3. **积分制翻译**：每讲座 10 点，防止滥用，管理员可充值
4. **批量提交**：翻译任务每 20 句提交一次，防止崩溃丢失全部进度
5. **防重复翻译**：`_running_tasks` 集合跟踪正在翻译的讲座
6. **CTE 优化**：首页摘要使用 PostgreSQL CTE 一次聚合，避免 N+1 查询
7. **图片精确定位**：`after_sentence_id` 实现图片在句子间的精确插入
8. **内存优化**：PDF 解析逐页处理，定期 GC，spaCy 禁用以节省内存
9. **前端无状态库**：使用 React 原生状态管理，避免引入额外复杂度
10. **API 代理**：Next.js rewrites 解决开发环境跨域，生产环境由 Nginx 统一代理
11. **多翻译引擎支持**：后端配置支持 Google/DeepSeek/OpenAI/DeepL/LibreTranslate 多种翻译引擎
12. **脚本化数据导入**：大量独立导入脚本实现 350+ 本 GA 系列著作的批量导入，支持 DOCX/EPUB/PDF 多格式
