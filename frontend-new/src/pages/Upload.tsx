import { useState } from 'react';
import { Link } from 'react-router-dom';
import { ArrowLeft, Upload as UploadIcon, FileText } from 'lucide-react';
import { useStore } from '../hooks/useStore';

export default function Upload() {
  const { user } = useStore();
  const [file, setFile] = useState<File | null>(null);
  const [isDragging, setIsDragging] = useState(false);

  if (!user?.is_admin) {
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

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(false);
    if (e.dataTransfer.files.length > 0) {
      setFile(e.dataTransfer.files[0]);
    }
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  const handleDragLeave = () => {
    setIsDragging(false);
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
          <p className="text-gray-600">上传新的书籍文件到库中</p>
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-8">
          {!file ? (
            <div
              onDrop={handleDrop}
              onDragOver={handleDragOver}
              onDragLeave={handleDragLeave}
              className={`border-2 border-dashed rounded-2xl p-12 text-center transition-all ${
                isDragging
                  ? 'border-[#1e3a8a] bg-[#1e3a8a]/5'
                  : 'border-gray-300 hover:border-[#1e3a8a] hover:bg-[#1e3a8a]/5'
              }`}
            >
              <div className="w-16 h-16 bg-[#1e3a8a]/10 rounded-full flex items-center justify-center mx-auto mb-4">
                <UploadIcon className="h-8 w-8 text-[#1e3a8a]" />
              </div>
              <p className="text-gray-700 mb-2">拖拽文件到此处或点击上传</p>
              <p className="text-gray-500 text-sm mb-4">支持 PDF, DOC, DOCX 格式</p>
              <label className="inline-block cursor-pointer">
                <input
                  type="file"
                  accept=".pdf,.doc,.docx"
                  onChange={(e) => e.target.files?.[0] && setFile(e.target.files[0])}
                  className="hidden"
                />
                <span className="px-6 py-3 bg-[#1e3a8a] text-white rounded-xl hover:bg-[#1e3a8a]/90 transition-colors inline-block">
                  选择文件
                </span>
              </label>
            </div>
          ) : (
            <div>
              <div className="flex items-center gap-4 p-4 bg-[#f8f5f0] rounded-xl mb-6">
                <div className="w-12 h-12 bg-[#1e3a8a]/10 rounded-xl flex items-center justify-center flex-shrink-0">
                  <FileText className="h-6 w-6 text-[#1e3a8a]" />
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-gray-900 font-medium truncate">{file.name}</p>
                  <p className="text-gray-500 text-sm">{(file.size / 1024 / 1024).toFixed(2)} MB</p>
                </div>
                <button
                  onClick={() => setFile(null)}
                  className="text-gray-400 hover:text-gray-600"
                >
                  ×
                </button>
              </div>

              <div className="space-y-4 mb-6">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    书名
                  </label>
                  <input
                    type="text"
                    className="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent"
                    placeholder="输入书名"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    作者
                  </label>
                  <input
                    type="text"
                    className="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent"
                    placeholder="输入作者名"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    分类
                  </label>
                  <select className="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent">
                    <option value="">选择分类</option>
                    <option value="philosophy">哲学</option>
                    <option value="spirituality">灵性</option>
                    <option value="science">科学</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    描述
                  </label>
                  <textarea
                    rows={3}
                    className="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent"
                    placeholder="书籍简介..."
                  />
                </div>
              </div>

              <div className="flex gap-4">
                <button
                  onClick={() => setFile(null)}
                  className="flex-1 py-3 border border-gray-300 text-gray-700 rounded-xl hover:bg-gray-50 transition-colors"
                >
                  取消
                </button>
                <button className="flex-1 py-3 bg-[#1e3a8a] text-white rounded-xl hover:bg-[#1e3a8a]/90 transition-colors">
                  上传
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
