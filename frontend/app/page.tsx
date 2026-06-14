'use client';

import { useEffect, useRef, useState, useCallback, Suspense } from 'react';
import { useSearchParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import GroupedBooksView from '@/app/components/GroupedBooksView';
import PaginatedBooksView from '@/app/components/PaginatedBooksView';
import SearchBooksView from '@/app/components/SearchBooksView';
import WaterfallBooksView from '@/app/components/WaterfallBooksView';

type ViewMode = 'waterfall' | 'group' | 'grid' | 'search';

const tabs: { key: ViewMode; label: string }[] = [
  { key: 'waterfall', label: '流式' },
  { key: 'group', label: '分类' },
  { key: 'grid', label: '网格' },
  { key: 'search', label: '搜索' },
];

function HomeContent() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const view = (searchParams.get('view') as ViewMode) || 'waterfall';

  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState<Array<{
    content_de: string;
    content_zh: string;
    book: string;
    ga_number: string;
    score: number;
    book_id: number | null;
    lecture_id: number | null;
    sentence_id: number | null;
  }>>([]);
  const [searchLoading, setSearchLoading] = useState(false);
  const searchTimerRef = useRef<ReturnType<typeof setTimeout>>(undefined);

  const doSearch = useCallback(async (q: string) => {
    if (!q.trim()) {
      setSearchResults([]);
      setSearchLoading(false);
      return;
    }
    setSearchLoading(true);
    try {
      const res = await fetch(`/api/search?q=${encodeURIComponent(q)}&k=8`);
      const data = await res.json();
      setSearchResults(data.results || []);
    } catch {
      setSearchResults([]);
    } finally {
      setSearchLoading(false);
    }
  }, []);

  useEffect(() => {
    if (searchTimerRef.current) clearTimeout(searchTimerRef.current);
    searchTimerRef.current = setTimeout(() => {
      doSearch(searchQuery);
    }, 300);
    return () => {
      if (searchTimerRef.current) clearTimeout(searchTimerRef.current);
    };
  }, [searchQuery, doSearch]);

  const [catalogStats, setCatalogStats] = useState<{total: number; collected: number} | null>(null);

  useEffect(() => {
    fetch('/api/catalog/stats')
      .then(r => r.json())
      .then(data => setCatalogStats({ total: data.total, collected: data.collected }))
      .catch(() => {});
  }, []);

  const switchView = (v: ViewMode) => {
    if (v === 'waterfall') router.push('/');
    else router.push(`/?view=${v}`);
  };

  return (
    <div className="page-container py-8">
      <div className="mb-6">
        <h1 className="text-3xl sm:text-4xl font-bold text-gray-900 tracking-tight">施泰纳著作库</h1>
        <p className="text-gray-500 mt-2 max-w-xl">Rudolf Steiner Gesamtausgabe 在线阅读与检索</p>
      </div>

      {/* 语义搜索框 */}
      <div className="mb-4 relative max-w-xl">
        <svg className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-indigo-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
        </svg>
        <input
          type="text"
          value={searchQuery}
          onChange={e => setSearchQuery(e.target.value)}
          placeholder="搜索施泰纳著作内容..."
          className="w-full pl-12 pr-4 py-3 bg-white border border-indigo-200 rounded-xl text-sm text-gray-700 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-300 transition-all shadow-sm"
        />
        <span className="absolute right-3 top-1/2 -translate-y-1/2 text-[10px] bg-indigo-50 text-indigo-500 px-2 py-0.5 rounded font-medium">语义搜索</span>
      </div>

      {/* 搜索结果 */}
      {searchQuery.trim() && (
        <div className="mb-6 max-w-xl">
          <p className="text-sm text-gray-500 mb-3">
            {searchLoading ? '搜索中...' : `${searchResults.length} 个结果`}
          </p>
          <div className="space-y-2">
            {searchResults.map((r, i) => (
              <a
                key={i}
                href={r.lecture_id && r.book_id ? `/books/${r.book_id}/lectures/${r.lecture_id}${r.sentence_id ? `?highlight=${r.sentence_id}` : ''}` : r.book_id ? `/books/${r.book_id}` : '#'}
                className="block bg-white border border-slate-200 rounded-xl p-4 hover:border-indigo-200 hover:shadow-sm transition-all"
              >
                {r.content_zh && <p className="text-sm text-gray-800 leading-relaxed mb-1.5 line-clamp-2">{r.content_zh}</p>}
                <p className="text-xs text-gray-500 leading-relaxed line-clamp-2">{r.content_de}</p>
                {r.book && <p className="text-[10px] text-gray-400 mt-2 pt-2 border-t border-slate-100">{r.book}</p>}
              </a>
            ))}
            {!searchLoading && searchResults.length === 0 && (
              <p className="text-gray-400 text-sm text-center py-6">无搜索结果</p>
            )}
          </div>
        </div>
      )}

      {/* 讲座目录入口 */}
      {!searchQuery.trim() && (
        <Link href="/lectures-catalog"
          className="block mb-6 bg-gradient-to-r from-indigo-50 to-emerald-50 border border-indigo-100 rounded-xl p-4 hover:border-indigo-200 hover:shadow-sm transition-all group"
        >
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-sm font-semibold text-indigo-900">📚 讲座编年目录</h3>
              <p className="text-xs text-gray-500 mt-0.5">
                Vortragsverzeichnis — 全部讲座编年索引
                {catalogStats && (
                  <span className="ml-2 text-indigo-500">
                    {catalogStats.total.toLocaleString()} 场讲座 · {catalogStats.collected.toLocaleString()} 已收录
                  </span>
                )}
              </p>
            </div>
            <svg className="w-5 h-5 text-indigo-300 group-hover:text-indigo-500 transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </div>
        </Link>
      )}

      <div className="flex mb-6 bg-gray-100 rounded-lg p-1 w-fit">
        {tabs.map(t => (
          <button
            key={t.key}
            type="button"
            onClick={() => switchView(t.key)}
            className={`px-4 py-1.5 rounded-md text-sm font-medium transition ${
              view === t.key ? 'bg-white text-gray-900 shadow-sm' : 'text-gray-500 hover:text-gray-700'
            }`}
          >
            {t.label}
          </button>
        ))}
      </div>

      {view === 'waterfall' && <WaterfallBooksView />}
      {view === 'group' && <GroupedBooksView />}
      {view === 'grid' && <PaginatedBooksView />}
      {view === 'search' && <SearchBooksView />}
    </div>
  );
}

export default function HomePage() {
  return (
    <Suspense fallback={
      <div className="page-container py-8">
        <div className="mb-6">
          <div className="h-10 w-48 bg-gray-200 rounded shimmer mb-2" />
          <div className="h-5 w-64 bg-gray-100 rounded shimmer" />
        </div>
        <div className="space-y-3">
          {Array.from({ length: 4 }).map((_, i) => (
            <div key={i} className="card p-5 shimmer h-20 rounded-xl" />
          ))}
        </div>
      </div>
    }>
      <HomeContent />
    </Suspense>
  );
}
