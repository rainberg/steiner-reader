# 讲座收藏与翻译标识清理实现计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 为 Steiner Reader 添加讲座收藏功能（前后端），并一次性清理数据库中 14,613 条句子的 `#SE数字-数字` 翻译标识。

**Architecture:** 后端新建 `user_favorites` 表和 `/api/favorites` 路由（复用现有 `require_user` 认证依赖）；前端在阅读页加星标按钮，新建 `/favorites` 列表页，导航栏加入口；翻译标识用独立 SQL 脚本一次性清理。

**Tech Stack:** FastAPI + SQLAlchemy 2 (async) + PostgreSQL（后端）；Next.js + TypeScript + Tailwind CSS（前端）；psycopg2（清理脚本）

---

## 文件结构

**新增文件：**
- `backend/app/routers/favorites.py` — 收藏 API 路由（POST/DELETE/GET/status）
- `frontend/app/favorites/page.tsx` — 收藏列表页
- `backend/scripts/clean_se_tags.py` — 翻译标识清理脚本

**修改文件：**
- `backend/app/db/models.py` — 新增 `UserFavorite` 模型
- `backend/app/main.py` — 注册 favorites 路由
- `frontend/lib/api.ts` — 新增收藏 API 函数和类型
- `frontend/app/books/[bookId]/lectures/[lectureId]/page.tsx` — 标题旁加收藏按钮
- `frontend/app/components/Header.tsx` — 导航栏加"我的收藏"入口

---

### Task 1: 新增 UserFavorite 数据库模型

**Files:**
- Modify: `backend/app/db/models.py`

- [ ] **Step 1: 在 models.py 末尾添加 UserFavorite 模型**

在 `backend/app/db/models.py` 文件末尾追加：

```python
class UserFavorite(Base):
    __tablename__ = "user_favorites"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), nullable=False, index=True)
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    lecture = relationship("Lecture", foreign_keys=[lecture_id])

    __table_args__ = (
        UniqueConstraint("user_id", "lecture_id", name="uq_user_lecture_favorite"),
    )
```

需要在文件顶部的 import 中确认 `UniqueConstraint` 已导入。检查现有 import：
```python
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Date, Boolean, Numeric
```
需添加 `UniqueConstraint`：
```python
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Date, Boolean, Numeric, UniqueConstraint
```

- [ ] **Step 2: 在生产数据库创建 user_favorites 表**

SSH 到生产服务器执行 DDL（避免依赖 SQLAlchemy 自动创建）：

```bash
ssh -i C:\Users\Administrator\.ssh\id_rsa root@66.154.112.162 "PGPASSWORD='Dd08120@' psql -U steiner -h localhost -d steiner_reader -c \"
CREATE TABLE IF NOT EXISTS user_favorites (
    id SERIAL PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    lecture_id INTEGER NOT NULL REFERENCES lectures(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(user_id, lecture_id)
);
CREATE INDEX IF NOT EXISTS ix_user_favorites_user_id ON user_favorites(user_id);
\""
```

- [ ] **Step 3: 验证表创建成功**

```bash
ssh -i C:\Users\Administrator\.ssh\id_rsa root@66.154.112.162 "PGPASSWORD='Dd08120@' psql -U steiner -h localhost -d steiner_reader -c '\d user_favorites'"
```

预期输出：显示表结构，包含 id、user_id、lecture_id、created_at 字段和唯一约束。

- [ ] **Step 4: Commit**

```bash
git add backend/app/db/models.py
git commit -m "feat(favorites): add UserFavorite model"
```

---

### Task 2: 后端收藏 API 路由

**Files:**
- Create: `backend/app/routers/favorites.py`
- Modify: `backend/app/main.py`

- [ ] **Step 1: 创建 favorites.py 路由文件**

创建 `backend/app/routers/favorites.py`：

