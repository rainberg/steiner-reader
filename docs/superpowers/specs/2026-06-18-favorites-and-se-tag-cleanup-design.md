# 讲座收藏与翻译标识清理设计

- **日期**: 2026-06-18
- **状态**: 已批准
- **范围**: Steiner Reader Web（后端 + 前端 + 数据清理脚本）

## 背景

用户提出两个需求：

1. **收藏单篇讲座**：当前系统无任何收藏功能。用户希望在阅读讲座时可以收藏，并在独立页面查看收藏列表。
2. **清理翻译标识**：数据库中 14,613 条句子的中文翻译（`text_zh`）嵌入了 `#SE数字-数字` 格式的源文档引用标识（如 `#SE190-012`），这些标识是 PDF 解析时被错误保留的，需要从译文文本中清除。用户明确要求**不修改翻译流程**，只做一次性数据清理。

## 目标

- 用户可在讲座阅读页一键收藏/取消收藏
- 收藏列表在独立页面 `/favorites` 展示，导航栏加入口
- 收藏数据存储在 steiner-reader 数据库，跨设备同步
- 一次性清除所有 `#SE数字-数字` 标识，不改动翻译代码

## 非目标

- 不支持收藏整本书（仅收藏单篇讲座）
- 不修改 translator.py 或 translate.py 的翻译流程
- 不做收藏分组、标签、笔记等扩展功能
- 不做收藏排序选项（按收藏时间倒序即可）

## 架构

### 数据存储

收藏数据存储在 steiner-reader 的 PostgreSQL（与讲座数据同库），通过 `user_id`（auth 服务的 UUID 字符串）关联用户。用户身份通过现有 `require_user` 依赖注入获取，该依赖调用 auth 服务验证 JWT 并返回 `AuthUser`（含 `id` 字段）。

### 认证流程

```
前端 → steiner-backend /api/favorites
         ↓ require_user 依赖
         → auth-service /api/auth/verify（验证 JWT）
         ← 返回 user_id (UUID 字符串)
         ← AuthUser.id
```

复用现有认证机制，无需新建认证逻辑。

## 详细设计

### 功能一：收藏讲座

#### 1.1 数据库模型

新建 `user_favorites` 表（在 `backend/app/db/models.py` 添加）：

```python
class UserFavorite(Base):
    __tablename__ = "user_favorites"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), nullable=False, index=True)  # auth 服务 UUID
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    lecture = relationship("Lecture", foreign_keys=[lecture_id])

    __table_args__ = (
        UniqueConstraint("user_id", "lecture_id", name="uq_user_lecture_favorite"),
    )
```

- `user_id` 用 VARCHAR(36) 存储 UUID 字符串（与 auth 服务一致，不建外键，因 users 表在另一数据库）
- `lecture_id` 外键关联 lectures，讲座删除时级联删除收藏
- 唯一约束防止重复收藏

#### 1.2 后端 API

新建 `backend/app/routers/favorites.py`，前缀 `/api/favorites`：

| 方法 | 路径 | 功能 | 认证 |
|------|------|------|------|
| POST | `/api/favorites/{lecture_id}` | 收藏讲座 | require_user |
| DELETE | `/api/favorites/{lecture_id}` | 取消收藏 | require_user |
| GET | `/api/favorites` | 获取收藏列表 | require_user |
| GET | `/api/favorites/{lecture_id}/status` | 查询单个讲座收藏状态 | require_user |

**POST /api/favorites/{lecture_id}**
- 若已收藏，返回 200（幂等）
- 若讲座不存在或非 lecture 类型，返回 404
- 响应：`{"favorited": true, "lecture_id": 123}`

**DELETE /api/favorites/{lecture_id}**
- 若未收藏，返回 200（幂等）
- 响应：`{"favorited": false, "lecture_id": 123}`

**GET /api/favorites**
- 查询参数：`page`（默认1）、`page_size`（默认20，最大50）
- 返回收藏的讲座列表（按收藏时间倒序），每项包含：lecture_id、title_de、title_zh、book_id、book_title_de、book_ga_number、lecture_date、favorited_at
- 响应：`{"items": [...], "total": 42, "page": 1, "page_size": 20}`

**GET /api/favorites/{lecture_id}/status**
- 响应：`{"favorited": true}` 或 `{"favorited": false}`
- 用于阅读页初始化收藏按钮状态

在 `backend/app/main.py` 注册路由。

#### 1.3 前端

**API 客户端**（`frontend/lib/api.ts`）新增函数：
- `addFavorite(lectureId: number): Promise<{favorited: boolean}>`
- `removeFavorite(lectureId: number): Promise<{favorited: boolean}>`
- `fetchFavorites(page?, pageSize?): Promise<FavoriteListResponse>`
- `fetchFavoriteStatus(lectureId: number): Promise<{favorited: boolean}>`

