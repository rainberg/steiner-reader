# Steiner 阅读平台 实施计划

> **架构:** 单VPS (Nginx + Next.js 前端 + FastAPI 后端 + PostgreSQL)

## 目标

构建一个帮助阅读和翻译鲁道夫·施泰纳著作的 Web 平台。
- 上传文字型 PDF → 自动解析结构 (书 → 演讲 → 段落 → 句子)
- 句子级德语→中文翻译
- 三种阅读模式: 德中对照 / 仅中文 / 仅德语
- 多用户支持 (付费系统后续接入)

## 技术栈

| 层级 | 技术 |
|------|------|
| 前端 | Next.js 14 (App Router) + Tailwind CSS |
| 后端 API | FastAPI (Python) |
| PDF 解析 | pdfplumber + spaCy (de_core_news_sm) |
| 翻译 | api2d.net (OpenAI 兼容) |
| 数据库 | PostgreSQL (本机) |
| ORM | SQLAlchemy (Python) + Prisma (Next.js) |
| 反向代理 | Nginx |
| 部署 | 单VPS (Docker Compose) |

## 项目结构

```
steiner-reader/
├── frontend/                  # Next.js 前端 (Vercel)
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx           # 首页/书架
│   │   ├── books/
│   │   │   └── [bookId]/
│   │   │       ├── page.tsx   # 书籍详情/演讲列表
│   │   │       └── lectures/
│   │   │           └── [lectureId]/
│   │   │               └── page.tsx  # 阅读界面
│   │   ├── upload/
│   │   │   └── page.tsx       # 上传PDF
│   │   └── api/               # Next.js API Routes (轻量)
│   │       └── auth/          # 用户认证 (后续)
│   ├── components/
│   │   ├── Reader.tsx         # 阅读器核心组件
│   │   ├── ReadingModeToggle.tsx  # 阅读模式切换
│   │   ├── BookCard.tsx       # 书籍卡片
│   │   ├── SentenceView.tsx   # 句子展示
│   │   └── Navbar.tsx
│   ├── lib/
│   │   ├── prisma.ts
│   │   └── api.ts             # 后端 API 客户端
│   ├── prisma/
│   │   └── schema.prisma
│   └── package.json
│
├── backend/                   # Python 后端服务
│   ├── app/
│   │   ├── main.py            # FastAPI 入口
│   │   ├── routers/
│   │   │   ├── books.py       # 书籍 CRUD
│   │   │   ├── upload.py      # PDF 上传 + 解析
│   │   │   └── translate.py   # 翻译触发
│   │   ├── services/
│   │   │   ├── pdf_parser.py  # PDF 结构解析
│   │   │   ├── sentence_split.py  # 句子分割
│   │   │   └── translator.py  # 翻译服务
│   │   ├── models/
│   │   │   └── schemas.py     # Pydantic 数据模型
│   │   └── db/
│   │       ├── database.py    # 数据库连接
│   │       └── models.py      # SQLAlchemy 模型
│   ├── requirements.txt
│   └── Dockerfile
│
└── PLAN.md                    # 本文件
```

## 数据库设计

```sql
-- 书籍 (GA 编号级别)
CREATE TABLE books (
    id            SERIAL PRIMARY KEY,
    ga_number     VARCHAR(20),           -- e.g. "GA 115"
    title_de      TEXT NOT NULL,         -- 德语书名
    title_zh      TEXT,                  -- 中文书名 (可选)
    pdf_filename  TEXT NOT NULL,         -- 原始PDF文件名
    cover_url     TEXT,                  -- 封面图
    created_at    TIMESTAMP DEFAULT NOW()
);

-- 演讲/章节
CREATE TABLE lectures (
    id            SERIAL PRIMARY KEY,
    book_id       INTEGER REFERENCES books(id) ON DELETE CASCADE,
    title_de      TEXT,                  -- 演讲标题 (如有)
    lecture_date  DATE,                  -- 演讲日期
    location      VARCHAR(200),          -- 演讲地点
    order_index   INTEGER NOT NULL,      -- 顺序
    created_at    TIMESTAMP DEFAULT NOW()
);

-- 段落
CREATE TABLE paragraphs (
    id            SERIAL PRIMARY KEY,
    lecture_id    INTEGER REFERENCES lectures(id) ON DELETE CASCADE,
    order_index   INTEGER NOT NULL,
    created_at    TIMESTAMP DEFAULT NOW()
);

-- 句子 (翻译的最小单元)
CREATE TABLE sentences (
    id            SERIAL PRIMARY KEY,
    paragraph_id  INTEGER REFERENCES paragraphs(id) ON DELETE CASCADE,
    order_index   INTEGER NOT NULL,
    text_de       TEXT NOT NULL,          -- 德语原文
    text_zh       TEXT,                   -- 中文翻译 (NULL = 未翻译)
    created_at    TIMESTAMP DEFAULT NOW()
);

-- 翻译任务 (追踪翻译状态)
CREATE TABLE translation_jobs (
    id            SERIAL PRIMARY KEY,
    book_id       INTEGER REFERENCES books(id) ON DELETE CASCADE,
    status        VARCHAR(20) DEFAULT 'pending',  -- pending/running/completed/failed
    total_sentences   INTEGER,
    translated_count  INTEGER DEFAULT 0,
    error_message TEXT,
    created_at    TIMESTAMP DEFAULT NOW(),
    updated_at    TIMESTAMP DEFAULT NOW()
);
```