```python
"""Favorites API router — user lecture favorites."""

import logging
from datetime import datetime
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, func, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.db.database import get_db
from app.db.models import UserFavorite, Lecture, Book
from app.models.schemas import FavoriteItem, FavoriteListResponse, FavoriteStatusResponse
from app.routers.auth import require_user, AuthUser

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/favorites", tags=["favorites"])


@router.post("/{lecture_id}")
async def add_favorite(
    lecture_id: int,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """收藏讲座（幂等：已收藏则返回成功）"""
    # 验证讲座存在且为 lecture 类型
    lecture = await db.get(Lecture, lecture_id)
    if not lecture or lecture.level != "lecture":
        raise HTTPException(status_code=404, detail="讲座不存在")

    # 检查是否已收藏
    existing = await db.execute(
        select(UserFavorite).where(
            UserFavorite.user_id == user.id,
            UserFavorite.lecture_id == lecture_id,
        )
    )
    if existing.scalar_one_or_none():
        return {"favorited": True, "lecture_id": lecture_id}

    # 创建收藏
    favorite = UserFavorite(
        user_id=user.id,
        lecture_id=lecture_id,
    )
    db.add(favorite)
    try:
        await db.commit()
    except IntegrityError:
        # 并发情况下唯一约束冲突，视为已收藏
        await db.rollback()
    return {"favorited": True, "lecture_id": lecture_id}


@router.delete("/{lecture_id}")
async def remove_favorite(
    lecture_id: int,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """取消收藏（幂等：未收藏则返回成功）"""
    await db.execute(
        delete(UserFavorite).where(
            UserFavorite.user_id == user.id,
            UserFavorite.lecture_id == lecture_id,
        )
    )
    await db.commit()
    return {"favorited": False, "lecture_id": lecture_id}


@router.get("")
async def list_favorites(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=20, ge=1, le=50),
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """获取收藏列表（按收藏时间倒序）"""
    # 计算总数
    count_query = select(func.count()).select_from(UserFavorite).where(
        UserFavorite.user_id == user.id
    )
    total = (await db.execute(count_query)).scalar() or 0

    # 查询收藏列表（关联讲座和书）
    offset = (page - 1) * page_size
    query = (
        select(
            UserFavorite.lecture_id,
            UserFavorite.created_at.label("favorited_at"),
            Lecture.id,
            Lecture.title_de,
            Lecture.title_zh,
            Lecture.lecture_date,
            Lecture.book_id,
            Book.title_de.label("book_title_de"),
            Book.ga_number.label("book_ga_number"),
        )
        .join(Lecture, UserFavorite.lecture_id == Lecture.id)
        .join(Book, Lecture.book_id == Book.id)
        .where(UserFavorite.user_id == user.id)
        .order_by(UserFavorite.created_at.desc())
        .offset(offset)
        .limit(page_size)
    )
    result = await db.execute(query)
    rows = result.all()

    items = [
        {
            "lecture_id": row.lecture_id,
            "title_de": row.title_de,
            "title_zh": row.title_zh,
            "book_id": row.book_id,
            "book_title_de": row.book_title_de,
            "book_ga_number": row.book_ga_number,
            "lecture_date": row.lecture_date.isoformat() if row.lecture_date else None,
            "favorited_at": row.favorited_at.isoformat() if row.favorited_at else None,
        }
        for row in rows
    ]

    return {
        "items": items,
        "total": total,
        "page": page,
        "page_size": page_size,
    }


@router.get("/{lecture_id}/status")
async def get_favorite_status(
    lecture_id: int,
    user: AuthUser = Depends(require_user),
    db: AsyncSession = Depends(get_db),
):
    """查询单个讲座的收藏状态"""
    result = await db.execute(
        select(UserFavorite.id).where(
            UserFavorite.user_id == user.id,
            UserFavorite.lecture_id == lecture_id,
        )
    )
    return {"favorited": result.scalar_one_or_none() is not None}
```

- [ ] **Step 2: 在 schemas.py 添加响应模型（可选，当前用 dict 返回）**

由于上述路由直接返回 dict，无需修改 schemas.py。跳过此步。

- [ ] **Step 3: 在 main.py 注册 favorites 路由**

修改 `backend/app/main.py`：

第7行的 import 添加 `favorites`：
```python
from app.routers import books, translate, images, auth, admin, lectures, paragraphs, recharge, downloads, edits, search, catalog, invite, completeness, favorites
```

在 `app.include_router(completeness.router)` 后添加：
```python
app.include_router(favorites.router)
```

- [ ] **Step 4: 部署后端到生产服务器并重启**

