'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { fetchBooks, Book } from '@/lib/api';

export default function HomePage() {
  const [books, setBooks] = useState<Book[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchBooks()
      .then(setBooks)
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  return (
    <main className="min-h-screen bg-gray-50">
      <div className="max-w-4xl mx-auto px-4 py-8">
        <div className="flex items-center justify-between mb-8">
          <div>
            <h1 className="text-3xl font-bold text-gray-900">Steiner Reader</h1>
            <p className="text-gray-500 mt-1">鲁道夫·施泰纳著作阅读平台</p>
          </div>
          <Link
            href="/upload"
            className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition"
          >
            📤 上传 PDF
          </Link>
        </div>

        {loading ? (
          <div className="text-center py-12 text-gray-400">加载中...</div>
        ) : books.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-400 text-lg mb-4">还没有书籍</p>
            <Link href="/upload" className="text-blue-600 hover:underline">
              上传第一个 PDF
            </Link>
          </div>
        ) : (
          <div className="grid gap-4">
            {books.map(book => (
              <BookCard key={book.id} book={book} />
            ))}
          </div>
        )}
      </div>
    </main>
  );
}

function BookCard({ book }: { book: Book }) {
  const totalSentences = book.lectures.reduce((sum, l) => sum + l.sentence_count, 0);

  return (
    <Link href={`/books/${book.id}`}>
      <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-6 hover:shadow-md transition">
        <div className="flex items-start justify-between">
          <div>
            <h2 className="text-xl font-semibold text-gray-900">
              {book.ga_number && (
                <span className="text-blue-600 mr-2">{book.ga_number}</span>
              )}
              {book.title_de}
            </h2>
            {book.title_zh && (
              <p className="text-gray-600 mt-1">{book.title_zh}</p>
            )}
          </div>
          <span className="text-sm text-gray-400">{book.pdf_filename.split('_').pop()}</span>
        </div>

        <div className="flex gap-4 mt-4 text-sm text-gray-500">
          <span>🎤 {book.lectures.length} 演讲</span>
          <span>📝 {totalSentences} 句子</span>
          <span>📅 {new Date(book.created_at).toLocaleDateString('zh-CN')}</span>
        </div>
      </div>
    </Link>
  );
}
