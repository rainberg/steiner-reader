'use client';

import { useCallback, useEffect, useRef, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import {
  fetchLecture,
  fetchParagraphs,
  getTranslationCost,
  getTranslationStatus,
  translateLecture,
  Lecture,
  Paragraph,
  Sentence,
  TranslationCost,
} from '@/lib/api';

type ReadingMode = 'de-zh' | 'de-only' | 'zh-only';

export default function LecturePage() {
  const params = useParams();
  const router = useRouter();
  const bookId = Number(params.bookId);
  const lectureId = Number(params.lectureId);

  const [lecture, setLecture] = useState<Lecture | null>(null);
  const [paragraphs, setParagraphs] = useState<Paragraph[]>([]);
  const [loading, setLoading] = useState(true);
  const [mode, setMode] = useState<ReadingMode>('de-zh');
  const [translating, setTranslating] = useState(false);
  const [translateMsg, setTranslateMsg] = useState<string | null>(null);
  const [costInfo, setCostInfo] = useState<TranslationCost | null>(null);
  const [userCredits, setUserCredits] = useState<number | null>(null);
  const [showTranslation, setShowTranslation] = useState<Set<number>>(new Set());
  const pollingRef = useRef<ReturnType<typeof setInterval> | null>(null);

  const startPolling = useCallback(() => {
    if (pollingRef.current) clearInterval(pollingRef.current);
    pollingRef.current = setInterval(async () => {
      try {
        const status = await getTranslationStatus(lectureId);
        if (status.completed) {
          if (pollingRef.current) clearInterval(pollingRef.current);
          setTranslating(false);
          setTranslateMsg(`翻译完成：${status.translated} 句`);
          await loadLecture();
        } else {
          setTranslateMsg(`翻译中：${status.translated}/${status.total} 句`);
        }
      } catch {
        // Keep polling; transient network errors should not stop the job display.
      }
    }, 3000);
  }, [lectureId]);

  const loadLecture = useCallback(async () => {
    try {
      const data = await fetchLecture(lectureId);
      setLecture(data);

      const [paras, cost] = await Promise.all([
        fetchParagraphs(lectureId),
        getTranslationCost(lectureId).catch(() => null),
      ]);
      setParagraphs(paras);

      if (cost) {
        setCostInfo(cost);
        if (cost.user_credits !== null) setUserCredits(cost.user_credits);
      }

      try {
        const status = await getTranslationStatus(lectureId);
        if (!status.completed && status.translated > 0) {
          setTranslating(true);
          startPolling();
        }
      } catch {
        // Status is auxiliary; the reader can still render without it.
      }
    } catch {
      router.push(`/books/${bookId}`);
    } finally {
      setLoading(false);
    }
  }, [bookId, lectureId, router, startPolling]);

  useEffect(() => {
    loadLecture();
    return () => {
      if (pollingRef.current) clearInterval(pollingRef.current);
    };
  }, [loadLecture]);

  const handleTranslate = async () => {
    const token = typeof window !== 'undefined' ? localStorage.getItem('steiner_token') : null;
    if (!token) {
      router.push('/login');
      return;
    }

    setTranslating(true);
    setTranslateMsg('正在启动翻译...');
    try {
      const res = await translateLecture(lectureId);
      if (res.status === 'already_translated') {
        setTranslating(false);
        setTranslateMsg('本章已经翻译完成');
        await loadLecture();
      } else {
        setTranslateMsg(`翻译中：0/${res.total} 句`);
        if (res.credits !== undefined) setUserCredits(res.credits);
        startPolling();
      }
    } catch (err: unknown) {
      setTranslating(false);
      setTranslateMsg(err instanceof Error ? err.message : '翻译失败');
    }
  };

  const toggleSentence = (id: number) => {
    setShowTranslation(prev => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin w-8 h-8 border-2 border-blue-500 border-t-transparent rounded-full" />
      </div>
    );
  }
  if (!lecture) return null;

  const token = typeof window !== 'undefined' ? localStorage.getItem('steiner_token') : null;
  const totalSentences = paragraphs.reduce((sum, p) => sum + (p.sentences?.length || 0), 0);
  const translatedSentences = paragraphs.reduce(
    (sum, p) => sum + (p.sentences || []).filter(s => s.content_zh || s.text_zh).length,
    0
  );
  const allTranslated = totalSentences > 0 && translatedSentences === totalSentences;

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50">
      <div className="sticky top-0 bg-white/90 backdrop-blur-sm border-b border-slate-200 z-10">
        <div className="max-w-4xl mx-auto px-4 py-2.5">
          <div className="flex items-center justify-between flex-wrap gap-2">
            <Link href={`/books/${bookId}`} className="text-blue-600 hover:text-blue-800 text-sm font-medium flex items-center gap-1">
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
              返回目录
            </Link>
            <div className="flex bg-slate-100 rounded-lg p-0.5">
              {(['de-zh', 'de-only', 'zh-only'] as ReadingMode[]).map(nextMode => (
                <button
                  key={nextMode}
                  type="button"
                  onClick={() => setMode(nextMode)}
                  disabled={(nextMode === 'de-zh' || nextMode === 'zh-only') && translatedSentences === 0}
                  className={`px-2.5 py-1 rounded-md text-xs font-medium transition ${
                    mode === nextMode ? 'bg-white shadow text-slate-900' : 'text-slate-500 hover:text-slate-700'
                  } ${((nextMode === 'de-zh' || nextMode === 'zh-only') && translatedSentences === 0) ? 'opacity-40 cursor-not-allowed' : ''}`}
                >
                  {nextMode === 'de-zh' ? '德中' : nextMode === 'de-only' ? '德语' : '中文'}
                </button>
              ))}
            </div>
          </div>
        </div>
      </div>

      {translateMsg && (
        <div className="max-w-4xl mx-auto px-4 mt-3">
          <div className="text-sm px-3 py-2 rounded-lg bg-amber-50 text-amber-700">
            {translateMsg}
          </div>
        </div>
      )}

      <div className="max-w-4xl mx-auto px-4 py-6">
        <div className="mb-6">
          <h1 className="text-xl font-bold text-slate-900 leading-tight">{lecture.title_de || 'Vortrag'}</h1>
          <div className="text-sm text-slate-500 mt-1.5 flex items-center gap-3 flex-wrap">
            {lecture.location && <span>{lecture.location}</span>}
            {lecture.lecture_date && <span>{lecture.lecture_date}</span>}
            <span>{paragraphs.length} 段</span>
            <span>{translatedSentences}/{totalSentences} 已译</span>
          </div>
        </div>

        {!allTranslated && !translating && (
          <div className="mb-6 bg-gradient-to-r from-blue-50 to-emerald-50 rounded-xl p-5 border border-blue-100/50 text-center">
            <p className="text-slate-600 text-sm mb-2">
              {translatedSentences === 0 ? '本章尚未翻译' : `已翻译 ${translatedSentences}/${totalSentences} 句`}
            </p>
            {token ? (
              <button onClick={handleTranslate} className="px-5 py-2 rounded-lg text-sm font-medium transition shadow-sm bg-blue-600 text-white hover:bg-blue-700">
                翻译本章（{costInfo?.cost || 10} 点，余额 {userCredits ?? 0}）
              </button>
            ) : (
              <Link href="/login" className="inline-block px-5 py-2 rounded-lg text-sm font-medium bg-slate-400 text-white hover:bg-slate-500 transition">
                登录后翻译
              </Link>
            )}
          </div>
        )}

        {translating && (
          <div className="mb-6 bg-amber-50 rounded-xl p-5 border border-amber-100 text-center animate-pulse">
            <p className="text-amber-700">翻译进行中...</p>
          </div>
        )}

        <div className="space-y-5">
          {paragraphs.map((para, pi) => (
            <div key={para.id} className="bg-white rounded-xl shadow-sm border border-slate-100 p-5">
              <div className="text-xs text-slate-300 mb-2 font-mono">§{pi + 1}</div>
              <div className="space-y-2.5">
                {(para.sentences || []).map((sent, si) => (
                  <SentenceView
                    key={sent.id}
                    sentence={sent}
                    mode={mode}
                    paragraphIndex={pi + 1}
                    index={si + 1}
                    showZh={showTranslation.has(sent.id)}
                    onToggle={() => toggleSentence(sent.id)}
                  />
                ))}
              </div>
            </div>
          ))}
        </div>

        <div className="mt-8 text-center">
          <Link href={`/books/${bookId}`} className="text-blue-600 hover:underline text-sm">
            返回目录
          </Link>
        </div>
      </div>
    </main>
  );
}

