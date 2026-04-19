'use client';

import { useEffect, useState, useRef } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import { fetchLecture, translateLecture, getTranslationStatus, Lecture, Sentence } from '@/lib/api';

type ReadingMode = 'de-zh' | 'de-only' | 'zh-only';

export default function LecturePage() {
  const params = useParams();
  const router = useRouter();
  const bookId = Number(params.bookId);
  const lectureId = Number(params.lectureId);

  const [lecture, setLecture] = useState<Lecture | null>(null);
  const [loading, setLoading] = useState(true);
  const [mode, setMode] = useState<ReadingMode>('de-only'); // Default to de-only
  const [translating, setTranslating] = useState(false);
  const [translateMsg, setTranslateMsg] = useState<string | null>(null);
  const pollingRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const loadLecture = async () => {
    try {
      const data = await fetchLecture(bookId, lectureId);
      setLecture(data);

      // Auto-switch mode based on translation availability
      const hasAnyTranslation = data.paragraphs.some(p => p.sentences.some(s => s.text_zh));
      if (hasAnyTranslation && mode === 'de-only') {
        setMode('de-zh');
      }
    } catch {
      router.push(`/books/${bookId}`);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadLecture();
    return () => {
      if (pollingRef.current) clearInterval(pollingRef.current);
    };
  }, [bookId, lectureId]);

  // Poll for translation progress
  const startPolling = () => {
    if (pollingRef.current) clearInterval(pollingRef.current);
    pollingRef.current = setInterval(async () => {
      try {
        const status = await getTranslationStatus(lectureId);
        if (status.completed) {
          // Translation done!
          if (pollingRef.current) clearInterval(pollingRef.current);
          setTranslating(false);
          setTranslateMsg(`✅ 翻译完成: ${status.translated} 句`);
          await loadLecture(); // Reload to show translations
          setMode('de-zh'); // Switch to bilingual mode
        } else {
          setTranslateMsg(`⏳ 翻译中: ${status.translated}/${status.total} 句`);
          // Update local counts without full reload
          setLecture(prev => {
            if (!prev) return prev;
            return { ...prev }; // Trigger re-render for count display
          });
        }
      } catch {
        // Keep polling on error
      }
    }, 3000);
  };

  const handleTranslate = async () => {
    setTranslating(true);
    setTranslateMsg('⏳ 启动翻译...');
    try {
      const res = await translateLecture(lectureId);
      if (res.status === 'already_translated') {
        setTranslating(false);
        setTranslateMsg('✅ 已翻译');
        await loadLecture();
        setMode('de-zh');
      } else {
        setTranslateMsg(`⏳ 翻译中: 0/${res.total} 句`);
        startPolling();
      }
    } catch (err: any) {
      setTranslating(false);
      setTranslateMsg(`❌ ${err.message}`);
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
              {/* Reading mode toggle */}
              <div className="flex bg-gray-100 rounded-lg p-1">
                <button
                  onClick={() => setMode('de-zh')}
                  disabled={!allTranslated && translatedSentences === 0}
                  className={`px-3 py-1 rounded-md text-sm transition ${
                    mode === 'de-zh' ? 'bg-white shadow text-gray-900' : 'text-gray-500'
                  } ${!allTranslated && translatedSentences === 0 ? 'opacity-40 cursor-not-allowed' : ''}`}
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
                  disabled={translatedSentences === 0}
                  className={`px-3 py-1 rounded-md text-sm transition ${
                    mode === 'zh-only' ? 'bg-white shadow text-gray-900' : 'text-gray-500'
                  } ${translatedSentences === 0 ? 'opacity-40 cursor-not-allowed' : ''}`}
                >
                  仅中文
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Translate status bar */}
      {translateMsg && (
        <div className="max-w-4xl mx-auto px-4 mt-3">
          <div className={`text-sm px-3 py-2 rounded-lg ${
            translateMsg.startsWith('✅') ? 'bg-green-50 text-green-700' :
            translateMsg.startsWith('❌') ? 'bg-red-50 text-red-700' :
            'bg-yellow-50 text-yellow-700'
          }`}>
            {translateMsg}
          </div>
        </div>
      )}

      {/* Content */}
      <div className="max-w-4xl mx-auto px-4 py-6">
        {/* Lecture title */}
        <div className="mb-6">
          <h1 className="text-xl font-bold text-gray-900">
            {lecture.title_de || 'Vortrag'}
          </h1>
          <div className="text-sm text-gray-500 mt-1 flex items-center gap-3 flex-wrap">
            {lecture.location && <span>📍 {lecture.location}</span>}
            {lecture.lecture_date && <span>📅 {lecture.lecture_date}</span>}
            <span>📄 {lecture.paragraphs.length} 段落</span>
            <span>💬 {translatedSentences}/{totalSentences} 已翻译</span>
          </div>
        </div>

        {/* Big translate button — shown prominently when not translated */}
        {!allTranslated && !translating && (
          <div className="mb-6 bg-gradient-to-r from-blue-50 to-green-50 rounded-xl p-6 border border-blue-100 text-center">
            <p className="text-gray-600 mb-3">
              {translatedSentences === 0
                ? '本篇演讲尚未翻译，当前仅显示德语原文'
                : `本篇演讲已翻译 ${translatedSentences}/${totalSentences} 句`
              }
            </p>
            <button
              onClick={handleTranslate}
              className="bg-blue-600 text-white px-6 py-3 rounded-lg text-base font-medium hover:bg-blue-700 transition shadow-sm"
            >
              🌐 {translatedSentences === 0 ? '翻译本篇演讲' : '继续翻译'}
            </button>
            <p className="text-xs text-gray-400 mt-2">翻译完成后可切换「德中对照」阅读模式</p>
          </div>
        )}

        {/* Translating indicator */}
        {translating && (
          <div className="mb-6 bg-yellow-50 rounded-xl p-6 border border-yellow-100 text-center">
            <div className="animate-pulse">
              <p className="text-yellow-700 text-lg">⏳ 翻译进行中...</p>
              <p className="text-yellow-600 text-sm mt-1">翻译完成后会自动显示</p>
            </div>
          </div>
        )}

        {/* Paragraphs */}
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

        {/* Bottom translate button */}
        {!allTranslated && !translating && (
          <div className="mt-8 text-center">
            <button
              onClick={handleTranslate}
              className="bg-blue-600 text-white px-6 py-3 rounded-lg text-base font-medium hover:bg-blue-700 transition shadow-sm"
            >
              🌐 {translatedSentences === 0 ? '翻译本篇演讲' : '继续翻译'}
            </button>
          </div>
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
        <span className="text-gray-300 text-xs mr-2 mt-1 w-5 text-right select-none">{index}</span>
        <p className="text-gray-800 leading-relaxed">{sentence.text_de}</p>
      </div>
    );
  }

  if (mode === 'zh-only') {
    return (
      <div className="flex">
        <span className="text-gray-300 text-xs mr-2 mt-1 w-5 text-right select-none">{index}</span>
        {hasTranslation ? (
          <p className="text-gray-700 leading-relaxed">{sentence.text_zh}</p>
        ) : (
          <p className="text-gray-400 italic leading-relaxed">（未翻译）</p>
        )}
      </div>
    );
  }

  // de-zh parallel
  return (
    <div className="flex">
      <span className="text-gray-300 text-xs mr-2 mt-1 w-5 text-right select-none">{index}</span>
      <div className="flex-1">
        <p className="text-gray-800 leading-relaxed">{sentence.text_de}</p>
        {hasTranslation && (
          <p className="text-gray-500 text-sm mt-1 leading-relaxed">{sentence.text_zh}</p>
        )}
      </div>
    </div>
  );
}
