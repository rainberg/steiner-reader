import { Link } from 'react-router-dom';
import { ArrowLeft, User, Coins, Settings, LogOut } from 'lucide-react';
import { useStore } from '../hooks/useStore';

export default function Profile() {
  const { user, setUser } = useStore();

  if (!user) {
    return (
      <div className="min-h-screen pt-24 pb-16 flex items-center justify-center">
        <div className="text-center">
          <p className="text-gray-500 text-lg mb-4">请先登录</p>
          <Link
            to="/login"
            className="inline-flex items-center gap-2 px-6 py-3 bg-[#1e3a8a] text-white rounded-xl hover:bg-[#1e3a8a]/90 transition-colors"
          >
            去登录
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen pt-24 pb-16">
      <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link
          to="/"
          className="inline-flex items-center gap-2 text-gray-600 hover:text-[#1e3a8a] transition-colors mb-8"
        >
          <ArrowLeft className="h-4 w-4" />
          返回
        </Link>

        <div className="bg-white rounded-2xl shadow-lg p-8">
          <div className="flex items-center gap-6 mb-8">
            <div className="w-20 h-20 bg-gradient-to-br from-[#1e3a8a] to-[#e0e7ff] rounded-full flex items-center justify-center">
              <User className="h-10 w-10 text-white" />
            </div>
            <div>
              <h1 className="text-2xl font-bold text-gray-900 font-['Playfair_Display']">
                {user.name || user.email}
              </h1>
              <p className="text-gray-600">{user.email}</p>
            </div>
          </div>

          <div className="space-y-4">
            <div className="flex items-center justify-between p-4 bg-[#f8f5f0] rounded-xl">
              <div className="flex items-center gap-3">
                <Coins className="h-5 w-5 text-[#d4a574]" />
                <span className="text-gray-700">积分余额</span>
              </div>
              <span className="text-xl font-bold text-[#1e3a8a]">{user.credits}</span>
            </div>

            <Link
              to="/recharge"
              className="flex items-center justify-between p-4 bg-white border border-gray-200 rounded-xl hover:border-[#1e3a8a] transition-colors"
            >
              <div className="flex items-center gap-3">
                <Settings className="h-5 w-5 text-gray-500" />
                <span className="text-gray-700">充值积分</span>
              </div>
              <ArrowLeft className="h-5 w-5 text-gray-400 rotate-180" />
            </Link>

            <button
              onClick={() => setUser(null)}
              className="w-full flex items-center justify-center gap-2 p-4 text-red-600 hover:bg-red-50 rounded-xl transition-colors"
            >
              <LogOut className="h-5 w-5" />
              退出登录
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
