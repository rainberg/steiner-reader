'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import { fetchLecture, translateLecture, Lecture, Sentence } from '@/lib/api';

type ReadingMode = 'de-zh' | 'de-only' | 'zh-only';

export default function LecturePage() {
  const params = useParams();
  const router = useRouter();
  const bookId = Number(params.bookId);
  const lectureId = Number(params.lectureId);

  const [lecture, setLecture] = useState<Lecture | null>(null);
  const [loading, setLoading] = useState(true);
  const [mode, setMode] = useState<ReadingMode>('de-zh');
  const [translating, setTranslating] = useState(false);
  const [translateStatus, setTranslateStatus] = useState<string | null>(null);

  const loadLecture = async () => {
    try {
      const data = await fetchLecture(bookId, lectureId);
      setLecture(data);
    } catch {
      router.push(`/books/${bookId}`);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadLecture();
  }, [bookId, lectureId]);

  const handleTranslate = async () => {
    setTranslating(true);
    setTranslateStatus(null);
    try {
      const res = await translateLecture(lectureId);
      setTranslateStatus(`✅ ${res.message}`);
      // Reload to show translations
      await loadLecture();
    } catch (err: any) {
      setTranslateStatus(`❌ ${err.message}`);
    } finally {
      setTranslating(false);
    }
  };

  if (loading) {
    return <div className="min-h-screen flex items-center justify-center text-gray-400">加载中...</div>;
  }

  if (!lecture) return null;

  const totalSentences = lecture.paragraphs.reduce((sum, p) => sum + p.sentences.length, 0);
  const translatedSentences = lecture.paragraphs.reduce(
    (sum, p) => sum + p.sentences.filter(s => s.text_zh).length,
    0
  );
  const allTranslated = translatedSentences === totalSentences && totalSentences > 0;

  return (
    <main className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="sticky top-0 bg-white border-b border-gray-200 z-10">
        <div className="max-w-4xl mx-auto px-4 py-3">
          <div className="flex items-center justify-between flex-wrap gap-2">
            <Link href={`/books/${bookId}`} className="text-blue-600 hover:underline text-sm">
              ← 返回目录
            </Link>

            <div className="flex items-center gap-2">
              {/* Translate button */}
              <button
                onClick={handleTranslate}
                disabled={translating || allTranslated}
                className={`px-3 py-1 rounded-lg text-sm transition ${
                  allTranslated
                    ? 'bg-green-100 text-green-600 cursor-default'
                    : 'bg-green-600 text-white hover:bg-green-700 disabled:opacity-50'
                }`}
              >
                {allTranslated ? '✅ 已翻译' : translating ? '翻译中...' : `🌐 翻译本章 (${translatedSentences}/${totalSentences})`}
              </button>

              {/* Reading mode toggle */}
              <div className="flex bg-gray-100 rounded-lg p-1">
                <button
                  onClick={() => setMode('de-zh')}
                  className={`px-3 py-1 rounded-md text-sm transition ${mode === 'de-zh' ? 'bg-white shadow text-gray-900' : 'text-gray-500'}`}
                >
                  德中对照
                </button>
                <button
                  onClick={() => setMode('de-only')}
                  className={`px-3 py-1 rounded-md text-sm transition ${mode === 'de-only' ? 'bg-white shadow text-gray-900' : 'text-gray-500'}`}
                >
                  仅德语
                </button>
                <button
                  onClick={() => setMode('zh-only')}
                  className={`px-3 py-1 rounded-md text-sm transition ${mode === 'zh-only' ? 'bg-white shadow text-gray-900' : 'text-gray-500'}`}
                >
                  仅中文
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Translate status */}
      {translateStatus && (
        <div className="max-w-4xl mx-auto px-4 mt-3">
          <div className={`text-sm px-3 py-2 rounded-lg ${translateStatus.startsWith('✅') ? 'bg-green-50 text-green-700' : 'bg-red-50 text-red-700'}`}>
            {translateStatus}
          </div>
        </div>
      )}

      {/* Content */}
      <div className="max-w-4xl mx-auto px-4 py-6">
        <div className="mb-6">
          <h1 className="text-xl font-bold text-gray-900">
            {lecture.title_de || 'Vortrag'}
          </h1>
          <div className="text-sm text-gray-500 mt-1">
            {lecture.location && <span>📍 {lecture.location}</span>}
            {lecture.lecture_date && <span className="ml-3">📅 {lecture.lecture_date}</span>}
            <span className="ml-3">📄 {lecture.paragraphs.length} 段落</span>
            <span className="ml-3">💬 {translatedSentences}/{totalSentences} 已翻译</span>
          </div>
        </div>

        <div className="space-y-6">
          {lecture.paragraphs.map((para, pi) => (
            <div key={para.id} className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
              <div className="text-xs text-gray-400 mb-3">¶ {pi + 1}</div>
              <div className="space-y-3">
                {para.sentences.map((sent, si) => (
                  <SentenceView key={sent.id} sentence={sent} mode={mode} index={si + 1} />
                ))}
              </div>
            </div>
          ))}
        </div>

        {lecture.paragraphs.length === 0 && (
          <div className="text-center py-12 text-gray-400">该演讲暂无内容</div>
        )}
      </div>
    </main>
  );
}

function SentenceView({ sentence, mode, index }: { sentence: Sentence; mode: ReadingMode; index: number }) {
  const hasTranslation = !!sentence.text_zh;

  if (mode === 'de-only') {
    return (
      <div className="flex">
        <span className="text-gray-300 text-xs mr-2 mt-1 w-5 text-right">{index}</span>
        <p className="text-gray-800 leading-relaxed">{sentence.text_de}</p>
      </div>
    );
  }

  if (mode === 'zh-only') {
    return (
      <div className="flex">
        <span className="text-gray-300 text-xs mr-2 mt-1 w-5 text-right">{index}</span>
        {hasTranslation ? (
          <p className="text-gray-700 leading-relaxed">{sentence.text_zh}</p>
        ) : (
          <p className="text-gray-400 italic leading-relaxed">（未翻译 — 点击上方按钮翻译本章）</p>
        )}
      </div>
    );
  }

  // de-zh parallel
  return (
    <div className="flex">
      <span className="text-gray-300 text-xs mr-2 mt-1 w-5 text-right">{index}</span>
      <div className="flex-1">
        <p className="text-gray-800 leading-relaxed">{sentence.text_de}</p>
        {hasTranslation && (
          <p className="text-gray-500 text-sm mt-1 leading-relaxed">{sentence.text_zh}</p>
        )}
      </div>
    </div>
  );
}
