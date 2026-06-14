'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import {
  clearAuth, fetchMe, getStoredUser, User,
  changePassword, changeEmail, changeUsername,
  fetchMyTransactions, CreditTransaction,
  bindPhone, bindEmail, unbindPhone, unbindEmail, deleteAccount,
  generateInviteCode, getMyInviteCodes, InviteCodeItem,
} from '@/lib/api';
import { SmsCodeInput, EmailCodeInput } from '@/app/components/SmsVerification';

type TabKey = 'info' | 'security' | 'binding' | 'credits' | 'invite' | 'account';

const TABS: { key: TabKey; label: string }[] = [
  { key: 'info', label: '个人信息' },
  { key: 'security', label: '安全设置' },
  { key: 'binding', label: '绑定管理' },
  { key: 'credits', label: '积分记录' },
  { key: 'account', label: '账户' },
];

export default function ProfilePage() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState<TabKey>('info');

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

  const [bindPhoneNum, setBindPhoneNum] = useState('');
  const [bindPhoneCode, setBindPhoneCode] = useState('');
  const [bindPhoneLoading, setBindPhoneLoading] = useState(false);
  const [bindPhoneError, setBindPhoneError] = useState('');
  const [bindPhoneSuccess, setBindPhoneSuccess] = useState('');

  const [bindEmailAddr, setBindEmailAddr] = useState('');
  const [bindEmailCode, setBindEmailCode] = useState('');
  const [bindEmailLoading, setBindEmailLoading] = useState(false);
  const [bindEmailError, setBindEmailError] = useState('');
  const [bindEmailSuccess, setBindEmailSuccess] = useState('');

  const [unbindLoading, setUnbindLoading] = useState(false);
  const [unbindError, setUnbindError] = useState('');

  const [deletePw, setDeletePw] = useState('');
  const [deleteEmailCode, setDeleteEmailCode] = useState('');
  const [deleteLoading, setDeleteLoading] = useState(false);
  const [deleteError, setDeleteError] = useState('');
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);

  const [transactions, setTransactions] = useState<CreditTransaction[]>([]);
  const [txLoading, setTxLoading] = useState(false);

  const refreshUser = async () => {
    const u = await fetchMe();
    setUser(u);
    localStorage.setItem('auth_user', JSON.stringify(u));
  };

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
        localStorage.setItem('auth_user', JSON.stringify(u));
        setLoading(false);
        setTxLoading(true);
        fetchMyTransactions().then(data => {
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
    setPwError(''); setPwSuccess('');
    if (newPassword !== confirmPassword) { setPwError('两次输入的新密码不一致'); return; }
    if (newPassword.length < 6) { setPwError('新密码至少需要 6 个字符'); return; }
    setPwLoading(true);
    try {
      await changePassword(oldPassword, newPassword);
      setPwSuccess('密码修改成功');
      setOldPassword(''); setNewPassword(''); setConfirmPassword('');
    } catch (err: unknown) { setPwError(err instanceof Error ? err.message : '修改密码失败'); }
    finally { setPwLoading(false); }
  };

  const handleChangeEmail = async (e: React.FormEvent) => {
    e.preventDefault();
    setEmailError(''); setEmailSuccess('');
    setEmailLoading(true);
    try {
      await changeEmail(newEmail, emailPassword);
      setEmailSuccess('邮箱修改成功');
      await refreshUser();
      setNewEmail(''); setEmailPassword('');
    } catch (err: unknown) { setEmailError(err instanceof Error ? err.message : '修改邮箱失败'); }
    finally { setEmailLoading(false); }
  };

  const handleChangeUsername = async (e: React.FormEvent) => {
    e.preventDefault();
    setUsernameError(''); setUsernameSuccess('');
    setUsernameLoading(true);
    try {
      await changeUsername(newUsername, usernamePassword);
      setUsernameSuccess('用户名修改成功');
      await refreshUser();
      setNewUsername(''); setUsernamePassword('');
    } catch (err: unknown) { setUsernameError(err instanceof Error ? err.message : '修改用户名失败'); }
    finally { setUsernameLoading(false); }
  };

  const handleBindPhone = async (e: React.FormEvent) => {
    e.preventDefault();
    setBindPhoneError(''); setBindPhoneSuccess('');
    if (!bindPhoneNum || !bindPhoneCode) {
      setBindPhoneError('请输入手机号和验证码');
      return;
    }
    setBindPhoneLoading(true);
    try {
      await bindPhone(bindPhoneNum, bindPhoneCode);
      setBindPhoneSuccess('手机号绑定成功');
      await refreshUser();
      setBindPhoneNum(''); setBindPhoneCode('');
    } catch (err: unknown) { setBindPhoneError(err instanceof Error ? err.message : '绑定失败'); }
    finally { setBindPhoneLoading(false); }
  };

  const handleBindEmail = async (e: React.FormEvent) => {
    e.preventDefault();
    setBindEmailError(''); setBindEmailSuccess('');
    if (!bindEmailAddr || !bindEmailCode) {
      setBindEmailError('请输入邮箱和验证码');
      return;
    }
    setBindEmailLoading(true);
    try {
      await bindEmail(bindEmailAddr, bindEmailCode);
      setBindEmailSuccess('邮箱绑定成功');
      await refreshUser();
      setBindEmailAddr(''); setBindEmailCode('');
    } catch (err: unknown) { setBindEmailError(err instanceof Error ? err.message : '绑定失败'); }
    finally { setBindEmailLoading(false); }
  };

  const handleUnbindPhone = async () => {
    setUnbindError(''); setUnbindLoading(true);
    try {
      await unbindPhone();
      await refreshUser();
    } catch (err: unknown) { setUnbindError(err instanceof Error ? err.message : '解绑失败'); }
    finally { setUnbindLoading(false); }
  };

  const handleUnbindEmail = async () => {
    setUnbindError(''); setUnbindLoading(true);
    try {
      await unbindEmail();
      await refreshUser();
    } catch (err: unknown) { setUnbindError(err instanceof Error ? err.message : '解绑失败'); }
    finally { setUnbindLoading(false); }
  };

  const handleDeleteAccount = async () => {
    setDeleteError(''); setDeleteLoading(true);
    try {
      const params: { password?: string; email_code?: string } = {};
      if (deletePw) params.password = deletePw;
      if (deleteEmailCode && user?.email) params.email_code = deleteEmailCode;
      await deleteAccount(params);
      clearAuth();
      router.push('/');
    } catch (err: unknown) { setDeleteError(err instanceof Error ? err.message : '注销失败'); }
    finally { setDeleteLoading(false); }
  };

  if (loading || !user) {
    return (
      <div className="min-h-[70vh] flex items-center justify-center">
        <div className="text-gray-400 text-sm">加载中...</div>
      </div>
    );
  }

  const inputClass = "w-full px-3 py-2.5 bg-white border border-gray-200 rounded-lg text-sm text-gray-700 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-300 transition-all";
  const hasPhone = !!user.phone;
  const hasEmail = !!user.email;

  return (
    <div className="max-w-2xl mx-auto px-4 py-8">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-xl font-bold text-gray-900">个人中心</h1>
        <Link href="/" className="text-sm text-indigo-500 hover:text-indigo-600">返回首页</Link>
      </div>

      <div className="flex gap-1 border-b border-gray-200 mb-6">
        {TABS.map(t => (
          <button key={t.key} type="button" onClick={() => setActiveTab(t.key)}
            className={`px-4 py-2.5 text-sm font-medium rounded-t-lg transition ${
              activeTab === t.key
                ? 'bg-white text-indigo-600 border border-b-white border-gray-200 -mb-px'
                : 'text-gray-500 hover:text-gray-700'
            }`}
          >{t.label}</button>
        ))}
      </div>

      {activeTab === 'info' && (
        <div className="space-y-6">
          <div className="card p-6">
            <h2 className="text-base font-semibold text-gray-800 mb-4">基本信息</h2>
            <div className="space-y-3">
              <div className="flex items-center justify-between py-2 border-b border-gray-100">
                <span className="text-sm text-gray-500">用户名</span>
                <span className="text-sm text-gray-800 font-medium">{user.display_name}</span>
              </div>
              <div className="flex items-center justify-between py-2 border-b border-gray-100">
                <span className="text-sm text-gray-500">邮箱</span>
                {hasEmail ? (
                  <span className="text-sm text-gray-800">{user.email}</span>
                ) : (
                  <span className="text-xs text-gray-400 bg-gray-50 px-2 py-0.5 rounded">未绑定</span>
                )}
              </div>
              <div className="flex items-center justify-between py-2 border-b border-gray-100">
                <span className="text-sm text-gray-500">手机号</span>
                {hasPhone ? (
                  <span className="text-sm text-gray-800">{user.phone}</span>
                ) : (
                  <span className="text-xs text-gray-400 bg-gray-50 px-2 py-0.5 rounded">未绑定</span>
                )}
              </div>
              <div className="flex items-center justify-between py-2 border-b border-gray-100">
                <span className="text-sm text-gray-500">积分</span>
                <span className="text-xs bg-amber-50 text-amber-700 border border-amber-200/60 px-2 py-0.5 rounded-full">
                  {(user.credits - (user.credits_reserved ?? 0)).toFixed(0)} 点
                  {(user.credits_reserved ?? 0) > 0 ? ` (冻结 ${user.credits_reserved?.toFixed(0) ?? 0})` : ''}
                </span>
              </div>
              {user.created_at && (
                <div className="flex items-center justify-between py-2">
                  <span className="text-sm text-gray-500">注册时间</span>
                  <span className="text-sm text-gray-800">{new Date(user.created_at).toLocaleDateString('zh-CN')}</span>
                </div>
              )}
            </div>
          </div>

          <div className="card p-6">
            <h2 className="text-base font-semibold text-gray-800 mb-4">修改用户名</h2>
            {usernameError && <div className="bg-red-50/80 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">{usernameError}</div>}
            {usernameSuccess && <div className="bg-green-50/80 border border-green-100 text-green-600 text-sm px-3 py-2 rounded-lg mb-4">{usernameSuccess}</div>}
            <form onSubmit={handleChangeUsername} className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-600 mb-1">新用户名</label>
                <input type="text" value={newUsername} onChange={e => setNewUsername(e.target.value)} placeholder="输入新用户名 (2-50字符)" required className={inputClass} />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-600 mb-1">确认密码</label>
                <input type="password" value={usernamePassword} onChange={e => setUsernamePassword(e.target.value)} placeholder="输入当前密码以确认" required className={inputClass} />
              </div>
              <button type="submit" disabled={usernameLoading} className="btn-primary w-full">{usernameLoading ? '修改中...' : '修改用户名'}</button>
            </form>
          </div>
        </div>
      )}

      {activeTab === 'security' && (
        <div className="card p-6">
          <h2 className="text-base font-semibold text-gray-800 mb-4">修改密码</h2>
          {pwError && <div className="bg-red-50/80 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">{pwError}</div>}
          {pwSuccess && <div className="bg-green-50/80 border border-green-100 text-green-600 text-sm px-3 py-2 rounded-lg mb-4">{pwSuccess}</div>}
          <form onSubmit={handleChangePassword} className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-600 mb-1">当前密码</label>
              <input type="password" value={oldPassword} onChange={e => setOldPassword(e.target.value)} placeholder="输入当前密码" required className={inputClass} />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-600 mb-1">新密码</label>
              <input type="password" value={newPassword} onChange={e => setNewPassword(e.target.value)} placeholder="至少 6 个字符" minLength={6} required className={inputClass} />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-600 mb-1">确认新密码</label>
              <input type="password" value={confirmPassword} onChange={e => setConfirmPassword(e.target.value)} placeholder="再次输入新密码" required className={inputClass} />
            </div>
            <button type="submit" disabled={pwLoading} className="btn-primary w-full">{pwLoading ? '修改中...' : '修改密码'}</button>
          </form>
        </div>
      )}

      {activeTab === 'binding' && (
        <div className="card p-6">
          <h2 className="text-base font-semibold text-gray-800 mb-4">绑定管理</h2>
          <p className="text-xs text-gray-400 mb-4">同一账号可同时绑定手机号和邮箱，支持两种方式登录。解绑后手机号/邮箱可绑定到其他账号。</p>

          <div className="space-y-4">
            <div className="flex items-center justify-between py-3 border-b border-gray-100">
              <div>
                <span className="text-sm font-medium text-gray-700">手机号</span>
                {hasPhone ? (
                  <span className="text-sm text-gray-500 ml-2">{user.phone}</span>
                ) : (
                  <span className="text-xs text-gray-400 ml-2">未绑定</span>
                )}
              </div>
              {hasPhone ? (
                <span className="text-xs text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded">已绑定</span>
              ) : (
                <span className="text-xs text-gray-400 bg-gray-50 px-2 py-0.5 rounded">未绑定</span>
              )}
            </div>

            {!hasPhone && (
              <div className="bg-gray-50/50 rounded-lg p-4">
                <h3 className="text-sm font-medium text-gray-700 mb-3">绑定手机号</h3>
                {bindPhoneError && <div className="bg-red-50/80 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-3">{bindPhoneError}</div>}
                {bindPhoneSuccess && <div className="bg-green-50/80 border border-green-100 text-green-600 text-sm px-3 py-2 rounded-lg mb-3">{bindPhoneSuccess}</div>}
                <form onSubmit={handleBindPhone} className="space-y-3">
                  <SmsCodeInput
                    phoneValue={bindPhoneNum}
                    onPhoneChange={setBindPhoneNum}
                    codeValue={bindPhoneCode}
                    onCodeChange={setBindPhoneCode}
                    compact
                  />
                  <button type="submit" disabled={bindPhoneLoading} className="btn-primary w-full text-sm">{bindPhoneLoading ? '绑定中...' : '绑定手机号'}</button>
                </form>
              </div>
            )}

            <div className="flex items-center justify-between py-3 border-b border-gray-100">
              <div>
                <span className="text-sm font-medium text-gray-700">邮箱</span>
                {hasEmail ? (
                  <span className="text-sm text-gray-500 ml-2">{user.email}</span>
                ) : (
                  <span className="text-xs text-gray-400 ml-2">未绑定</span>
                )}
              </div>
              {hasEmail ? (
                <span className="text-xs text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded">已绑定</span>
              ) : (
                <span className="text-xs text-gray-400 bg-gray-50 px-2 py-0.5 rounded">未绑定</span>
              )}
            </div>

            {!hasEmail && (
              <div className="bg-gray-50/50 rounded-lg p-4">
                <h3 className="text-sm font-medium text-gray-700 mb-3">绑定邮箱</h3>
                {bindEmailError && <div className="bg-red-50/80 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-3">{bindEmailError}</div>}
                {bindEmailSuccess && <div className="bg-green-50/80 border border-green-100 text-green-600 text-sm px-3 py-2 rounded-lg mb-3">{bindEmailSuccess}</div>}
                <form onSubmit={handleBindEmail} className="space-y-3">
                  <EmailCodeInput
                    emailValue={bindEmailAddr}
                    onEmailChange={setBindEmailAddr}
                    codeValue={bindEmailCode}
                    onCodeChange={setBindEmailCode}
                    compact
                  />
                  <button type="submit" disabled={bindEmailLoading} className="btn-primary w-full text-sm">{bindEmailLoading ? '绑定中...' : '绑定邮箱'}</button>
                </form>
              </div>
            )}

            {(hasPhone || hasEmail) && (
              <div className="bg-gray-50/50 rounded-lg p-4 mt-4">
                <h3 className="text-sm font-medium text-gray-700 mb-3">解绑</h3>
                {unbindError && <div className="bg-red-50/80 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-3">{unbindError}</div>}
                <p className="text-xs text-gray-400 mb-3">解绑后，该手机号/邮箱可绑定到其他账号。至少保留一种登录方式。</p>
                <div className="flex gap-3">
                  {hasPhone && (
                    <button type="button" onClick={handleUnbindPhone} disabled={unbindLoading}
                      className="flex-1 px-3 py-2 bg-orange-50 border border-orange-200 text-orange-600 rounded-lg text-sm font-medium hover:bg-orange-100 transition-colors disabled:opacity-50">
                      {unbindLoading ? '解绑中...' : '解绑手机号'}
                    </button>
                  )}
                  {hasEmail && (
                    <button type="button" onClick={handleUnbindEmail} disabled={unbindLoading}
                      className="flex-1 px-3 py-2 bg-orange-50 border border-orange-200 text-orange-600 rounded-lg text-sm font-medium hover:bg-orange-100 transition-colors disabled:opacity-50">
                      {unbindLoading ? '解绑中...' : '解绑邮箱'}
                    </button>
                  )}
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {activeTab === 'credits' && (
        <div className="card p-6">
          <h2 className="text-base font-semibold text-gray-800 mb-4">积分记录</h2>
          <div className="flex items-center gap-3 mb-4 pb-3 border-b border-gray-100">
            <span className="text-sm text-gray-500">当前积分</span>
            <span className="text-sm font-semibold text-amber-700">{(user.credits - (user.credits_reserved ?? 0)).toFixed(0)} 点</span>
            {(user.credits_reserved ?? 0) > 0 && (
              <span className="text-xs text-gray-400">冻结 {user.credits_reserved?.toFixed(0)} 点</span>
            )}
          </div>
          {txLoading ? (
            <p className="text-sm text-gray-400">加载中...</p>
          ) : transactions.length === 0 ? (
            <p className="text-sm text-gray-400">暂无积分记录</p>
          ) : (
            <div className="space-y-0">
              <div className="flex items-center justify-between py-2 text-xs text-gray-400 border-b border-gray-100">
                <span className="flex-1">类型</span>
                <span className="w-14 text-right">变动</span>
                <span className="w-16 text-right">余额</span>
                <span className="w-24 text-right">时间</span>
              </div>
              {transactions.slice(0, 50).map(tx => (
                <div key={tx.id} className="flex items-center justify-between py-2.5 border-b border-gray-50 text-sm">
                  <div className="flex-1">
                    <span className="text-gray-700">{TX_LABELS[tx.transaction_type] || tx.transaction_type}</span>
                    {tx.description && <span className="text-gray-400 text-xs ml-2">{tx.description}</span>}
                  </div>
                  <div className="flex items-center gap-3 shrink-0">
                    <span className={`w-14 text-right text-xs font-medium ${tx.amount > 0 ? 'text-emerald-600' : 'text-red-500'}`}>
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
      )}

      {activeTab === 'invite' && (
        <InviteTab />
      )}

      {activeTab === 'account' && (
        <div className="space-y-6">
          <div className="card p-6">
            <h2 className="text-base font-semibold text-gray-800 mb-4">退出登录</h2>
            <p className="text-sm text-gray-500 mb-4">退出登录后将清除本地登录状态。</p>
            <button type="button" onClick={handleLogout}
              className="w-full px-4 py-2.5 bg-gray-50 border border-gray-200 text-gray-600 rounded-lg text-sm font-medium hover:bg-gray-100 transition-colors">
              退出登录
            </button>
          </div>

          <div className="card p-6 border-red-100">
            <h2 className="text-base font-semibold text-red-600 mb-2">注销账户</h2>
            <p className="text-xs text-gray-400 mb-4">
              注销后账户将被停用，手机号和邮箱将被释放（可绑定到其他账号）。此操作不可逆。
            </p>
            {deleteError && <div className="bg-red-50/80 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">{deleteError}</div>}
            {!showDeleteConfirm ? (
              <button type="button" onClick={() => setShowDeleteConfirm(true)}
                className="w-full px-4 py-2.5 bg-red-50 border border-red-200 text-red-600 rounded-lg text-sm font-medium hover:bg-red-100 transition-colors">
                申请注销账户
              </button>
            ) : (
              <div className="space-y-3">
                <div className="bg-red-50/50 border border-red-100 rounded-lg p-3">
                  <p className="text-sm text-red-700 font-medium">确认注销账户？</p>
                  <p className="text-xs text-red-500 mt-1">此操作不可逆，您的所有数据将被清除，手机号和邮箱将被释放。</p>
                </div>
                {user?.email && (
                  <EmailCodeInput
                    emailValue={user.email}
                    onEmailChange={() => {}}
                    codeValue={deleteEmailCode}
                    onCodeChange={setDeleteEmailCode}
                    compact
                  />
                )}
                <input type="password" value={deletePw} onChange={e => setDeletePw(e.target.value)} placeholder="当前密码（如有）" className={inputClass} />
                <div className="flex gap-3">
                  <button type="button" onClick={() => { setShowDeleteConfirm(false); setDeletePw(''); setDeleteError(''); setDeleteEmailCode(''); }}
                    className="flex-1 px-4 py-2.5 bg-gray-50 border border-gray-200 text-gray-600 rounded-lg text-sm font-medium hover:bg-gray-100 transition-colors">
                    取消
                  </button>
                  <button type="button" onClick={handleDeleteAccount} disabled={deleteLoading}
                    className="flex-1 px-4 py-2.5 bg-red-600 text-white rounded-lg text-sm font-medium hover:bg-red-700 transition-colors disabled:opacity-50">
                    {deleteLoading ? '注销中...' : '确认注销'}
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

function InviteTab() {
  const [data, setData] = useState<{ quota: number; used: number; remaining: number; codes: InviteCodeItem[] } | null>(null);
  const [loading, setLoading] = useState(true);
  const [genLoading, setGenLoading] = useState(false);
  const [error, setError] = useState('');
  const [copied, setCopied] = useState('');

  const load = () => {
    setLoading(true);
    getMyInviteCodes().then(setData).catch(() => {}).finally(() => setLoading(false));
  };

  useEffect(() => { load(); }, []);

  const handleGenerate = async () => {
    setGenLoading(true);
    setError('');
    try {
      await generateInviteCode();
      load();
    } catch (err: any) {
      setError(err.message || '生成失败');
    } finally {
      setGenLoading(false);
    }
  };

  const handleCopy = (code: string) => {
    navigator.clipboard.writeText(code);
    setCopied(code);
    setTimeout(() => setCopied(''), 2000);
  };

  if (loading) return <div className="text-center py-8 text-gray-400">加载中...</div>;

  return (
    <div>
      <div className="flex items-center justify-between mb-4">
        <div>
          <span className="text-sm text-gray-600">配额：{data?.used || 0}/{data?.quota || 0} 已使用</span>
        </div>
        <button
          onClick={handleGenerate}
          disabled={genLoading || (data?.remaining ?? 0) <= 0}
          className="px-4 py-1.5 bg-indigo-600 text-white text-sm rounded hover:bg-indigo-700 disabled:opacity-50"
        >
          {genLoading ? "生成中..." : "生成邀请码"}
        </button>
      </div>

      {error && <div className="mb-4 p-2 bg-red-50 text-red-600 rounded text-sm">{error}</div>}

      {!data?.codes.length ? (
        <div className="text-center py-8 text-gray-400">暂无邀请码</div>
      ) : (
        <div className="space-y-3">
          {data.codes.map(c => (
            <div key={c.id} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <div>
                <span className="font-mono text-sm tracking-wider">{c.code}</span>
                <span className="ml-2 text-xs text-gray-400">{c.credits} 积分</span>
              </div>
              <div className="flex items-center gap-2">
                {c.status === 'active' ? (
                  <>
                    <span className="text-xs text-green-600">未使用</span>
                    <button onClick={() => handleCopy(c.code)}
                      className="px-2 py-0.5 text-xs bg-indigo-600 text-white rounded hover:bg-indigo-700">
                      {copied === c.code ? '已复制' : '复制'}
                    </button>
                  </>
                ) : (
                  <span className="text-xs text-gray-400">已使用</span>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
