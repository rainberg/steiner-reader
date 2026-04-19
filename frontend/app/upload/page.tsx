'use client';

import { useState, useRef } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { uploadPdf } from '@/lib/api';

export default function UploadPage() {
  const router = useRouter();
  const fileInput = useRef<HTMLInputElement>(null);
  const [uploading, setUploading] = useState(false);
  const [result, setResult] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [dragOver, setDragOver] = useState(false);

  const handleUpload = async (file: File) => {
    if (!file.name.toLowerCase().endsWith('.pdf')) {
      setError('请上传 PDF 文件');
      return;
    }

    setUploading(true);
    setError(null);
    setResult(null);

    try {
      const res = await uploadPdf(file);
      setResult(`✅ ${res.message}`);
      setTimeout(() => router.push(`/books/${res.book_id}`), 2000);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setUploading(false);
    }
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setDragOver(false);
    const file = e.dataTransfer.files[0];
    if (file) handleUpload(file);
  };

  return (
    <main className="min-h-screen bg-gray-50">
      <div className="max-w-2xl mx-auto px-4 py-8">
        <Link href="/" className="text-blue-600 hover:underline text-sm">← 返回书架</Link>

        <h1 className="text-2xl font-bold text-gray-900 mt-4 mb-2">上传 PDF</h1>
        <p className="text-gray-500 mb-8">上传施泰纳著作的文字型 PDF，系统将自动解析结构</p>

        <div
          onDragOver={(e) => { e.preventDefault(); setDragOver(true); }}
          onDragLeave={() => setDragOver(false)}
          onDrop={handleDrop}
          onClick={() => fileInput.current?.click()}
          className={`
            border-2 border-dashed rounded-2xl p-12 text-center cursor-pointer transition
            ${dragOver ? 'border-blue-500 bg-blue-50' : 'border-gray-300 hover:border-gray-400'}
          `}
        >
          <input
            ref={fileInput}
            type="file"
            accept=".pdf"
            className="hidden"
            onChange={(e) => {
              const file = e.target.files?.[0];
              if (file) handleUpload(file);
            }}
          />

          {uploading ? (
            <div>
              <div className="text-4xl mb-4">⏳</div>
              <p className="text-gray-600">正在解析 PDF...</p>
              <p className="text-sm text-gray-400 mt-2">大文件可能需要几分钟</p>
            </div>
          ) : (
            <div>
              <div className="text-4xl mb-4">📄</div>
              <p className="text-gray-600 font-medium">点击或拖拽上传 PDF</p>
              <p className="text-sm text-gray-400 mt-2">仅支持文字型 PDF（非扫描件）</p>
            </div>
          )}
        </div>

        {result && (
          <div className="mt-6 bg-green-50 border border-green-200 rounded-lg p-4 text-green-700">
            {result}
          </div>
        )}

        {error && (
          <div className="mt-6 bg-red-50 border border-red-200 rounded-lg p-4 text-red-700">
            ❌ {error}
          </div>
        )}
      </div>
    </main>
  );
}