```bash
scp -i C:\Users\Administrator\.ssh\id_rsa backend/app/routers/favorites.py root@66.154.112.162:/opt/steiner-reader/backend/app/routers/favorites.py
scp -i C:\Users\Administrator\.ssh\id_rsa backend/app/db/models.py root@66.154.112.162:/opt/steiner-reader/backend/app/db/models.py
scp -i C:\Users\Administrator\.ssh\id_rsa backend/app/main.py root@66.154.112.162:/opt/steiner-reader/backend/app/main.py
ssh -i C:\Users\Administrator\.ssh\id_rsa root@66.154.112.162 "systemctl restart steiner-backend.service && sleep 2 && systemctl is-active steiner-backend.service"
```

预期输出：`active`

- [ ] **Step 5: 验证 API 可访问**

```bash
ssh -i C:\Users\Administrator\.ssh\id_rsa root@66.154.112.162 "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8000/api/favorites -H 'Authorization: Bearer invalid'"
```

预期输出：`401`（未认证，说明路由已注册）

- [ ] **Step 6: Commit**

```bash
git add backend/app/routers/favorites.py backend/app/main.py
git commit -m "feat(favorites): add favorites API router"
```

---

### Task 3: 前端 API 客户端函数

**Files:**
- Modify: `frontend/lib/api.ts`

- [ ] **Step 1: 在 api.ts 添加收藏相关类型和函数**

在 `frontend/lib/api.ts` 文件末尾追加：

```typescript
// --- Favorites ---

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

export async function addFavorite(lectureId: number): Promise<{ favorited: boolean }> {
  const res = await authFetch(`/api/favorites/${lectureId}`, { method: 'POST' });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '收藏失败' }));
    throw new Error(err.detail || '收藏失败');
  }
  return res.json();
}

export async function removeFavorite(lectureId: number): Promise<{ favorited: boolean }> {
  const res = await authFetch(`/api/favorites/${lectureId}`, { method: 'DELETE' });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '取消收藏失败' }));
    throw new Error(err.detail || '取消收藏失败');
  }
  return res.json();
}

export async function fetchFavorites(page: number = 1, pageSize: number = 20): Promise<FavoriteListResponse> {
  const params = new URLSearchParams({ page: String(page), page_size: String(pageSize) });
  const res = await authFetch(`/api/favorites?${params}`, { cache: 'no-store' });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '获取收藏列表失败' }));
    throw new Error(err.detail || '获取收藏列表失败');
  }
  return res.json();
}

export async function fetchFavoriteStatus(lectureId: number): Promise<{ favorited: boolean }> {
  const res = await authFetch(`/api/favorites/${lectureId}/status`, { cache: 'no-store' });
  if (!res.ok) {
    return { favorited: false };
  }
  return res.json();
}
```

- [ ] **Step 2: Commit**

```bash
git add frontend/lib/api.ts
git commit -m "feat(favorites): add frontend API client functions"
```

---

### Task 4: 阅读页收藏按钮

**Files:**
- Modify: `frontend/app/books/[bookId]/lectures/[lectureId]/page.tsx`

- [ ] **Step 1: 添加收藏状态和加载逻辑**

在 `frontend/app/books/[bookId]/lectures/[lectureId]/page.tsx` 中：

1. 在 import 语句中添加 `fetchFavoriteStatus, addFavorite, removeFavorite`：

找到第6-28行的 import 块，在 `updateStoredCredits,` 后添加：
```typescript
  fetchFavoriteStatus, addFavorite, removeFavorite,
```

2. 在 state 声明区域（约第59行 `const [revisionsMap, setRevisionsMap]` 后）添加：
```typescript
  const [isFavorited, setIsFavorited] = useState(false);
  const [favoriteLoading, setFavoriteLoading] = useState(false);
```

3. 在 `loadLecture` 函数内（约第84行 `setLecture(data);` 后）添加收藏状态加载：
```typescript
      // 加载收藏状态
      fetchFavoriteStatus(lectureId)
        .then(status => setIsFavorited(status.favorited))
        .catch(() => {});
```

- [ ] **Step 2: 添加收藏切换处理函数**

在 `loadLecture` 函数后（约第124行后）添加：

```typescript
  const handleToggleFavorite = async () => {
    const token = localStorage.getItem('access_token');
    if (!token) {
      router.push('/login');
      return;
    }
    if (favoriteLoading) return;
    setFavoriteLoading(true);
    const wasFavorited = isFavorited;
    setIsFavorited(!wasFavorited); // 乐观更新
    try {
      if (wasFavorited) {
        await removeFavorite(lectureId);
      } else {
        await addFavorite(lectureId);
      }
    } catch (e) {
      setIsFavorited(wasFavorited); // 回滚
    } finally {
      setFavoriteLoading(false);
    }
  };
```

