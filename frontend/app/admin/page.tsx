"use client";

import { useState, useEffect, useMemo } from "react";
import { useRouter } from "next/navigation";
import { adminAddCredits, adminUpdateUser, adminResetPassword } from "@/lib/api";

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
  const [editEmail, setEditEmail] = useState("");

  // Reset password modal state
  const [resetModal, setResetModal] = useState<{ user: User } | null>(null);
  const [newPassword, setNewPassword] = useState("");

  const token = typeof window !== "undefined" ? localStorage.getItem("steiner_token") : null;

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
      setSuccess(data.message);
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
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">用户管理</h1>
        <p className="text-gray-500 mt-1">管理用户账户和点数</p>
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
    </div>
  );
}
