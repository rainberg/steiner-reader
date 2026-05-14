'use client';

import { useState, useRef, useCallback } from 'react';
import { useRouter } from 'next/navigation';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || '';

export default function UploadPage() {
  const router = useRouter();
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [files, setFiles] = useState<File[]>([]);
  const [uploading, setUploading] = useState(false);
  const [result, setResult] = useState<{
    success: boolean;
    message: string;
    gaNumber?: string;
    chapters?: number;
  } | null>(null);

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    const dropped = Array.from(e.dataTransfer.files).filter(
      f => f.name.endsWith('.epub') || f.name.endsWith('.docx')
    );
    if (dropped.length > 0) setFiles(prev => [...prev, ...dropped]);
  }, []);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFiles(prev => [...prev, ...Array.from(e.target.files!)]);
    }
  };

  const removeFile = (idx: number) => {
    setFiles(prev => prev.filter((_, i) => i !== idx));
  };

  const handleUpload = async () => {
    if (files.length === 0) return;
    setUploading(true);
    setResult(null);

    const token = localStorage.getItem('steiner_token');
    try {
      const formData = new FormData();
      files.forEach(f => formData.append('files', f));

      const res = await fetch(`${API_BASE}/api/books/upload`, {
        method: 'POST',
        headers: token ? { Authorization: `Bearer ${token}` } : {},
        body: formData,
      });

      if (!res.ok) {
        const err = await res.json().catch(() => ({ detail: '上传失败' }));
        throw new Error(err.detail || '上传失败');
      }

      const data = await res.json();
      setResult({
        success: true,
        message: data.message || `成功上传 ${files.length} 本书`,
        gaNumber: data.ga_number,
        chapters: data.chapters,
      });
      setFiles([]);
    } catch (err: unknown) {
      setResult({
        success: false,
        message: err instanceof Error ? err.message : '上传失败',
      });
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="page-container py-8">
      {/* Back link */}
      <button
        onClick={() => router.push('/')}
        className="inline-flex items-center gap-1 text-sm text-gray-400 hover:text-indigo-500 transition-colors mb-6"
      >
        <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
        </svg>
        返回
      </button>

      <h1 className="text-2xl font-bold text-gray-900 mb-1">上传著作</h1>
      <p className="text-sm text-gray-500 mb-8">
        支持 EPUB 和 DOCX 格式。文件会自动解析章节、段落和句子结构。
      </p>

      {/* Drop zone */}
      <div
        onDragOver={e => e.preventDefault()}
        onDrop={handleDrop}
        onClick={() => fileInputRef.current?.click()}
        className="border-2 border-dashed border-gray-200 rounded-xl p-12 text-center
                   hover:border-indigo-300 hover:bg-indigo-50/20 transition-all cursor-pointer mb-6"
      >
        <svg className="w-10 h-10 mx-auto text-gray-300 mb-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
        </svg>
        <p className="text-sm text-gray-500">
          拖拽文件到这里，或 <span className="text-indigo-500 font-medium">点击选择文件</span>
        </p>
        <p className="text-xs text-gray-400 mt-1">支持 EPUB、DOCX 格式</p>
        <input
          ref={fileInputRef}
          type="file"
          accept=".epub,.docx"
          multiple
          onChange={handleFileChange}
          className="hidden"
        />
      </div>

      {/* File list */}
      {files.length > 0 && (
        <div className="card p-4 mb-6">
          <h3 className="text-sm font-medium text-gray-700 mb-3">
            已选择 {files.length} 个文件
          </h3>
          <div className="space-y-2">
            {files.map((f, i) => (
              <div key={i} className="flex items-center justify-between py-2 border-b border-gray-50 last:border-0">
                <div className="flex items-center gap-2 min-w-0">
                  <svg className="w-4 h-4 text-gray-400 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  <span className="text-sm text-gray-700 truncate">{f.name}</span>
                  <span className="text-xs text-gray-400">
                    {(f.size / 1024).toFixed(0)} KB
                  </span>
                </div>
                <button
                  onClick={() => removeFile(i)}
                  className="text-xs text-red-400 hover:text-red-600 transition-colors"
                >
                  移除
                </button>
              </div>
            ))}
          </div>
          <button
            onClick={handleUpload}
            disabled={uploading}
            className="btn-primary mt-4 w-full"
          >
            {uploading ? (
              <span className="flex items-center justify-center gap-2">
                <div className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                上传解析中…
              </span>
            ) : (
              `上传 ${files.length} 个文件`
            )}
          </button>
        </div>
      )}

      {/* Result */}
      {result && (
        <div className={`card p-5 ${result.success ? 'border-green-100 bg-green-50/30' : 'border-red-100 bg-red-50/30'}`}>
          <div className="flex items-start gap-3">
            {result.success ? (
              <svg className="w-5 h-5 text-green-500 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            ) : (
              <svg className="w-5 h-5 text-red-500 mt-0.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            )}
            <div>
              <p className={`text-sm font-medium ${result.success ? 'text-green-700' : 'text-red-700'}`}>
                {result.success ? '上传成功' : '上传失败'}
              </p>
              <p className="text-sm text-gray-500 mt-1">{result.message}</p>
              {result.gaNumber && (
                <p className="text-xs text-gray-400 mt-0.5">
                  {result.gaNumber} · {result.chapters} 章节
                </p>
              )}
              {result.success && (
                <button
                  onClick={() => router.push('/')}
                  className="text-xs text-indigo-500 hover:text-indigo-600 mt-2 inline-block"
                >
                  返回书籍列表
                </button>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
