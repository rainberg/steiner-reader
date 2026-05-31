'use client';

import { useCallback, useEffect, useRef, useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import {
  registerWithEmail,
  loginWithPassword,
  loginWithPhone,
  registerWithPhone,
  generateSliderCaptcha,
  verifySliderCaptcha,
  sendSmsCode,
  SliderCaptcha,
} from '@/lib/api';

type Tab = 'password' | 'sms' | 'register';
type RegisterSub = 'email' | 'phone';

const inputCls =
  'w-full px-3 py-2.5 bg-white border border-gray-200 rounded-lg text-sm text-gray-700 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-300 transition-all';

function SliderCaptchaWidget({ onVerified }: { onVerified: (captchaId: string, captchaX: number) => void }) {
  const [captcha, setCaptcha] = useState<SliderCaptcha | null>(null);
  const [sliderX, setSliderX] = useState(0);
  const [isDragging, setIsDragging] = useState(false);
  const [verified, setVerified] = useState(false);
  const [loading, setLoading] = useState(false);
  const [imgScale, setImgScale] = useState(1);
  const trackRef = useRef<HTMLDivElement>(null);
  const bgRef = useRef<HTMLImageElement>(null);
  const startXRef = useRef(0);
  const startSliderXRef = useRef(0);

  const loadCaptcha = useCallback(async () => {
    setLoading(true);
    try {
      const data = await generateSliderCaptcha();
      setCaptcha(data);
      setSliderX(0);
      setVerified(false);
      setImgScale(1);
    } catch {
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadCaptcha();
  }, [loadCaptcha]);

  const updateScale = useCallback(() => {
    if (bgRef.current && bgRef.current.naturalWidth > 0) {
      setImgScale(bgRef.current.clientWidth / bgRef.current.naturalWidth);
    }
  }, []);

  useEffect(() => {
    const img = bgRef.current;
    if (!img) return;
    const onLoad = () => updateScale();
    if (img.complete) onLoad();
    else img.addEventListener('load', onLoad);
    const observer = new ResizeObserver(() => updateScale());
    observer.observe(img);
    return () => {
      img.removeEventListener('load', onLoad);
      observer.disconnect();
    };
  }, [captcha, updateScale]);

  useEffect(() => {
    if (verified && captcha) {
      onVerified(captcha.captcha_id, Math.round(sliderX / imgScale));
    }
  }, [verified, captcha, sliderX, imgScale, onVerified]);

  const handleDragStart = (e: React.MouseEvent | React.TouchEvent) => {
    if (verified) return;
    setIsDragging(true);
    const clientX = 'touches' in e ? e.touches[0].clientX : e.clientX;
    startXRef.current = clientX;
    startSliderXRef.current = sliderX;
  };

  const handleDragMove = useCallback(
    (e: MouseEvent | TouchEvent) => {
      if (!isDragging || !captcha) return;
      const clientX = 'touches' in e ? e.touches[0].clientX : e.clientX;
      const delta = clientX - startXRef.current;
      const scaledPW = captcha.puzzle_width * imgScale;
      const maxX = trackRef.current ? trackRef.current.offsetWidth - scaledPW : 280;
      const newX = Math.max(0, Math.min(maxX, startSliderXRef.current + delta));
      setSliderX(newX);
    },
    [isDragging, captcha, imgScale]
  );

  const handleDragEnd = useCallback(async () => {
    if (!isDragging || !captcha) return;
    setIsDragging(false);
    try {
      const originalX = Math.round(sliderX / imgScale);
      const result = await verifySliderCaptcha(captcha.captcha_id, originalX);
      if (result.success) {
        setVerified(true);
      } else {
        setVerified(false);
        await loadCaptcha();
      }
    } catch {
      setVerified(false);
      await loadCaptcha();
    }
  }, [isDragging, captcha, sliderX, imgScale, loadCaptcha]);

  useEffect(() => {
    if (!isDragging) return;
    window.addEventListener('mousemove', handleDragMove);
    window.addEventListener('mouseup', handleDragEnd);
    window.addEventListener('touchmove', handleDragMove);
    window.addEventListener('touchend', handleDragEnd);
    return () => {
      window.removeEventListener('mousemove', handleDragMove);
      window.removeEventListener('mouseup', handleDragEnd);
      window.removeEventListener('touchmove', handleDragMove);
      window.removeEventListener('touchend', handleDragEnd);
    };
  }, [isDragging, handleDragMove, handleDragEnd]);

  if (!captcha) return null;

  if (verified) {
    return (
      <div className="flex items-center gap-2 text-xs text-green-600 bg-green-50 px-3 py-1.5 rounded-lg">
        <svg className="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
        </svg>
        滑块验证已通过
      </div>
    );
  }

  const scaledY = captcha.y_position * imgScale;
  const scaledPW = captcha.puzzle_width * imgScale;

  return (
    <div>
      <label className="block text-sm font-medium text-gray-600 mb-1">滑块验证</label>
      <div className="relative rounded-lg overflow-hidden border border-gray-200 bg-gray-100 select-none">
        <div className="relative">
          <img
            ref={bgRef}
            src={captcha.bg_image}
            alt=""
            className="w-full h-auto block"
            draggable={false}
          />
          <img
            src={captcha.slider_image}
            alt=""
            className="absolute top-0 left-0"
            style={{
              transform: `translateX(${sliderX}px) translateY(${scaledY}px)`,
              width: scaledPW,
              height: scaledPW,
            }}
            draggable={false}
          />
        </div>
        <div ref={trackRef} className="relative h-10 bg-gray-200 border-t border-gray-300 cursor-pointer">
          <div
            className="absolute top-0 left-0 h-full bg-indigo-100 rounded-l-lg"
            style={{ width: sliderX + scaledPW }}
          />
          <div
            className="absolute top-1 left-0 h-8 bg-white border border-gray-300 rounded-lg shadow-sm flex items-center justify-center text-gray-400"
            style={{ transform: `translateX(${sliderX}px)`, width: scaledPW }}
            onMouseDown={handleDragStart}
            onTouchStart={handleDragStart}
          >
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 9l4-4 4 4m0 6l-4 4-4-4" />
            </svg>
          </div>
          {!isDragging && sliderX === 0 && (
            <div className="absolute inset-0 flex items-center justify-center text-xs text-gray-400 pointer-events-none">
              拖动滑块完成验证
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function SmsCodeInput({
  phone,
  phoneValue,
  onPhoneChange,
  codeValue,
  onCodeChange,
  captchaId,
  captchaX,
  captchaVerified,
}: {
  phone: string;
  phoneValue: string;
  onPhoneChange: (v: string) => void;
  codeValue: string;
  onCodeChange: (v: string) => void;
  captchaId: string;
  captchaX: number;
  captchaVerified: boolean;
}) {
  const [countdown, setCountdown] = useState(0);
  const countdownRef = useRef<ReturnType<typeof setInterval> | null>(null);
  const [sending, setSending] = useState(false);

  useEffect(() => {
    return () => {
      if (countdownRef.current) clearInterval(countdownRef.current);
    };
  }, []);

  const handleSend = async () => {
    if (countdown > 0 || !captchaVerified || !phoneValue) return;
    if (!/^1[3-9]\d{9}$/.test(phoneValue)) return;
    setSending(true);
    try {
      await sendSmsCode(phoneValue, captchaId, captchaX);
      setCountdown(60);
      countdownRef.current = setInterval(() => {
        setCountdown(prev => {
          if (prev <= 1) {
            if (countdownRef.current) clearInterval(countdownRef.current);
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    } catch {
    } finally {
      setSending(false);
    }
  };

  return (
    <>
      <div>
        <label className="block text-sm font-medium text-gray-600 mb-1">手机号</label>
        <input
          type="tel"
          value={phoneValue}
          onChange={e => onPhoneChange(e.target.value)}
          placeholder="11位手机号"
          required
          maxLength={11}
          className={inputCls}
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-600 mb-1">验证码</label>
        <div className="flex gap-2">
          <input
            type="text"
            value={codeValue}
            onChange={e => onCodeChange(e.target.value)}
            placeholder="6位验证码"
            required
            maxLength={6}
            className={`flex-1 ${inputCls}`}
          />
          <button
            type="button"
            onClick={handleSend}
            disabled={countdown > 0 || !captchaVerified || !phoneValue || sending}
            className={`px-3 py-2.5 rounded-lg text-sm font-medium whitespace-nowrap transition ${
              countdown > 0 || !captchaVerified || !phoneValue || sending
                ? 'bg-gray-100 text-gray-400 cursor-not-allowed'
                : 'bg-indigo-50 text-indigo-600 hover:bg-indigo-100'
            }`}
          >
            {countdown > 0 ? `${countdown}s` : '获取验证码'}
          </button>
        </div>
      </div>
    </>
  );
}

export default function LoginPage() {
  const router = useRouter();
  const [tab, setTab] = useState<Tab>('password');
  const [regSub, setRegSub] = useState<RegisterSub>('email');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const [account, setAccount] = useState('');
  const [password, setPassword] = useState('');

  const [smsPhone, setSmsPhone] = useState('');
  const [smsCode, setSmsCode] = useState('');
  const [smsCaptchaId, setSmsCaptchaId] = useState('');
  const [smsCaptchaX, setSmsCaptchaX] = useState(0);
  const [smsCaptchaVerified, setSmsCaptchaVerified] = useState(false);

  const [regEmail, setRegEmail] = useState('');
  const [regEmailPwd, setRegEmailPwd] = useState('');
  const [regEmailConfirm, setRegEmailConfirm] = useState('');
  const [regDisplayName, setRegDisplayName] = useState('');

  const [regPhone, setRegPhone] = useState('');
  const [regPhoneCode, setRegPhoneCode] = useState('');
  const [regPhonePwd, setRegPhonePwd] = useState('');
  const [regPhoneConfirm, setRegPhoneConfirm] = useState('');
  const [regPhoneDisplayName, setRegPhoneDisplayName] = useState('');
  const [regCaptchaId, setRegCaptchaId] = useState('');
  const [regCaptchaX, setRegCaptchaX] = useState(0);
  const [regCaptchaVerified, setRegCaptchaVerified] = useState(false);

  const handleSmsCaptchaVerified = useCallback((captchaId: string, captchaX: number) => {
    setSmsCaptchaId(captchaId);
    setSmsCaptchaX(captchaX);
    setSmsCaptchaVerified(true);
  }, []);

  const handleRegCaptchaVerified = useCallback((captchaId: string, captchaX: number) => {
    setRegCaptchaId(captchaId);
    setRegCaptchaX(captchaX);
    setRegCaptchaVerified(true);
  }, []);

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
    if (!smsCaptchaVerified) {
      setError('请先完成滑块验证');
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
    if (regEmailPwd !== regEmailConfirm) {
      setError('两次输入的密码不一致');
      return;
    }
    setLoading(true);
    try {
      await registerWithEmail(regEmail, regEmailPwd, regDisplayName || undefined);
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
    if (!regCaptchaVerified) {
      setError('请先完成滑块验证');
      return;
    }
    setLoading(true);
    try {
      await registerWithPhone(regPhone, regPhoneCode, regPhonePwd, regPhoneDisplayName || undefined);
      window.dispatchEvent(new Event('auth-changed'));
      router.push('/');
      router.refresh();
    } catch (err: unknown) {
      setError(err instanceof Error ? err.message : '注册失败');
    } finally {
      setLoading(false);
    }
  };

  const switchTab = (t: Tab) => {
    setTab(t);
    setError('');
  };

  const tabs: { key: Tab; label: string }[] = [
    { key: 'password', label: '密码登录' },
    { key: 'sms', label: '验证码登录' },
    { key: 'register', label: '注册' },
  ];

  return (
    <div className="min-h-[70vh] flex items-center justify-center">
      <div className="w-full max-w-sm px-4">
        <div className="card p-8">
          <h1 className="text-xl font-bold text-gray-900 mb-1">
            {tab === 'register' ? '注册' : '登录'}
          </h1>
          <p className="text-sm text-gray-500 mb-6">
            {tab === 'register' ? '注册即赠送翻译积分' : '登录以使用翻译和上传功能'}
          </p>

          <div className="flex mb-6 border-b border-gray-200">
            {tabs.map(t => (
              <button
                key={t.key}
                type="button"
                onClick={() => switchTab(t.key)}
                className={`flex-1 pb-2 text-sm font-medium transition border-b-2 -mb-px ${
                  tab === t.key
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

          {tab === 'password' && (
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
              <button type="submit" disabled={loading} className="btn-primary w-full">
                {loading ? '处理中...' : '登录'}
              </button>
            </form>
          )}

          {tab === 'sms' && (
            <form onSubmit={handleSmsLogin} className="space-y-4">
              <SliderCaptchaWidget onVerified={handleSmsCaptchaVerified} />
              <SmsCodeInput
                phone="sms"
                phoneValue={smsPhone}
                onPhoneChange={setSmsPhone}
                codeValue={smsCode}
                onCodeChange={setSmsCode}
                captchaId={smsCaptchaId}
                captchaX={smsCaptchaX}
                captchaVerified={smsCaptchaVerified}
              />
              <p className="text-xs text-gray-400">未注册的手机号将自动创建账号</p>
              <button type="submit" disabled={loading} className="btn-primary w-full">
                {loading ? '处理中...' : '登录'}
              </button>
            </form>
          )}

          {tab === 'register' && (
            <>
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

              {regSub === 'email' && (
                <form onSubmit={handleEmailRegister} className="space-y-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-600 mb-1">邮箱</label>
                    <input
                      type="email"
                      value={regEmail}
                      onChange={e => setRegEmail(e.target.value)}
                      placeholder="输入邮箱地址"
                      required
                      className={inputCls}
                    />
                  </div>
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
                  <button type="submit" disabled={loading} className="btn-primary w-full">
                    {loading ? '处理中...' : '注册'}
                  </button>
                </form>
              )}

              {regSub === 'phone' && (
                <form onSubmit={handlePhoneRegister} className="space-y-4">
                  <SliderCaptchaWidget onVerified={handleRegCaptchaVerified} />
                  <SmsCodeInput
                    phone="reg"
                    phoneValue={regPhone}
                    onPhoneChange={setRegPhone}
                    codeValue={regPhoneCode}
                    onCodeChange={setRegPhoneCode}
                    captchaId={regCaptchaId}
                    captchaX={regCaptchaX}
                    captchaVerified={regCaptchaVerified}
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
                  <button type="submit" disabled={loading} className="btn-primary w-full">
                    {loading ? '处理中...' : '注册'}
                  </button>
                </form>
              )}
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
