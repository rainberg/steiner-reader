import { useState, useRef, useCallback } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { ArrowLeft, Upload as UploadIcon, FileText, CheckCircle, AlertCircle } from 'lucide-react';
import { useStore } from '../hooks/useStore';

export default function Upload() {
  const { user } = useStore();
  const navigate = useNavigate();
  const fileInputRef = useRef<HTMLInputElement>(null);
  const [files, setFiles] = useState<File[]>([]);
  const [uploading, setUploading] = useState(false);
  const [isDragging, setIsDragging] = useState(false);
  const [result, setResult] = useState<{
    success: boolean;
    message: string;
    gaNumber?: string;
    chapters?: number;
  } | null>(null);

  if (!user || user.is_admin !== 1) {
    return (
      <div className="min-h-screen pt-24 pb-16 flex items-center justify-center">
        <div className="text-center">
          <p className="text-gray-500 text-lg mb-4">没有权限访问此页面</p>
          <Link
            to="/"
            className="inline-flex items-center gap-2 px-6 py-3 bg-[#1e3a8a] text-white rounded-xl hover:bg-[#1e3a8a]/90 transition-colors"
          >
            返回首页
          </Link>
        </div>
      </div>
    );
  }

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    const dropped = Array.from(e.dataTransfer.files).filter(
      (f) => /\.(epub|docx|pdf)$/i.test(f.name)
    );
    if (dropped.length > 0) setFiles((prev) => [...prev, ...dropped]);
  }, []);

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFiles((prev) => [...prev, ...Array.from(e.target.files!)]);
    }
  };

  const removeFile = (idx: number) => {
    setFiles((prev) => prev.filter((_, i) => i !== idx));
  };

  const handleUpload = async () => {
    if (files.length === 0) return;
    setUploading(true);
    setResult(null);

    const token = localStorage.getItem('steiner_token');
    try {
      const formData = new FormData();
      files.forEach((f) => formData.append('files', f));

      const res = await fetch('/api/books/upload', {
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
    <div className="min-h-screen pt-24 pb-16">
      <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link
          to="/admin"
          className="inline-flex items-center gap-2 text-gray-600 hover:text-[#1e3a8a] transition-colors mb-8"
        >
          <ArrowLeft className="h-4 w-4" />
          返回管理
        </Link>

        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2 font-['Playfair_Display']">
            上传书籍
          </h1>
          <p className="text-gray-600">支持 EPUB、DOCX 和 PDF 格式，文件会自动解析章节、段落和句子结构。</p>
        </div>

        <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-8">
          <div
            onDrop={handleDrop}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onClick={() => fileInputRef.current?.click()}
            className={`border-2 border-dashed rounded-2xl p-12 text-center transition-all cursor-pointer ${
              isDragging
                ? 'border-[#1e3a8a] bg-[#1e3a8a]/5'
                : 'border-gray-200 hover:border-[#1e3a8a]/30 hover:bg-[#1e3a8a]/5'
            }`}
          >
            <div className="w-16 h-16 bg-[#1e3a8a]/10 rounded-full flex items-center justify-center mx-auto mb-4">
              <UploadIcon className="h-8 w-8 text-[#1e3a8a]" />
            </div>
            <p className="text-gray-700 mb-2">
              拖拽文件到这里，或 <span className="text-[#1e3a8a] font-medium">点击选择文件</span>
            </p>
            <p className="text-gray-400 text-sm">支持 EPUB · DOCX · PDF 格式</p>
            <input
              ref={fileInputRef}
              type="file"
              accept=".epub,.docx,.pdf"
              multiple
              onChange={handleFileChange}
              className="hidden"
            />
          </div>

          {files.length > 0 && (
            <div className="mt-6">
              <h3 className="text-sm font-medium text-gray-700 mb-3">
                已选择 {files.length} 个文件
              </h3>
              <div className="space-y-2">
                {files.map((f, i) => (
                  <div key={i} className="flex items-center justify-between py-2 border-b border-gray-50 last:border-0">
                    <div className="flex items-center gap-2 min-w-0">
                      <FileText className="h-4 w-4 text-gray-400 shrink-0" />
                      <span className="text-sm text-gray-700 truncate">{f.name}</span>
                      <span className="text-xs text-gray-400">
                        {(f.size / 1024).toFixed(0)} KB
                      </span>
                    </div>
                    <button
                      onClick={() => removeFile(i)}
                      className="text-xs text-red-400 hover:text-red-600 transition-colors ml-2"
                    >
                      移除
                    </button>
                  </div>
                ))}
              </div>
              <button
                onClick={handleUpload}
                disabled={uploading}
                className="w-full mt-4 py-3 bg-[#1e3a8a] text-white rounded-xl font-medium hover:bg-[#1e3a8a]/90 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
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

          {result && (
            <div className={`mt-6 rounded-2xl p-5 ${result.success ? 'bg-green-50 border border-green-100' : 'bg-red-50 border border-red-100'}`}>
              <div className="flex items-start gap-3">
                {result.success ? (
                  <CheckCircle className="h-5 w-5 text-green-500 mt-0.5 shrink-0" />
                ) : (
                  <AlertCircle className="h-5 w-5 text-red-500 mt-0.5 shrink-0" />
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
                      onClick={() => navigate('/')}
                      className="text-xs text-[#1e3a8a] hover:text-[#1e3a8a]/80 mt-2 inline-block"
                    >
                      返回书籍列表
                    </button>
                  )}
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
