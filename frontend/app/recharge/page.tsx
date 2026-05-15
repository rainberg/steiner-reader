"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import { getStoredUser, User } from "@/lib/api";

const API_BASE = "";

export default function RechargePage() {
  const router = useRouter();
  const [user, setUser] = useState<User | null>(null);
  const [amount, setAmount] = useState("");
  const [image, setImage] = useState<File | null>(null);
  const [preview, setPreview] = useState("");
  const [loading, setLoading] = useState(false);
  const [msg, setMsg] = useState("");
  const [error, setError] = useState("");
  const [history, setHistory] = useState<Array<{
    id: number; amount: number; status: string; admin_note: string | null;
    created_at: string; updated_at: string | null;
  }>>([]);

  useEffect(() => {
    const u = getStoredUser();
    if (!u) { router.push("/login"); return; }
    setUser(u);
    loadHistory();
  }, [router]);

  const loadHistory = async () => {
    const token = localStorage.getItem("steiner_token");
    try {
      const res = await fetch(`${API_BASE}/api/recharge/my-requests`, {
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
    setError("");
    setMsg("");
    const amt = parseInt(amount, 10);
    if (!amt || amt <= 0) { setError("请输入有效金额"); return; }
    if (!image) { setError("请上传付款凭证"); return; }

    setLoading(true);
    const token = localStorage.getItem("steiner_token");
    try {
      const formData = new FormData();
      formData.append("amount", String(amt));
      formData.append("payment_image", image);

      const res = await fetch(`${API_BASE}/api/recharge/submit`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
        body: formData,
      });
      const data = await res.json();
      if (res.ok) {
        setMsg(data.message);
        setAmount("");
        setImage(null);
        setPreview("");
        loadHistory();
      } else {
        setError(data.detail || "提交失败");
      }
    } catch {
      setError("网络错误");
    } finally {
      setLoading(false);
    }
  };

  const statusLabel = (s: string) =>
    s === "pending" ? "待审核" : s === "approved" ? "已通过" : "已拒绝";

  return (
    <div className="max-w-2xl mx-auto px-4 py-8">
      <div className="flex items-center justify-between mb-6">
        <h1 className="text-xl font-bold text-gray-900">充值申请</h1>
        <Link href="/" className="text-sm text-blue-500 hover:text-blue-600">返回首页</Link>
      </div>

      {/* QR Code */}
      <div className="card p-6 mb-6 text-center">
        <h2 className="text-sm font-medium text-gray-700 mb-3">请扫描收款码完成付款</h2>
        <img
          src={`${API_BASE}/api/recharge/payment-qr`}
          alt="收款码"
          className="max-w-xs mx-auto rounded-lg border border-gray-200"
          onError={(e) => { (e.target as HTMLImageElement).style.display = "none"; }}
        />
        <p className="text-xs text-gray-400 mt-2">若未显示收款码，请联系管理员</p>
      </div>

      {/* Submit Form */}
      <div className="card p-6 mb-6">
        <h2 className="text-sm font-medium text-gray-700 mb-4">填写充值信息</h2>

        {error && <div className="bg-red-50 text-red-600 text-sm px-3 py-2 rounded-lg mb-4">{error}</div>}
        {msg && <div className="bg-green-50 text-green-600 text-sm px-3 py-2 rounded-lg mb-4">{msg}</div>}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">充值金额</label>
            <input
              type="number"
              value={amount}
              onChange={e => setAmount(e.target.value)}
              placeholder="输入充值金额"
              required
              className="w-full px-3 py-2.5 border border-gray-200 rounded-lg text-sm"
            />
          </div>

          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">上传付款凭证</label>
            <input
              type="file"
              accept="image/*"
              onChange={handleImageChange}
              required
              className="w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
            {preview && (
              <img src={preview} alt="预览" className="mt-2 max-w-xs rounded-lg border" />
            )}
          </div>

          <button type="submit" disabled={loading} className="btn-primary w-full">
            {loading ? "提交中..." : "提交申请"}
          </button>
        </form>
      </div>

      {/* History */}
      <div className="card p-6">
        <h2 className="text-sm font-medium text-gray-700 mb-4">申请记录</h2>
        {history.length === 0 ? (
          <p className="text-sm text-gray-400">暂无申请记录</p>
        ) : (
          <div className="space-y-2">
            {history.map(r => (
              <div key={r.id} className="flex items-center justify-between py-2 border-b border-gray-100 text-sm">
                <div>
                  <span className="text-gray-700">{r.amount} 点</span>
                  <span className={`ml-2 px-1.5 py-0.5 rounded text-xs ${
                    r.status === "pending" ? "bg-yellow-50 text-yellow-700" :
                    r.status === "approved" ? "bg-green-50 text-green-700" :
                    "bg-red-50 text-red-700"
                  }`}>{statusLabel(r.status)}</span>
                  {r.admin_note && <span className="text-gray-400 text-xs ml-2">{r.admin_note}</span>}
                </div>
                <span className="text-gray-400 text-xs">{new Date(r.created_at).toLocaleDateString("zh-CN")}</span>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