新增类型：
```typescript
export interface FavoriteItem {
  lecture_id: number;
  title_de: string | null;
  title_zh: string | null;
  book_id: number;
  book_title_de: string;
  book_ga_number: string | null;
  lecture_date: string | null;
  favorited_at: string;
}

export interface FavoriteListResponse {
  items: FavoriteItem[];
  total: number;
  page: number;
  page_size: number;
}
```

**阅读页收藏按钮**（`frontend/app/books/[bookId]/lectures/[lectureId]/page.tsx`）：
- 在讲座标题旁加星标按钮（☆/★ 切换）
- 页面加载时调用 `fetchFavoriteStatus` 初始化状态
- 点击调用 `addFavorite`/`removeFavorite`，乐观更新 UI
- 未登录时点击跳转登录页

**收藏列表页**（新建 `frontend/app/favorites/page.tsx`）：
- 展示收藏的讲座列表，每项显示：书名（GA编号）、讲座标题、日期、收藏时间
- 点击跳转到讲座阅读页
- 支持分页（每页20条）
- 空状态提示"暂无收藏"
- 未登录跳转登录页

**导航栏入口**（`frontend/app/components/Header.tsx`）：
- 登录后显示"我的收藏"链接，指向 `/favorites`
- 与现有的"个人中心"等链接并列

### 功能二：清理翻译标识

#### 2.1 清理脚本

新建 `backend/scripts/clean_se_tags.py`：

- 连接 steiner-reader 数据库
- 用 SQL 正则替换清除 `text_zh` 中的 `#SE数字-数字` 标识
- 处理标识前后的多余空格（如"身体#SE190-018身体"→"身体身体"，"有机体#SE190-029为"→"有机体为"）
- 清理规则：
  1. 删除 `#SE\d+-\d+` 模式
  2. 合并标识位置前后多余的空格为单个空格（若标识在句中）
  3. 删除标识后的行首空格（若标识在句末）
- 先执行 SELECT 统计影响范围，再执行 UPDATE
- 输出清理前后的样例对比，便于验证

#### 2.2 清理逻辑

```sql
-- PostgreSQL 正则替换
UPDATE sentences
SET text_zh = btrim(regexp_replace(text_zh, '\s*#SE\d+-\d+\s*', ' ', 'g'))
WHERE text_zh ~ '#SE\d+-\d+';
```

- `\s*#SE\d+-\d+\s*` 匹配标识及前后空白
- 替换为单个空格，避免前后词粘连
- `btrim` 去除首尾可能残留的空格

#### 2.3 验证

清理后执行验证查询：
- `SELECT COUNT(*) FROM sentences WHERE text_zh ~ '#SE'` 应返回 0
- 抽样检查清理后的句子文本是否通顺

## 错误处理

- **收藏不存在的讲座**：POST 返回 404
- **未登录访问收藏 API**：返回 401（由 `require_user` 处理）
- **数据库唯一约束冲突**（并发收藏同一讲座）：捕获后返回 200（幂等）
- **清理脚本**：先备份受影响句子的原始 text_zh 到临时表，出错可回滚

## 测试

项目无测试框架，采用手动验证：

1. **收藏功能**：
   - 登录后在阅读页点击收藏，刷新页面状态保持
   - 在 `/favorites` 页面查看收藏列表
   - 取消收藏后列表更新
   - 未登录访问 `/favorites` 跳转登录

2. **翻译标识清理**：
   - 清理前查询 14,613 条
   - 清理后查询 0 条
   - 抽样检查 10 条清理后的文本

## 部署

1. 后端：rsync 同步代码，重启 steiner-backend 服务
2. 前端：rsync 同步代码，npm run build，重启 steiner-frontend 服务
3. 数据库：执行清理脚本（生产环境，先备份）
4. 新表 `user_favorites` 由 SQLAlchemy 自动创建（或手动执行 DDL）

## 影响范围

- **新增文件**：
  - `backend/app/routers/favorites.py`
  - `frontend/app/favorites/page.tsx`
  - `backend/scripts/clean_se_tags.py`
- **修改文件**：
  - `backend/app/db/models.py`（新增 UserFavorite 模型）
  - `backend/app/main.py`（注册 favorites 路由）
  - `frontend/lib/api.ts`（新增收藏 API 函数和类型）
  - `frontend/app/books/[bookId]/lectures/[lectureId]/page.tsx`（加收藏按钮）
  - `frontend/app/components/Header.tsx`（加导航入口）
- **数据库**：新增 `user_favorites` 表，清理 `sentences.text_zh` 中 14,613 条记录
