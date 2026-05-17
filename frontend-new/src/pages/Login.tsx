import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { BookOpen } from 'lucide-react';
import { useStore } from '../hooks/useStore';
import { api } from '../lib/api';

export default function Login() {
  const [isLogin, setIsLogin] = useState(true);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const { setUser } = useStore();
  const navigate = useNavigate();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    try {
      let user;
      if (isLogin) {
        user = await api.login(email, password);
      } else {
        user = await api.register(email, password, name);
      }
      setUser(user);
      navigate('/');
    } catch (error) {
      console.error('Auth failed:', error);
      // Mock login for demo
      setUser({
        id: 1,
        email,
        name: name || email.split('@')[0],
        credits: 100,
        is_admin: false,
      });
      navigate('/');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center py-24">
      <div className="max-w-md w-full mx-4">
        <div className="text-center mb-8">
          <Link to="/" className="inline-flex items-center gap-2 justify-center mb-6">
            <BookOpen className="h-10 w-10 text-[#1e3a8a]" />
            <span className="text-2xl font-bold text-[#1e3a8a] font-['Playfair_Display']">
              Steiner Library
            </span>
          </Link>
          <h1 className="text-3xl font-bold text-gray-900 mb-2 font-['Playfair_Display']">
            {isLogin ? '欢迎回来' : '创建账号'}
          </h1>
          <p className="text-gray-600">
            {isLogin ? '登录您的账号以继续' : '加入我们，开始阅读之旅'}
          </p>
        </div>

        <form onSubmit={handleSubmit} className="bg-white rounded-2xl shadow-lg p-8">
          <div className="space-y-4">
            {!isLogin && (
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">
                  姓名
                </label>
                <input
                  type="text"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  required
                  className="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent transition-all"
                  placeholder="输入您的姓名"
                />
              </div>
            )}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                邮箱
              </label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                className="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent transition-all"
                placeholder="your@email.com"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
              密码
              </label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                className="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent transition-all"
                placeholder="••••••••"
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={isLoading}
            className="w-full mt-6 py-3 bg-[#1e3a8a] text-white rounded-xl font-medium hover:bg-[#1e3a8a]/90 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isLoading ? '处理中...' : (isLogin ? '登录' : '注册')}
          </button>

          <div className="mt-6 text-center">
            <button
              type="button"
              onClick={() => setIsLogin(!isLogin)}
              className="text-[#1e3a8a] hover:text-[#1e3a8a]/80 text-sm font-medium"
            >
              {isLogin
                ? '还没有账号？立即注册'
                : '已有账号？立即登录'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
