import { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { ArrowLeft, User, Coins, KeyRound, Mail, LogOut } from 'lucide-react';
import { useStore } from '../hooks/useStore';
import { api, getStoredUser, clearAuth } from '../lib/api';
import type { CreditTransaction } from '../types';

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

export default function Profile() {
  const navigate = useNavigate();
  const { user, setUser } = useStore();
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
      navigate('/login');
      return;
    }
    setUser(stored);
    api.fetchMe()
      .then(u => {
        setUser(u);
        localStorage.setItem('steiner_user', JSON.stringify(u));
        setLoading(false);
        setTxLoading(true);
        api.fetchMyTransactions(u.id).then(data => {
          setTransactions(data.transactions || []);
        }).catch(() => {}).finally(() => setTxLoading(false));
      })
      .catch(() => {
        clearAuth();
        setUser(null);
        navigate('/login');
      });
  }, [navigate, setUser]);

  const handleLogout = () => {
    clearAuth();
    setUser(null);
    navigate('/');
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
      await api.changePassword(oldPassword, newPassword);
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
      await api.changeEmail(newEmail, emailPassword);
      setEmailSuccess('邮箱修改成功');
      const u = await api.fetchMe();
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
      const res = await api.changeUsername(newUsername, usernamePassword);
      setUsernameSuccess(res.message);
      const u = await api.fetchMe();
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
      <div className="min-h-screen pt-6 pb-16 flex items-center justify-center">
        <div className="text-gray-400 text-sm">加载中...</div>
      </div>
    );
  }

  const inputClass = "w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl text-sm text-gray-700 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent transition-all";

  return (
    <div className="min-h-screen pt-6 pb-16">
      <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link
          to="/"
          className="inline-flex items-center gap-2 text-gray-600 hover:text-[#1e3a8a] transition-colors mb-8"
        >
          <ArrowLeft className="h-4 w-4" />
          返回首页
        </Link>

        <h1 className="text-2xl font-bold text-gray-900 mb-6 font-display">个人中心</h1>

        <div className="bg-white rounded-2xl shadow-lg p-8 mb-6">
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

        <div className="bg-white rounded-2xl shadow-lg p-8 mb-6">
          <div className="flex items-center gap-2 mb-4">
            <KeyRound className="h-5 w-5 text-[#1e3a8a]" />
            <h2 className="text-lg font-semibold text-gray-800">修改密码</h2>
          </div>
          {pwError && (
            <div className="bg-red-50 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">{pwError}</div>
          )}
          {pwSuccess && (
            <div className="bg-green-50 border border-green-100 text-green-600 text-sm px-3 py-2 rounded-lg mb-4">{pwSuccess}</div>
          )}
          <form onSubmit={handleChangePassword} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">当前密码</label>
              <input type="password" value={oldPassword} onChange={e => setOldPassword(e.target.value)} placeholder="输入当前密码" required className={inputClass} />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">新密码</label>
              <input type="password" value={newPassword} onChange={e => setNewPassword(e.target.value)} placeholder="至少 6 个字符" minLength={6} required className={inputClass} />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">确认新密码</label>
              <input type="password" value={confirmPassword} onChange={e => setConfirmPassword(e.target.value)} placeholder="再次输入新密码" required className={inputClass} />
            </div>
            <button type="submit" disabled={pwLoading} className="w-full py-3 bg-[#1e3a8a] text-white rounded-xl font-medium hover:bg-[#1e3a8a]/90 transition-colors disabled:opacity-50 disabled:cursor-not-allowed">
              {pwLoading ? '修改中...' : '修改密码'}
            </button>
          </form>
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-8 mb-6">
          <div className="flex items-center gap-2 mb-4">
            <User className="h-5 w-5 text-[#1e3a8a]" />
            <h2 className="text-lg font-semibold text-gray-800">修改用户名</h2>
          </div>
          {usernameError && (
            <div className="bg-red-50 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">{usernameError}</div>
          )}
          {usernameSuccess && (
            <div className="bg-green-50 border border-green-100 text-green-600 text-sm px-3 py-2 rounded-lg mb-4">{usernameSuccess}</div>
          )}
          <form onSubmit={handleChangeUsername} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">新用户名</label>
              <input type="text" value={newUsername} onChange={e => setNewUsername(e.target.value)} placeholder="输入新用户名 (2-50字符)" required className={inputClass} />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">确认密码</label>
              <input type="password" value={usernamePassword} onChange={e => setUsernamePassword(e.target.value)} placeholder="输入当前密码以确认" required className={inputClass} />
            </div>
            <button type="submit" disabled={usernameLoading} className="w-full py-3 bg-[#1e3a8a] text-white rounded-xl font-medium hover:bg-[#1e3a8a]/90 transition-colors disabled:opacity-50 disabled:cursor-not-allowed">
              {usernameLoading ? '修改中...' : '修改用户名'}
            </button>
          </form>
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-8 mb-6">
          <div className="flex items-center gap-2 mb-4">
            <Mail className="h-5 w-5 text-[#1e3a8a]" />
            <h2 className="text-lg font-semibold text-gray-800">修改邮箱</h2>
          </div>
          {emailError && (
            <div className="bg-red-50 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">{emailError}</div>
          )}
          {emailSuccess && (
            <div className="bg-green-50 border border-green-100 text-green-600 text-sm px-3 py-2 rounded-lg mb-4">{emailSuccess}</div>
          )}
          <form onSubmit={handleChangeEmail} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">新邮箱</label>
              <input type="email" value={newEmail} onChange={e => setNewEmail(e.target.value)} placeholder="输入新邮箱地址" required className={inputClass} />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">确认密码</label>
              <input type="password" value={emailPassword} onChange={e => setEmailPassword(e.target.value)} placeholder="输入当前密码以确认" required className={inputClass} />
            </div>
            <button type="submit" disabled={emailLoading} className="w-full py-3 bg-[#1e3a8a] text-white rounded-xl font-medium hover:bg-[#1e3a8a]/90 transition-colors disabled:opacity-50 disabled:cursor-not-allowed">
              {emailLoading ? '修改中...' : '修改邮箱'}
            </button>
          </form>
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-8 mb-6">
          <div className="flex items-center gap-2 mb-4">
            <Coins className="h-5 w-5 text-[#1e3a8a]" />
            <h2 className="text-lg font-semibold text-gray-800">积分记录</h2>
          </div>
          {txLoading ? (
            <p className="text-sm text-gray-400">加载中...</p>
          ) : transactions.length === 0 ? (
            <p className="text-sm text-gray-400">暂无积分记录</p>
          ) : (
            <div className="space-y-2 max-h-80 overflow-y-auto">
              {transactions.slice(0, 50).map(tx => (
                <div key={tx.id} className="flex items-center justify-between py-2 border-b border-gray-100 text-sm">
                  <div className="flex-1 min-w-0">
                    <span className="text-gray-700">{TX_LABELS[tx.transaction_type] || tx.transaction_type}</span>
                    {tx.description && <span className="text-gray-400 text-xs ml-2 truncate">{tx.description}</span>}
                  </div>
                  <div className="flex items-center gap-3 shrink-0 ml-2">
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

        <div className="bg-white rounded-2xl shadow-lg p-8">
          <div className="flex items-center gap-2 mb-4">
            <LogOut className="h-5 w-5 text-red-500" />
            <h2 className="text-lg font-semibold text-gray-800">账户操作</h2>
          </div>
          <button
            type="button"
            onClick={handleLogout}
            className="w-full py-3 bg-red-50 border border-red-200 text-red-600 rounded-xl font-medium hover:bg-red-100 transition-colors"
          >
            退出登录
          </button>
        </div>
      </div>
    </div>
  );
}
