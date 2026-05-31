# Steiner Reader Web — 交接文档

**生成日期**: 2026-05-31  
**项目地址**: https://steiner.3mudi.com  
**代码仓库**: https://github.com/rainberg/steiner-reader

---

## 一、项目概述

Steiner Reader 是一个鲁道夫·施泰纳（Rudolf Steiner）德语著作的在线阅读平台，提供德中双语对照阅读、AI 翻译、积分付费、PDF 下载等功能。

### 技术栈
- **前端**: Next.js 16 (Turbopack) + TypeScript + Tailwind CSS
- **后端**: FastAPI + SQLAlchemy (async) + PostgreSQL
- **认证**: 独立 auth-service（JWT），后端通过 HTTP 调用验证
- **部署**: Cloudcone VPS (66.154.112.162) + Cloudflare CDN + Nginx
- **AI 翻译**: 通过外部翻译 API 批量翻译德语句子
- **测试**: pytest + pytest-asyncio（30 个测试，SQLite 内存数据库）

### 生产环境
- **服务器**: 66.154.112.162，SSH as root，密码 `3Ai9px4N5p`
- **后端**: systemd `steiner-backend` — uvicorn on 127.0.0.1:8000
- **前端**: systemd `steiner-frontend` — Next.js on 127.0.0.1:3000
- **数据库**: PostgreSQL，用户 `steiner`，数据库 `steiner_reader`，密码 `Dd08120@`
- **部署命令**:
  ```bash
  # 推荐：git pull 方式部署
  plink -ssh root@66.154.112.162 -pw "3Ai9px4N5p" "cd /opt/steiner-reader && git fetch origin && git reset --hard origin/main && systemctl restart steiner-backend.service && cd frontend && npm run build && systemctl restart steiner-frontend.service"

  # 备用：pscp 传输方式
  pscp -r -pw "3Ai9px4N5p" backend\app root@66.154.112.162:/opt/steiner-reader/backend/
  plink -ssh root@66.154.112.162 -pw "3Ai9px4N5p" "systemctl restart steiner-backend.service"
  pscp -r -pw "3Ai9px4N5p" frontend\app root@66.154.112.162:/opt/steiner-reader/frontend/
  pscp -pw "3Ai9px4N5p" frontend\lib\api.ts root@66.154.112.162:/opt/steiner-reader/frontend/lib/api.ts
  plink -ssh root@66.154.112.162 -pw "3Ai9px4N5p" "cd /opt/steiner-reader/frontend && npm run build && systemctl restart steiner-frontend.service"
  ```

---

## 二、核心功能实现状态

### ✅ 已完成功能

| # | 功能 | 实现说明 |
|---|------|---------|
| 1 | **翻译付费墙** | 用户消费积分才能看到翻译内容；`is_published=true` 时翻译对所有用户免费可见；管理员也需付费 |
| 2 | **翻译进度轮询** | 前端每 3 秒轮询 `translation-status` API，显示 `translated/total` 进度 + `is_running` 状态 |
| 3 | **already_translated 处理** | 当翻译已存在于数据库时，后端返回 `already_translated`，前端刷新页面显示翻译内容 |
| 4 | **贡献记录** | `contributions` 表记录翻译/下载/修订贡献，含 `display_name`/`book_id`/`cost`/`grants_download` 字段 |
| 5 | **下载权限管理** | `grant_access`/`check_download_access` 统一管理，翻译贡献者自动获得下载权限 |
| 6 | **积分系统** | `reserve_credits`/`settle_credits`/`refund_credits`/`atomic_deduct_credits` 完整实现 |
| 7 | **充值系统** | `recharge_requests` 表 + 充值审核流程（上传支付截图→管理员审核→通过 auth-service API 加积分） |
| 8 | **管理员页面** | 用户管理（列表/切换管理员/删除）、充值审核、标题管理 |
| 9 | **认证集成** | auth-service JWT 验证 + `display_name` fallback 到 `/api/auth/me` + `is_admin` 字段 |
| 10 | **积分同步** | Header 使用 React state + storage 事件 + `updateStoredCredits` 函数同步积分 |
| 11 | **缓存破坏** | `translation-status` API 返回 `Cache-Control: no-store` + 前端 `_t=Date.now()` |
| 12 | **PDF 下载** | reportlab 中德双语 PDF 生成 + `download-pdf` 端点 + 前端对接 |
| 13 | **句子修订** | 用户可消费积分修改译文，`edits.py` 实现修订逻辑 |
| 14 | **translation_publications 三态表** | `translating`/`published`/`failed` 三态，替代 `is_published` 布尔字段，已回填 33 条已发布讲座 |
| 15 | **user_translation_jobs 持久化** | 替代内存变量 `_running_tasks`，翻译状态持久化到数据库，服务器重启不丢失 |
| 16 | **孤儿任务检测** | running 超过 30 分钟的 job 自动标记为 failed，每次翻译请求时自动执行 |
| 17 | **积分显示统一** | Header/Profile/讲座页面统一显示可用积分（`credits - credits_reserved`），有冻结时额外提示 |
| 18 | **自动化测试** | pytest + pytest-asyncio，30 个测试全部通过 |

