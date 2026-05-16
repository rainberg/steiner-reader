'use client';

import { useState } from 'react';

interface SearchResult {
  content_de: string;
  content_zh: string;
  book: string;
  score: number;
}

export default function SearchModal() {
  const [open, setOpen] = useState(false);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);

  const doSearch = async () => {
    if (!query.trim()) return;
    setLoading(true);
    try {
      const res = await fetch(`/api/search?q=${encodeURIComponent(query)}&k=8`);
      const data = await res.json();
      setResults(data.results || []);
    } catch {
      setResults([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <button onClick={() => setOpen(true)} className="text-sm text-gray-500 hover:text-indigo-600 transition-colors px-2" title="语义搜索">
        🔍
      </button>
      {open && (
        <div className="fixed inset-0 z-50 flex items-start justify-center pt-20 bg-black/30" onClick={() => setOpen(false)}>
          <div className="bg-white rounded-2xl shadow-2xl w-full max-w-2xl mx-4 max-h-[80vh] flex flex-col" onClick={e => e.stopPropagation()}>
            <div className="p-4 border-b flex gap-2">
              <input value={query} onChange={e => setQuery(e.target.value)} onKeyDown={e => e.key === 'Enter' && doSearch()}
                placeholder="搜索施泰纳著作..." autoFocus
                className="flex-1 px-3 py-2 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500/20" />
              <button onClick={doSearch} disabled={loading} className="px-4 py-2 bg-indigo-600 text-white text-sm rounded-lg hover:bg-indigo-700 disabled:opacity-50">
                {loading ? '搜索中...' : '搜索'}
              </button>
              <button onClick={() => setOpen(false)} className="px-3 py-2 text-gray-400 hover:text-gray-600 text-sm">✕</button>
            </div>
            <div className="overflow-y-auto p-4 space-y-3">
              {results.map((r, i) => (
                <div key={i} className="p-4 bg-slate-50 rounded-xl">
                  {r.content_zh && <p className="text-base text-gray-800 leading-relaxed mb-2">{r.content_zh}</p>}
                  <p className="text-sm text-gray-500 leading-relaxed">{r.content_de}</p>
                  {r.book && <p className="text-xs text-gray-400 mt-2 pt-2 border-t border-slate-200">{r.book}</p>}
                </div>
              ))}
              {!loading && results.length === 0 && query && (
                <p className="text-gray-400 text-sm text-center py-8">无搜索结果</p>
              )}
            </div>
          </div>
        </div>
      )}
    </>
  );
}
