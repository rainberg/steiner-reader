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