### ⚠️ 部分实现功能

| # | 功能 | 当前状态 | 缺失部分 |
|---|------|---------|---------|
| 1 | **翻译进度由后端驱动** | 前端轮询 `translation-status` 获取进度 | 进度来自实时翻译计数，非 `user_translation_jobs.total_sentences/completed_sentences` 驱动 |
| 2 | **is_published 双写** | 翻译时同时更新 `Lecture.is_published` 和 `TranslationPublication` | 尚未完全切换到只读 `TranslationPublication`，`Lecture.is_published` 仍被前端使用 |

### ❌ 未实现功能

| # | 功能 | 说明 |
|---|------|------|
| 1 | **translation_publications 完全替代 is_published** | 前端仍从 `Lecture.is_published` 判断翻译可见性，应改为从 `TranslationPublication` 读取 |
| 2 | **translation-cost 接口扩展** | 设计文档要求返回 `translation_published`/`download_cost`/`translated_in_database` 等字段 |
| 3 | **display_name 回填** | 已有贡献记录的 `display_name` 可能为空，需用 admin 凭证调用 auth-service API 回填 |
| 4 | **翻译进度由 job 表驱动** | `user_translation_jobs` 有 `total_sentences`/`completed_sentences` 字段但未在翻译过程中更新 |

---

## 三、本轮修复和新增内容（2026-05-31）

### 🔴 高优先级 — 已完成

| # | 功能 | 修改文件 | 说明 |
|---|------|---------|------|
| 1 | **TranslationPublication 三态表** | `models.py`, `translation_service.py`, `translate.py` | `translating`/`published`/`failed` 替代 `is_published` 布尔字段 |
| 2 | **UserTranslationJob 持久化** | `models.py`, `translation_service.py`, `translate.py` | 替代 `_running_tasks`/`_running_task_info` 内存变量 |
| 3 | **孤儿任务检测** | `translation_service.py` | `detect_orphan_jobs()`，running 超过 30 分钟自动标记为 failed |
| 4 | **translation-status is_running** | `translate.py` | 新增 `is_running` 字段从数据库查询 |
| 5 | **PDF 下载** | `pdf_generator.py`, `downloads.py`, `page.tsx`, `api.ts` | reportlab 中德双语 PDF 生成 + 前端对接 |

### 🟡 中优先级 — 已完成

| # | 功能 | 修改文件 | 说明 |
|---|------|---------|------|
| 6 | **compute_price 默认值回退** | `credit_service.py` | 新增 `default: Decimal \| None = None` 参数 |
| 7 | **add_contribution 死代码清理** | `credit_service.py`, `translate.py`, `downloads.py`, `edits.py` | 移除未使用的 `amount: Decimal` 参数 |
| 8 | **fetchLecture/fetchParagraphs 改为 authFetch** | `api.ts` | 四个函数改用 `authFetch` 携带 Authorization header |
| 9 | **my_recharge_requests datetime 序列化** | `recharge.py` | `.isoformat()` 序列化 |
| 10 | **积分显示统一** | `auth.py`, `Header.tsx`, `profile/page.tsx`, `api.ts` | 统一显示可用积分（`credits - credits_reserved`） |
| 11 | **自动化测试** | `pytest.ini`, `conftest.py`, 5 个测试文件 | 30 个测试全部通过 |

### 🐛 BUG 修复

| # | 文件 | BUG 描述 |
|---|------|---------|
| 1 | `models.py` | `TranslationPublication`/`UserTranslationJob` 模型与生产数据库表结构不匹配（缺少 `book_id`/`scope`/`mode` 等字段），已对齐 |
| 2 | `translate.py` | `set_publication_status`/`start_translation_job` 缺少 `book_id` 参数，已补充 |
| 3 | `Header.tsx` | 状态栏显示总积分而非可用积分，与讲座页面不一致，已修复 |
| 4 | `auth.py` | `/api/auth/me` 未返回 `credits_reserved`，前端无法计算可用积分，已修复 |

---

## 四、数据库结构

### 核心表

