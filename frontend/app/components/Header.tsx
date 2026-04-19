'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { useRouter } from 'next/navigation';

interface User {
  id: number;
  username: string;
  email: string;
  credits: number;
}

function getStoredUser(): User | null {
  if (typeof window === 'undefined') return null;
  const u = localStorage.getItem('steiner_user');
  return u ? JSON.parse(u) : null;
}

function clearAuth() {
  localStorage.removeItem('steiner_token');
  localStorage.removeItem('steiner_user');
}

async function fetchMe(): Promise<User> {
  const token = localStorage.getItem('steiner_token');
  const res = await fetch('/api/auth/me', {
    headers: token ? { Authorization: `Bearer ${token}` } : {},
  });
  if (!res.ok) throw new Error('未登录');
  return res.json();
}

export default function Header() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    const stored = getStoredUser();
    if (stored) {
      setUser(stored);
      fetchMe().then(u => {
        setUser(u);
        localStorage.setItem('steiner_user', JSON.stringify(u));
      }).catch(() => {
        clearAuth();
        setUser(null);
      });
    }
  }, []);

  const handleLogout = () => {
    clearAuth();
    setUser(null);
    router.refresh();
  };

  return (
    <div className="bg-white border-b border-gray-100">
      <div className="max-w-4xl mx-auto px-4 py-2 flex items-center justify-between">
        <Link href="/" className="text-lg font-bold text-gray-900 hover:text-blue-600 transition">
          Steiner Reader
        </Link>
        {user ? (
          <div className="flex items-center gap-4">
            <div className="text-sm text-gray-500">
              <span className="text-gray-700 font-medium">{user.username}</span>
              <span className="ml-2 bg-yellow-50 text-yellow-700 px-2 py-0.5 rounded-full text-xs font-medium">
                {user.credits} 点
              </span>
            </div>
            <button onClick={handleLogout} className="text-sm text-gray-400 hover:text-gray-600 transition">退出</button>
          </div>
        ) : (
          <Link href="/login" className="text-sm bg-blue-600 text-white px-4 py-1.5 rounded-lg hover:bg-blue-700 transition">登录</Link>
        )}
      </div>
    </div>
  );
}

