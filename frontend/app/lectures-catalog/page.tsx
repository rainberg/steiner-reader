'use client';

import { useEffect, useState, useCallback } from 'react';
import Link from 'next/link';
import {
  getCatalogLectures,
  getCatalogStats,
  getCatalogLocations,
  CatalogLecture,
  CatalogStats,
  CatalogLocation,
} from '@/lib/api';

type FilterStatus = 'all' | 'collected' | 'matched' | 'pending';

const statusButtons: { key: FilterStatus; label: string }[] = [
  { key: 'all', label: '全部' },
  { key: 'collected', label: '已收录' },
  { key: 'matched', label: '精确匹配' },
  { key: 'pending', label: '待收集' },
];

function formatDate(dateStr: string | null): string {
  if (!dateStr) return '—';
  try {
    const d = new Date(dateStr);
    if (isNaN(d.getTime())) return dateStr;
    return d.toLocaleDateString('zh-CN', { year: 'numeric', month: 'long', day: 'numeric' });
  } catch {
    return dateStr;
  }
}

function groupByYear(items: CatalogLecture[]): Record<string, CatalogLecture[]> {
  const groups: Record<string, CatalogLecture[]> = {};
  for (const item of items) {
    const year = item.year ?? '未知';
    if (!groups[year]) groups[year] = [];
    groups[year].push(item);
  }
  return groups;
}