## API 设计

### 后端 API (FastAPI, port 8000)

```
POST   /api/books/upload          # 上传PDF，触发结构解析
GET    /api/books                  # 获取所有书籍列表
GET    /api/books/{id}             # 获取书籍详情 + 演讲列表
GET    /api/books/{id}/lectures/{lecture_id}  # 获取演讲内容(句子)
POST   /api/books/{id}/translate   # 触发翻译 (按需)
GET    /api/jobs/{id}              # 查询翻译进度
```

### 前端 API Route (Next.js, 轻量代理)

```
/api/books                         # 代理到后端
/api/books/[id]/translate          # 代理翻译请求
```

## 核心用户流程

```
用户上传 PDF
    │
    ▼
系统解析结构（免费）
    ├── 识别演讲/段落/句子
    ├── 存储德语原文
    └── 向用户展示：仅德语可读
    │
    ▼
用户触发翻译（未来付费触发）
    │
    ▼
系统逐句翻译（句子级，异步任务）
    ├── 翻译完成，存入数据库
    └── 用户可读德中对照 / 仅中文 / 仅德语
```

## VPS 部署架构 (Docker Compose)

```
                    ┌─────────────────────────────┐
                    │           VPS               │
                    │                             │
  用户 ──HTTPS──▶   │  Nginx (:80/443)            │
                    │    ├── / → Next.js (:3000)  │
                    │    └── /api → FastAPI (:8000)│
                    │                             │
                    │  Next.js 容器 (:3000)        │
                    │  FastAPI 容器 (:8000)        │
                    │  PostgreSQL 容器 (:5432)     │
                    │                             │
                    └─────────────────────────────┘
```

```yaml
# docker-compose.yml (示意)
services:
  nginx:
    image: nginx:alpine
    ports: ["80:80", "443:443"]
    volumes:
      - ./nginx.conf:/etc/nginx/conf.d/default.conf
      - /etc/letsencrypt:/etc/letsencrypt  # HTTPS证书

  frontend:
    build: ./frontend
    expose: ["3000"]

  backend:
    build: ./backend
    expose: ["8000"]
    environment:
      - DATABASE_URL=postgresql://steiner:password@db:5432/steiner_reader
      - API2D_API_KEY=${API2D_API_KEY}
    volumes:
      - ./uploads:/app/uploads  # PDF文件持久化

  db:
    image: postgres:16
    environment:
      POSTGRES_DB: steiner_reader
      POSTGRES_USER: steiner
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

## 实施阶段

### 阶段一: 后端核心 (PDF解析 + 数据库)
1. 初始化 Python 后端项目 (FastAPI)
2. 设计数据库模型 (SQLAlchemy)
3. 实现 PDF 解析服务 (pdfplumber)
4. 实现句子分割 (spaCy)
5. 实现翻译服务 (api2d.net)
6. 实现 API 路由

### 阶段二: 前端 (Next.js)
7. 初始化 Next.js 项目
8. 实现书籍列表页
9. 实现阅读器组件 (三种模式)
10. 实现 PDF 上传页
11. 实现翻译触发 + 进度显示

### 阶段三: 联调 + 部署
12. 前后端联调
13. 编写 Docker Compose 配置 (前端+后端+PostgreSQL+Nginx)
14. VPS 部署 (Docker Compose up)
15. Nginx 反向代理配置 (域名 + HTTPS)
16. 端到端测试

### 阶段四: 支付 (后续)
17. 集成支付宝/微信支付
18. 用户系统
19. 按书付费逻辑
