'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { login, register } from '@/lib/api';

export default function AuthPage() {
  const router = useRouter();
  const [isLogin, setIsLogin] = useState(true);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      if (isLogin) {
        await login(username, password);
      } else {
        await register(username, email, password);
      }
      router.push('/');
      router.refresh();
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      <div className="max-w-md w-full">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900">Steiner Reader</h1>
          <p className="text-gray-500 mt-1">鲁道夫·施泰纳著作阅读平台</p>
        </div>

        <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
          <div className="flex mb-6">
            <button
              onClick={() => { setIsLogin(true); setError(''); }}
              className={`flex-1 py-2 text-center text-sm font-medium rounded-l-lg transition ${isLogin ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`}
            >登录</button>
            <button
              onClick={() => { setIsLogin(false); setError(''); }}
              className={`flex-1 py-2 text-center text-sm font-medium rounded-r-lg transition ${!isLogin ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-500 hover:bg-gray-200'}`}
            >注册</button>
          </div>

          {error && (
            <div className="mb-4 text-sm text-red-600 bg-red-50 px-3 py-2 rounded-lg">{error}</div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm text-gray-600 mb-1">用户名</label>
              <input type="text" value={username} onChange={e => setUsername(e.target.value)}
                className="w-full px-3 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder="请输入用户名" required />
            </div>

            {!isLogin && (
              <div>
                <label className="block text-sm text-gray-600 mb-1">邮箱</label>
                <input type="email" value={email} onChange={e => setEmail(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                  placeholder="请输入邮箱" required />
              </div>
            )}

            <div>
              <label className="block text-sm text-gray-600 mb-1">密码</label>
              <input type="password" value={password} onChange={e => setPassword(e.target.value)}
                className="w-full px-3 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                placeholder={isLogin ? '请输入密码' : '至少6个字符'} minLength={6} required />
            </div>

            <button type="submit" disabled={loading}
              className="w-full bg-blue-600 text-white py-2.5 rounded-lg font-medium hover:bg-blue-700 transition disabled:opacity-50">
              {loading ? '处理中...' : isLogin ? '登录' : '注册'}
            </button>
          </form>

          {!isLogin && (
            <p className="mt-4 text-xs text-gray-400 text-center">注册即赠送 100 点翻译额度</p>
          )}
        </div>

        <div className="text-center mt-4">
          <Link href="/" className="text-sm text-blue-600 hover:underline">← 返回首页</Link>
        </div>
      </div>
    </main>
  );
}
