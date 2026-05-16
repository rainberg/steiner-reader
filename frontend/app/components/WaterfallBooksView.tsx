'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { fetchBookSummariesPaginated, BookSummary } from '@/lib/api';

export default function WaterfallBooksView() {
  const [books, setBooks] = useState<BookSummary[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchBookSummariesPaginated({ page_size: 500 })
      .then(data => {
        // Random shuffle
        for (let i = data.length - 1; i > 0; i--) {
          const j = Math.floor(Math.random() * (i + 1));
          [data[i], data[j]] = [data[j], data[i]];
        }
        setBooks(data);
      })
      .catch(() => {})
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div className="text-center py-12 text-gray-400 text-sm">加载中...</div>;

  return (
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
            <span className="text-[10px] text-gray-300">{book.lecture_count} 章节</span>
            <span className="text-[10px] text-gray-300">{book.sentence_count} 句</span>
          </div>
        </Link>
      ))}
    </div>
  );
}