| 表名 | 说明 | 关键字段 |
|------|------|---------|
| `books` | 书籍 | `id`, `ga_number`, `title_de`, `title_zh` |
| `lectures` | 讲座 | `id`, `book_id`, `title_de`, `title_zh`, `is_published`, `is_translating`, `translate_progress`, `translate_total` |
| `paragraphs` | 段落 | `id`, `lecture_id`, `order_index` |
| `sentences` | 句子 | `id`, `paragraph_id`, `text_de`, `text_zh`, `order_index` |
| `contributions` | 贡献记录 | `id`, `user_id`(varchar36), `lecture_id`, `contribution_type`, `display_name`, `book_id`, `cost`, `grants_download` |
| `recharge_requests` | 充值请求 | `id`, `user_id`(varchar36), `amount`, `coefficient`, `payment_image`, `status`(pending/approved/rejected) |
| `lecture_access` | 访问权限 | `user_id`, `lecture_id`, `access_type` |
| `credit_settings` | 积分设置 | `action`, `price` |
| `translation_jobs` | 翻译任务（旧，按书） | `id`, `book_id`, `status` |
| **`translation_publications`** | **翻译发布状态（新）** | `id`, `lecture_id`, `book_id`, `scope`, `status`(translating/published/failed), `first_contributor_user_id`, `published_at`, `error_message` |
| **`user_translation_jobs`** | **用户翻译任务（新）** | `id`, `user_id`, `lecture_id`, `book_id`, `mode`, `status`(pending/running/completed/failed), `total_sentences`, `completed_sentences`, `error_message` |

### 注意事项
- `user_id` 字段从 Integer 迁移到了 String(36)（UUID），因为 auth-service 使用 UUID
- `contributions.display_name` 可能为空（旧记录未回填）
- `translation_publications` 已回填 33 条已发布讲座数据
- `user_translation_jobs` 当前为空（0 行），新翻译任务会自动写入
- 生产数据库的 `translation_publications` 和 `user_translation_jobs` 表结构与 models.py 已完全对齐

---

## 五、认证系统

### 架构
- 独立 auth-service，运行在不同端口
- 后端通过 HTTP 调用 auth-service 验证 JWT
- 前端 localStorage 存储 `access_token`（JWT）和 `auth_user`（用户信息 JSON）

### 关键 API
- `POST /api/auth/login` — 登录
- `POST /api/auth/verify` — 验证 token（**不返回 display_name**）
- `GET /api/auth/me` — 获取完整用户信息（**返回 display_name, credits, credits_reserved**）
- `POST /api/admin/users/{id}/add-credits` — 管理员加积分

### 积分计算
- **总积分**: `credits`（auth-service 返回）
- **冻结积分**: `credits_reserved`（翻译任务 reserve 后冻结）
- **可用积分**: `credits - credits_reserved`（前端统一显示此值）
- Header、Profile、讲座页面均显示可用积分

### 已知问题
- `/api/auth/verify` 不返回 `display_name`，后端需要 fallback 到 `/api/auth/me`
- 前端 `fetchMe` 需要从 `role === 'admin'` 派生 `is_admin` 字段
- localStorage key 从 `steiner_token` 迁移到 `access_token`，`steiner_user` 迁移到 `auth_user`

---

## 六、文件结构说明

### 后端关键文件
```
backend/app/
├── main.py              # FastAPI 应用入口，路由注册
├── config.py            # 配置（数据库 URL、auth-service URL）
├── db/
│   ├── database.py      # 数据库连接
│   └── models.py        # SQLAlchemy 模型（含 TranslationPublication、UserTranslationJob）
├── models/
│   └── schemas.py       # Pydantic 模型
├── routers/
│   ├── auth.py          # 认证路由（JWT 验证、display_name fallback、credits_reserved 返回）
│   ├── books.py         # 书籍/讲座/下载权限 API
│   ├── lectures.py      # 讲座详情 API
│   ├── translate.py     # 翻译 API（核心：翻译任务、进度、扣费、job 持久化）
│   ├── downloads.py     # 下载 API（购买下载权限、PDF 下载、贡献者列表）
│   ├── edits.py         # 句子修订 API
│   ├── admin.py         # 管理员 API（用户管理、充值审核、标题管理）
│   ├── recharge.py      # 充值 API（充值请求、审核）
│   └── ...
└── services/
    ├── auth_client.py        # auth-service HTTP 客户端
    ├── credit_service.py     # 积分服务（扣费、贡献、访问权限、compute_price 默认值回退）
    ├── translation_service.py # 翻译服务（job 持久化、孤儿检测、发布状态管理）
    ├── pdf_generator.py      # PDF 生成服务（reportlab 中德双语）
    └── translator.py         # 翻译服务（外部 API 调用）
```

