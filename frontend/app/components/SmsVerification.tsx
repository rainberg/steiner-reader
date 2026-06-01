'use client';

import { useCallback, useEffect, useRef, useState } from 'react';
import {
  generateSliderCaptcha,
  verifySliderCaptcha,
  sendSmsCode,
  sendEmailCode,
  SliderCaptcha,
} from '@/lib/api';

const inputCls =
  'w-full px-3 py-2.5 bg-white border border-gray-200 rounded-lg text-sm text-gray-700 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-300 transition-all';

export function SliderCaptchaWidget({ onVerified }: { onVerified: (captchaId: string, captchaX: number) => void }) {
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

export function SmsCodeInput({
  phoneValue,
  onPhoneChange,
  codeValue,
  onCodeChange,
  captchaId,
  captchaX,
  captchaVerified,
  onCodeSent,
}: {
  phoneValue: string;
  onPhoneChange: (v: string) => void;
  codeValue: string;
  onCodeChange: (v: string) => void;
  captchaId: string;
  captchaX: number;
  captchaVerified: boolean;
  onCodeSent?: () => void;
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
      onCodeSent?.();
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
            placeholder="4位验证码"
            required
            maxLength={4}
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

export function EmailCodeInput({
  emailValue,
  onEmailChange,
  codeValue,
  onCodeChange,
  captchaId,
  captchaX,
  captchaVerified,
  onCodeSent,
}: {
  emailValue: string;
  onEmailChange: (v: string) => void;
  codeValue: string;
  onCodeChange: (v: string) => void;
  captchaId: string;
  captchaX: number;
  captchaVerified: boolean;
  onCodeSent?: () => void;
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
    if (countdown > 0 || !captchaVerified || !emailValue) return;
    if (!emailValue.includes('@')) return;
    setSending(true);
    try {
      await sendEmailCode(emailValue, captchaId, captchaX);
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
      onCodeSent?.();
    } catch {
    } finally {
      setSending(false);
    }
  };

  return (
    <>
      <div>
        <label className="block text-sm font-medium text-gray-600 mb-1">邮箱</label>
        <input
          type="email"
          value={emailValue}
          onChange={e => onEmailChange(e.target.value)}
          placeholder="输入邮箱地址"
          required
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
            disabled={countdown > 0 || !captchaVerified || !emailValue || sending}
            className={`px-3 py-2.5 rounded-lg text-sm font-medium whitespace-nowrap transition ${
              countdown > 0 || !captchaVerified || !emailValue || sending
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
