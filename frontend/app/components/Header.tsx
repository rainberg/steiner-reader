'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { clearAuth, fetchMe, getStoredUser, User } from '@/lib/api';
import SearchModal from './SearchModal';

export default function Header() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const stored = getStoredUser();
    if (stored) {
      setUser(stored);
      fetchMe()
        .then(nextUser => {
          setUser(nextUser);
          localStorage.setItem('steiner_user', JSON.stringify(nextUser));
        })
        .catch(() => {
          clearAuth();
          setUser(null);
        });
    }

    const handleAuthChange = () => {
      const u = getStoredUser();
      setUser(u);
    };
    window.addEventListener('auth-changed', handleAuthChange);
    return () => window.removeEventListener('auth-changed', handleAuthChange);
  }, []);

  const handleLogout = () => {
    clearAuth();
    setUser(null);
    router.refresh();
  };

  return (
    <header className="sticky top-0 z-40 bg-white/90 backdrop-blur-md border-b border-gray-100/80">
      <div className="page-container flex items-center justify-between h-14">
        <Link href="/" className="flex items-center gap-2 group">
          <span className="text-xl font-bold text-gray-900 group-hover:text-indigo-600 transition-colors">
            Steiner Reader
          </span>
          <span className="hidden sm:inline text-xs text-gray-400 mt-1">施泰纳著作</span>
        </Link>

        <div className="flex items-center gap-3">
          {user ? (
            <>
              <SearchModal />
              <Link href="/recharge" className="text-sm text-gray-500 hover:text-indigo-600 transition-colors px-2">
                充值
              </Link>
              {user.is_admin ? (
                <>
                <Link href="/upload" className="text-sm text-gray-500 hover:text-indigo-600 transition-colors px-2">
                  上传
                </Link>
                <Link href="/admin" className="text-sm text-purple-600 hover:text-purple-800 transition-colors px-2">
                  管理
                </Link>
                </>
              ) : null}
              <div className="flex items-center gap-2 pl-2 border-l border-gray-200">
                <Link href="/profile" className="text-sm text-gray-600 font-medium hover:text-indigo-600 transition-colors">
                  {user.username}
                </Link>
                <span className="text-xs bg-amber-50 text-amber-700 border border-amber-200/60 px-2 py-0.5 rounded-full">
                  {user.credits} 点
                </span>
                <Link href="/profile" className="text-xs text-gray-400 hover:text-indigo-500 transition-colors ml-1">
                  个人中心
                </Link>
                <button
                  type="button"
                  onClick={handleLogout}
                  className="text-xs text-gray-400 hover:text-gray-600 transition-colors ml-1"
                >
                  退出
                </button>
              </div>
            </>
          ) : (
            <Link href="/login" className="btn-primary text-sm !px-4 !py-1.5">
              登录
            </Link>
          )}
        </div>
      </div>
    </header>
  );
}
