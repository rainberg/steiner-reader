"use client";

import { useMemo, useState } from "react";
import Link from "next/link";
import type { BookSummary } from "@/lib/api";

export default function HomeClient({ books, loadError }: { books: BookSummary[]; loadError: string | null }) {
  const [search, setSearch] = useState("");

  const filteredBooks = useMemo(() => {
    const q = search.trim().toLowerCase();
    if (!q) return books;
    return books.filter((book) =>
      (book.ga_number?.toLowerCase() || "").includes(q) ||
      book.title_de.toLowerCase().includes(q) ||
      (book.title_zh?.toLowerCase() || "").includes(q)
    );
  }, [books, search]);

  const totalLectures = books.reduce((sum, book) => sum + book.lecture_count, 0);
  const totalSentences = books.reduce((sum, book) => sum + book.sentence_count, 0);

  return (
    <div className="page-container py-8">
      <div className="mb-8">
        <h1 className="text-3xl sm:text-4xl font-bold text-gray-900 tracking-tight">施泰纳著作库</h1>
        <p className="text-gray-500 mt-2 max-w-xl">
          Rudolf Steiner <span className="text-gray-400">Gesamtausgabe</span>
          {" · "}在线阅读与检索
        </p>
        <div className="flex items-center gap-4 mt-4 text-sm text-gray-400">
          <span className="flex items-center gap-1">{books.length} 本图书</span>
          <span className="flex items-center gap-1">{totalLectures.toLocaleString()} 场讲座</span>
          <span className="flex items-center gap-1">{totalSentences.toLocaleString()} 句文本</span>
        </div>
      </div>

      {loadError && (
        <div className="mb-4 rounded-lg border border-amber-200 bg-amber-50 px-3 py-2 text-sm text-amber-700">
          {loadError}
        </div>
      )}

      <div className="mb-6 relative">
        <input
          type="text"
          placeholder="搜索 GA 编号或书名"
          value={search}
          onChange={(event) => setSearch(event.target.value)}
          className="w-full pl-4 pr-4 py-2.5 bg-white border border-gray-200 rounded-xl text-sm text-gray-700 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-300 transition-all"
        />
      </div>

      {filteredBooks.length === 0 ? (
        <div className="text-center py-16">
          <p className="text-gray-400 text-lg mb-2">{search ? `未找到："${search}"` : "暂无图书数据"}</p>
          {!search && (
            <Link href="/upload" className="text-indigo-500 hover:text-indigo-600 text-sm">
              前往上传页面
            </Link>
          )}
        </div>
      ) : (
        <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {filteredBooks.map((book) => (
            <BookCard key={book.id} book={book} />
          ))}
        </div>
      )}
    </div>
  );
}

function BookCard({ book }: { book: BookSummary }) {
  return (
    <Link href={`/books/${book.id}`}>
      <div className="card p-5 h-full flex flex-col group">
        <div className="flex items-start justify-between mb-2">
          {book.ga_number ? (
            <span className="inline-block bg-indigo-50 text-indigo-700 text-xs font-semibold px-2 py-0.5 rounded-md border border-indigo-100/50">
              {book.ga_number}
            </span>
          ) : (
            <span />
          )}
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
    </Link>
  );
}
