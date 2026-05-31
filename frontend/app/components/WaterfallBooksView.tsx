'use client';

import { useEffect, useState, useCallback, useRef } from 'react';
import Link from 'next/link';
import { fetchBookSummariesPaginated, BookSummary } from '@/lib/api';

const FIRST_PAGE_SIZE = 10;
const PAGE_SIZE = 24;

export default function WaterfallBooksView() {
  const [books, setBooks] = useState<BookSummary[]>([]);
  const [loading, setLoading] = useState(true);
  const [hasMore, setHasMore] = useState(true);
  const [page, setPage] = useState(1);
  const loaderRef = useRef<HTMLDivElement>(null);

  const loadPage = useCallback(async (p: number) => {
    setLoading(true);
    const pageSize = p === 1 ? FIRST_PAGE_SIZE : PAGE_SIZE;
    const data = await fetchBookSummariesPaginated({ page: p, page_size: pageSize, sort_by: 'created_at', sort_dir: 'desc' });
    if (p === 1) {
      for (let i = data.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [data[i], data[j]] = [data[j], data[i]];
      }
      setBooks(data);
    } else {
      setBooks(prev => [...prev, ...data]);
    }
    setHasMore(data.length === pageSize);
    setLoading(false);
  }, []);

  useEffect(() => { loadPage(1); }, [loadPage]);

  // Intersection observer for infinite scroll
  useEffect(() => {
    const el = loaderRef.current;
    if (!el) return;
    const obs = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting && hasMore && !loading) {
        setPage(p => p + 1);
        loadPage(page + 1);
      }
    }, { rootMargin: '200px' });
    obs.observe(el);
    return () => obs.disconnect();
  }, [hasMore, loading, page, loadPage]);

  return (
    <div>
      <div className="columns-1 sm:columns-2 lg:columns-3 gap-4 space-y-4">
        {books.map(book => (
          <Link
            key={book.id}
            href={`/books/${book.id}`}
            className="block break-inside-avoid mb-4 bg-white rounded-xl shadow-sm border border-slate-100 p-5 hover:shadow-md hover:border-slate-200 transition-all"
          >
            <h3 className="text-sm font-semibold text-gray-800 leading-snug line-clamp-3">
              {book.title_zh || book.title_de}
            </h3>
            <p className="text-xs text-gray-400 mt-1 line-clamp-2">{book.title_de}</p>
            <div className="flex items-center gap-3 mt-3 pt-3 border-t border-gray-50">
              <span className="text-[10px] text-gray-400">{book.ga_number}</span>
              <span className="text-[10px] text-gray-300">{book.lecture_count} 章</span>
            </div>
          </Link>
        ))}
      </div>
      <div ref={loaderRef} className="text-center py-6">
        {loading && <span className="text-gray-400 text-sm">加载中...</span>}
        {!hasMore && books.length > 0 && <span className="text-gray-300 text-xs">已加载全部</span>}
      </div>
    </div>
  );
}
