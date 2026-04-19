'use client';

import { useEffect, useState, useCallback } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import { fetchBook, translateLecture, getTranslationStatus, BookDetail, LectureListItem } from '@/lib/api';

export default function BookPage() {
  const params = useParams();
  const router = useRouter();
  const bookId = Number(params.bookId);
  const [book, setBook] = useState<BookDetail | null>(null);
  const [loading, setLoading] = useState(true);
  // Track which lectures are currently being translated
  const [translatingIds, setTranslatingIds] = useState<Set<number>>(new Set());

  const loadBook = useCallback(async () => {
    try {
      const data = await fetchBook(bookId);
      setBook(data);
    } catch {
      router.push('/');
    } finally {
      setLoading(false);
    }
  }, [bookId, router]);

  useEffect(() => {
    loadBook();
  }, [loadBook]);

  // Poll translation status for lectures that are being translated
  useEffect(() => {
    if (translatingIds.size === 0) return;

    const interval = setInterval(async () => {
      const stillTranslating = new Set<number>();

      for (const lectureId of translatingIds) {
        try {
          const status = await getTranslationStatus(lectureId);
          if (status.completed) {
            // Done! Update locally
            setBook(prev => {
              if (!prev) return prev;
              return {
                ...prev,
                lectures: prev.lectures.map(l =>
                  l.id === lectureId
                    ? { ...l, translated_count: status.translated }
                    : l
                ),
              };
            });
          } else {
            // Still translating — update count
            setBook(prev => {
              if (!prev) return prev;
              return {
                ...prev,
                lectures: prev.lectures.map(l =>
                  l.id === lectureId
                    ? { ...l, translated_count: status.translated }
                    : l
                ),
              };
            });
            stillTranslating.add(lectureId);
          }
        } catch {
          stillTranslating.add(lectureId);
        }
      }

      setTranslatingIds(stillTranslating);
    }, 3000); // Poll every 3 seconds

    return () => clearInterval(interval);
  }, [translatingIds]);

  const handleTranslate = async (lectureId: number, e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();

    setTranslatingIds(prev => new Set(prev).add(lectureId));
    try {
      await translateLecture(lectureId);
      // Start polling (handled by the effect above)
    } catch (err: any) {
      alert('翻译启动失败: ' + err.message);
      setTranslatingIds(prev => {
        const next = new Set(prev);
        next.delete(lectureId);
        return next;
      });
    }
  };

  if (loading) {
    return <div className="min-h-screen flex items-center justify-center text-gray-400">加载中...</div>;
  }

  if (!book) return null;

  const totalSentences = book.lectures.reduce((sum, l) => sum + l.sentence_count, 0);
  const translatedSentences = book.lectures.reduce((sum, l) => sum + l.translated_count, 0);

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
          {book.lectures.map((lec, i) => (
            <LectureCard
              key={lec.id}
              lecture={lec}
              index={i + 1}
              bookId={book.id}
              isTranslating={translatingIds.has(lec.id)}
              onTranslate={handleTranslate}
            />
          ))}
        </div>
      </div>
    </main>
  );
}

function LectureCard({
  lecture,
  index,
  bookId,
  isTranslating,
  onTranslate,
}: {
  lecture: LectureListItem;
  index: number;
  bookId: number;
  isTranslating: boolean;
  onTranslate: (id: number, e: React.MouseEvent) => void;
}) {
  const isFullyTranslated = lecture.sentence_count > 0 && lecture.translated_count === lecture.sentence_count;
  const hasSomeTranslation = lecture.translated_count > 0 && !isFullyTranslated;

  return (
    <div className="bg-white rounded-lg border border-gray-100 p-4 hover:shadow-sm transition">
      <div className="flex items-center justify-between gap-3">
        {/* Clickable lecture title */}
        <Link href={`/books/${bookId}/lectures/${lecture.id}`} className="flex-1 min-w-0">
          <div>
            <span className="text-gray-400 text-sm mr-3">{index}.</span>
            <span className="font-medium text-gray-800">
              {lecture.title_de || 'Vortrag'}
            </span>
            {lecture.location && (
              <span className="text-gray-400 ml-2 text-sm">📍 {lecture.location}</span>
            )}
            <div className="text-xs text-gray-400 mt-1 ml-6">
              {lecture.lecture_date && <span className="mr-3">📅 {lecture.lecture_date}</span>}
              <span>{lecture.sentence_count} 句</span>
            </div>
          </div>
        </Link>

        {/* Translation status & button */}
        <div className="flex items-center gap-2 shrink-0">
          {isFullyTranslated ? (
            <span className="text-xs bg-green-50 text-green-600 px-2 py-1 rounded-full">
              ✅ 已翻译
            </span>
          ) : isTranslating ? (
            <span className="text-xs bg-yellow-50 text-yellow-600 px-2 py-1 rounded-full animate-pulse">
              ⏳ 翻译中 {lecture.translated_count}/{lecture.sentence_count}
            </span>
          ) : hasSomeTranslation ? (
            <>
              <span className="text-xs bg-yellow-50 text-yellow-600 px-2 py-1 rounded-full">
                {lecture.translated_count}/{lecture.sentence_count}
              </span>
              <button
                onClick={(e) => onTranslate(lecture.id, e)}
                className="text-xs bg-green-600 text-white px-3 py-1 rounded-full hover:bg-green-700 transition"
              >
                🌐 继续翻译
              </button>
            </>
          ) : (
            <button
              onClick={(e) => onTranslate(lecture.id, e)}
              className="text-xs bg-blue-600 text-white px-3 py-1 rounded-full hover:bg-blue-700 transition"
            >
              🌐 翻译
            </button>
          )}
          <Link
            href={`/books/${bookId}/lectures/${lecture.id}`}
            className="text-blue-500 text-sm hover:underline"
          >
            阅读 →
          </Link>
        </div>
      </div>
    </div>
  );
}