- [ ] **Step 3: 在标题旁添加收藏按钮**

找到第291行的 `<h1>` 标签，将其替换为带收藏按钮的版本：

原代码：
```tsx
          <h1 className="text-xl font-bold text-slate-900 leading-tight whitespace-pre-line">{lecture.title_de || 'Vortrag'}</h1>
```

替换为：
```tsx
          <div className="flex items-start gap-3">
            <h1 className="text-xl font-bold text-slate-900 leading-tight whitespace-pre-line flex-1">{lecture.title_de || 'Vortrag'}</h1>
            <button
              type="button"
              onClick={handleToggleFavorite}
              disabled={favoriteLoading}
              title={isFavorited ? '取消收藏' : '收藏讲座'}
              className="text-2xl shrink-0 leading-none mt-1 transition-transform hover:scale-110 disabled:opacity-50"
            >
              {isFavorited ? '★' : '☆'}
            </button>
          </div>
```

- [ ] **Step 4: Commit**

```bash
git add frontend/app/books/[bookId]/lectures/[lectureId]/page.tsx
git commit -m "feat(favorites): add favorite button to lecture reader"
```

---

### Task 5: 收藏列表页

**Files:**
- Create: `frontend/app/favorites/page.tsx`

- [ ] **Step 1: 创建收藏列表页**

创建 `frontend/app/favorites/page.tsx`：

```tsx
'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { fetchFavorites, getStoredUser, FavoriteItem } from '@/lib/api';

const PAGE_SIZE = 20;

export default function FavoritesPage() {
  const router = useRouter();
  const [items, setItems] = useState<FavoriteItem[]>([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const load = (p: number) => {
    setLoading(true);
    setError('');
    fetchFavorites(p, PAGE_SIZE)
      .then(data => {
        setItems(data.items);
        setTotal(data.total);
        setPage(data.page);
      })
      .catch(e => setError(e.message || '加载失败'))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    const stored = getStoredUser();
    if (!stored) {
      router.push('/login');
      return;
    }
    load(1);
  }, [router]);

  const totalPages = Math.ceil(total / PAGE_SIZE);

  return (
    <div className="page-container py-8">
      <div className="max-w-4xl mx-auto">
        <div className="flex items-center justify-between mb-6">
          <h1 className="text-xl font-bold text-gray-900">我的收藏</h1>
          <span className="text-sm text-gray-500">共 {total} 篇</span>
        </div>

        {loading ? (
          <p className="text-sm text-gray-400">加载中...</p>
        ) : error ? (
          <div className="bg-red-50 border border-red-100 text-red-600 text-sm px-4 py-3 rounded-lg">
            {error}
          </div>
        ) : items.length === 0 ? (
          <div className="text-center py-16">
            <p className="text-gray-400 text-sm mb-4">暂无收藏</p>
            <Link href="/" className="text-sm text-indigo-600 hover:text-indigo-700">
              浏览讲座去收藏 →
            </Link>
          </div>
        ) : (
          <>
            <div className="space-y-3">
              {items.map(item => (
                <Link
                  key={item.lecture_id}
                  href={`/books/${item.book_id}/lectures/${item.lecture_id}`}
                  className="block card p-4 hover:shadow-md transition-shadow"
                >
                  <div className="flex items-start justify-between gap-3">
                    <div className="flex-1 min-w-0">
                      <h3 className="text-sm font-medium text-gray-900 truncate">
                        {item.title_de || 'Vortrag'}
                      </h3>
                      {item.title_zh && (
                        <p className="text-xs text-gray-500 mt-0.5 truncate">{item.title_zh}</p>
                      )}
                      <div className="flex items-center gap-3 mt-2 text-xs text-gray-400">
                        <span>GA{item.book_ga_number || '?'}</span>
                        <span className="truncate">{item.book_title_de}</span>
                        {item.lecture_date && <span>{item.lecture_date}</span>}
                      </div>
                    </div>
                    <div className="text-xs text-gray-300 shrink-0">
                      {item.favorited_at && new Date(item.favorited_at).toLocaleDateString('zh-CN')}
                    </div>
                  </div>
                </Link>
              ))}
            </div>

            {totalPages > 1 && (
              <div className="flex items-center justify-center gap-2 mt-8">
                <button
                  type="button"
                  onClick={() => load(page - 1)}
                  disabled={page <= 1}
                  className="px-3 py-1.5 text-sm border border-gray-200 rounded-lg disabled:opacity-40 hover:bg-gray-50"
                >
                  上一页
                </button>
                <span className="text-sm text-gray-500">{page} / {totalPages}</span>
                <button
                  type="button"
                  onClick={() => load(page + 1)}
                  disabled={page >= totalPages}
                  className="px-3 py-1.5 text-sm border border-gray-200 rounded-lg disabled:opacity-40 hover:bg-gray-50"
                >
                  下一页
                </button>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}
```