### 前端关键文件
```
frontend/
├── lib/api.ts           # API 客户端（authFetch、积分同步、类型定义、downloadLecturePdf）
├── app/
│   ├── components/
│   │   └── Header.tsx   # 顶部导航（可用积分显示、管理链接、充值入口）
│   ├── admin/page.tsx   # 管理员页面（用户管理、充值审核）
│   ├── login/page.tsx   # 登录页面
│   ├── profile/page.tsx # 个人中心（可用积分 + 冻结提示）
│   ├── recharge/page.tsx # 充值页面
│   └── books/[bookId]/lectures/[lectureId]/page.tsx  # 讲座阅读页（核心，PDF 下载）
```

### 测试文件
```
backend/tests/
├── conftest.py                  # SQLite 内存数据库 fixture
├── test_credit_service.py       # 5 tests（compute_price + add_contribution）
├── test_translation_models.py   # 7 tests（TranslationPublication + UserTranslationJob 模型）
├── test_translation_service.py  # 13 tests（job 持久化、孤儿检测、发布状态）
├── test_pdf_generator.py        # 3 tests（PDF 生成）
└── test_recharge.py             # 2 tests（datetime 序列化）
```

### 迁移脚本
```
scripts/
├── migrate_translation_tables.sql  # 回填 translation_publications 数据
└── migrate_users.sql               # 用户迁移脚本
```

---

## 七、下一步改善建议

### 🔴 高优先级

1. **translation_publications 完全替代 is_published** — 前端仍从 `Lecture.is_published` 判断翻译可见性，应改为从 `TranslationPublication` 读取。当前是双写状态（同时更新两者）。

2. **翻译进度由 job 表驱动** — `user_translation_jobs` 有 `total_sentences`/`completed_sentences` 字段，但翻译过程中未更新这些字段。应在 `_do_translate_lecture` 的每个 batch 完成后更新 `completed_sentences`。

3. **display_name 回填** — 已有贡献记录的 `display_name` 可能为空，需用 admin 凭证调用 auth-service API 回填。

### 🟡 中优先级

4. **translation-cost 接口扩展** — 返回 `translation_published`/`download_cost`/`translated_in_database` 等字段，让前端能区分"已发布"和"翻译中"状态。

5. **充值审核页面用户名查询性能** — 当前逐个用户查询 auth-service，当充值记录多时会很慢。建议批量查询或缓存。

6. **前端 is_running 状态展示** — 前端已使用 `is_running` 字段判断翻译状态，但 UI 上未区分"翻译中"和"翻译失败"状态，应增加失败重试按钮。

### 🟢 低优先级

7. **清理临时文件** — 项目根目录有大量临时脚本和 `.bak` 文件，应添加到 `.gitignore` 或删除。

8. **贡献者显示优化** — 当多个用户贡献同一讲座时，应聚合显示。

9. **PDF 中文字体回退** — `pdf_generator.py` 尝试加载 WenQuanYiMicroHei，如不存在则回退到 Windows 微软雅黑。生产服务器已确认有 WenQuanYiMicroHei。

---

## 八、Git 提交记录

最近 5 次提交：

```
164bcbd fix: 积分显示统一为可用积分(credits - credits_reserved)
3107878 fix: 迁移脚本对齐生产表结构（book_id, first_contributor_user_id）
e0d07f0 fix: 模型对齐生产数据库表结构
67d5864 feat: translation_publications三态表 + user_translation_jobs持久化 + PDF下载 + BUG修复 + 测试
ebad545 fix: 移除状态栏上传链接 + 修复admin页面userId类型为string
```

---

## 九、测试

### 运行测试
```bash
cd backend
python -m pytest tests/ -v
```

### 测试覆盖
- **test_credit_service** (5 tests): `compute_price` 默认值回退、`add_contribution` 无 amount 参数
- **test_translation_models** (7 tests): `TranslationPublication`/`UserTranslationJob` 模型创建、状态值、默认值、孤儿检测
- **test_translation_service** (13 tests): `is_lecture_running`、`start/complete/fail_translation_job`、`detect_orphan_jobs`、`get/set_publication_status`
- **test_pdf_generator** (3 tests): PDF 生成（正常/缺中文/空讲座）
- **test_recharge** (2 tests): datetime 序列化为 ISO 格式

### 测试基础设施
- `pytest.ini`: `asyncio_mode = auto`
- `conftest.py`: SQLite 内存数据库 fixture（`sqlite+aiosqlite:///:memory:`）
- 所有测试独立运行，不依赖外部服务
