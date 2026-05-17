import { Link } from 'react-router-dom';
import { ArrowLeft, Book, Users, Upload, TrendingUp } from 'lucide-react';
import { useStore } from '../hooks/useStore';

export default function Admin() {
  const { user } = useStore();

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

  const stats = [
    { label: '书籍总数', value: '128', icon: Book, color: 'text-[#1e3a8a]', bg: 'bg-[#1e3a8a]/10' },
    { label: '用户总数', value: '1,234', icon: Users, color: 'text-[#d4a574]', bg: 'bg-[#d4a574]/10' },
    { label: '总翻译次数', value: '12,456', icon: TrendingUp, color: 'text-green-600', bg: 'bg-green-100' },
  ];

  return (
    <div className="min-h-screen pt-24 pb-16">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link
          to="/"
          className="inline-flex items-center gap-2 text-gray-600 hover:text-[#1e3a8a] transition-colors mb-8"
        >
          <ArrowLeft className="h-4 w-4" />
          返回
        </Link>

        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2 font-['Playfair_Display']">
            管理后台
          </h1>
          <p className="text-gray-600">管理书籍、用户和翻译内容</p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          {stats.map((stat, idx) => {
            const Icon = stat.icon;
            return (
              <div key={idx} className="bg-white rounded-2xl shadow-sm p-6">
                <div className={`w-12 h-12 ${stat.bg} rounded-xl flex items-center justify-center mb-4`}>
                  <Icon className={`h-6 w-6 ${stat.color}`} />
                </div>
                <div className="text-3xl font-bold text-gray-900 mb-1">{stat.value}</div>
                <div className="text-gray-600">{stat.label}</div>
              </div>
            );
          })}
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <Link
            to="/upload"
            className="flex items-center gap-4 p-6 bg-white rounded-2xl shadow-sm hover:shadow-md transition-shadow"
          >
            <div className="w-12 h-12 bg-[#1e3a8a]/10 rounded-xl flex items-center justify-center">
              <Upload className="h-6 w-6 text-[#1e3a8a]" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-gray-900">上传书籍</h3>
              <p className="text-gray-500 text-sm">添加新的书籍和内容</p>
            </div>
          </Link>
          <div className="flex items-center gap-4 p-6 bg-white rounded-2xl shadow-sm hover:shadow-md transition-shadow cursor-not-allowed opacity-50">
            <div className="w-12 h-12 bg-gray-100 rounded-xl flex items-center justify-center">
              <Users className="h-6 w-6 text-gray-500" />
            </div>
            <div>
              <h3 className="text-lg font-semibold text-gray-900">用户管理</h3>
              <p className="text-gray-500 text-sm">管理用户账户和权限</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
