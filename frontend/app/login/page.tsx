'use client';

import { useState, useEffect, Suspense } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import Link from 'next/link';
import {
  registerWithEmail,
  loginWithPassword,
  loginWithPhone,
  registerWithPhone,
} from '@/lib/api';
import { SmsCodeInput, EmailCodeInput } from '@/app/components/SmsVerification';

type View = 'login' | 'register';
type LoginTab = 'password' | 'sms';
type RegisterSub = 'email' | 'phone';

const inputCls =
  'w-full px-3 py-2.5 bg-white border border-gray-200 rounded-lg text-sm text-gray-700 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-300 transition-all';

export default function LoginPage() {
  return (
    <Suspense>
      <LoginContent />
    </Suspense>
  );
}

function LoginContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [view, setView] = useState<View>('login');
  const [loginTab, setLoginTab] = useState<LoginTab>('password');
  const [regSub, setRegSub] = useState<RegisterSub>('email');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const [account, setAccount] = useState('');
  const [password, setPassword] = useState('');

  const [smsPhone, setSmsPhone] = useState('');
  const [smsCode, setSmsCode] = useState('');

  const [regEmail, setRegEmail] = useState('');
  const [regEmailPwd, setRegEmailPwd] = useState('');
  const [regEmailConfirm, setRegEmailConfirm] = useState('');
  const [regDisplayName, setRegDisplayName] = useState('');
  const [regEmailCode, setRegEmailCode] = useState('');

  const [regPhone, setRegPhone] = useState('');
  const [regPhoneCode, setRegPhoneCode] = useState('');
  const [regPhonePwd, setRegPhonePwd] = useState('');
  const [regPhoneConfirm, setRegPhoneConfirm] = useState('');
  const [regPhoneDisplayName, setRegPhoneDisplayName] = useState('');
  const [regInviteCode, setRegInviteCode] = useState('');

  // Auto-fill invite code from URL and switch to register view
  useEffect(() => {
    const invite = searchParams.get('invite');
    if (invite) {
      setRegInviteCode(invite.toUpperCase());
      setView('register');
    }
  }, [searchParams]);

  const switchView = (v: View) => {
    setView(v);
    setError('');
    setRegInviteCode('');
  };

  const switchLoginTab = (t: LoginTab) => {
    setLoginTab(t);
    setError('');
  };

  const handlePasswordLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    if (!account || !password) {
      setError('请输入账号和密码');
      return;
    }
    setLoading(true);
    try {
      await loginWithPassword(account, password);
      window.dispatchEvent(new Event('auth-changed'));
      router.push('/');
      router.refresh();
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : '登录失败');
    } finally {
      setLoading(false);
    }
  };

  const handleSmsLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    if (!smsPhone || !smsCode) {
      setError('请输入手机号和验证码');
      return;
    }
    setLoading(true);
    try {
      await loginWithPhone(smsPhone, smsCode);
      window.dispatchEvent(new Event('auth-changed'));
      router.push('/');
      router.refresh();
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : '登录失败');
    } finally {
      setLoading(false);
    }
  };

  const handleEmailRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    if (!regEmailCode) {
      setError('请输入邮箱验证码');
      return;
    }
    if (regEmailPwd !== regEmailConfirm) {
      setError('两次输入的密码不一致');
      return;
    }
    setLoading(true);
    try {
      await registerWithEmail(regEmail, regEmailPwd, regDisplayName || undefined, regEmailCode, regInviteCode || undefined);
      window.dispatchEvent(new Event('auth-changed'));
      router.push('/');
      router.refresh();
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : '注册失败');
    } finally {
      setLoading(false);
    }
  };

  const handlePhoneRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    if (!regPhoneCode) {
      setError('请输入验证码');
      return;
    }
    if (!regPhonePwd) {
      setError('请设置密码');
      return;
    }
    if (regPhonePwd !== regPhoneConfirm) {
      setError('两次输入的密码不一致');
      return;
    }
    setLoading(true);
    try {
      await registerWithPhone(regPhone, regPhoneCode, regPhonePwd, regPhoneDisplayName || undefined, regInviteCode || undefined);
      window.dispatchEvent(new Event('auth-changed'));
      router.push('/');
      router.refresh();
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : '注册失败');
    } finally {
      setLoading(false);
    }
  };

  const loginTabs: { key: LoginTab; label: string }[] = [
    { key: 'password', label: '密码登录' },
    { key: 'sms', label: '验证码登录' },
  ];

  return (
    <div className="min-h-[70vh] flex items-center justify-center">
      <div className="w-full max-w-sm px-4">
        <div className="card p-8">
          {/* ── 登录视图 ── */}
          {view === 'login' && (
            <>
              <h1 className="text-xl font-bold text-gray-900 mb-1">登录</h1>
              <p className="text-sm text-gray-500 mb-6">登录以使用翻译和上传功能</p>

              <div className="flex mb-6 border-b border-gray-200">
                {loginTabs.map(t => (
                  <button
                    key={t.key}
                    type="button"
                    onClick={() => switchLoginTab(t.key)}
                    className={`flex-1 pb-2 text-sm font-medium transition border-b-2 -mb-px ${
                      loginTab === t.key
                        ? 'border-indigo-500 text-indigo-600'
                        : 'border-transparent text-gray-400 hover:text-gray-600'
                    }`}
                  >
                    {t.label}
                  </button>
                ))}
              </div>

              {error && (
                <div className="bg-red-50/80 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">
                  {error}
                </div>
              )}

              {loginTab === 'password' && (
                <form onSubmit={handlePasswordLogin} className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-600 mb-1">邮箱或手机号</label>
                    <input
                      type="text"
                      value={account}
                      onChange={e => setAccount(e.target.value)}
                      placeholder="输入邮箱或手机号"
                      required
                      className={inputCls}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-600 mb-1">密码</label>
                    <input
                      type="password"
                      value={password}
                      onChange={e => setPassword(e.target.value)}
                      placeholder="输入密码"
                      required
                      className={inputCls}
                    />
                  </div>
                  <div className="flex justify-end">
                    <Link href="/forgot-password" className="text-xs text-indigo-500 hover:text-indigo-600">忘记密码？</Link>
                  </div>
                  <button type="submit" disabled={loading} className="btn-primary w-full">
                    {loading ? '处理中...' : '登录'}
                  </button>
                </form>
              )}

              {loginTab === 'sms' && (
                <form onSubmit={handleSmsLogin} className="space-y-4">
                  <SmsCodeInput
                    phoneValue={smsPhone}
                    onPhoneChange={setSmsPhone}
                    codeValue={smsCode}
                    onCodeChange={setSmsCode}
                  />
                  <p className="text-xs text-gray-400">未注册的手机号将自动创建账号</p>
                  <button type="submit" disabled={loading} className="btn-primary w-full">
                    {loading ? '处理中...' : '登录'}
                  </button>
                </form>
              )}

              <div className="mt-6 pt-4 border-t border-gray-100 text-center">
                <button
                  type="button"
                  onClick={() => switchView('register')}
                  className="text-sm text-indigo-500 hover:text-indigo-600"
                >
                  没有账号？立即注册
                </button>
              </div>
            </>
          )}

          {/* ── 注册视图 ── */}
          {view === 'register' && (
            <>
              <h1 className="text-xl font-bold text-gray-900 mb-1">注册</h1>
              <p className="text-sm text-gray-500 mb-6">注册即赠送翻译积分</p>

              <div className="flex mb-4 bg-gray-100 rounded-lg p-1">
                <button
                  type="button"
                  onClick={() => { setRegSub('email'); setError(''); }}
                  className={`flex-1 py-1.5 rounded-md text-sm font-medium transition ${
                    regSub === 'email' ? 'bg-white text-gray-900 shadow-sm' : 'text-gray-500'
                  }`}
                >
                  邮箱注册
                </button>
                <button
                  type="button"
                  onClick={() => { setRegSub('phone'); setError(''); }}
                  className={`flex-1 py-1.5 rounded-md text-sm font-medium transition ${
                    regSub === 'phone' ? 'bg-white text-gray-900 shadow-sm' : 'text-gray-500'
                  }`}
                >
                  手机号注册
                </button>
              </div>

              {error && (
                <div className="bg-red-50/80 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">
                  {error}
                </div>
              )}

              {regSub === 'email' && (
                <form onSubmit={handleEmailRegister} className="space-y-4">
                  <EmailCodeInput
                    emailValue={regEmail}
                    onEmailChange={setRegEmail}
                    codeValue={regEmailCode}
                    onCodeChange={setRegEmailCode}
                  />
                  <div>
                    <label className="block text-sm font-medium text-gray-600 mb-1">昵称（可选）</label>
                    <input
                      type="text"
                      value={regDisplayName}
                      onChange={e => setRegDisplayName(e.target.value)}
                      placeholder="输入昵称"
                      className={inputCls}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-600 mb-1">密码</label>
                    <input
                      type="password"
                      value={regEmailPwd}
                      onChange={e => setRegEmailPwd(e.target.value)}
                      placeholder="至少 6 个字符"
                      minLength={6}
                      required
                      className={inputCls}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-600 mb-1">确认密码</label>
                    <input
                      type="password"
                      value={regEmailConfirm}
                      onChange={e => setRegEmailConfirm(e.target.value)}
                      placeholder="再次输入密码"
                      minLength={6}
                      required
                      className={inputCls}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-600 mb-1">邀请码（可选）</label>
                    <input
                      type="text"
                      value={regInviteCode}
                      onChange={e => setRegInviteCode(e.target.value.toUpperCase())}
                      placeholder="邀请码（可选）"
                      className={inputCls}
                    />
                  </div>
                  <button type="submit" disabled={loading} className="btn-primary w-full">
                    {loading ? '处理中...' : '注册'}
                  </button>
                </form>
              )}

              {regSub === 'phone' && (
                <form onSubmit={handlePhoneRegister} className="space-y-4">
                  <SmsCodeInput
                    phoneValue={regPhone}
                    onPhoneChange={setRegPhone}
                    codeValue={regPhoneCode}
                    onCodeChange={setRegPhoneCode}
                  />
                  <div>
                    <label className="block text-sm font-medium text-gray-600 mb-1">设置密码</label>
                    <input
                      type="password"
                      value={regPhonePwd}
                      onChange={e => setRegPhonePwd(e.target.value)}
                      placeholder="至少 6 个字符"
                      minLength={6}
                      required
                      className={inputCls}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-600 mb-1">确认密码</label>
                    <input
                      type="password"
                      value={regPhoneConfirm}
                      onChange={e => setRegPhoneConfirm(e.target.value)}
                      placeholder="再次输入密码"
                      minLength={6}
                      required
                      className={inputCls}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-600 mb-1">昵称（可选）</label>
                    <input
                      type="text"
                      value={regPhoneDisplayName}
                      onChange={e => setRegPhoneDisplayName(e.target.value)}
                      placeholder="输入昵称"
                      className={inputCls}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-600 mb-1">邀请码（可选）</label>
                    <input
                      type="text"
                      value={regInviteCode}
                      onChange={e => setRegInviteCode(e.target.value.toUpperCase())}
                      placeholder="邀请码（可选）"
                      className={inputCls}
                    />
                  </div>
                  <button type="submit" disabled={loading} className="btn-primary w-full">
                    {loading ? '处理中...' : '注册'}
                  </button>
                </form>
              )}

              <div className="mt-6 pt-4 border-t border-gray-100 text-center">
                <button
                  type="button"
                  onClick={() => switchView('login')}
                  className="text-sm text-indigo-500 hover:text-indigo-600"
                >
                  已有账号？返回登录
                </button>
              </div>
            </>
          )}
        </div>

        <div className="text-center mt-4">
          <Link href="/" className="text-sm text-indigo-500 hover:text-indigo-600">
            返回首页
          </Link>
        </div>
      </div>
    </div>
  );
}
