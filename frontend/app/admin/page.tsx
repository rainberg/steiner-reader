"use client";

import { useState, useEffect, useMemo, useRef } from "react";
import { useRouter } from "next/navigation";
import { adminAddCredits, adminUpdateUser, adminResetPassword, fetchCreditSettings, updateCreditSetting, CreditSetting } from "@/lib/api";

interface User {
  id: number;
  username: string;
  email: string;
  credits: number;
  is_admin: number;
  created_at: string;
}

export default function AdminPage() {
  const router = useRouter();
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [editUserId, setEditUserId] = useState<number | null>(null);
  const [newCredits, setNewCredits] = useState("");
  const [addCreditsValue, setAddCreditsValue] = useState("");
  const [success, setSuccess] = useState("");
  const [currentUserId, setCurrentUserId] = useState<number | null>(null);
  const [search, setSearch] = useState("");

  // Edit user modal state
  const [editModal, setEditModal] = useState<{ user: User } | null>(null);
  const [editUsername, setEditUsername] = useState("");

  // Tab state
  const [activeTab, setActiveTab] = useState<"users" | "settings" | "recharge" | "upload" | "fixes" | "books">("users");
  const [creditSettings, setCreditSettings] = useState<CreditSetting[]>([]);
  const [settingsLoading, setSettingsLoading] = useState(false);
  const [editEmail, setEditEmail] = useState("");

  // Reset password modal state
  const [resetModal, setResetModal] = useState<{ user: User } | null>(null);
  const [newPassword, setNewPassword] = useState("");

  const token = typeof window !== "undefined" ? localStorage.getItem("access_token") : null;

  useEffect(() => {
    if (!token) {
      router.push("/login");
      return;
    }
    fetchCurrentUser();
    fetchUsers();
  }, []);

  const fetchCurrentUser = async () => {
    try {
      const res = await fetch("/api/auth/me", {
        headers: { Authorization: `Bearer ${token}` },
      });
      if (res.ok) {
        const data = await res.json();
        setCurrentUserId(data.id);
      }
    } catch (err) {
      console.error("获取当前用户失败:", err);
    }
  };

  const fetchUsers = async () => {
    try {
      const res = await fetch("/api/admin/users", {
        headers: { Authorization: `Bearer ${token}` },
      });
      if (res.status === 403) {
        setError("需要管理员权限");
        return;
      }
      if (!res.ok) throw new Error("获取用户列表失败");
      const data = await res.json();
      setUsers(data.users);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const filteredUsers = useMemo(() => {
    if (!search.trim()) return users;
    const q = search.toLowerCase();
    return users.filter(
      (u) =>
        u.username.toLowerCase().includes(q) ||
        u.email.toLowerCase().includes(q)
    );
  }, [users, search]);

  const handleSetCredits = async (userId: number) => {
    if (!newCredits || isNaN(parseInt(newCredits))) {
      setError("请输入有效的点数");
      return;
    }
    try {
      const res = await fetch(`/api/admin/users/${userId}/credits`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ credits: parseInt(newCredits) }),
      });
      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.detail || "设置点数失败");
      }
      const data = await res.json();
      setSuccess(`已将 ${data.username} 的点数设置为 ${data.new_credits}`);
      setEditUserId(null);
      setNewCredits("");
      fetchUsers();
    } catch (err: any) {
      setError(err.message);
    }
  };

  const handleAddCredits = async (userId: number) => {
    if (!addCreditsValue || isNaN(parseInt(addCreditsValue))) {
      setError("请输入有效的点数");
      return;
    }
    try {
      const data = await adminAddCredits(userId, parseInt(addCreditsValue));
      setSuccess(`已为 ${data.username} 添加 ${data.added} 点，当前总额: ${data.new_credits}`);
      setAddCreditsValue("");
      fetchUsers();
    } catch (err: any) {
      setError(err.message);
    }
  };

  const openEditModal = (user: User) => {
    setEditModal({ user });
    setEditUsername(user.username);
    setEditEmail(user.email);
  };

  const handleUpdateUser = async () => {
    if (!editModal) return;
    try {
      const data = await adminUpdateUser(editModal.user.id, {
        username: editUsername,
        email: editEmail,
      });
      setSuccess(`用户 ${data.username} 信息已更新`);
      setEditModal(null);
      fetchUsers();
    } catch (err: any) {
      setError(err.message);
    }
  };

  const openResetModal = (user: User) => {
    setResetModal({ user });
    setNewPassword("");
  };

  const handleResetPassword = async () => {
    if (!resetModal) return;
    if (newPassword.length < 6) {
      setError("密码至少 6 个字符");
      return;
    }
    try {
      const data = await adminResetPassword(resetModal.user.id, newPassword);
      setSuccess(data.message || "密码已重置");
      setResetModal(null);
      setNewPassword("");
    } catch (err: any) {
      setError(err.message);
    }
  };

  const handleToggleAdmin = async (userId: number, username: string, currentIsAdmin: number) => {
    const action = currentIsAdmin ? "取消管理员权限" : "设为管理员";
    if (!window.confirm(`确定要${action}用户 "${username}" 吗？`)) return;
    try {
      const res = await fetch(`/api/admin/users/${userId}/toggle-admin`, {
        method: "PUT",
        headers: { Authorization: `Bearer ${token}` },
      });
      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.detail || "操作失败");
      }
      const data = await res.json();
      setSuccess(data.message || `已${action}`);
      fetchUsers();
    } catch (err: any) {
      setError(err.message);
    }
  };

  const handleDeleteUser = async (userId: number, username: string) => {
    if (!window.confirm(`确定要删除用户 "${username}" 吗？此操作不可恢复！`)) return;
    try {
      const res = await fetch(`/api/admin/users/${userId}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` },
      });
      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.detail || "删除失败");
      }
      const data = await res.json();
      setSuccess(data.message || "用户已删除");
      fetchUsers();
    } catch (err: any) {
      setError(err.message);
    }
  };

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto p-6">
        <div className="text-center text-gray-500">加载中...</div>
      </div>
    );
  }

  return (
    <div className="max-w-6xl mx-auto p-6">
      <div className="mb-6">
        <div className="flex gap-2 border-b border-gray-200 pb-0">
          <button
            onClick={() => setActiveTab("users")}
            className={`px-4 py-2 text-sm font-medium rounded-t-lg transition ${
              activeTab === "users" ? "bg-white text-blue-600 border border-b-white border-gray-200 -mb-px" : "text-gray-500 hover:text-gray-700"
            }`}
          >
            用户管理
          </button>
          <button
            onClick={() => { setActiveTab("settings"); loadCreditSettings(); }}
            className={`px-4 py-2 text-sm font-medium rounded-t-lg transition ${
              activeTab === "settings" ? "bg-white text-blue-600 border border-b-white border-gray-200 -mb-px" : "text-gray-500 hover:text-gray-700"
            }`}
          >
            积分设置
          </button>
          <button
            onClick={() => setActiveTab("recharge")}
            className={`px-4 py-2 text-sm font-medium rounded-t-lg transition ${
              activeTab === "recharge" ? "bg-white text-blue-600 border border-b-white border-gray-200 -mb-px" : "text-gray-500 hover:text-gray-700"
            }`}
          >
            充值审核
          </button>
          <button
            onClick={() => setActiveTab("upload")}
            className={`px-4 py-2 text-sm font-medium rounded-t-lg transition ${
              activeTab === "upload" ? "bg-white text-blue-600 border border-b-white border-gray-200 -mb-px" : "text-gray-500 hover:text-gray-700"
            }`}
          >
            上传书籍
          </button>
          <button
            onClick={() => setActiveTab("fixes")}
            className={`px-4 py-2 text-sm font-medium rounded-t-lg transition ${
              activeTab === "fixes" ? "bg-white text-blue-600 border border-b-white border-gray-200 -mb-px" : "text-gray-500 hover:text-gray-700"
            }`}
          >
            翻译修正
          </button>
          <button
            onClick={() => setActiveTab("books")}
            className={`px-4 py-2 text-sm font-medium rounded-t-lg transition ${
              activeTab === "books" ? "bg-white text-blue-600 border border-b-white border-gray-200 -mb-px" : "text-gray-500 hover:text-gray-700"
            }`}
          >
            书籍管理
          </button>
        </div>
      </div>

      {activeTab === "users" ? (
      <>
      <div className="mb-4">
        <p className="text-gray-500 text-sm">管理用户账户和点数</p>
      </div>

      {error && (
        <div className="mb-4 p-3 bg-red-50 text-red-700 rounded-lg">
          {error}
          <button onClick={() => setError("")} className="float-right text-red-500 hover:text-red-700">&times;</button>
        </div>
      )}

      {success && (
        <div className="mb-4 p-3 bg-green-50 text-green-700 rounded-lg">
          {success}
          <button onClick={() => setSuccess("")} className="float-right text-green-500 hover:text-green-700">&times;</button>
        </div>
      )}

      {/* Search bar */}
      <div className="mb-4">
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="搜索用户名或邮箱..."
          className="w-full max-w-sm px-4 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        {search && (
          <span className="ml-2 text-sm text-gray-500">
            找到 {filteredUsers.length} 个用户
          </span>
        )}
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">用户</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">邮箱</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">点数</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">角色</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">注册时间</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">操作</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100">
            {filteredUsers.map((user) => {
              const isCurrentUser = currentUserId === user.id;
              return (
                <tr key={user.id} className={`hover:bg-gray-50 ${isCurrentUser ? "bg-blue-50/30" : ""}`}>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <div className="text-sm font-medium text-gray-900">
                      {user.username}
                      {isCurrentUser && (
                        <span className="ml-2 inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-blue-100 text-blue-800">
                          当前用户
                        </span>
                      )}
                    </div>
                    <div className="text-sm text-gray-500">ID: {user.id}</div>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {user.email}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    {editUserId === user.id ? (
                      <div className="flex items-center gap-2">
                        <input
                          type="number"
                          value={newCredits}
                          onChange={(e) => setNewCredits(e.target.value)}
                          className="w-20 px-2 py-1 border rounded text-sm"
                          placeholder="点数"
                        />
                        <button
                          onClick={() => handleSetCredits(user.id)}
                          className="px-2 py-1 bg-blue-600 text-white text-xs rounded hover:bg-blue-700"
                        >
                          设置
                        </button>
                        <button
                          onClick={() => setEditUserId(null)}
                          className="px-2 py-1 text-gray-500 text-xs hover:text-gray-700"
                        >
                          取消
                        </button>
                      </div>
                    ) : (
                      <div className="flex items-center gap-2">
                        <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-yellow-50 text-yellow-700">
                          {user.credits} 点
                        </span>
                        <button
                          onClick={() => {
                            setEditUserId(user.id);
                            setNewCredits(user.credits.toString());
                          }}
                          className="text-blue-600 hover:text-blue-800 text-sm"
                        >
                          修改
                        </button>
                      </div>
                    )}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <div className="flex items-center gap-2">
                      {user.is_admin ? (
                        <>
                          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-50 text-purple-700">
                            管理员
                          </span>
                          <button
                            onClick={() => handleToggleAdmin(user.id, user.username, user.is_admin)}
                            className="px-2 py-1 bg-green-600 text-white text-xs rounded hover:bg-green-700"
                          >
                            取消管理
                          </button>
                        </>
                      ) : (
                        <>
                          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-gray-100 text-gray-800">
                            用户
                          </span>
                          <button
                            onClick={() => handleToggleAdmin(user.id, user.username, user.is_admin)}
                            className="px-2 py-1 bg-purple-600 text-white text-xs rounded hover:bg-purple-700"
                          >
                            设为管理员
                          </button>
                        </>
                      )}
                    </div>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {new Date(user.created_at).toLocaleDateString("zh-CN")}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm">
                    <div className="flex flex-wrap items-center gap-2">
                      <input
                        type="number"
                        value={addCreditsValue}
                        onChange={(e) => setAddCreditsValue(e.target.value)}
                        className="w-16 px-2 py-1 border rounded text-sm"
                        placeholder="添加"
                      />
                      <button
                        onClick={() => handleAddCredits(user.id)}
                        className="px-2 py-1 bg-green-600 text-white text-xs rounded hover:bg-green-700"
                      >
                        充值
                      </button>
                      <button
                        onClick={() => openEditModal(user)}
                        className="px-2 py-1 bg-blue-600 text-white text-xs rounded hover:bg-blue-700"
                      >
                        编辑
                      </button>
                      <button
                        onClick={() => openResetModal(user)}
                        className="px-2 py-1 bg-orange-600 text-white text-xs rounded hover:bg-orange-700"
                      >
                        重置密码
                      </button>
                      {isCurrentUser ? (
                        <span className="px-2 py-1 text-gray-400 text-xs">
                          当前用户
                        </span>
                      ) : (
                        <button
                          onClick={() => handleDeleteUser(user.id, user.username)}
                          className="px-2 py-1 bg-red-600 text-white text-xs rounded hover:bg-red-700"
                        >
                          删除
                        </button>
                      )}
                    </div>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      <div className="mt-6 text-sm text-gray-500">
        共 {users.length} 个用户{search ? ` (显示 ${filteredUsers.length} 个)` : ""}
      </div>

      {/* Edit User Modal */}
      {editModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
          <div className="bg-white rounded-xl shadow-lg p-6 w-full max-w-md mx-4">
            <h2 className="text-lg font-bold text-gray-900 mb-4">编辑用户: {editModal.user.username}</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">用户名</label>
                <input
                  type="text"
                  value={editUsername}
                  onChange={(e) => setEditUsername(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">邮箱</label>
                <input
                  type="email"
                  value={editEmail}
                  onChange={(e) => setEditEmail(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>
            </div>
            <div className="flex justify-end gap-3 mt-6">
              <button
                onClick={() => setEditModal(null)}
                className="px-4 py-2 text-sm text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200"
              >
                取消
              </button>
              <button
                onClick={handleUpdateUser}
                className="px-4 py-2 text-sm text-white bg-blue-600 rounded-lg hover:bg-blue-700"
              >
                保存
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Reset Password Modal */}
      {resetModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
          <div className="bg-white rounded-xl shadow-lg p-6 w-full max-w-md mx-4">
            <h2 className="text-lg font-bold text-gray-900 mb-4">重置密码: {resetModal.user.username}</h2>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">新密码</label>
              <input
                type="password"
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                placeholder="至少 6 个字符"
                className="w-full px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
            <div className="flex justify-end gap-3 mt-6">
              <button
                onClick={() => setResetModal(null)}
                className="px-4 py-2 text-sm text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200"
              >
                取消
              </button>
              <button
                onClick={handleResetPassword}
                className="px-4 py-2 text-sm text-white bg-orange-600 rounded-lg hover:bg-orange-700"
              >
                确认重置
              </button>
            </div>
          </div>
        </div>
      )}
      </>
      ) : activeTab === "settings" ? (
      <CreditSettingsTab
        settings={creditSettings}
        loading={settingsLoading}
        onUpdate={async (key: string, value: number) => {
          await updateCreditSetting(key, value);
          await loadCreditSettings();
        }}
      />
      ) : activeTab === "recharge" ? (
      <RechargeReviewTab />
      ) : activeTab === "fixes" ? (
      <TranslationFixesTab />
      ) : activeTab === "books" ? (
      <BooksManageTab />
      ) : (
      <UploadTab />
      )}
    </div>
  );

  function loadCreditSettings() {
    setSettingsLoading(true);
    fetchCreditSettings()
      .then(setCreditSettings)
      .catch((e) => setError(e.message))
      .finally(() => setSettingsLoading(false));
  }
}

function CreditSettingsTab({
  settings,
  loading,
  onUpdate,
}: {
  settings: CreditSetting[];
  loading: boolean;
  onUpdate: (key: string, value: number) => Promise<void>;
}) {
  const [editingKey, setEditingKey] = useState<string | null>(null);
  const [editValue, setEditValue] = useState("");
  const [msg, setMsg] = useState("");

  const LABELS: Record<string, string> = {
    translate_coefficient: "翻译系数 (每句×系数)",
    edit_translation_coefficient: "编辑译文系数 (每句×系数)",
    edit_source_coefficient: "编辑原文系数 (每句×系数)",
    download_lecture_price: "单章下载 (0=免费)",
    download_book_price: "全书下载 (0=免费)",
    recharge_coefficient: "充值兑换系数 (1元=积分)",
  };

  const handleSave = async (key: string) => {
    const val = parseInt(editValue, 10);
    if (isNaN(val) || val < 0) { setMsg("请输入有效数字"); return; }
    try {
      await onUpdate(key, val);
      setEditingKey(null);
      setMsg("保存成功");
    } catch {
      setMsg("保存失败");
    }
  };

  if (loading) {
    return <div className="text-center py-8 text-gray-400">加载中...</div>;
  }

  return (
    <div>
      <p className="text-gray-500 text-sm mb-4">配置各项点数消耗价格</p>
      {msg && (
        <div className="mb-4 p-2 bg-green-50 text-green-700 rounded text-sm">
          {msg}
          <button onClick={() => setMsg("")} className="float-right">&times;</button>
        </div>
      )}
      <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">配置项</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">说明</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">当前值 (点数)</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">操作</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100">
            {settings.map((s) => (
              <tr key={s.key} className="hover:bg-gray-50">
                <td className="px-6 py-4 text-sm font-medium text-gray-900">{s.key}</td>
                <td className="px-6 py-4 text-sm text-gray-500">{LABELS[s.key || ""] || s.description}</td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span className="text-sm font-mono text-gray-700">{s.value}</span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  {editingKey === s.key ? (
                    <div className="flex items-center gap-2">
                      <input
                        type="number"
                        value={editValue}
                        onChange={e => setEditValue(e.target.value)}
                        className="w-20 px-2 py-1 border rounded text-sm"
                      />
                      <button onClick={() => handleSave(s.key || "")} className="px-2 py-1 bg-blue-600 text-white text-xs rounded hover:bg-blue-700">保存</button>
                      <button onClick={() => setEditingKey(null)} className="px-2 py-1 text-gray-500 text-xs">取消</button>
                    </div>
                  ) : (
                    <button
                      onClick={() => { setEditingKey(s.key || null); setEditValue(String(s.value)); }}
                      className="text-blue-600 hover:text-blue-800 text-sm"
                    >
                      修改
                    </button>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function RechargeReviewTab() {
  const [requests, setRequests] = useState<Array<{
    id: number; user_id: string; username: string; amount: number;
    coefficient: number; credits: number;
    payment_image: string | null; status: string; admin_note: string | null;
    created_at: string; updated_at: string | null;
  }>>([]);
  const [loading, setLoading] = useState(true);
  const [qrUploading, setQrUploading] = useState(false);
  const [reviewMsg, setReviewMsg] = useState("");

  const loadRequests = () => {
    const token = localStorage.getItem("access_token");
    fetch("/api/recharge/admin/pending-requests", {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then(r => r.json())
      .then(setRequests)
      .catch(() => {})
      .finally(() => setLoading(false));
  };

  useEffect(() => { loadRequests(); }, []);

  const handleReview = async (id: number, status: string, note: string) => {
    const token = localStorage.getItem("access_token");
    const res = await fetch(`/api/recharge/admin/review/${id}`, {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: `Bearer ${token}` },
      body: JSON.stringify({ status, admin_note: note }),
    });
    const data = await res.json();
    setReviewMsg(data.message || "");
    loadRequests();
  };

  const handleQrUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setQrUploading(true);
    const token = localStorage.getItem("access_token");
    const formData = new FormData();
    formData.append("qr_image", file);
    await fetch("/api/recharge/admin/upload-qr", {
      method: "POST",
      headers: { Authorization: `Bearer ${token}` },
      body: formData,
    });
    setQrUploading(false);
    setReviewMsg("收款码已上传");
  };

  const statusBadge = (s: string) => {
    const c = s === "pending" ? "bg-yellow-50 text-yellow-700" :
              s === "approved" ? "bg-green-50 text-green-700" : "bg-red-50 text-red-700";
    const t = s === "pending" ? "待审核" : s === "approved" ? "已通过" : "已拒绝";
    return <span className={`px-2 py-0.5 rounded text-xs font-medium ${c}`}>{t}</span>;
  };

  if (loading) return <div className="text-center py-8 text-gray-400">加载中...</div>;

  return (
    <div>
      {reviewMsg && <div className="mb-4 p-2 bg-green-50 text-green-700 rounded text-sm">{reviewMsg}</div>}

      {/* QR Code Upload */}
      <div className="mb-6 bg-white rounded-xl shadow-sm border border-gray-100 p-5">
        <h3 className="text-sm font-medium text-gray-800 mb-3">收款码管理</h3>
        <div className="flex items-center gap-4">
          <img
            src="/api/recharge/payment-qr"
            alt="收款码"
            className="w-24 h-24 object-contain border rounded"
            onError={(e) => { (e.target as HTMLImageElement).style.display = "none"; }}
          />
          <label className="cursor-pointer px-4 py-2 bg-blue-600 text-white text-sm rounded-lg hover:bg-blue-700">
            {qrUploading ? "上传中..." : "上传收款码"}
            <input type="file" accept="image/*" onChange={handleQrUpload} className="hidden" />
          </label>
        </div>
      </div>

      {/* Recharge Requests */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">用户</th>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">金额 (元)</th>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">兑换</th>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">积分</th>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">凭证</th>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">状态</th>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">时间</th>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">操作</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100">
            {requests.map(r => (
              <tr key={r.id} className="hover:bg-gray-50">
                <td className="px-4 py-3 text-sm">{r.username}</td>
                <td className="px-4 py-3 text-sm">{r.amount} 元</td>
                <td className="px-4 py-3 text-sm text-gray-500">×{r.coefficient || 10}</td>
                <td className="px-4 py-3 text-sm font-medium">{r.credits || r.amount * (r.coefficient || 10)} 积分</td>
                <td className="px-4 py-3">
                  {r.payment_image ? (
                    <a href={`/api/recharge/payment-proof/${r.payment_image}`} target="_blank"
                       className="text-blue-600 text-xs hover:underline">
                      查看凭证
                    </a>
                  ) : <span className="text-gray-300 text-xs">-</span>}
                </td>
                <td className="px-4 py-3">{statusBadge(r.status)}</td>
                <td className="px-4 py-3 text-xs text-gray-400">{new Date(r.created_at).toLocaleDateString("zh-CN")}</td>
                <td className="px-4 py-3">
                  {r.status === "pending" ? (
                    <div className="flex gap-2">
                      <button onClick={() => handleReview(r.id, "approved", "")}
                              className="px-2 py-1 bg-green-600 text-white text-xs rounded hover:bg-green-700">
                        批准
                      </button>
                      <button onClick={() => handleReview(r.id, "rejected", "")}
                              className="px-2 py-1 bg-red-600 text-white text-xs rounded hover:bg-red-700">
                        拒绝
                      </button>
                    </div>
                  ) : (
                    <span className="text-xs text-gray-400">{r.admin_note || "-"}</span>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function UploadTab() {
  const [files, setFiles] = useState<File[]>([]);
  const [uploading, setUploading] = useState(false);
  const [result, setResult] = useState<{ success: boolean; message: string; gaNumber?: string; chapters?: number } | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    const dropped = Array.from(e.dataTransfer.files).filter(f => /\.(epub|docx|pdf)$/i.test(f.name));
    if (dropped.length) setFiles(prev => [...prev, ...dropped]);
  };

  const handleUpload = async () => {
    if (!files.length) return;
    setUploading(true);
    setResult(null);
    const token = localStorage.getItem("access_token");
    try {
      const formData = new FormData();
      files.forEach(f => formData.append("files", f));
      const res = await fetch("/api/books/upload", {
        method: "POST",
        headers: token ? { Authorization: `Bearer ${token}` } : {},
        body: formData,
      });
      const data = await res.json();
      if (res.ok) {
        setResult({ success: true, message: data.message, gaNumber: data.ga_number, chapters: data.chapters });
        setFiles([]);
      } else {
        setResult({ success: false, message: data.detail || "上传失败" });
      }
    } catch {
      setResult({ success: false, message: "网络错误" });
    } finally {
      setUploading(false);
    }
  };

  return (
    <div>
      <p className="text-gray-500 text-sm mb-4">上传 EPUB、DOCX 或 PDF，自动解析章节段落结构。</p>
      <div
        onDragOver={e => e.preventDefault()}
        onDrop={handleDrop}
        onClick={() => fileInputRef.current?.click()}
        className="border-2 border-dashed border-gray-200 rounded-xl p-12 text-center hover:border-indigo-300 hover:bg-indigo-50/20 transition-all cursor-pointer mb-6"
      >
        <p className="text-sm text-gray-500">拖拽文件或 <span className="text-indigo-500 font-medium">点击选择</span></p>
        <p className="text-xs text-gray-400 mt-1">EPUB · DOCX · PDF</p>
        <input ref={fileInputRef} type="file" accept=".epub,.docx,.pdf" multiple onChange={e => { if (e.target.files) setFiles(prev => [...prev, ...Array.from(e.target.files!)]); }} className="hidden" />
      </div>
      {files.length > 0 && (
        <div className="bg-white rounded-xl shadow-sm border border-gray-100 p-4 mb-6">
          <h3 className="text-sm font-medium text-gray-700 mb-3">已选择 {files.length} 个文件</h3>
          {files.map((f, i) => (
            <div key={i} className="flex items-center justify-between py-2 border-b border-gray-50">
              <span className="text-sm text-gray-700 truncate">{f.name}</span>
              <span className="text-xs text-gray-400">{(f.size / 1024).toFixed(0)} KB</span>
              <button onClick={() => setFiles(prev => prev.filter((_, j) => j !== i))} className="text-xs text-red-400 hover:text-red-600 ml-2">移除</button>
            </div>
          ))}
          <button onClick={handleUpload} disabled={uploading} className="btn-primary mt-4 w-full">
            {uploading ? "上传解析中..." : `上传 ${files.length} 个文件`}
          </button>
        </div>
      )}
      {result && (
        <div className={`rounded-xl p-5 ${result.success ? "bg-green-50 border border-green-100" : "bg-red-50 border border-red-100"}`}>
          <p className={`text-sm font-medium ${result.success ? "text-green-700" : "text-red-700"}`}>{result.success ? "上传成功" : "上传失败"}</p>
          <p className="text-sm text-gray-500 mt-1">{result.message}</p>
          {result.gaNumber && <p className="text-xs text-gray-400 mt-0.5">{result.gaNumber} · {result.chapters} 章节</p>}
        </div>
      )}
    </div>
  );
}

function TranslationFixesTab() {
  const [fixes, setFixes] = useState<Array<{id:number;pattern:string;replacement:string;enabled:boolean}>>([]);
  const [loading, setLoading] = useState(true);
  const [msg, setMsg] = useState("");
  const [editing, setEditing] = useState<number | null>(null);
  const [editPat, setEditPat] = useState("");
  const [editRep, setEditRep] = useState("");
  const [newPat, setNewPat] = useState("");
  const [newRep, setNewRep] = useState("");

  const load = () => {
    fetch("/api/admin/translation-fixes", { headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` } })
      .then(r => r.json()).then(setFixes).finally(() => setLoading(false));
  };
  useEffect(load, []);

  const addFix = async () => {
    if (!newPat || !newRep) return;
    await fetch("/api/admin/translation-fixes", { method: "POST", headers: { "Content-Type": "application/json", Authorization: `Bearer ${localStorage.getItem("access_token")}` }, body: JSON.stringify({ pattern: newPat, replacement: newRep, enabled: true }) });
    setNewPat(""); setNewRep(""); load(); setMsg("已添加");
  };

  const updateFix = async (id: number) => {
    await fetch(`/api/admin/translation-fixes/${id}`, { method: "PUT", headers: { "Content-Type": "application/json", Authorization: `Bearer ${localStorage.getItem("access_token")}` }, body: JSON.stringify({ pattern: editPat, replacement: editRep, enabled: true }) });
    setEditing(null); load(); setMsg("已保存");
  };

  const deleteFix = async (id: number) => {
    await fetch(`/api/admin/translation-fixes/${id}`, { method: "DELETE", headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` } });
    load(); setMsg("已删除");
  };

  const applyAll = async () => {
    setMsg("正在应用...");
    const res = await fetch("/api/admin/translation-fixes/apply-all", { method: "POST", headers: { Authorization: `Bearer ${localStorage.getItem("access_token")}` } });
    const d = await res.json();
    setMsg(d.message || "完成");
  };

  if (loading) return <div className="text-center py-8 text-gray-400">加载中...</div>;

  return (
    <div>
      {msg && <div className="mb-4 p-2 bg-green-50 text-green-700 rounded text-sm">{msg}</div>}
      <div className="mb-4 bg-white rounded-xl shadow-sm border border-gray-100 p-4 flex gap-2 items-end">
        <div className="flex-1"><label className="text-xs text-gray-500">匹配</label><input value={newPat} onChange={e => setNewPat(e.target.value)} className="w-full px-2 py-1.5 border rounded text-sm" /></div>
        <div className="flex-1"><label className="text-xs text-gray-500">替换</label><input value={newRep} onChange={e => setNewRep(e.target.value)} className="w-full px-2 py-1.5 border rounded text-sm" /></div>
        <button onClick={addFix} className="px-3 py-1.5 bg-blue-600 text-white text-sm rounded hover:bg-blue-700">添加</button>
      </div>
      <div className="mb-4"><button onClick={applyAll} className="px-4 py-2 bg-emerald-600 text-white text-sm rounded-lg hover:bg-emerald-700">应用到全部现有翻译</button></div>
      <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50"><tr><th className="px-4 py-2 text-left text-xs text-gray-500">匹配</th><th className="px-4 py-2 text-left text-xs text-gray-500">替换</th><th className="px-4 py-2 text-left text-xs text-gray-500 w-20">状态</th><th className="px-4 py-2 text-left text-xs text-gray-500 w-24">操作</th></tr></thead>
          <tbody className="divide-y divide-gray-100">
            {fixes.map(f => (
              <tr key={f.id} className="hover:bg-gray-50">
                {editing === f.id ? (
                  <><td className="px-4 py-2"><input value={editPat} onChange={e => setEditPat(e.target.value)} className="w-full px-2 py-1 border rounded text-sm" /></td>
                  <td className="px-4 py-2"><input value={editRep} onChange={e => setEditRep(e.target.value)} className="w-full px-2 py-1 border rounded text-sm" /></td>
                  <td className="px-4 py-2 text-xs"><span className="text-yellow-600">编辑中</span></td>
                  <td className="px-4 py-2 flex gap-1"><button onClick={() => updateFix(f.id)} className="px-2 py-1 bg-green-600 text-white text-xs rounded">保存</button><button onClick={() => setEditing(null)} className="px-2 py-1 text-gray-500 text-xs">取消</button></td></>
                ) : (
                  <><td className="px-4 py-2 text-sm text-gray-700 font-mono">{f.pattern}</td>
                  <td className="px-4 py-2 text-sm text-gray-600">{f.replacement}</td>
                  <td className="px-4 py-2 text-xs">{f.enabled ? <span className="text-green-600">启用</span> : <span className="text-gray-400">禁用</span>}</td>
                  <td className="px-4 py-2 flex gap-1"><button onClick={() => { setEditing(f.id); setEditPat(f.pattern); setEditRep(f.replacement); }} className="px-2 py-1 bg-blue-600 text-white text-xs rounded">编辑</button><button onClick={() => deleteFix(f.id)} className="px-2 py-1 bg-red-600 text-white text-xs rounded">删除</button></td></>
                )}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

function BooksManageTab() {
  const [books, setBooks] = useState<Array<{id:number;ga_number:string;title_de:string;title_zh:string|null;created_at:string}>>([]);
  const [loading, setLoading] = useState(false);
  const [search, setSearch] = useState("");
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(false);
  const [lectures, setLectures] = useState<Array<{id:number;title_de:string;title_zh:string|null;order_index:number}>>([]);
  const [selectedBook, setSelectedBook] = useState<{id:number;ga_number:string}|null>(null);
  const [msg, setMsg] = useState("");
  const [editingBook, setEditingBook] = useState<number|null>(null);
  const [editingLec, setEditingLec] = useState<number|null>(null);
  const [editDe, setEditDe] = useState("");
  const [editZh, setEditZh] = useState("");

  const loadBooks = (p: number, s: string) => {
    setLoading(true);
    const qs = new URLSearchParams({page:String(p),page_size:"20",sort_by:"created_at",sort_dir:"desc"});
    if(s) qs.set("search", s);
    fetch("/api/books/summary?"+qs).then(r=>r.json()).then(data=>{setBooks(data);setHasMore(data.length===20);}).finally(()=>setLoading(false));
  };

  useEffect(()=>{loadBooks(1,"");},[]);

  const doSearch = () => { setPage(1); loadBooks(1, search); };

  const loadLectures = (bookId: number, ga: string) => { setSelectedBook({id:bookId,ga_number:ga}); fetch("/api/books/"+bookId).then(r=>r.json()).then(d=>setLectures(d.lectures||[])); };

  const saveBookTitle = async (bookId: number) => { const t=localStorage.getItem("access_token"); await fetch("/api/admin/books/"+bookId+"/titles",{method:"PUT",headers:{"Content-Type":"application/json","Authorization":"Bearer "+t},body:JSON.stringify({title_de:editDe,title_zh:editZh})}); setEditingBook(null); loadBooks(page,search); setMsg("已保存"); };

  const saveLecTitle = async (lecId: number) => { const t=localStorage.getItem("access_token"); await fetch("/api/admin/lectures/"+lecId+"/titles",{method:"PUT",headers:{"Content-Type":"application/json","Authorization":"Bearer "+t},body:JSON.stringify({title_de:editDe,title_zh:editZh})}); setEditingLec(null); if(selectedBook) loadLectures(selectedBook.id,selectedBook.ga_number); setMsg("已保存"); };

  return (<div>
    {msg&&<div className="mb-4 p-2 bg-green-50 text-green-700 rounded text-sm">{msg}</div>}
    <div className="flex gap-4"><div className="w-1/2"><div className="flex gap-2 mb-2">
      <input value={search} onChange={e=>setSearch(e.target.value)} onKeyDown={e=>e.key==="Enter"&&doSearch()} placeholder="搜索 GA号/书名..." className="flex-1 px-2 py-1.5 border rounded text-sm"/>
      <button onClick={doSearch} className="px-3 py-1.5 bg-blue-600 text-white text-sm rounded">搜索</button>
    </div>
    <div className="bg-white rounded-xl shadow-sm border border-gray-100 max-h-96 overflow-y-auto">
      {loading?<div className="text-center py-8 text-gray-400">加载中...</div>:books.length===0?<div className="text-center py-8 text-gray-400">无结果</div>:
      books.map(b=>(<div key={b.id} className={"px-4 py-2 border-b border-gray-50 cursor-pointer hover:bg-gray-50 "+(selectedBook&&selectedBook.id===b.id?"bg-blue-50":"")} onClick={()=>loadLectures(b.id,b.ga_number)}>
        {editingBook===b.id ? (<div className="flex gap-2" onClick={e=>e.stopPropagation()}><input value={editDe} onChange={e=>setEditDe(e.target.value)} className="flex-1 px-2 py-1 border rounded text-sm"/><input value={editZh} onChange={e=>setEditZh(e.target.value)} className="flex-1 px-2 py-1 border rounded text-sm"/><button onClick={()=>saveBookTitle(b.id)} className="px-2 py-1 bg-green-600 text-white text-xs rounded">保存</button><button onClick={()=>setEditingBook(null)} className="px-2 py-1 text-gray-500 text-xs">取消</button></div>):
        (<div><div className="text-xs text-gray-400">{b.ga_number}</div><div className="text-sm text-gray-800 truncate">{b.title_zh||b.title_de}</div><div className="text-xs text-gray-400 truncate">{b.title_de}</div><button onClick={e=>{e.stopPropagation();setEditingBook(b.id);setEditDe(b.title_de);setEditZh(b.title_zh||"")}} className="text-xs text-blue-500 mt-1">编辑标题</button></div>)}
      </div>))}
    </div>
    <div className="flex justify-center gap-2 mt-2">{page>1&&<button onClick={()=>{const np=page-1;setPage(np);loadBooks(np,search);}} className="px-3 py-1 text-sm bg-gray-100 rounded hover:bg-gray-200">上一页</button>}{hasMore&&<button onClick={()=>{const np=page+1;setPage(np);loadBooks(np,search);}} className="px-3 py-1 text-sm bg-gray-100 rounded hover:bg-gray-200">下一页</button>}</div>
    </div><div className="w-1/2"><h3 className="text-sm font-medium text-gray-700 mb-2">{selectedBook?selectedBook.ga_number+" 章节":"选择书籍查看章节"}</h3><div className="bg-white rounded-xl shadow-sm border border-gray-100 max-h-96 overflow-y-auto">
      {lectures.map(l=>(<div key={l.id} className="px-4 py-2 border-b border-gray-50">
        {editingLec===l.id ? (<div className="flex gap-2"><input value={editDe} onChange={e=>setEditDe(e.target.value)} className="flex-1 px-2 py-1 border rounded text-sm"/><input value={editZh} onChange={e=>setEditZh(e.target.value)} className="flex-1 px-2 py-1 border rounded text-sm"/><button onClick={()=>saveLecTitle(l.id)} className="px-2 py-1 bg-green-600 text-white text-xs rounded">保存</button><button onClick={()=>setEditingLec(null)} className="px-2 py-1 text-gray-500 text-xs">取消</button></div>):
        (<div><div className="text-sm text-gray-800">{l.title_zh||l.title_de}</div><div className="text-xs text-gray-400">{l.title_de}</div><button onClick={()=>{setEditingLec(l.id);setEditDe(l.title_de);setEditZh(l.title_zh||"")}} className="text-xs text-blue-500 mt-1">编辑</button></div>)}
      </div>))}
    </div></div></div>
  </div>);
}
