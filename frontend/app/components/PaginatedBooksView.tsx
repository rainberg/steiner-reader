'use client';

import { useEffect, useState } from 'react';
import { fetchBookSummariesPaginated, fetchBookCount, BookSummary } from '@/lib/api';

const PAGE_SIZE = 24;

export default function PaginatedBooksView() {
  const [books, setBooks] = useState<BookSummary[]>([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [sortBy, setSortBy] = useState('created_at');
  const [sortDir, setSortDir] = useState('desc');
  const [loading, setLoading] = useState(true);

  const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE));

  useEffect(() => {
    fetchBookCount().then(setTotal);
  }, []);

  useEffect(() => {
    setLoading(true);
    fetchBookSummariesPaginated({ page, page_size: PAGE_SIZE, sort_by: sortBy, sort_dir: sortDir })
      .then(setBooks)
      .catch(() => setBooks([]))
      .finally(() => setLoading(false));
  }, [page, sortBy, sortDir]);

  const handleSort = (key: string) => {
    if (sortBy === key) {
      setSortDir(d => (d === 'asc' ? 'desc' : 'asc'));
    } else {
      setSortBy(key);
      setSortDir(key === 'title_de' ? 'asc' : 'desc');
    }
    setPage(1);
  };

  const sortLabel = (key: string, label: string) => (
    <button
      type="button"
      onClick={() => handleSort(key)}
      className={`text-xs px-2.5 py-1 rounded-md border transition-colors ${
        sortBy === key
          ? 'bg-indigo-50 text-indigo-700 border-indigo-200'
          : 'bg-white text-gray-500 border-gray-200 hover:border-gray-300'
      }`}
    >
      {label}
      {sortBy === key && (sortDir === 'asc' ? ' ↑' : ' ↓')}
    </button>
  );

  return (
    <div>
      <div className="flex items-center justify-between mb-4">
        <span className="text-sm text-gray-500">{total} 本图书</span>
        <div className="flex items-center gap-1.5">
          {sortLabel('ga_number', 'GA 编号')}
          {sortLabel('title_de', '标题')}
          {sortLabel('lecture_count', '讲座数')}
          {sortLabel('created_at', '时间')}
        </div>
      </div>

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
                  {book.image_count > 0 && (
                    <>
                      <span>·</span>
                      <span>{book.image_count} 图</span>
                    </>
                  )}
                </div>
              </div>
            </a>
          ))}
        </div>
      )}

      {totalPages > 1 && (
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
