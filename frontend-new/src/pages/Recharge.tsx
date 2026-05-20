import { useEffect, useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { ArrowLeft, QrCode, Upload, Clock, CheckCircle, XCircle, ImagePlus } from 'lucide-react';
import { getStoredUser } from '../lib/api';

interface RechargeRequest {
  id: number;
  amount: number;
  status: string;
  admin_note: string | null;
  created_at: string;
  updated_at: string | null;
}

export default function Recharge() {
  const navigate = useNavigate();
  const [amount, setAmount] = useState('');
  const [image, setImage] = useState<File | null>(null);
  const [preview, setPreview] = useState('');
  const [loading, setLoading] = useState(false);
  const [msg, setMsg] = useState('');
  const [error, setError] = useState('');
  const [history, setHistory] = useState<RechargeRequest[]>([]);

  useEffect(() => {
    const u = getStoredUser();
    if (!u) {
      navigate('/login');
      return;
    }
    loadHistory();
  }, [navigate]);

  const loadHistory = async () => {
    const token = localStorage.getItem('steiner_token');
    try {
      const res = await fetch('/api/recharge/my-requests', {
        headers: { Authorization: `Bearer ${token}` },
      });
      if (res.ok) setHistory(await res.json());
    } catch {}
  };

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setImage(file);
    setPreview(URL.createObjectURL(file));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setMsg('');
    const amt = parseInt(amount, 10);
    if (!amt || amt <= 0) {
      setError('请输入有效金额');
      return;
    }
    if (!image) {
      setError('请上传付款凭证');
      return;
    }

    setLoading(true);
    const token = localStorage.getItem('steiner_token');
    try {
      const formData = new FormData();
      formData.append('amount', String(amt));
      formData.append('payment_image', image);

      const res = await fetch('/api/recharge/submit', {
        method: 'POST',
        headers: { Authorization: `Bearer ${token}` },
        body: formData,
      });
      const data = await res.json();
      if (res.ok) {
        setMsg(data.message);
        setAmount('');
        setImage(null);
        setPreview('');
        loadHistory();
      } else {
        setError(data.detail || '提交失败');
      }
    } catch {
      setError('网络错误');
    } finally {
      setLoading(false);
    }
  };

  const statusLabel = (s: string) =>
    s === 'pending' ? '待审核' : s === 'approved' ? '已通过' : '已拒绝';

  const statusIcon = (s: string) => {
    if (s === 'pending') return <Clock className="h-3.5 w-3.5" />;
    if (s === 'approved') return <CheckCircle className="h-3.5 w-3.5" />;
    return <XCircle className="h-3.5 w-3.5" />;
  };

  const statusClass = (s: string) =>
    s === 'pending'
      ? 'bg-amber-50 text-amber-700'
      : s === 'approved'
        ? 'bg-emerald-50 text-emerald-700'
        : 'bg-red-50 text-red-700';

  return (
    <div className="min-h-screen pt-6 pb-16">
      <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link
          to="/profile"
          className="inline-flex items-center gap-2 text-gray-600 hover:text-[#1e3a8a] transition-colors mb-8"
        >
          <ArrowLeft className="h-4 w-4" />
          返回
        </Link>

        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2 font-display">
            充值申请
          </h1>
          <p className="text-gray-600">扫描收款码付款后提交充值申请</p>
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-6 mb-6 text-center">
          <div className="flex items-center justify-center gap-2 mb-4">
            <QrCode className="h-5 w-5 text-[#1e3a8a]" />
            <h2 className="text-sm font-semibold text-gray-700">请扫描收款码完成付款</h2>
          </div>
          <img
            src="/api/recharge/payment-qr"
            alt="收款码"
            className="max-w-xs mx-auto rounded-xl border border-gray-200 shadow-sm"
            onError={(e) => {
              (e.target as HTMLImageElement).style.display = 'none';
            }}
          />
          <p className="text-xs text-gray-400 mt-3">若未显示收款码，请联系管理员</p>
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-6 mb-6">
          <div className="flex items-center gap-2 mb-4">
            <Upload className="h-5 w-5 text-[#1e3a8a]" />
            <h2 className="text-sm font-semibold text-gray-700">填写充值信息</h2>
          </div>

          {error && (
            <div className="bg-red-50 text-red-600 text-sm px-4 py-3 rounded-xl mb-4">
              {error}
            </div>
          )}
          {msg && (
            <div className="bg-emerald-50 text-emerald-600 text-sm px-4 py-3 rounded-xl mb-4">
              {msg}
            </div>
          )}

          <form onSubmit={handleSubmit} className="space-y-5">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1.5">
                充值金额
              </label>
              <input
                type="number"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                placeholder="输入充值金额"
                required
                className="w-full px-4 py-3 bg-gray-50 border border-gray-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent transition-all"
              />
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1.5">
                上传付款凭证
              </label>
              <div className="relative">
                <input
                  type="file"
                  accept="image/*"
                  onChange={handleImageChange}
                  required
                  className="w-full text-sm text-gray-500 file:mr-4 file:py-2.5 file:px-4 file:rounded-xl file:border-0 file:text-sm file:font-medium file:bg-[#1e3a8a]/10 file:text-[#1e3a8a] hover:file:bg-[#1e3a8a]/20 transition-all"
                />
              </div>
              {preview && (
                <div className="mt-3 relative inline-block">
                  <img
                    src={preview}
                    alt="预览"
                    className="max-w-xs rounded-xl border border-gray-200 shadow-sm"
                  />
                  <button
                    type="button"
                    onClick={() => {
                      setImage(null);
                      setPreview('');
                    }}
                    className="absolute -top-2 -right-2 w-6 h-6 bg-red-500 text-white rounded-full flex items-center justify-center text-xs hover:bg-red-600 transition-colors"
                  >
                    ×
                  </button>
                </div>
              )}
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full py-3 bg-[#1e3a8a] text-white rounded-xl font-medium hover:bg-[#1e3a8a]/90 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
            >
              {loading ? '提交中...' : '提交申请'}
            </button>
          </form>
        </div>

        <div className="bg-white rounded-2xl shadow-lg p-6">
          <div className="flex items-center gap-2 mb-4">
            <ImagePlus className="h-5 w-5 text-[#1e3a8a]" />
            <h2 className="text-sm font-semibold text-gray-700">申请记录</h2>
          </div>
          {history.length === 0 ? (
            <p className="text-sm text-gray-400 text-center py-4">暂无申请记录</p>
          ) : (
            <div className="space-y-2">
              {history.map((r) => (
                <div
                  key={r.id}
                  className="flex items-center justify-between py-3 px-4 border-b border-gray-100 last:border-0"
                >
                  <div className="flex items-center gap-3">
                    <span className="text-gray-700 font-medium text-sm">
                      {r.amount} 点
                    </span>
                    <span
                      className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium ${statusClass(r.status)}`}
                    >
                      {statusIcon(r.status)}
                      {statusLabel(r.status)}
                    </span>
                    {r.admin_note && (
                      <span className="text-gray-400 text-xs">{r.admin_note}</span>
                    )}
                  </div>
                  <span className="text-gray-400 text-xs">
                    {new Date(r.created_at).toLocaleDateString('zh-CN')}
                  </span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