export default function LecturesCatalogPage() {
  const [stats, setStats] = useState<CatalogStats | null>(null);
  const [locations, setLocations] = useState<CatalogLocation[]>([]);
  const [lectures, setLectures] = useState<CatalogLecture[]>([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [pageSize] = useState(50);
  const [loading, setLoading] = useState(true);

  // Filters
  const [yearFrom, setYearFrom] = useState(1888);
  const [yearTo, setYearTo] = useState(1924);
  const [locationCode, setLocationCode] = useState('');
  const [gaNumber, setGaNumber] = useState('');
  const [filterStatus, setFilterStatus] = useState<FilterStatus>('all');

  const fetchLectures = useCallback(async (p: number = 1) => {
    setLoading(true);
    try {
      const params: Record<string, any> = {
        page: p,
        page_size: pageSize,
        year_from: yearFrom || undefined,
        year_to: yearTo || undefined,
      };
      if (locationCode) params.location_code = locationCode;
      if (gaNumber) params.ga_number = gaNumber;
      if (filterStatus === 'collected') params.is_collected = true;
      if (filterStatus === 'matched') {
        params.is_collected = true;
        params.is_lecture_matched = true;
      }
      if (filterStatus === 'pending') params.is_collected = false;

      const data = await getCatalogLectures(params);
      setLectures(data.items);
      setTotal(data.total);
      setPage(data.page);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }, [yearFrom, yearTo, locationCode, gaNumber, filterStatus, pageSize]);

  useEffect(() => {
    getCatalogStats().then(setStats).catch(console.error);
    getCatalogLocations().then(setLocations).catch(console.error);
  }, []);

  useEffect(() => {
    fetchLectures(1);
  }, [fetchLectures]);

  const handleSearch = () => {
    setPage(1);
    fetchLectures(1);
  };

  const handleReset = () => {
    setYearFrom(1888);
    setYearTo(1924);
    setLocationCode('');
    setGaNumber('');
    setFilterStatus('all');
  };

  const totalPages = Math.ceil(total / pageSize);
  const yearGroups = groupByYear(lectures);
  const sortedYears = Object.keys(yearGroups).sort((a, b) => Number(a) - Number(b));
  const notCollected = stats ? stats.total - stats.collected : 0;

  return (
    <div className="page-container py-8">
      {/* Header */}
      <div className="mb-6">
        <h1 className="text-3xl sm:text-4xl font-bold text-gray-900 tracking-tight">讲座编年目录</h1>
        <p className="text-gray-500 mt-2 max-w-xl">
          Vortragsverzeichnis — 鲁道夫·施泰纳全部讲座编年索引
        </p>
      </div>

      {/* Stats bar */}
      {stats && (
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 mb-6">
          <div className="card p-4 text-center">
            <div className="text-2xl font-bold text-gray-900">{stats.total.toLocaleString()}</div>
            <div className="text-xs text-gray-500 mt-1">讲座总数</div>
          </div>
          <div className="card p-4 text-center">
            <div className="text-2xl font-bold text-emerald-600">{stats.collected.toLocaleString()}</div>
            <div className="text-xs text-gray-500 mt-1">已收录</div>
          </div>
          <div className="card p-4 text-center">
            <div className="text-2xl font-bold text-blue-600">{stats.lecture_matched.toLocaleString()}</div>
            <div className="text-xs text-gray-500 mt-1">精确匹配</div>
          </div>
          <div className="card p-4 text-center">
            <div className="text-2xl font-bold text-gray-400">{notCollected.toLocaleString()}</div>
            <div className="text-xs text-gray-500 mt-1">待收集</div>
          </div>
        </div>
      )}

      {/* Filter area */}
      <div className="card p-5 mb-6">
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
          {/* Year range */}
          <div>
            <label className="block text-xs font-medium text-gray-500 mb-1">年份范围</label>
            <div className="flex items-center gap-2">
              <input
                type="number"
                value={yearFrom}
                onChange={e => setYearFrom(Number(e.target.value) || 1888)}
                className="w-full px-3 py-2 text-sm border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500/30 focus:border-indigo-300"
                min={1888}
                max={1924}
              />
              <span className="text-gray-400 text-sm shrink-0">—</span>
              <input
                type="number"
                value={yearTo}
                onChange={e => setYearTo(Number(e.target.value) || 1924)}
                className="w-full px-3 py-2 text-sm border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500/30 focus:border-indigo-300"
                min={1888}
                max={1924}
              />
            </div>
          </div>

          {/* Location */}
          <div>
            <label className="block text-xs font-medium text-gray-500 mb-1">地点</label>
            <select
              value={locationCode}
              onChange={e => setLocationCode(e.target.value)}
              className="w-full px-3 py-2 text-sm border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500/30 focus:border-indigo-300 bg-white"
            >
              <option value="">全部地点</option>
              {locations.map(loc => (
                <option key={loc.code} value={loc.code}>
                  {loc.full_name} ({loc.lecture_count})
                </option>
              ))}
            </select>
          </div>

          {/* GA number */}
          <div>
            <label className="block text-xs font-medium text-gray-500 mb-1">GA 编号</label>
            <input
              type="text"
              value={gaNumber}
              onChange={e => setGaNumber(e.target.value)}
              placeholder="如 GA 094"
              className="w-full px-3 py-2 text-sm border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500/30 focus:border-indigo-300"
            />
          </div>

          {/* Search / Reset */}
          <div className="flex items-end gap-2">
            <button type="button" onClick={handleSearch} className="btn-primary text-sm !py-2 flex-1">
              搜索
            </button>
            <button type="button" onClick={handleReset} className="btn-secondary text-sm !py-2 flex-1">
              重置
            </button>
          </div>
        </div>

        {/* Collection status buttons */}
        <div>
          <label className="block text-xs font-medium text-gray-500 mb-2">收录状态</label>
          <div className="flex gap-2">
            {statusButtons.map(btn => (
              <button
                key={btn.key}
                type="button"
                onClick={() => setFilterStatus(btn.key)}
                className={`px-4 py-1.5 rounded-lg text-sm font-medium transition-all duration-150 ${
                  filterStatus === btn.key
                    ? 'bg-indigo-600 text-white shadow-sm'
                    : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                }`}
              >
                {btn.label}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Lecture list */}
      {loading ? (
        <div className="space-y-3">
          {Array.from({ length: 6 }).map((_, i) => (
            <div key={i} className="shimmer h-14 rounded-xl" />
          ))}
        </div>
      ) : lectures.length === 0 ? (
        <div className="text-center py-16 text-gray-400">
          <svg className="w-12 h-12 mx-auto mb-3 text-gray-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
          </svg>
          <p className="text-sm">暂无匹配的讲座</p>
        </div>
      ) : (
        <div className="space-y-6">
          {sortedYears.map(year => (
            <div key={year}>
              <h2 className="text-lg font-bold text-gray-800 mb-2 sticky top-14 bg-gray-50/90 backdrop-blur-sm py-1 z-10">
                {year} 年
                <span className="text-xs font-normal text-gray-400 ml-2">{yearGroups[year].length} 场讲座</span>
              </h2>
              <div className="space-y-1">
                {yearGroups[year].map(lecture => {
                  const href = lecture.is_lecture_matched && lecture.matched_lecture_id && lecture.matched_book_id
                    ? `/books/${lecture.matched_book_id}/lectures/${lecture.matched_lecture_id}`
                    : lecture.is_collected && lecture.matched_book_id
                      ? `/books/${lecture.matched_book_id}`
                      : null;
                  const isClickable = href !== null;
                  const statusColor = lecture.is_collected
                    ? lecture.is_lecture_matched
                      ? 'bg-blue-500'
                      : 'bg-emerald-500'
                    : 'bg-gray-300';

                  const row = (
                    <div
                      className={`card px-4 py-3 flex items-center gap-3 ${
                        isClickable ? 'cursor-pointer hover:border-indigo-200' : ''
                      }`}
                    >
                      {/* Status dot */}
                      <span className={`shrink-0 w-2.5 h-2.5 rounded-full ${statusColor}`} />

                      {/* Date */}
                      <span className="text-sm text-gray-500 font-mono w-28 shrink-0 truncate">
                        {formatDate(lecture.lecture_date)}
                      </span>

                      {/* Location */}
                      {lecture.location_code && (
                        <span className="text-xs bg-gray-50 text-gray-500 px-2 py-0.5 rounded border border-gray-100 whitespace-nowrap shrink-0">
                          {lecture.location_code}
                          {lecture.location_name && ` · ${lecture.location_name}`}
                        </span>
                      )}

                      {/* Schmidt number */}
                      {lecture.schmidt_number && (
                        <span className="text-xs text-gray-400 font-mono shrink-0">
                          {lecture.schmidt_number}
                        </span>
                      )}

                      {/* GA number badge */}
                      {lecture.ga_number && (
                        <span className="text-xs font-semibold text-indigo-600 bg-indigo-50 border border-indigo-100/60 px-2 py-0.5 rounded-md shrink-0">
                          {lecture.ga_number}
                        </span>
                      )}

                      {/* Spacer */}
                      <div className="flex-1" />

                      {/* Click indicator */}
                      {isClickable && (
                        <svg className="w-4 h-4 text-gray-300 group-hover:text-indigo-400 transition-colors shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                        </svg>
                      )}
                    </div>
                  );

                  return isClickable ? (
                    <Link key={lecture.id} href={href!} className="block group">
                      {row}
                    </Link>
                  ) : (
                    <div key={lecture.id}>{row}</div>
                  );
                })}
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Pagination */}
      {totalPages > 1 && (
        <div className="flex items-center justify-center gap-4 mt-8">
          <button
            type="button"
            disabled={page <= 1}
            onClick={() => fetchLectures(page - 1)}
            className="btn-secondary text-sm !py-2 !px-4 disabled:opacity-40 disabled:cursor-not-allowed"
          >
            上一页
          </button>
          <span className="text-sm text-gray-500">
            第 {page} / {totalPages} 页 · 共 {total} 条
          </span>
          <button
            type="button"
            disabled={page >= totalPages}
            onClick={() => fetchLectures(page + 1)}
            className="btn-secondary text-sm !py-2 !px-4 disabled:opacity-40 disabled:cursor-not-allowed"
          >
            下一页
          </button>
        </div>
      )}
    </div>
  );
}