function ImageView({ url }: { url: string }) {
  const [open, setOpen] = useState(false);

  return (
    <>
      <button
        type="button"
        className="my-3 cursor-pointer rounded-lg overflow-hidden border border-slate-200 hover:border-blue-300 transition inline-block"
        onClick={() => setOpen(true)}
      >
        <img src={url} alt="" className="max-w-full h-auto max-h-64 object-contain" loading="lazy" />
      </button>
      {open && (
        <div className="fixed inset-0 bg-black/70 z-50 flex items-center justify-center p-4" onClick={() => setOpen(false)}>
          <img src={url} alt="" className="max-w-full max-h-full object-contain" />
        </div>
      )}
    </>
  );
}

function SentenceView({
  sentence,
  mode,
  paragraphIndex,
  index,
  showZh,
  onToggle,
}: {
  sentence: Sentence;
  mode: ReadingMode;
  paragraphIndex: number;
  index: number;
  showZh: boolean;
  onToggle: () => void;
}) {
  const de = sentence.content_de || sentence.text_de || '';
  const zh = sentence.content_zh || sentence.text_zh || '';
  const hasTranslation = !!zh;
  const [localShow, setLocalShow] = useState(false);
  const isZhVisible = mode === 'de-zh' || mode === 'zh-only' || showZh || localShow;

  if (mode === 'zh-only') {
    return (
      <div className="flex items-start gap-2">
        <span className="text-xs text-slate-300 font-mono shrink-0 min-w-[3rem] text-right select-none">§{paragraphIndex}.{index}</span>
        {sentence.image_url && <ImageView url={sentence.image_url} />}
        {hasTranslation ? (
          <p className="text-slate-700 leading-relaxed text-[15px]">{zh}</p>
        ) : (
          <p className="text-slate-300 italic text-sm">（未翻译）</p>
        )}
      </div>
    );
  }

  if (mode === 'de-only' && !isZhVisible) {
    return (
      <div className="flex items-start gap-2 group cursor-pointer" onClick={() => hasTranslation && setLocalShow(true)}>
        <span className="text-xs text-slate-300 font-mono shrink-0 min-w-[3rem] text-right select-none">§{paragraphIndex}.{index}</span>
        {sentence.image_url && <ImageView url={sentence.image_url} />}
        <p className="text-slate-800 leading-relaxed text-[15px] group-hover:text-blue-700 transition">{de}</p>
        {hasTranslation && <span className="shrink-0 text-[10px] text-blue-400 opacity-0 group-hover:opacity-100 transition mt-1">译</span>}
      </div>
    );
  }

  return (
    <div className="flex items-start gap-2" onDoubleClick={onToggle}>
      <span className="text-xs text-slate-300 font-mono shrink-0 min-w-[3rem] text-right select-none">§{paragraphIndex}.{index}</span>
      <div className="flex-1">
        {sentence.image_url && <ImageView url={sentence.image_url} />}
        <p className="text-slate-800 leading-relaxed text-[15px]">{de}</p>
        {hasTranslation && isZhVisible && <p className="text-slate-500 text-sm mt-1 leading-relaxed">{zh}</p>}
      </div>
    </div>
  );
}
