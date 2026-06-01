'use client';

import { useCallback, useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import { resetPassword } from '@/lib/api';
import { SliderCaptchaWidget, EmailCodeInput } from '@/app/components/SmsVerification';

const inputCls =
  'w-full px-3 py-2.5 bg-white border border-gray-200 rounded-lg text-sm text-gray-700 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-300 transition-all';

export default function ForgotPasswordPage() {
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [emailCode, setEmailCode] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [captchaId, setCaptchaId] = useState('');
  const [captchaX, setCaptchaX] = useState(0);
  const [captchaVerified, setCaptchaVerified] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [loading, setLoading] = useState(false);

  const handleCaptchaVerified = useCallback((captchaId: string, captchaX: number) => {
    setCaptchaId(captchaId);
    setCaptchaX(captchaX);
    setCaptchaVerified(true);
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    if (!captchaVerified) {
      setError('请先完成滑块验证');
      return;
    }
    if (!emailCode) {
      setError('请输入验证码');
      return;
    }
    if (newPassword.length < 6) {
      setError('密码至少需要 6 个字符');
      return;
    }
    if (newPassword !== confirmPassword) {
      setError('两次输入的密码不一致');
      return;
    }

    setLoading(true);
    try {
      await resetPassword(email, emailCode, newPassword);
      setSuccess('密码重置成功，即将跳转到登录页');
      setTimeout(() => router.push('/login'), 2000);
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : '重置密码失败');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-[70vh] flex items-center justify-center">
      <div className="w-full max-w-sm px-4">
        <div className="card p-8">
          <h1 className="text-xl font-bold text-gray-900 mb-1">重置密码</h1>
          <p className="text-sm text-gray-500 mb-6">通过邮箱验证码重置您的密码</p>

          {error && (
            <div className="bg-red-50/80 border border-red-100 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">
              {error}
            </div>
          )}
          {success && (
            <div className="bg-green-50/80 border border-green-100 text-green-600 text-sm px-3 py-2 rounded-lg mb-4">
              {success}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-4">
            <SliderCaptchaWidget onVerified={handleCaptchaVerified} />
            <EmailCodeInput
              emailValue={email}
              onEmailChange={setEmail}
              codeValue={emailCode}
              onCodeChange={setEmailCode}
              captchaId={captchaId}
              captchaX={captchaX}
              captchaVerified={captchaVerified}
            />
            <div>
              <label className="block text-sm font-medium text-gray-600 mb-1">新密码</label>
              <input
                type="password"
                value={newPassword}
                onChange={e => setNewPassword(e.target.value)}
                placeholder="至少 6 个字符"
                minLength={6}
                required
                className={inputCls}
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
                className={inputCls}
              />
            </div>
            <button type="submit" disabled={loading} className="btn-primary w-full">
              {loading ? '处理中...' : '重置密码'}
            </button>
          </form>

          <div className="text-center mt-4">
            <Link href="/login" className="text-sm text-indigo-500 hover:text-indigo-600">
              返回登录
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