- [ ] **Step 2: Commit**

```bash
git add frontend/app/favorites/page.tsx
git commit -m "feat(favorites): add favorites list page"
```

---

### Task 6: 导航栏收藏入口

**Files:**
- Modify: `frontend/app/components/Header.tsx`

- [ ] **Step 1: 在导航栏添加"我的收藏"链接**

在 `frontend/app/components/Header.tsx` 中，找到第100行的充值链接：

```tsx
              <Link href="/recharge" className="text-sm text-gray-500 hover:text-indigo-600 transition-colors px-2">
                充值
              </Link>
```

在其后添加：

```tsx
              <Link href="/favorites" className="text-sm text-gray-500 hover:text-indigo-600 transition-colors px-2">
                收藏
              </Link>
```

- [ ] **Step 2: Commit**

```bash
git add frontend/app/components/Header.tsx
git commit -m "feat(favorites): add favorites link to header navigation"
```

---

### Task 7: 前端构建与部署

**Files:**
- 无新文件，部署现有修改

- [ ] **Step 1: 同步前端代码到生产服务器**

```bash
scp -i C:\Users\Administrator\.ssh\id_rsa frontend/lib/api.ts root@66.154.112.162:/opt/steiner-reader/frontend/lib/api.ts
scp -i C:\Users\Administrator\.ssh\id_rsa "frontend/app/books/[bookId]/lectures/[lectureId]/page.tsx" "root@66.154.112.162:/opt/steiner-reader/frontend/app/books/[bookId]/lectures/[lectureId]/page.tsx"
scp -i C:\Users\Administrator\.ssh\id_rsa frontend/app/favorites/page.tsx root@66.154.112.162:/opt/steiner-reader/frontend/app/favorites/page.tsx
scp -i C:\Users\Administrator\.ssh\id_rsa frontend/app/components/Header.tsx root@66.154.112.162:/opt/steiner-reader/frontend/app/components/Header.tsx
```

注意：需先在服务器创建 favorites 目录：
```bash
ssh -i C:\Users\Administrator\.ssh\id_rsa root@66.154.112.162 "mkdir -p /opt/steiner-reader/frontend/app/favorites"
```

- [ ] **Step 2: 构建前端**

```bash
ssh -i C:\Users\Administrator\.ssh\id_rsa root@66.154.112.162 "cd /opt/steiner-reader/frontend && npm run build 2>&1 | tail -20"
```

预期输出：构建成功，显示路由列表包含 `/favorites`。

- [ ] **Step 3: 重启前端服务**

```bash
ssh -i C:\Users\Administrator\.ssh\id_rsa root@66.154.112.162 "systemctl restart steiner-frontend.service && sleep 2 && systemctl is-active steiner-frontend.service"
```

预期输出：`active`

- [ ] **Step 4: 手动验证收藏功能**

1. 访问 https://steiner.3mudi.com 登录
2. 打开任意讲座阅读页，确认标题旁有 ☆ 按钮
3. 点击 ☆ 变为 ★，刷新页面仍为 ★
4. 点击导航栏"收藏"，进入 /favorites 页面，确认列表显示该讲座
5. 返回讲座页点击 ★ 变回 ☆，刷新 /favorites 列表为空

---

### Task 8: 翻译标识清理脚本

**Files:**
- Create: `backend/scripts/clean_se_tags.py`

- [ ] **Step 1: 创建清理脚本**

创建 `backend/scripts/clean_se_tags.py`：

