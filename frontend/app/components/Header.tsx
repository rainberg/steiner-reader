'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { clearAuth, fetchMe, getStoredUser, getUserCredits, updateStoredCredits, User } from '@/lib/api';
import SearchModal from './SearchModal';

export default function Header() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [credits, setCredits] = useState(0);
  const [pendingRecharges, setPendingRecharges] = useState(0);

  useEffect(() => {
    const stored = getStoredUser();
    if (!stored) return;
    setUser(stored);
    setCredits(getUserCredits());
    fetchMe()
      .then(nextUser => {
        setUser(nextUser);
        const total = typeof nextUser.credits === 'number' ? nextUser.credits : parseFloat(String(nextUser.credits)) || 0;
        const reserved = nextUser.credits_reserved ?? 0;
        const available = total - reserved;
        setCredits(available);
        updateStoredCredits(available);
      })
      .catch(() => {
        clearAuth();
        setUser(null);
      });

    if (stored.is_admin) {
      const poll = () => {
        const token = localStorage.getItem('access_token');
        if (!token) return;
        fetch('/api/recharge/admin/pending-requests', { headers: { Authorization: `Bearer ${token}` } })
          .then(r => r.json())
          .then(data => {
            const pending = (data || []).filter((r: {status:string}) => r.status === 'pending').length;
            setPendingRecharges(pending);
          }).catch(() => {});
      };
      poll();
      const interval = setInterval(poll, 60000);
      return () => clearInterval(interval);
    }

    const onStorage = () => {
      const u = getStoredUser();
      if (u) {
        setUser(u);
        const total = typeof u.credits === 'number' ? u.credits : parseFloat(String(u.credits)) || 0;
        const reserved = u.credits_reserved ?? 0;
        setCredits(total - reserved);
      }
    };
    const handleAuthChange = () => {
      const u = getStoredUser();
      setUser(u);
      if (u) {
        const total = typeof u.credits === 'number' ? u.credits : parseFloat(String(u.credits)) || 0;
        const reserved = u.credits_reserved ?? 0;
        setCredits(total - reserved);
      }
    };
    window.addEventListener('storage', onStorage);
    window.addEventListener('auth-changed', handleAuthChange);
    return () => {
      window.removeEventListener('storage', onStorage);
      window.removeEventListener('auth-changed', handleAuthChange);
    };
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
                <Link href="/admin" className="text-sm text-purple-600 hover:text-purple-800 transition-colors px-2 relative">
                  管理
                  {pendingRecharges > 0 && (
                    <span className="absolute -top-2 -right-1 bg-red-500 text-white text-[10px] min-w-[18px] h-[18px] flex items-center justify-center rounded-full px-1">{pendingRecharges}</span>
                  )}
                </Link>
                </>
              ) : null}
              <div className="flex items-center gap-2 pl-2 border-l border-gray-200">
                <Link href="/profile" className="text-sm text-gray-600 font-medium hover:text-indigo-600 transition-colors">
                  {user.display_name || user.username || '用户'}
                </Link>
                <span className="text-xs bg-amber-50 text-amber-700 border border-amber-200/60 px-2 py-0.5 rounded-full">
                  {credits.toFixed(0)} 点
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
