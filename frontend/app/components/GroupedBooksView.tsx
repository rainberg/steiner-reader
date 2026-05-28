'use client';

import { useEffect, useState } from 'react';
import { fetchBookGroups, BookGroup } from '@/lib/api';

export default function GroupedBooksView() {
  const [groups, setGroups] = useState<BookGroup[]>([]);
  const [expanded, setExpanded] = useState<Set<string>>(new Set());
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchBookGroups()
      .then(setGroups)
      .catch(() => setError('加载分组数据失败'))
      .finally(() => setLoading(false));
  }, []);

  const toggle = (group: string) => {
    setExpanded(prev => {
      const next = new Set(prev);
      if (next.has(group)) next.delete(group);
      else next.add(group);
      return next;
    });
  };

  if (loading) {
    return (
      <div className="space-y-3">
        {Array.from({ length: 6 }).map((_, i) => (
          <div key={i} className="card p-5 shimmer h-20 rounded-xl" />
        ))}
      </div>
    );
  }

  if (error) {
    return <div className="rounded-lg border border-amber-200 bg-amber-50 px-3 py-2 text-sm text-amber-700">{error}</div>;
  }

  return (
    <div className="space-y-3">
      {groups.map(g => (
        <div key={g.group} className="card overflow-hidden">
          <button
            type="button"
            onClick={() => toggle(g.group || "")}
            className="w-full flex items-center justify-between px-5 py-4 hover:bg-gray-50/60 transition-colors text-left"
          >
            <div className="flex items-center gap-3">
              <span className="inline-block bg-indigo-50 text-indigo-700 text-sm font-bold px-3 py-1 rounded-lg border border-indigo-100/60 min-w-[5rem] text-center">
                {g.group}
              </span>
              <div className="text-sm text-gray-500">
                <span className="font-medium text-gray-700">{g.book_count}</span> 本
                <span className="mx-1.5 text-gray-300">·</span>
                {g.lecture_count} 讲
                <span className="mx-1.5 text-gray-300">·</span>
                {g.sentence_count.toLocaleString()} 句
              </div>
            </div>
            <svg
              className={`w-5 h-5 text-gray-400 transition-transform ${expanded.has(g.group || "") ? 'rotate-180' : ''}`}
              fill="none" viewBox="0 0 24 24" stroke="currentColor"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
            </svg>
          </button>

          {expanded.has(g.group || "") && (
            <div className="border-t border-gray-100 px-5 py-4 bg-gray-50/30">
              <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
                {(g.books || []).map(book => (
                  <a key={book.id} href={`/books/${book.id}`}>
                    <div className="card p-4 h-full flex flex-col group">
                      <div className="flex items-start justify-between mb-2">
                        {book.ga_number ? (
                          <span className="inline-block bg-indigo-50 text-indigo-700 text-xs font-semibold px-2 py-0.5 rounded-md border border-indigo-100/50">
                            {book.ga_number}
                          </span>
                        ) : <span />}
                      </div>
                      <h3 className="text-sm font-semibold text-gray-900 leading-snug line-clamp-2">{book.title_zh || book.title_de}</h3>
                      <p className="text-xs text-gray-500 mt-1 line-clamp-1">{book.title_de}</p>
                      <div className="mt-auto pt-2 flex items-center gap-2 text-xs text-gray-400">
                        <span>{book.lecture_count} 讲</span>
                        <span>·</span>
                        <span>{book.sentence_count.toLocaleString()} 句</span>
                      </div>
                    </div>
                  </a>
                ))}
              </div>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
