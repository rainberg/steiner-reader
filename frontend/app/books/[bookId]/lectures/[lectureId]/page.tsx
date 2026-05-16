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
  getDownloadPermission,
  editSentence,
  fetchSentenceEdits,
  fetchContributions,
  Lecture,
  Paragraph,
  Sentence,
  TranslationCost,
  DownloadPermission,
  ContributionDisplay,
  EditLogEntry,
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

  // New state: publication, download, contributions, editing
  const [isPublished, setIsPublished] = useState(false);
  const [downloadPerm, setDownloadPerm] = useState<DownloadPermission | null>(null);
  const [contributions, setContributions] = useState<ContributionDisplay[]>([]);
  const [editTransCost, setEditTransCost] = useState<number>(1);
  const [editSourceCost, setEditSourceCost] = useState<number>(1);
  const [editingSentenceId, setEditingSentenceId] = useState<number | null>(null);
  const [editField, setEditField] = useState<'text_de' | 'text_zh'>('text_zh');
  const [editValue, setEditValue] = useState('');
  const [editMsg, setEditMsg] = useState<string | null>(null);

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

      // Check publication from lecture response
      setIsPublished(data.is_published === true);

      const [paras, cost, perm, contribs] = await Promise.all([
        fetchParagraphs(lectureId),
        getTranslationCost(lectureId).catch(() => null),
        getDownloadPermission(lectureId).catch(() => null),
        fetchContributions(lectureId).catch(() => []),
      ]);
      setParagraphs(paras);
      setContributions(contribs);

      if (cost) {
        setCostInfo(cost);
        if (cost.user_credits !== null) setUserCredits(cost.user_credits);
      }
      if (perm) {
        setDownloadPerm(perm);
      }

      // Store costs from lecture response
      if (typeof data.edit_translation_cost === 'number') setEditTransCost(data.edit_translation_cost);
      if (typeof data.edit_source_cost === 'number') setEditSourceCost(data.edit_source_cost);

      try {
        const status = await getTranslationStatus(lectureId);
        if (status.is_translating && !status.completed) {
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
        setTranslateMsg(`翻译中：${res.translated}/${res.total} 句`);
        if (res.credits !== undefined) setUserCredits(res.credits);
        startPolling();
      }
    } catch (err: unknown) {
      setTranslating(false);
      setTranslateMsg(err instanceof Error ? err.message : '翻译失败');
    }
  };

  const handleDownload = () => {
    if (paragraphs.length === 0) return;

    const title = lecture?.title_de || 'Lecture';
    const titleZh = lecture?.title_zh || '';
    const loc = lecture?.location || '';
    const date = lecture?.lecture_date || '';

    let sentencesHtml = '';
    let pi = 0;
    for (const para of paragraphs) {
      pi++;
      let si = 0;
      for (const sent of (para.sentences || [])) {
        si++;
        const de = (sent.text_de || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        const zh = (sent.text_zh || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
        const zhShow = zh || '<i style="color:#94a3b8">（未翻译）</i>';
        sentencesHtml += `<div style="margin-bottom:0.8em;border-left:3px solid #e5e7eb;padding-left:1em"><div style="font-size:0.95em;line-height:1.7;color:#1e293b">${pi}.${si} ${de}</div><div style="font-size:0.9em;line-height:1.7;color:#64748b;margin-top:0.15em">${zhShow}</div></div>`;
      }
    }

    const html = `<!DOCTYPE html>
<html lang="de">
<head><meta charset="utf-8"><title>${title} — 中德双语</title>
<style>
body{font-family:"Noto Serif","Noto Serif SC",Georgia,serif;max-width:800px;margin:0 auto;padding:2em 1.5em;background:#fff;color:#1a1a1a}
h1{font-size:1.4em;color:#1e3a5f;border-bottom:2px solid #1e3a5f;padding-bottom:0.4em;margin-bottom:0.2em}
h2{font-size:1em;color:#666;font-weight:normal;margin-top:0;margin-bottom:1.5em}
.meta{font-size:0.75em;color:#94a3b8;margin-bottom:2em}
.notice{font-size:0.7em;color:#cbd5e1;text-align:center;margin-top:3em}
</style></head>
<body>
<h1>${title}</h1><h2>${titleZh}</h2>
<div class="meta">${loc}${loc&&date?' — ':''}${date} · ${(()=>{let n=0;paragraphs.forEach(p=>n+=(p.sentences||[]).length);return n})()} 句</div>
${sentencesHtml}
<div class="notice">Generated by Steiner Reader — 仅供个人学习使用</div>
</body></html>`;

    const base64 = btoa(unescape(encodeURIComponent(html)));
    const dataUrl = 'data:text/html;charset=utf-8;base64,' + base64;
    window.open(dataUrl, '_blank');
  };

  const handleEditSentence = async (sentenceId: number) => {
    if (editValue.trim() === '') {
      setEditMsg('内容不能为空');
      return;
    }
    try {
      const res = await editSentence(sentenceId, { field: editField, new_value: editValue });
      setUserCredits(res.credits_remaining);
      setEditingSentenceId(null);
      setEditMsg(null);
      await loadLecture(); // Refresh to show updated text
    } catch (err: unknown) {
      setEditMsg(err instanceof Error ? err.message : '编辑失败');
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
  const hasDownloadAccess = downloadPerm?.has_permission === true || false;
  const canEdit = isPublished && !!token;

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
                  disabled={(nextMode === 'de-zh' || nextMode === 'zh-only') && !isPublished && translatedSentences === 0}
                  className={`px-2.5 py-1 rounded-md text-xs font-medium transition ${
                    mode === nextMode ? 'bg-white shadow text-slate-900' : 'text-slate-500 hover:text-slate-700'
                  } ${((nextMode === 'de-zh' || nextMode === 'zh-only') && !isPublished && translatedSentences === 0) ? 'opacity-40 cursor-not-allowed' : ''}`}
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
            {isPublished && <span className="text-emerald-600 font-medium">译文已公开</span>}
          </div>
        </div>

        {/* Not published: show translate card */}
        {!isPublished && !translating && (
          <div className="mb-6 bg-gradient-to-r from-blue-50 to-emerald-50 rounded-xl p-5 border border-blue-100/50 text-center">
            <p className="text-slate-600 text-sm mb-2">
              {translatedSentences === 0 ? '本章译文尚未公开' : `数据库中已有 ${translatedSentences}/${totalSentences} 句译文，但尚未公开`}
            </p>
            <p className="text-slate-500 text-xs mb-3">贡献点数翻译本讲后，译文将对所有用户可见</p>
            {token ? (
              <button onClick={handleTranslate} className="px-5 py-2 rounded-lg text-sm font-medium transition shadow-sm bg-blue-600 text-white hover:bg-blue-700">
                贡献点数翻译本讲（{costInfo?.cost || 10} 点，余额 {userCredits ?? 0}）
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

        {/* Published: Download section — only for contributors */}
        {isPublished && hasDownloadAccess && (
          <div className="mb-6 bg-white rounded-xl shadow-sm border border-slate-100 p-5">
            <div className="flex items-center justify-between flex-wrap gap-3">
              <div>
                <p className="text-sm font-medium text-slate-800">下载</p>
                <p className="text-xs text-slate-500 mt-0.5">下载权限已开通，请及时下载</p>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-xs text-amber-600 bg-amber-50 px-2 py-1 rounded">请及时下载已解锁内容。本网站不保证长期运行或永久提供访问。</span>
                <a
                  href={`/api/lectures/${lectureId}/download`}
                  target="_blank"
                  rel="noopener noreferrer"
                  onClick={async (e) => {
                    e.preventDefault();
                    await handleDownload();
                  }}
                  style={{
                    display: 'inline-block',
                    padding: '8px 16px',
                    borderRadius: '8px',
                    fontSize: '14px',
                    fontWeight: 700,
                    color: '#fff',
                    backgroundColor: '#059669',
                    border: '1px solid #047857',
                    boxShadow: '0 1px 3px rgba(0,0,0,0.12)',
                    cursor: 'pointer',
                    textDecoration: 'none',
                  }}
                >
                  下载
                </a>
              </div>
            </div>
          </div>
        )}

        {/* Contributors display */}
        {contributions.length > 0 && (
          <div className="mb-6 bg-white rounded-xl shadow-sm border border-slate-100 p-4">
            <p className="text-xs text-slate-500 mb-1">贡献者</p>
            <div className="flex flex-wrap gap-2">
              {contributions.map((c, i) => (
                <span key={i} className="text-xs bg-slate-100 text-slate-700 px-2 py-0.5 rounded-full">
                  {c.username} ({c.contribution_type === 'first_translation' ? '首次翻译' : c.contribution_type === 'revision' ? '修订' : '下载'})
                </span>
              ))}
            </div>
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
                    canEdit={canEdit}
                    editingSentenceId={editingSentenceId}
                    editField={editField}
                    editValue={editValue}
                    editMsg={editMsg}
                    editTransCost={editTransCost}
                    editSourceCost={editSourceCost}
                    userCredits={userCredits}
                    onEditClick={(sid: number, field: 'text_de' | 'text_zh', currentValue: string) => {
                      setEditingSentenceId(sid);
                      setEditField(field);
                      setEditValue(currentValue);
                      setEditMsg(null);
                    }}
                    onEditCancel={() => { setEditingSentenceId(null); setEditMsg(null); }}
                    onEditSave={handleEditSentence}
                    onEditValueChange={setEditValue}
                  />
                ))}
              </div>
            </div>
          ))}
        </div>

        {/* Bottom download section — only for contributors */}
        {isPublished && hasDownloadAccess && (
          <div className="mt-8 text-center">
            <span className="text-xs text-amber-600 block mb-2">请及时下载已解锁内容。本网站不保证长期运行或永久提供访问。</span>
            <a
              href={`/api/lectures/${lectureId}/download`}
              target="_blank"
              rel="noopener noreferrer"
              onClick={async (e) => {
                e.preventDefault();
                await handleDownload();
              }}
              style={{
                display: 'inline-block',
                padding: '10px 24px',
                borderRadius: '8px',
                fontSize: '14px',
                fontWeight: 700,
                color: '#fff',
                backgroundColor: '#059669',
                border: '1px solid #047857',
                boxShadow: '0 1px 3px rgba(0,0,0,0.12)',
                cursor: 'pointer',
                textDecoration: 'none',
              }}
            >
              下载
            </a>
          </div>
        )}

        <div className="mt-6 text-center">
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
  canEdit,
  editingSentenceId,
  editField,
  editValue,
  editMsg,
  editTransCost,
  editSourceCost,
  userCredits,
  onEditClick,
  onEditCancel,
  onEditSave,
  onEditValueChange,
}: {
  sentence: Sentence;
  mode: ReadingMode;
  paragraphIndex: number;
  index: number;
  showZh: boolean;
  onToggle: () => void;
  canEdit: boolean;
  editingSentenceId: number | null;
  editField: 'text_de' | 'text_zh';
  editValue: string;
  editMsg: string | null;
  editTransCost: number;
  editSourceCost: number;
  userCredits: number | null;
  onEditClick: (sid: number, field: 'text_de' | 'text_zh', currentValue: string) => void;
  onEditCancel: () => void;
  onEditSave: (sid: number) => void;
  onEditValueChange: (val: string) => void;
}) {
  const de = sentence.content_de || sentence.text_de || '';
  const zh = sentence.content_zh || sentence.text_zh || '';
  const hasTranslation = !!zh;
  const [localShow, setLocalShow] = useState(false);
  const isZhVisible = mode === 'de-zh' || mode === 'zh-only' || showZh || localShow;
  const isEditing = editingSentenceId === sentence.id;
  const editCost = editField === 'text_zh' ? editTransCost : editSourceCost;

  if (isEditing) {
    return (
      <div className="flex items-start gap-2">
        <span className="text-xs text-slate-300 font-mono shrink-0 min-w-[3rem] text-right select-none">§{paragraphIndex}.{index}</span>
        <div className="flex-1 space-y-2">
          <div className="flex gap-2">
            <select
              value={editField}
              onChange={e => onEditClick(sentence.id, e.target.value as 'text_de' | 'text_zh', e.target.value === 'text_de' ? de : zh)}
              className="text-xs border border-slate-200 rounded px-2 py-1 bg-white"
            >
              <option value="text_zh">编辑译文</option>
              <option value="text_de">编辑原文</option>
            </select>
            <span className="text-xs text-slate-400 self-center">消耗 {editCost} 点（余额 {userCredits ?? 0}）</span>
          </div>
          <textarea
            value={editValue}
            onChange={e => onEditValueChange(e.target.value)}
            className="w-full border border-slate-200 rounded-lg p-2 text-sm text-slate-800 min-h-[60px]"
            rows={3}
          />
          {editMsg && <p className="text-xs text-red-500">{editMsg}</p>}
          <div className="flex gap-2">
            <button onClick={() => onEditSave(sentence.id)} className="px-3 py-1 text-xs rounded bg-blue-600 text-white hover:bg-blue-700">保存</button>
            <button onClick={onEditCancel} className="px-3 py-1 text-xs rounded bg-slate-100 text-slate-600 hover:bg-slate-200">取消</button>
          </div>
        </div>
      </div>
    );
  }

  if (mode === 'zh-only') {
    return (
      <div className="flex items-start gap-2 group">
        <span className="text-xs text-slate-300 font-mono shrink-0 min-w-[3rem] text-right select-none">§{paragraphIndex}.{index}</span>
        {sentence.image_url && <ImageView url={sentence.image_url} />}
        {hasTranslation ? (
          <p className="text-slate-700 leading-relaxed text-[15px] flex-1">{zh}</p>
        ) : (
          <p className="text-slate-300 italic text-sm flex-1">（未翻译）</p>
        )}
        {canEdit && hasTranslation && (
          <button
            onClick={() => onEditClick(sentence.id, 'text_zh', zh)}
            className="shrink-0 text-[10px] text-slate-300 hover:text-blue-500 opacity-0 group-hover:opacity-100 transition"
            title="编辑译文"
          >
            ✎
          </button>
        )}
      </div>
    );
  }

  if (mode === 'de-only' && !isZhVisible) {
    return (
      <div className="flex items-start gap-2 group cursor-pointer" onClick={() => hasTranslation && setLocalShow(true)}>
        <span className="text-xs text-slate-300 font-mono shrink-0 min-w-[3rem] text-right select-none">§{paragraphIndex}.{index}</span>
        {sentence.image_url && <ImageView url={sentence.image_url} />}
        <p className="text-slate-800 leading-relaxed text-[15px] group-hover:text-blue-700 transition flex-1">{de}</p>
        {hasTranslation && <span className="shrink-0 text-[10px] text-blue-400 opacity-0 group-hover:opacity-100 transition mt-1">译</span>}
        {canEdit && (
          <button
            onClick={e => { e.stopPropagation(); onEditClick(sentence.id, 'text_de', de); }}
            className="shrink-0 text-[10px] text-slate-300 hover:text-blue-500 opacity-0 group-hover:opacity-100 transition"
            title="编辑原文"
          >
            ✎
          </button>
        )}
      </div>
    );
  }

  return (
    <div className="flex items-start gap-2 group" onDoubleClick={onToggle}>
      <span className="text-xs text-slate-300 font-mono shrink-0 min-w-[3rem] text-right select-none">§{paragraphIndex}.{index}</span>
      <div className="flex-1">
        {sentence.image_url && <ImageView url={sentence.image_url} />}
        <p className="text-slate-800 leading-relaxed text-[15px]">{de}</p>
        {hasTranslation && isZhVisible && <p className="text-slate-500 text-sm mt-1 leading-relaxed">{zh}</p>}
      </div>
      {canEdit && (
        <div className="flex flex-col gap-0.5 opacity-0 group-hover:opacity-100 transition">
          <button
            onClick={() => onEditClick(sentence.id, 'text_de', de)}
            className="text-[10px] text-slate-300 hover:text-blue-500"
            title="编辑原文 ({editSourceCost}点)"
          >
            ✎ D
          </button>
          {hasTranslation && (
            <button
              onClick={() => onEditClick(sentence.id, 'text_zh', zh)}
              className="text-[10px] text-slate-300 hover:text-emerald-500"
              title="编辑译文 ({editTransCost}点)"
            >
              ✎ 中
            </button>
          )}
        </div>
      )}
    </div>
  );
}
