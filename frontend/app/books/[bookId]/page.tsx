'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import { fetchBook, BookDetail } from '@/lib/api';

export default function BookPage() {
  const params = useParams();
  const router = useRouter();
  const bookId = Number(params.bookId);
  const [book, setBook] = useState<BookDetail | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchBook(bookId)
      .then(setBook)
      .catch(() => router.push('/'))
      .finally(() => setLoading(false));
  }, [bookId, router]);

  if (loading) {
    return <div className="min-h-screen flex items-center justify-center text-gray-400">加载中...</div>;
  }

  if (!book) return null;

  // Count total sentences across all lectures
  const totalSentences = book.lectures.reduce(
    (sum, lec) => sum + lec.paragraphs.reduce((s, p) => s + p.sentences.length, 0),
    0
  );
  const translatedSentences = book.lectures.reduce(
    (sum, lec) => sum + lec.paragraphs.reduce(
      (s, p) => s + p.sentences.filter(sent => sent.text_zh).length, 0
    ),
    0
  );

  return (
    <main className="min-h-screen bg-gray-50">
      <div className="max-w-4xl mx-auto px-4 py-8">
        <Link href="/" className="text-blue-600 hover:underline text-sm">← 返回书架</Link>

        <div className="mt-4 mb-8">
          <h1 className="text-2xl font-bold text-gray-900">
            {book.ga_number && <span className="text-blue-600 mr-2">{book.ga_number}</span>}
            {book.title_de}
          </h1>
          {book.title_zh && <p className="text-gray-600 mt-1">{book.title_zh}</p>}
          <p className="text-sm text-gray-400 mt-2">
            💬 {translatedSentences}/{totalSentences} 句已翻译
          </p>
        </div>

        <h2 className="text-lg font-semibold text-gray-700 mb-4">
          演讲目录 ({book.lectures.length})
        </h2>

        <div className="grid gap-2">
          {book.lectures.map((lec, i) => {
            const lecTotal = lec.paragraphs.reduce((s, p) => s + p.sentences.length, 0);
            const lecTranslated = lec.paragraphs.reduce(
              (s, p) => s + p.sentences.filter(sent => sent.text_zh).length, 0
            );
            const isFullyTranslated = lecTotal > 0 && lecTranslated === lecTotal;

            return (
              <Link key={lec.id} href={`/books/${book.id}/lectures/${lec.id}`}>
                <div className="bg-white rounded-lg border border-gray-100 p-4 hover:shadow-sm transition flex items-center justify-between">
                  <div className="flex-1">
                    <span className="text-gray-400 text-sm mr-3">{i + 1}.</span>
                    <span className="font-medium text-gray-800">
                      {lec.title_de || 'Vortrag'}
                    </span>
                    {lec.location && (
                      <span className="text-gray-400 ml-2 text-sm">📍 {lec.location}</span>
                    )}
                  </div>
                  <div className="text-sm text-gray-400 flex gap-3 items-center">
                    {lec.lecture_date && <span>{lec.lecture_date}</span>}
                    <span>{lecTotal} 句</span>
                    {isFullyTranslated ? (
                      <span className="text-green-500">✅</span>
                    ) : lecTranslated > 0 ? (
                      <span className="text-yellow-500">{lecTranslated}/{lecTotal}</span>
                    ) : null}
                    <span className="text-blue-500">阅读 →</span>
                  </div>
                </div>
              </Link>
            );
          })}
        </div>
      </div>
    </main>
  );
}
