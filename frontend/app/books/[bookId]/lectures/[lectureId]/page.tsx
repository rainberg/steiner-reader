'use client';

import { useEffect, useState, useRef } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import { fetchLecture, translateLecture, getTranslationStatus, fetchLectureImages, getStoredUser, getTranslationCost, Lecture, Sentence, LectureImage, TranslationCost } from '@/lib/api';

type ReadingMode = 'de-zh' | 'de-only' | 'zh-only';

export default function LecturePage() {
  const params = useParams();
  const router = useRouter();
  const bookId = Number(params.bookId);
  const lectureId = Number(params.lectureId);

  const [lecture, setLecture] = useState<Lecture | null>(null);
  const [images, setImages] = useState<LectureImage[]>([]);
  const [loading, setLoading] = useState(true);
  const [mode, setMode] = useState<ReadingMode>('de-only');
  const [translating, setTranslating] = useState(false);
  const [translateMsg, setTranslateMsg] = useState<string | null>(null);
  const [lightboxImg, setLightboxImg] = useState<string | null>(null);
  const [costInfo, setCostInfo] = useState<TranslationCost | null>(null);
  const [userCredits, setUserCredits] = useState<number | null>(null);
  const pollingRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const loadLecture = async () => {
    try {
      const [data, imgs] = await Promise.all([
        fetchLecture(bookId, lectureId),
        fetchLectureImages(lectureId).catch(() => []),
      ]);
      setLecture(data);
      setImages(imgs);
      const hasAnyTranslation = data.paragraphs.some(p => p.sentences.some(s => s.text_zh));
      if (hasAnyTranslation && mode === 'de-only') setMode('de-zh');

      // Load translation cost
      try {
        const cost = await getTranslationCost(lectureId);
        setCostInfo(cost);
        if (cost.user_credits !== null) setUserCredits(cost.user_credits);
      } catch {}
    } catch {
      router.push(`/books/${bookId}`);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadLecture();
    return () => { if (pollingRef.current) clearInterval(pollingRef.current); };
  }, [bookId, lectureId]);

  const startPolling = () => {
    if (pollingRef.current) clearInterval(pollingRef.current);
    pollingRef.current = setInterval(async () => {
      try {
        const status = await getTranslationStatus(lectureId);
        if (status.completed) {
          if (pollingRef.current) clearInterval(pollingRef.current);
          setTranslating(false);
          setTranslateMsg(`✅ 翻译完成: ${status.translated} 句`);
          await loadLecture();
          setMode('de-zh');
        } else {
          setTranslateMsg(`⏳ 翻译中: ${status.translated}/${status.total} 句`);
        }
      } catch {}
    }, 3000);
  };

  const handleTranslate = async () => {
    const user = getStoredUser();
    if (!user) {
      router.push('/login');
      return;
    }

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
        setTranslateMsg(`⏳ 翻译中: 0/${res.total} 句 (消耗 ${res.cost} 点)`);
        if (res.credits !== undefined) setUserCredits(res.credits);
        startPolling();
      }
    } catch (err: any) {
      setTranslating(false);
      if (err.message.includes('点数不足') || err.message.includes('请先登录')) {
        setTranslateMsg(`❌ ${err.message}`);
      } else {
        setTranslateMsg(`❌ ${err.message}`);
      }
    }
  };

  if (loading) return <div className="min-h-screen flex items-center justify-center text-gray-400">加载中...</div>;
  if (!lecture) return null;

  const totalSentences = lecture.paragraphs.reduce((sum, p) => sum + p.sentences.length, 0);
  const translatedSentences = lecture.paragraphs.reduce((sum, p) => sum + p.sentences.filter(s => s.text_zh).length, 0);
  const allTranslated = translatedSentences === totalSentences && totalSentences > 0;
  const user = getStoredUser();

  // Build image lookup by paragraph ID
  const imagesByParagraph: Record<number, LectureImage[]> = {};
  for (const img of images) {
    if (img.after_paragraph_id) {
      if (!imagesByParagraph[img.after_paragraph_id]) imagesByParagraph[img.after_paragraph_id] = [];
      imagesByParagraph[img.after_paragraph_id].push(img);
    }
  }

  return (
    <main className="min-h-screen bg-gray-50">
      {lightboxImg && (
        <div className="fixed inset-0 bg-black/80 z-50 flex items-center justify-center p-4 cursor-pointer" onClick={() => setLightboxImg(null)}>
          <img src={lightboxImg} className="max-w-full max-h-full object-contain rounded-lg" />
        </div>
      )}

      {/* Header */}
      <div className="sticky top-0 bg-white border-b border-gray-200 z-10">
        <div className="max-w-4xl mx-auto px-4 py-3">
          <div className="flex items-center justify-between flex-wrap gap-2">
            <Link href={`/books/${bookId}`} className="text-blue-600 hover:underline text-sm">← 返回目录</Link>
            <div className="flex items-center gap-2">
              <div className="flex bg-gray-100 rounded-lg p-1">
                <button onClick={() => setMode('de-zh')}
                  disabled={!allTranslated && translatedSentences === 0}
                  className={`px-3 py-1 rounded-md text-sm transition ${mode === 'de-zh' ? 'bg-white shadow text-gray-900' : 'text-gray-500'} ${!allTranslated && translatedSentences === 0 ? 'opacity-40 cursor-not-allowed' : ''}`}
                >德中对照</button>
                <button onClick={() => setMode('de-only')}
                  className={`px-3 py-1 rounded-md text-sm transition ${mode === 'de-only' ? 'bg-white shadow text-gray-900' : 'text-gray-500'}`}
                >仅德语</button>
                <button onClick={() => setMode('zh-only')}
                  disabled={translatedSentences === 0}
                  className={`px-3 py-1 rounded-md text-sm transition ${mode === 'zh-only' ? 'bg-white shadow text-gray-900' : 'text-gray-500'} ${translatedSentences === 0 ? 'opacity-40 cursor-not-allowed' : ''}`}
                >仅中文</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      {translateMsg && (
        <div className="max-w-4xl mx-auto px-4 mt-3">
          <div className={`text-sm px-3 py-2 rounded-lg ${translateMsg.startsWith('✅') ? 'bg-green-50 text-green-700' : translateMsg.startsWith('❌') ? 'bg-red-50 text-red-700' : 'bg-yellow-50 text-yellow-700'}`}>
            {translateMsg}
          </div>
        </div>
      )}

      <div className="max-w-4xl mx-auto px-4 py-6">
        <div className="mb-6">
          <h1 className="text-xl font-bold text-gray-900">{lecture.title_de || 'Vortrag'}</h1>
          <div className="text-sm text-gray-500 mt-1 flex items-center gap-3 flex-wrap">
            {lecture.location && <span>📍 {lecture.location}</span>}
            {lecture.lecture_date && <span>📅 {lecture.lecture_date}</span>}
            <span>📄 {lecture.paragraphs.length} 段落</span>
            <span>💬 {translatedSentences}/{totalSentences} 已翻译</span>
            {images.length > 0 && <span>🖼️ {images.length} 插图</span>}
          </div>
        </div>

        {/* Translate button section */}
        {!allTranslated && !translating && (
          <div className="mb-6 bg-gradient-to-r from-blue-50 to-green-50 rounded-xl p-6 border border-blue-100 text-center">
            <p className="text-gray-600 mb-2">
              {translatedSentences === 0 ? '本篇演讲尚未翻译' : `已翻译 ${translatedSentences}/${totalSentences} 句`}
            </p>
            {costInfo && !costInfo.already_translated && (
              <p className="text-sm text-gray-500 mb-3">
                翻译消耗 <span className="font-semibold text-orange-600">{costInfo.cost} 点</span>
                {user ? (
                  <span> · 当前余额 <span className="font-semibold">{userCredits ?? user.credits} 点</span></span>
                ) : (
                  <span> · <Link href="/login" className="text-blue-600 hover:underline">登录</Link>后可翻译</span>
                )}
              </p>
            )}
            <button
              onClick={handleTranslate}
              disabled={costInfo && user && !costInfo.can_afford ? true : undefined}
              className={`px-6 py-3 rounded-lg text-base font-medium transition shadow-sm ${
                !user
                  ? 'bg-gray-400 text-white hover:bg-gray-500'
                  : costInfo && !costInfo.can_afford
                  ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                  : 'bg-blue-600 text-white hover:bg-blue-700'
              }`}
            >
              {!user ? '🔑 登录后翻译' : costInfo && !costInfo.can_afford ? '⚡ 点数不足' : `🌐 翻译本篇 (${costInfo?.cost || 10} 点)`}
            </button>
          </div>
        )}

        {translating && (
          <div className="mb-6 bg-yellow-50 rounded-xl p-6 border border-yellow-100 text-center animate-pulse">
            <p className="text-yellow-700 text-lg">⏳ 翻译进行中...</p>
          </div>
        )}

        {/* Content: paragraphs with inline images */}
        <div className="space-y-6">
          {lecture.paragraphs.map((para, pi) => (
            <div key={para.id}>
              <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-5">
                <div className="text-xs text-gray-400 mb-3">¶ {pi + 1}</div>
                <div className="space-y-3">
                  {para.sentences.map((sent, si) => (
                    <SentenceView key={sent.id} sentence={sent} mode={mode} index={si + 1} />
                  ))}
                </div>
              </div>
              {imagesByParagraph[para.id]?.map((img) => (
                <div key={img.id} className="mt-3 flex justify-center">
                  <div
                    className="bg-white rounded-xl border border-gray-100 overflow-hidden shadow-sm cursor-pointer hover:shadow-md transition max-w-md"
                    onClick={() => setLightboxImg(`/api/images/${img.filename}`)}
                  >
                    <img src={`/api/images/${img.filename}`} alt={`插图 (第${img.page_number}页)`}
                      className="w-full h-auto object-contain" />
                    <div className="px-3 py-1.5 text-xs text-gray-400 text-center">🖼️ 第 {img.page_number} 页</div>
                  </div>
                </div>
              ))}
            </div>
          ))}
        </div>
      </div>
    </main>
  );
}

function SentenceView({ sentence, mode, index }: { sentence: Sentence; mode: ReadingMode; index: number }) {
  const hasTranslation = !!sentence.text_zh;
  if (mode === 'de-only') return (
    <div className="flex"><span className="text-gray-300 text-xs mr-2 mt-1 w-5 text-right select-none">{index}</span><p className="text-gray-800 leading-relaxed">{sentence.text_de}</p></div>
  );
  if (mode === 'zh-only') return (
    <div className="flex"><span className="text-gray-300 text-xs mr-2 mt-1 w-5 text-right select-none">{index}</span>
      {hasTranslation ? <p className="text-gray-700 leading-relaxed">{sentence.text_zh}</p> : <p className="text-gray-400 italic">（未翻译）</p>}</div>
  );
  return (
    <div className="flex"><span className="text-gray-300 text-xs mr-2 mt-1 w-5 text-right select-none">{index}</span>
      <div className="flex-1"><p className="text-gray-800 leading-relaxed">{sentence.text_de}</p>
        {hasTranslation && <p className="text-gray-500 text-sm mt-1 leading-relaxed">{sentence.text_zh}</p>}</div></div>
  );
}
