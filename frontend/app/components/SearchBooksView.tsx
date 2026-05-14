'use client';

import { useEffect, useState, useRef } from 'react';
import { fetchBookSummariesPaginated, fetchBookCount, BookSummary } from '@/lib/api';

const PAGE_SIZE = 24;

export default function SearchBooksView() {
  const [query, setQuery] = useState('');
  const [books, setBooks] = useState<BookSummary[]>([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [loading, setLoading] = useState(false);
  const [searched, setSearched] = useState(false);
  const timerRef = useRef<ReturnType<typeof setTimeout>>(undefined);

  const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE));

  const doSearch = (q: string, p: number) => {
    if (!q.trim()) {
      setBooks([]);
      setTotal(0);
      setSearched(false);
      return;
    }
    setLoading(true);
    setSearched(true);
    Promise.all([
      fetchBookSummariesPaginated({ page: p, page_size: PAGE_SIZE, search: q }),
      fetchBookCount(q),
    ])
      .then(([b, t]) => {
        setBooks(b);
        setTotal(t);
      })
      .catch(() => {
        setBooks([]);
        setTotal(0);
      })
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    if (timerRef.current) clearTimeout(timerRef.current);
    timerRef.current = setTimeout(() => {
      setPage(1);
      doSearch(query, 1);
    }, 300);
    return () => {
      if (timerRef.current) clearTimeout(timerRef.current);
    };
  }, [query]);

  useEffect(() => {
    if (searched) doSearch(query, page);
  }, [page]);

  return (
    <div>
      <div className="relative max-w-xl mx-auto mb-8">
        <svg className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
        </svg>
        <input
          type="text"
          value={query}
          onChange={e => setQuery(e.target.value)}
          placeholder="搜索 GA 编号、德语标题或中文标题..."
          className="w-full pl-12 pr-4 py-3.5 bg-white border border-gray-200 rounded-xl text-sm text-gray-700 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-300 transition-all shadow-sm"
          autoFocus
        />
      </div>

      {searched && (
        <p className="text-sm text-gray-500 mb-4">
          {loading ? '搜索中...' : `找到 ${total} 个结果`}
        </p>
      )}

      {!searched && (
        <div className="text-center py-16 text-gray-400">
          <svg className="w-12 h-12 mx-auto mb-3 text-gray-300" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
          <p>输入关键词开始搜索</p>
        </div>
      )}

      {searched && !loading && books.length === 0 && (
        <div className="text-center py-16 text-gray-400">
          <p>没有找到匹配的图书</p>
        </div>
      )}

      {loading ? (
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {Array.from({ length: 6 }).map((_, i) => (
            <div key={i} className="card p-5 shimmer h-32 rounded-xl" />
          ))}
        </div>
      ) : (
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {books.map(book => (
            <a key={book.id} href={`/books/${book.id}`}>
              <div className="card p-5 h-full flex flex-col group">
                <div className="flex items-start justify-between mb-2">
                  {book.ga_number ? (
                    <span className="inline-block bg-indigo-50 text-indigo-700 text-xs font-semibold px-2 py-0.5 rounded-md border border-indigo-100/50">
                      {book.ga_number}
                    </span>
                  ) : <span />}
                </div>
                <h2 className="text-lg font-semibold text-gray-900 leading-snug line-clamp-2">{book.title_zh || book.title_de}</h2>
                <p className="text-sm text-gray-500 mt-1 line-clamp-2">{book.title_de}</p>
                <div className="mt-auto pt-3 flex items-center gap-3 text-xs text-gray-400">
                  <span>{book.lecture_count} 讲</span>
                  <span>·</span>
                  <span>{book.sentence_count.toLocaleString()} 句</span>
                </div>
              </div>
            </a>
          ))}
        </div>
      )}

      {searched && totalPages > 1 && (
        <div className="flex items-center justify-center gap-2 mt-6">
          <button
            type="button"
            disabled={page <= 1}
            onClick={() => setPage(p => Math.max(1, p - 1))}
            className="btn-secondary !px-3 !py-1.5 text-sm disabled:opacity-40"
          >
            上一页
          </button>
          <span className="text-sm text-gray-500 px-3">
            {page} / {totalPages}
          </span>
          <button
            type="button"
            disabled={page >= totalPages}
            onClick={() => setPage(p => Math.min(totalPages, p + 1))}
            className="btn-secondary !px-3 !py-1.5 text-sm disabled:opacity-40"
          >
            下一页
          </button>
        </div>
      )}
    </div>
  );
}