```python
"""一次性清理 sentences.text_zh 中的 #SE数字-数字 翻译标识。

用法：
    python3 clean_se_tags.py           # 预览模式，只显示影响范围和样例
    python3 clean_se_tags.py --execute # 执行清理
"""

import argparse
import psycopg2
import re

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "steiner_reader",
    "user": "steiner",
    "password": "Dd08120@",
}

# 匹配 #SE数字-数字 及前后空白
SE_PATTERN = r"\s*#SE\d+-\d+\s*"


def main():
    parser = argparse.ArgumentParser(description="清理翻译标识 #SE数字-数字")
    parser.add_argument("--execute", action="store_true", help="执行清理（默认只预览）")
    args = parser.parse_args()

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # 1. 统计影响范围
    cur.execute("SELECT COUNT(*) FROM sentences WHERE text_zh ~ '#SE\\d+-\\d+'")
    total = cur.fetchone()[0]
    print(f"包含 #SE 标识的句子数: {total}")

    if total == 0:
        print("无需清理")
        return

    # 2. 显示清理前样例（10条）
    cur.execute("""
        SELECT id, text_zh FROM sentences
        WHERE text_zh ~ '#SE\\d+-\\d+'
        ORDER BY id
        LIMIT 10
    """)
    print("\n--- 清理前样例 ---")
    samples = cur.fetchall()
    for sid, text in samples:
        print(f"  [{sid}] {text[:120]}")

    # 3. 显示清理后样例
    print("\n--- 清理后样例 ---")
    for sid, text in samples:
        cleaned = re.sub(SE_PATTERN, " ", text).strip()
        print(f"  [{sid}] {cleaned[:120]}")

    if not args.execute:
        print("\n预览模式，未执行清理。添加 --execute 参数执行清理。")
        cur.close()
        conn.close()
        return

    # 4. 执行清理
    print("\n--- 执行清理 ---")
    cur.execute("""
        UPDATE sentences
        SET text_zh = btrim(regexp_replace(text_zh, '\\s*#SE\\d+-\\d+\\s*', ' ', 'g'))
        WHERE text_zh ~ '#SE\\d+-\\d+'
    """)
    updated = cur.rowcount
    conn.commit()
    print(f"已更新 {updated} 条句子")

    # 5. 验证
    cur.execute("SELECT COUNT(*) FROM sentences WHERE text_zh ~ '#SE\\d+-\\d+'")
    remaining = cur.fetchone()[0]
    print(f"清理后剩余 #SE 标识句子数: {remaining}")

    if remaining > 0:
        print("警告：仍有残留标识，请检查")
    else:
        print("清理完成，所有 #SE 标识已移除")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: 上传脚本到生产服务器并预览**

```bash
scp -i C:\Users\Administrator\.ssh\id_rsa backend/scripts/clean_se_tags.py root@66.154.112.162:/tmp/clean_se_tags.py
ssh -i C:\Users\Administrator\.ssh\id_rsa root@66.154.112.162 "python3 /tmp/clean_se_tags.py"
```

预期输出：显示 14,613 条句子和清理前后样例对比。

- [ ] **Step 3: 执行清理**

```bash
ssh -i C:\Users\Administrator\.ssh\id_rsa root@66.154.112.162 "python3 /tmp/clean_se_tags.py --execute"
```

预期输出：`已更新 14613 条句子`，`清理后剩余 #SE 标识句子数: 0`

- [ ] **Step 4: 验证清理结果**

```bash
ssh -i C:\Users\Administrator\.ssh\id_rsa root@66.154.112.162 "PGPASSWORD='Dd08120@' psql -U steiner -h localhost -d steiner_reader -c \"SELECT COUNT(*) FROM sentences WHERE text_zh ~ '#SE'\""
```

预期输出：`0`

- [ ] **Step 5: Commit**

```bash
git add backend/scripts/clean_se_tags.py
git commit -m "chore(data): add script to clean #SE translation tags"
```

---

### Task 9: 推送到 GitHub

**Files:**
- 无

- [ ] **Step 1: 推送所有提交**

```bash
git push origin main
```

预期输出：推送成功，显示提交计数。

- [ ] **Step 2: 验证最终状态**

1. 访问 https://steiner.3mudi.com 确认网站正常
2. 登录后在导航栏看到"收藏"链接
3. 打开讲座阅读页确认 ☆ 按钮存在
4. 打开任意已翻译讲座，确认中文译文无 #SE 标识
