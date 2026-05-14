'use client';

import { useSearchParams, useRouter } from 'next/navigation';
import { Suspense } from 'react';
import GroupedBooksView from '@/app/components/GroupedBooksView';
import PaginatedBooksView from '@/app/components/PaginatedBooksView';
import SearchBooksView from '@/app/components/SearchBooksView';

type ViewMode = 'group' | 'grid' | 'search';

const tabs: { key: ViewMode; label: string }[] = [
  { key: 'group', label: '分类' },
  { key: 'grid', label: '网格' },
  { key: 'search', label: '搜索' },
];

function HomeContent() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const view = (searchParams.get('view') as ViewMode) || 'group';

  const switchView = (v: ViewMode) => {
    if (v === 'group') router.push('/');
    else router.push(`/?view=${v}`);
  };

  return (
    <div className="page-container py-8">
      <div className="mb-6">
        <h1 className="text-3xl sm:text-4xl font-bold text-gray-900 tracking-tight">施泰纳著作库</h1>
        <p className="text-gray-500 mt-2 max-w-xl">Rudolf Steiner Gesamtausgabe 在线阅读与检索</p>
      </div>

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
