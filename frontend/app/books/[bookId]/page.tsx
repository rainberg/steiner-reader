'use client';

import { useEffect, useMemo, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import { fetchBook, Book, Lecture } from '@/lib/api';

interface TreeLecture extends Lecture {
  children: TreeLecture[];
}

function buildTree(lectures: Lecture[]): TreeLecture[] {
  const map = new Map<number, TreeLecture>();
  const roots: TreeLecture[] = [];

  for (const lecture of lectures) {
    map.set(lecture.id, { ...lecture, children: [] });
  }

  for (const lecture of lectures) {
    const node = map.get(lecture.id)!;
    const parentId = lecture.parent_id;
    if (parentId && map.has(parentId)) {
      map.get(parentId)!.children.push(node);
    } else {
      roots.push(node);
    }
  }

  return roots;
}

/** Count all leaf lectures (those with sentences) in the tree */
function countLeafLectures(nodes: TreeLecture[]): number {
  let count = 0;
  for (const node of nodes) {
    if (node.children.length === 0) {
      count++;
    } else {
      count += countLeafLectures(node.children);
    }
  }
  return count;
}

/** Aggregate sentence/translation stats across the whole tree */
function aggregateStats(nodes: TreeLecture[]): { total: number; translated: number; images: number } {
  let total = 0;
  let translated = 0;
  let images = 0;
  for (const node of nodes) {
    total += node.sentence_count || 0;
    translated += node.translated_count || 0;
    images += node.image_count || 0;
    if (node.children.length > 0) {
      const child = aggregateStats(node.children);
      total += child.total;
      translated += child.translated;
      images += child.images;
    }
  }
  return { total, translated, images };
}

export default function BookDetailPage() {
  const params = useParams();
  const router = useRouter();
  const bookId = Number(params.bookId);
  const [book, setBook] = useState<Book | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchBook(bookId)
      .then(setBook)
      .catch(() => router.push('/'))
      .finally(() => setLoading(false));
  }, [bookId, router]);

  const sortedLectures = useMemo(
    () => [...(book?.lectures || [])].sort((a, b) => a.order_index - b.order_index),
    [book]
  );
  const tree = useMemo(() => buildTree(sortedLectures), [sortedLectures]);

  if (loading) return <LoadingSkeleton />;
  if (!book) return null;

  const chapterCount = sortedLectures.length;
  const leafCount = countLeafLectures(tree);
  const stats = aggregateStats(tree);

  return (
    <div className="page-container py-8">
      <Link href="/" className="inline-flex items-center gap-1 text-sm text-gray-400 hover:text-indigo-500 transition-colors mb-6">
        <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
        </svg>
        全部书籍
      </Link>

      <div className="mb-8">
        <div className="flex items-center gap-3 mb-2">
          {book.ga_number && (
            <span className="text-xs font-semibold text-indigo-600 bg-indigo-50 border border-indigo-100/60 px-2.5 py-0.5 rounded-md">
              {book.ga_number}
            </span>
          )}
        </div>
        <h1 className="text-2xl sm:text-3xl font-bold text-gray-900 leading-tight">
          {book.title_de}
        </h1>
        {book.title_zh && <p className="text-base text-gray-500 mt-1">{book.title_zh}</p>}
        {book.subtitle_de && <p className="text-sm text-gray-400 mt-0.5 italic">{book.subtitle_de}</p>}

        {/* Book stats summary */}
        <div className="flex items-center gap-4 mt-3 text-xs text-gray-400">
          <span>{chapterCount > leafCount ? `${leafCount} 章节 · ${chapterCount} 条目` : `${chapterCount} 章节`}</span>
          {stats.total > 0 && (
            <>
              <span className="text-gray-200">|</span>
              <span>{stats.total} 句</span>
              {stats.translated > 0 && (
                <span className="text-emerald-500">{stats.translated} 已译</span>
              )}
              {stats.images > 0 && (
                <span>{stats.images} 图</span>
              )}
            </>
          )}
        </div>
      </div>

      {tree.length === 0 ? (
        <div className="text-center py-16 text-gray-400">
          <svg className="w-12 h-12 mx-auto mb-3 text-gray-200" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
          </svg>
          <p className="text-sm">暂无章节</p>
        </div>
      ) : (
        <div className="space-y-2">
          {tree.map(node => (
            <LectureNode key={node.id} node={node} depth={0} />
          ))}
        </div>
      )}
    </div>
  );
}

/** Depth-based indentation classes */
function depthIndent(depth: number): string {
  if (depth <= 0) return '';
  if (depth === 1) return 'ml-4 sm:ml-6';
  return `ml-8 sm:ml-12`;
}

