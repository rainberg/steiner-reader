'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { clearAuth, fetchMe, getStoredUser, User, changePassword, changeEmail, changeUsername, fetchMyTransactions, CreditTransaction } from '@/lib/api';

export default function ProfilePage() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [pwLoading, setPwLoading] = useState(false);
  const [pwError, setPwError] = useState('');
  const [pwSuccess, setPwSuccess] = useState('');

  const [newEmail, setNewEmail] = useState('');
  const [emailPassword, setEmailPassword] = useState('');
  const [emailLoading, setEmailLoading] = useState(false);
  const [emailError, setEmailError] = useState('');
  const [emailSuccess, setEmailSuccess] = useState('');

  const [newUsername, setNewUsername] = useState('');
  const [usernamePassword, setUsernamePassword] = useState('');
  const [usernameLoading, setUsernameLoading] = useState(false);
  const [usernameError, setUsernameError] = useState('');
  const [usernameSuccess, setUsernameSuccess] = useState('');

  const [transactions, setTransactions] = useState<CreditTransaction[]>([]);
  const [txLoading, setTxLoading] = useState(false);

  useEffect(() => {
    const stored = getStoredUser();
    if (!stored) {
      router.push('/login');
      return;
    }
    setUser(stored);
    fetchMe()
      .then(u => {
        setUser(u);
        localStorage.setItem('steiner_user', JSON.stringify(u));
        setLoading(false);
        // Fetch transaction history
        setTxLoading(true);
        fetchMyTransactions(u.id).then(data => {
          setTransactions(data.transactions || []);
        }).catch(() => {}).finally(() => setTxLoading(false));
      })
      .catch(() => {
        clearAuth();
        router.push('/login');
      });
  }, [router]);

  const TX_LABELS: Record<string, string> = {
    translate_lecture: '翻译章节',
    translate_book: '翻译全书',
    edit_translation: '编辑译文',
    edit_source: '编辑原文',
    download_lecture: '下载PDF',
    download_book: '下载全书PDF',
    admin_add: '管理员充值',
    admin_set: '管理员设置',
    register_bonus: '注册奖励',
  };

  const handleLogout = () => {
    clearAuth();
    router.push('/');
    router.refresh();
  };

  const handleChangePassword = async (e: React.FormEvent) => {
    e.preventDefault();
    setPwError('');
    setPwSuccess('');
    if (newPassword !== confirmPassword) {
      setPwError('两次输入的新密码不一致');
      return;
    }
    if (newPassword.length < 6) {
      setPwError('新密码至少需要 6 个字符');
      return;
    }
    setPwLoading(true);
    try {
      await changePassword(oldPassword, newPassword);
      setPwSuccess('密码修改成功');
      setOldPassword('');
      setNewPassword('');
      setConfirmPassword('');
    } catch (err: unknown) {
      setPwError(err instanceof Error ? err.message : '修改密码失败');
    } finally {
      setPwLoading(false);
    }
  };

  const handleChangeEmail = async (e: React.FormEvent) => {
    e.preventDefault();
    setEmailError('');
    setEmailSuccess('');
    setEmailLoading(true);
    try {
      await changeEmail(newEmail, emailPassword);
      setEmailSuccess('邮箱修改成功');
      const u = await fetchMe();
      setUser(u);
      localStorage.setItem('steiner_user', JSON.stringify(u));
      setNewEmail('');
      setEmailPassword('');
    } catch (err: unknown) {
      setEmailError(err instanceof Error ? err.message : '修改邮箱失败');
    } finally {
      setEmailLoading(false);
    }
  };

  const handleChangeUsername = async (e: React.FormEvent) => {
    e.preventDefault();
    setUsernameError('');
    setUsernameSuccess('');
    setUsernameLoading(true);
    try {
      const res = await changeUsername(newUsername, usernamePassword);
      setUsernameSuccess(res.message);
      const u = await fetchMe();
      setUser(u);
      localStorage.setItem('steiner_user', JSON.stringify(u));
      setNewUsername('');
      setUsernamePassword('');
    } catch (err: unknown) {
      setUsernameError(err instanceof Error ? err.message : '修改用户名失败');
    } finally {
      setUsernameLoading(false);
    }
  };

  if (loading || !user) {
    return (
      <div className="min-h-[70vh] flex items-center justify-center">
        <div className="text-gray-400 text-sm">加载中...</div>
      </div>
    );
  }

  const inputClass = "w-full px-3 py-2.5 bg-white border border-gray-200 rounded-lg text-sm text-gray-700 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-300 transition-all";

  return (
    <div className="max-w-2xl mx-auto px-4 py-8">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-xl font-bold text-gray-900">个人中心</h1>
        <Link href="/" className="text-sm text-indigo-500 hover:text-indigo-600">
          返回首页
        </Link>
      </div>

      {/* 用户信息卡片 */}
      <div className="card p-8 mb-6">
        <h2 className="text-lg font-semibold text-gray-800 mb-4">用户信息</h2>
        <div className="space-y-3">
          <div className="flex items-center justify-between py-2 border-b border-gray-100">
            <span className="text-sm text-gray-500">用户名</span>
            <span className="text-sm text-gray-800 font-medium">{user.username}</span>
          </div>
          <div className="flex items-center justify-between py-2 border-b border-gray-100">
            <span className="text-sm text-gray-500">邮箱</span>
            <span className="text-sm text-gray-800">{user.email}</span>
          </div>
          <div className="flex items-center justify-between py-2 border-b border-gray-100">
            <span className="text-sm text-gray-500">积分</span>
            <span className="text-xs bg-amber-50 text-amber-700 border border-amber-200/60 px-2 py-0.5 rounded-full">{user.credits} 点</span>
          </div>
          {user.created_at && (
            <div className="flex items-center justify-between py-2">
              <span className="text-sm text-gray-500">注册时间</span>
              <span className="text-sm text-gray-800">{new Date(user.created_at).toLocaleDateString('zh-CN')}</span>
            </div>
          )}
        </div>
      </div>

      {/* 修改密码 */}
      <div className="card p-8 mb-6">
        <h2 className="text-lg font-semibold text-gray-800 mb-4">修改密码</h2>

        {pwError && (
          <div className="bg-red-50/80 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">
            {pwError}
          </div>
        )}
        {pwSuccess && (
          <div className="bg-green-50/80 border border-green-100 text-green-600 text-sm px-3 py-2 rounded-lg mb-4">
            {pwSuccess}
          </div>
        )}

        <form onSubmit={handleChangePassword} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">当前密码</label>
            <input
              type="password"
              value={oldPassword}
              onChange={e => setOldPassword(e.target.value)}
              placeholder="输入当前密码"
              required
              className={inputClass}
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">新密码</label>
            <input
              type="password"
              value={newPassword}
              onChange={e => setNewPassword(e.target.value)}
              placeholder="至少 6 个字符"
              minLength={6}
              required
              className={inputClass}
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">确认新密码</label>
            <input
              type="password"
              value={confirmPassword}
              onChange={e => setConfirmPassword(e.target.value)}
              placeholder="再次输入新密码"
              required
              className={inputClass}
            />
          </div>
          <button type="submit" disabled={pwLoading} className="btn-primary w-full">
            {pwLoading ? '修改中...' : '修改密码'}
          </button>
        </form>
      </div>

      {/* 修改用户名 */}
      <div className="card p-8 mb-6">
        <h2 className="text-lg font-semibold text-gray-800 mb-4">修改用户名</h2>

        {usernameError && (
          <div className="bg-red-50/80 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">
            {usernameError}
          </div>
        )}
        {usernameSuccess && (
          <div className="bg-green-50/80 border border-green-100 text-green-600 text-sm px-3 py-2 rounded-lg mb-4">
            {usernameSuccess}
          </div>
        )}

        <form onSubmit={handleChangeUsername} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">新用户名</label>
            <input
              type="text"
              value={newUsername}
              onChange={e => setNewUsername(e.target.value)}
              placeholder="输入新用户名 (2-50字符)"
              required
              className={inputClass}
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">确认密码</label>
            <input
              type="password"
              value={usernamePassword}
              onChange={e => setUsernamePassword(e.target.value)}
              placeholder="输入当前密码以确认"
              required
              className={inputClass}
            />
          </div>
          <button type="submit" disabled={usernameLoading} className="btn-primary w-full">
            {usernameLoading ? '修改中...' : '修改用户名'}
          </button>
        </form>
      </div>

      {/* 修改邮箱 */}
      <div className="card p-8 mb-6">
        <h2 className="text-lg font-semibold text-gray-800 mb-4">修改邮箱</h2>

        {emailError && (
          <div className="bg-red-50/80 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">
            {emailError}
          </div>
        )}
        {emailSuccess && (
          <div className="bg-green-50/80 border border-green-100 text-green-600 text-sm px-3 py-2 rounded-lg mb-4">
            {emailSuccess}
          </div>
        )}

        <form onSubmit={handleChangeEmail} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">新邮箱</label>
            <input
              type="email"
              value={newEmail}
              onChange={e => setNewEmail(e.target.value)}
              placeholder="输入新邮箱地址"
              required
              className={inputClass}
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">确认密码</label>
            <input
              type="password"
              value={emailPassword}
              onChange={e => setEmailPassword(e.target.value)}
              placeholder="输入当前密码以确认"
              required
              className={inputClass}
            />
          </div>
          <button type="submit" disabled={emailLoading} className="btn-primary w-full">
            {emailLoading ? '修改中...' : '修改邮箱'}
          </button>
        </form>
      </div>

      {/* 积分记录 */}
      <div className="card p-8 mb-6">
        <h2 className="text-lg font-semibold text-gray-800 mb-4">积分记录</h2>
        {txLoading ? (
          <p className="text-sm text-gray-400">加载中...</p>
        ) : transactions.length === 0 ? (
          <p className="text-sm text-gray-400">暂无积分记录</p>
        ) : (
          <div className="space-y-2 max-h-80 overflow-y-auto">
            {transactions.slice(0, 50).map(tx => (
              <div key={tx.id} className="flex items-center justify-between py-2 border-b border-gray-100 text-sm">
                <div className="flex-1">
                  <span className="text-gray-700">{TX_LABELS[tx.transaction_type] || tx.transaction_type}</span>
                  {tx.description && <span className="text-gray-400 text-xs ml-2">{tx.description}</span>}
                </div>
                <div className="flex items-center gap-3 shrink-0">
                  <span className={tx.amount > 0 ? 'text-emerald-500 text-xs' : 'text-red-400 text-xs'}>
                    {tx.amount > 0 ? `+${tx.amount}` : tx.amount}
                  </span>
                  <span className="text-gray-400 text-xs w-16 text-right">{tx.balance_after}</span>
                  <span className="text-gray-300 text-xs w-24 text-right">
                    {new Date(tx.created_at).toLocaleDateString('zh-CN')}
                  </span>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* 退出登录 */}
      <div className="card p-8">
        <h2 className="text-lg font-semibold text-gray-800 mb-4">账户操作</h2>
        <button
          type="button"
          onClick={handleLogout}
          className="w-full px-4 py-2.5 bg-red-50 border border-red-200 text-red-600 rounded-lg text-sm font-medium hover:bg-red-100 transition-colors"
        >
          退出登录
        </button>
      </div>
    </div>
  );
}