function LectureNode({ node, depth }: { node: TreeLecture; depth: number }) {
  const isHeading = node.level === 'heading';
  const hasChildren = node.children.length > 0;
  const hasContent = (node.sentence_count ?? 0) > 0;
  const indent = depthIndent(depth);

  if (isHeading) {

    const headingContent = (
      <div className={`section-heading ${depth >= 1 ? 'sub-heading' : ''} ${hasContent ? 'hover:border-indigo-200 cursor-pointer transition-colors' : ''}`}>
        <div className="flex items-center gap-2 flex-wrap">
          {node.lecture_date && (
            <span className="text-[10px] text-indigo-400 font-mono">{node.lecture_date}</span>
          )}
          {node.location && (
            <span className="text-[10px] bg-indigo-50/50 text-indigo-500 px-1.5 py-0.5 rounded">
              {node.location}
            </span>
          )}
        </div>
        <h2 className={`${depth >= 1 ? 'text-sm' : 'text-base'} font-semibold text-indigo-800 mt-0.5`}>
          {node.title_de}
        </h2>
        {node.title_zh && <p className="text-xs text-indigo-500/70 mt-0.5">{node.title_zh}</p>}
        {hasContent && (
          <div className="flex items-center gap-2 mt-1.5 text-[10px] text-indigo-400">
            <span>{node.sentence_count} 句</span>
            {(node.translated_count ?? 0) > 0 && (
              <span className="text-emerald-500">已译 {node.translated_count}</span>
            )}
          </div>
        )}
      </div>
    );

    return (
      <div>
        {hasContent ? (
          <Link href={`/books/${node.book_id}/lectures/${node.id}`} className={indent}>
            {headingContent}
          </Link>
        ) : (
          <div className={indent}>{headingContent}</div>
        )}

        {hasChildren && (
          <div className="mt-1.5 space-y-1.5">
            {node.children.map(child => (
              <LectureNode key={child.id} node={child} depth={depth + 1} />
            ))}
          </div>
        )}
      </div>
    );
  }

  // Regular lecture card
  return (
    <div>
      <Link href={`/books/${node.book_id}/lectures/${node.id}`}>
        <div className={`card p-4 ${indent} flex items-center justify-between gap-4 group`}>
          <div className="min-w-0 flex-1">
            <div className="flex items-center gap-2 flex-wrap">
              {node.lecture_date && (
                <span className="text-xs text-gray-400 font-mono whitespace-nowrap">{node.lecture_date}</span>
              )}
              {node.location && (
                <span className="text-xs bg-gray-50 text-gray-500 px-1.5 py-0.5 rounded border border-gray-100 whitespace-nowrap">
                  {node.location}
                </span>
              )}
            </div>
            <h3 className={`${depth >= 1 ? 'text-sm' : 'text-base'} font-medium text-gray-900 mt-1 leading-snug line-clamp-2 group-hover:text-indigo-600 transition-colors`}>
              {node.title_de || 'Vortrag'}
            </h3>
            {node.title_zh && <p className="text-sm text-gray-500 mt-0.5 line-clamp-1">{node.title_zh}</p>}
          </div>

          <div className="flex items-center gap-3 shrink-0">
            {node.sentence_count > 0 && (
              <div className="text-right">
                <span className="text-xs text-gray-400 whitespace-nowrap block">
                  {node.sentence_count} 句
                </span>
                <div className="flex items-center gap-1 mt-0.5">
                  {(node.translated_count ?? 0) > 0 && (
                    <span className="text-[10px] text-emerald-500">{node.translated_count} 已译</span>
                  )}
                  {(node.image_count ?? 0) > 0 && (
                    <span className="text-[10px] text-gray-400">图 {node.image_count}</span>
                  )}
                </div>
              </div>
            )}
            <svg className="w-4 h-4 text-gray-300 group-hover:text-indigo-400 transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </div>
        </div>
      </Link>

      {hasChildren && (
        <div className="mt-1.5 space-y-1.5">
          {node.children.map(child => (
            <LectureNode key={child.id} node={child} depth={depth + 1} />
          ))}
        </div>
      )}
    </div>
  );
}

function LoadingSkeleton() {
  return (
    <div className="page-container py-8">
      <div className="shimmer h-4 w-20 rounded mb-6" />
      <div className="shimmer h-8 w-72 rounded mb-2" />
      <div className="shimmer h-4 w-48 rounded mb-8" />
      <div className="space-y-3">
        {Array.from({ length: 8 }).map((_, i) => (
          <div key={i} className="shimmer h-16 rounded-xl" />
        ))}
      </div>
    </div>
  );
}
