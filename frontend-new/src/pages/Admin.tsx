import { useState, useEffect, useMemo, useRef } from 'react';
import { Link } from 'react-router-dom';
import { ArrowLeft, Users, Settings, CreditCard, BookPlus } from 'lucide-react';
import { useStore } from '../hooks/useStore';
import { api } from '../lib/api';
import type { User, CreditSetting } from '../types';

export default function Admin() {
  const { user } = useStore();
  const [activeTab, setActiveTab] = useState<'users' | 'settings' | 'recharge' | 'upload'>('users');

  if (!user || user.is_admin !== 1) {
    return (
      <div className="min-h-screen pt-6 pb-16 flex items-center justify-center">
        <div className="text-center">
          <p className="text-gray-500 text-lg mb-4">没有权限访问此页面</p>
          <Link
            to="/"
            className="inline-flex items-center gap-2 px-6 py-3 bg-[#1e3a8a] text-white rounded-xl hover:bg-[#1e3a8a]/90 transition-colors"
          >
            返回首页
          </Link>
        </div>
      </div>
    );
  }

  const tabs = [
    { key: 'users' as const, label: '用户管理', icon: Users },
    { key: 'settings' as const, label: '积分设置', icon: Settings },
    { key: 'recharge' as const, label: '充值审核', icon: CreditCard },
    { key: 'upload' as const, label: '上传书籍', icon: BookPlus },
  ];

  return (
    <div className="min-h-screen pt-6 pb-16">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link
          to="/"
          className="inline-flex items-center gap-2 text-gray-600 hover:text-[#1e3a8a] transition-colors mb-8"
        >
          <ArrowLeft className="h-4 w-4" />
          返回
        </Link>

        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-2 font-display">
            管理后台
          </h1>
          <p className="text-gray-600">管理用户、积分和系统设置</p>
        </div>

        <div className="flex gap-1 border-b border-gray-200 mb-6">
          {tabs.map((tab) => {
            const Icon = tab.icon;
            return (
              <button
                key={tab.key}
                onClick={() => setActiveTab(tab.key)}
                className={`flex items-center gap-2 px-5 py-3 text-sm font-medium rounded-t-lg transition-all ${
                  activeTab === tab.key
                    ? 'bg-white text-[#1e3a8a] border border-b-white border-gray-200 -mb-px'
                    : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50'
                }`}
              >
                <Icon className="h-4 w-4" />
                {tab.label}
              </button>
            );
          })}
        </div>

        {activeTab === 'users' && <UsersTab currentUserId={user.id} />}
        {activeTab === 'settings' && <CreditSettingsTab />}
        {activeTab === 'recharge' && <RechargeReviewTab />}
        {activeTab === 'upload' && <UploadTab />}
      </div>
    </div>
  );
}

function UsersTab({ currentUserId }: { currentUserId: number }) {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [search, setSearch] = useState('');
  const [editUserId, setEditUserId] = useState<number | null>(null);
  const [newCredits, setNewCredits] = useState('');
  const [addCreditsValue, setAddCreditsValue] = useState('');
  const [editModal, setEditModal] = useState<User | null>(null);
  const [editUsername, setEditUsername] = useState('');
  const [editEmail, setEditEmail] = useState('');
  const [resetModal, setResetModal] = useState<User | null>(null);
  const [newPassword, setNewPassword] = useState('');

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const token = localStorage.getItem('steiner_token');
      const res = await fetch('/api/admin/users', {
        headers: { Authorization: `Bearer ${token}` },
      });
      if (res.status === 403) {
        setError('需要管理员权限');
        return;
      }
      if (!res.ok) throw new Error('获取用户列表失败');
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
      (u) => u.username.toLowerCase().includes(q) || u.email.toLowerCase().includes(q)
    );
  }, [users, search]);

  const handleSetCredits = async (userId: number) => {
    if (!newCredits || isNaN(parseInt(newCredits))) {
      setError('请输入有效的点数');
      return;
    }
    try {
      const token = localStorage.getItem('steiner_token');
      const res = await fetch(`/api/admin/users/${userId}/credits`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ credits: parseInt(newCredits) }),
      });
      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.detail || '设置点数失败');
      }
      const data = await res.json();
      setSuccess(`已将 ${data.username} 的点数设置为 ${data.new_credits}`);
      setEditUserId(null);
      setNewCredits('');
      fetchUsers();
    } catch (err: any) {
      setError(err.message);
    }
  };

  const handleAddCredits = async (userId: number) => {
    if (!addCreditsValue || isNaN(parseInt(addCreditsValue))) {
      setError('请输入有效的点数');
      return;
    }
    try {
      const data = await api.adminAddCredits(userId, parseInt(addCreditsValue));
      setSuccess(`已为 ${data.username} 添加 ${data.added} 点，当前总额: ${data.new_credits}`);
      setAddCreditsValue('');
      fetchUsers();
    } catch (err: any) {
      setError(err.message);
    }
  };

  const openEditModal = (user: User) => {
    setEditModal(user);
    setEditUsername(user.username);
    setEditEmail(user.email);
  };

  const handleUpdateUser = async () => {
    if (!editModal) return;
    try {
      const data = await api.adminUpdateUser(editModal.id, {
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
    setResetModal(user);
    setNewPassword('');
  };

  const handleResetPassword = async () => {
    if (!resetModal) return;
    if (newPassword.length < 6) {
      setError('密码至少 6 个字符');
      return;
    }
    try {
      const data = await api.adminResetPassword(resetModal.id, newPassword);
      setSuccess(data.message);
      setResetModal(null);
      setNewPassword('');
    } catch (err: any) {
      setError(err.message);
    }
  };

  const handleToggleAdmin = async (userId: number, username: string, currentIsAdmin: number) => {
    const action = currentIsAdmin ? '取消管理员权限' : '设为管理员';
    if (!window.confirm(`确定要${action}用户 "${username}" 吗？`)) return;
    try {
      const token = localStorage.getItem('steiner_token');
      const res = await fetch(`/api/admin/users/${userId}/toggle-admin`, {
        method: 'PUT',
        headers: { Authorization: `Bearer ${token}` },
      });
      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.detail || '操作失败');
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
      const token = localStorage.getItem('steiner_token');
      const res = await fetch(`/api/admin/users/${userId}`, {
        method: 'DELETE',
        headers: { Authorization: `Bearer ${token}` },
      });
      if (!res.ok) {
        const data = await res.json();
        throw new Error(data.detail || '删除失败');
      }
      const data = await res.json();
      setSuccess(data.message || '用户已删除');
      fetchUsers();
    } catch (err: any) {
      setError(err.message);
    }
  };

  if (loading) {
    return (
      <div className="text-center py-12 text-gray-400">加载中...</div>
    );
  }

  return (
    <>
      <div className="mb-4">
        <p className="text-gray-500 text-sm">管理用户账户和点数</p>
      </div>

      {error && (
        <div className="mb-4 p-3 bg-red-50 text-red-700 rounded-lg">
          {error}
          <button onClick={() => setError('')} className="float-right text-red-500 hover:text-red-700">&times;</button>
        </div>
      )}

      {success && (
        <div className="mb-4 p-3 bg-green-50 text-green-700 rounded-lg">
          {success}
          <button onClick={() => setSuccess('')} className="float-right text-green-500 hover:text-green-700">&times;</button>
        </div>
      )}

      <div className="mb-4">
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          placeholder="搜索用户名或邮箱..."
          className="w-full max-w-sm px-4 py-2 border border-gray-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent bg-white"
        />
        {search && (
          <span className="ml-2 text-sm text-gray-500">
            找到 {filteredUsers.length} 个用户
          </span>
        )}
      </div>

      <div className="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
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
            {filteredUsers.map((u) => {
              const isCurrentUser = currentUserId === u.id;
              return (
                <tr key={u.id} className={`hover:bg-gray-50 ${isCurrentUser ? 'bg-[#1e3a8a]/5' : ''}`}>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <div className="text-sm font-medium text-gray-900">
                      {u.username}
                      {isCurrentUser && (
                        <span className="ml-2 inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-[#1e3a8a]/10 text-[#1e3a8a]">
                          当前用户
                        </span>
                      )}
                    </div>
                    <div className="text-sm text-gray-500">ID: {u.id}</div>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {u.email}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    {editUserId === u.id ? (
                      <div className="flex items-center gap-2">
                        <input
                          type="number"
                          value={newCredits}
                          onChange={(e) => setNewCredits(e.target.value)}
                          className="w-20 px-2 py-1 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-[#1e3a8a]"
                          placeholder="点数"
                        />
                        <button
                          onClick={() => handleSetCredits(u.id)}
                          className="px-2 py-1 bg-[#1e3a8a] text-white text-xs rounded-lg hover:bg-[#1e3a8a]/90"
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
                        <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-[#d4a574]/10 text-[#d4a574]">
                          {u.credits} 点
                        </span>
                        <button
                          onClick={() => {
                            setEditUserId(u.id);
                            setNewCredits(u.credits.toString());
                          }}
                          className="text-[#1e3a8a] hover:text-[#1e3a8a]/80 text-sm"
                        >
                          修改
                        </button>
                      </div>
                    )}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <div className="flex items-center gap-2">
                      {u.is_admin ? (
                        <>
                          <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-50 text-purple-700">
                            管理员
                          </span>
                          <button
                            onClick={() => handleToggleAdmin(u.id, u.username, u.is_admin!)}
                            className="px-2 py-1 bg-green-600 text-white text-xs rounded-lg hover:bg-green-700"
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
                            onClick={() => handleToggleAdmin(u.id, u.username, u.is_admin!)}
                            className="px-2 py-1 bg-purple-600 text-white text-xs rounded-lg hover:bg-purple-700"
                          >
                            设为管理员
                          </button>
                        </>
                      )}
                    </div>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                    {u.created_at ? new Date(u.created_at).toLocaleDateString('zh-CN') : '-'}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-sm">
                    <div className="flex flex-wrap items-center gap-2">
                      <input
                        type="number"
                        value={addCreditsValue}
                        onChange={(e) => setAddCreditsValue(e.target.value)}
                        className="w-16 px-2 py-1 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-[#1e3a8a]"
                        placeholder="添加"
                      />
                      <button
                        onClick={() => handleAddCredits(u.id)}
                        className="px-2 py-1 bg-green-600 text-white text-xs rounded-lg hover:bg-green-700"
                      >
                        充值
                      </button>
                      <button
                        onClick={() => openEditModal(u)}
                        className="px-2 py-1 bg-[#1e3a8a] text-white text-xs rounded-lg hover:bg-[#1e3a8a]/90"
                      >
                        编辑
                      </button>
                      <button
                        onClick={() => openResetModal(u)}
                        className="px-2 py-1 bg-orange-600 text-white text-xs rounded-lg hover:bg-orange-700"
                      >
                        重置密码
                      </button>
                      {isCurrentUser ? (
                        <span className="px-2 py-1 text-gray-400 text-xs">当前用户</span>
                      ) : (
                        <button
                          onClick={() => handleDeleteUser(u.id, u.username)}
                          className="px-2 py-1 bg-red-600 text-white text-xs rounded-lg hover:bg-red-700"
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
        共 {users.length} 个用户{search ? ` (显示 ${filteredUsers.length} 个)` : ''}
      </div>

      {editModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
          <div className="bg-white rounded-2xl shadow-lg p-6 w-full max-w-md mx-4">
            <h2 className="text-lg font-bold text-gray-900 mb-4">编辑用户: {editModal.username}</h2>
            <div className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">用户名</label>
                <input
                  type="text"
                  value={editUsername}
                  onChange={(e) => setEditUsername(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">邮箱</label>
                <input
                  type="email"
                  value={editEmail}
                  onChange={(e) => setEditEmail(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent"
                />
              </div>
            </div>
            <div className="flex justify-end gap-3 mt-6">
              <button
                onClick={() => setEditModal(null)}
                className="px-4 py-2 text-sm text-gray-700 bg-gray-100 rounded-xl hover:bg-gray-200"
              >
                取消
              </button>
              <button
                onClick={handleUpdateUser}
                className="px-4 py-2 text-sm text-white bg-[#1e3a8a] rounded-xl hover:bg-[#1e3a8a]/90"
              >
                保存
              </button>
            </div>
          </div>
        </div>
      )}

      {resetModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50">
          <div className="bg-white rounded-2xl shadow-lg p-6 w-full max-w-md mx-4">
            <h2 className="text-lg font-bold text-gray-900 mb-4">重置密码: {resetModal.username}</h2>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">新密码</label>
              <input
                type="password"
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                placeholder="至少 6 个字符"
                className="w-full px-3 py-2 border border-gray-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent"
              />
            </div>
            <div className="flex justify-end gap-3 mt-6">
              <button
                onClick={() => setResetModal(null)}
                className="px-4 py-2 text-sm text-gray-700 bg-gray-100 rounded-xl hover:bg-gray-200"
              >
                取消
              </button>
              <button
                onClick={handleResetPassword}
                className="px-4 py-2 text-sm text-white bg-orange-600 rounded-xl hover:bg-orange-700"
              >
                确认重置
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

function CreditSettingsTab() {
  const [settings, setSettings] = useState<CreditSetting[]>([]);
  const [loading, setLoading] = useState(true);
  const [editingKey, setEditingKey] = useState<string | null>(null);
  const [editValue, setEditValue] = useState('');
  const [msg, setMsg] = useState('');

  const LABELS: Record<string, string> = {
    translate_coefficient: '翻译系数 (每句×系数)',
    edit_translation_coefficient: '编辑译文系数 (每句×系数)',
    edit_source_coefficient: '编辑原文系数 (每句×系数)',
    download_lecture_price: '单章下载 (0=免费)',
    download_book_price: '全书下载 (0=免费)',
  };

  useEffect(() => {
    loadSettings();
  }, []);

  const loadSettings = async () => {
    setLoading(true);
    try {
      const data = await api.fetchCreditSettings();
      setSettings(data);
    } catch (err: any) {
      setMsg(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleSave = async (key: string) => {
    const val = parseInt(editValue, 10);
    if (isNaN(val) || val < 0) {
      setMsg('请输入有效数字');
      return;
    }
    try {
      await api.updateCreditSetting(key, val);
      setEditingKey(null);
      setMsg('保存成功');
      loadSettings();
    } catch {
      setMsg('保存失败');
    }
  };

  if (loading) {
    return <div className="text-center py-12 text-gray-400">加载中...</div>;
  }

  return (
    <div>
      <p className="text-gray-500 text-sm mb-4">配置各项点数消耗价格</p>
      {msg && (
        <div className="mb-4 p-2 bg-green-50 text-green-700 rounded-lg text-sm">
          {msg}
          <button onClick={() => setMsg('')} className="float-right">&times;</button>
        </div>
      )}
      <div className="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
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
                <td className="px-6 py-4 text-sm text-gray-500">{LABELS[s.key] || s.description}</td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span className="text-sm font-mono text-gray-700">{s.value}</span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  {editingKey === s.key ? (
                    <div className="flex items-center gap-2">
                      <input
                        type="number"
                        value={editValue}
                        onChange={(e) => setEditValue(e.target.value)}
                        className="w-20 px-2 py-1 border border-gray-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-[#1e3a8a]"
                      />
                      <button onClick={() => handleSave(s.key)} className="px-2 py-1 bg-[#1e3a8a] text-white text-xs rounded-lg hover:bg-[#1e3a8a]/90">保存</button>
                      <button onClick={() => setEditingKey(null)} className="px-2 py-1 text-gray-500 text-xs">取消</button>
                    </div>
                  ) : (
                    <button
                      onClick={() => { setEditingKey(s.key); setEditValue(String(s.value)); }}
                      className="text-[#1e3a8a] hover:text-[#1e3a8a]/80 text-sm"
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
    id: number; user_id: number; username: string; amount: number;
    payment_image: string | null; status: string; admin_note: string | null;
    created_at: string; updated_at: string | null;
  }>>([]);
  const [loading, setLoading] = useState(true);
  const [qrUploading, setQrUploading] = useState(false);
  const [reviewMsg, setReviewMsg] = useState('');

  useEffect(() => {
    loadRequests();
  }, []);

  const loadRequests = () => {
    const token = localStorage.getItem('steiner_token');
    fetch('/api/recharge/admin/pending-requests', {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((r) => r.json())
      .then(setRequests)
      .catch(() => {})
      .finally(() => setLoading(false));
  };

  const handleReview = async (id: number, status: string, note: string) => {
    const token = localStorage.getItem('steiner_token');
    const res = await fetch(`/api/recharge/admin/review/${id}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
      body: JSON.stringify({ status, admin_note: note }),
    });
    const data = await res.json();
    setReviewMsg(data.message || '');
    loadRequests();
  };

  const handleQrUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    setQrUploading(true);
    const token = localStorage.getItem('steiner_token');
    const formData = new FormData();
    formData.append('qr_image', file);
    await fetch('/api/recharge/admin/upload-qr', {
      method: 'POST',
      headers: { Authorization: `Bearer ${token}` },
      body: formData,
    });
    setQrUploading(false);
    setReviewMsg('收款码已上传');
  };

  const statusBadge = (s: string) => {
    const c = s === 'pending' ? 'bg-yellow-50 text-yellow-700' :
              s === 'approved' ? 'bg-green-50 text-green-700' : 'bg-red-50 text-red-700';
    const t = s === 'pending' ? '待审核' : s === 'approved' ? '已通过' : '已拒绝';
    return <span className={`px-2 py-0.5 rounded text-xs font-medium ${c}`}>{t}</span>;
  };

  if (loading) return <div className="text-center py-12 text-gray-400">加载中...</div>;

  return (
    <div>
      {reviewMsg && (
        <div className="mb-4 p-2 bg-green-50 text-green-700 rounded-lg text-sm">
          {reviewMsg}
          <button onClick={() => setReviewMsg('')} className="float-right">&times;</button>
        </div>
      )}

      <div className="mb-6 bg-white rounded-2xl shadow-sm border border-gray-100 p-5">
        <h3 className="text-sm font-medium text-gray-800 mb-3">收款码管理</h3>
        <div className="flex items-center gap-4">
          <img
            src="/api/recharge/payment-qr"
            alt="收款码"
            className="w-24 h-24 object-contain border rounded-lg"
            onError={(e) => { (e.target as HTMLImageElement).style.display = 'none'; }}
          />
          <label className="cursor-pointer px-4 py-2 bg-[#1e3a8a] text-white text-sm rounded-xl hover:bg-[#1e3a8a]/90">
            {qrUploading ? '上传中...' : '上传收款码'}
            <input type="file" accept="image/*" onChange={handleQrUpload} className="hidden" />
          </label>
        </div>
      </div>

      <div className="bg-white rounded-2xl shadow-sm border border-gray-100 overflow-hidden">
        <table className="w-full">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">用户</th>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">金额</th>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">凭证</th>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">状态</th>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">时间</th>
              <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">操作</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-100">
            {requests.map((r) => (
              <tr key={r.id} className="hover:bg-gray-50">
                <td className="px-4 py-3 text-sm">{r.username}</td>
                <td className="px-4 py-3 text-sm font-medium">{r.amount} 点</td>
                <td className="px-4 py-3">
                  {r.payment_image ? (
                    <a href={`/api/recharge/payment-proof/${r.payment_image}`} target="_blank" rel="noreferrer"
                       className="text-[#1e3a8a] text-xs hover:underline">查看凭证</a>
                  ) : <span className="text-gray-300 text-xs">-</span>}
                </td>
                <td className="px-4 py-3">{statusBadge(r.status)}</td>
                <td className="px-4 py-3 text-xs text-gray-400">{new Date(r.created_at).toLocaleDateString('zh-CN')}</td>
                <td className="px-4 py-3">
                  {r.status === 'pending' ? (
                    <div className="flex gap-2">
                      <button onClick={() => handleReview(r.id, 'approved', '')}
                              className="px-2 py-1 bg-green-600 text-white text-xs rounded-lg hover:bg-green-700">批准</button>
                      <button onClick={() => handleReview(r.id, 'rejected', '')}
                              className="px-2 py-1 bg-red-600 text-white text-xs rounded-lg hover:bg-red-700">拒绝</button>
                    </div>
                  ) : (
                    <span className="text-xs text-gray-400">{r.admin_note || '-'}</span>
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
    const dropped = Array.from(e.dataTransfer.files).filter((f) => /\.(epub|docx|pdf)$/i.test(f.name));
    if (dropped.length) setFiles((prev) => [...prev, ...dropped]);
  };

  const handleUpload = async () => {
    if (!files.length) return;
    setUploading(true);
    setResult(null);
    const token = localStorage.getItem('steiner_token');
    try {
      const formData = new FormData();
      files.forEach((f) => formData.append('files', f));
      const res = await fetch('/api/books/upload', {
        method: 'POST',
        headers: token ? { Authorization: `Bearer ${token}` } : {},
        body: formData,
      });
      const data = await res.json();
      if (res.ok) {
        setResult({ success: true, message: data.message, gaNumber: data.ga_number, chapters: data.chapters });
        setFiles([]);
      } else {
        setResult({ success: false, message: data.detail || '上传失败' });
      }
    } catch {
      setResult({ success: false, message: '网络错误' });
    } finally {
      setUploading(false);
    }
  };

  return (
    <div>
      <p className="text-gray-500 text-sm mb-4">上传 EPUB、DOCX 或 PDF，自动解析章节段落结构。</p>
      <div
        onDragOver={(e) => e.preventDefault()}
        onDrop={handleDrop}
        onClick={() => fileInputRef.current?.click()}
        className="border-2 border-dashed border-gray-200 rounded-2xl p-12 text-center hover:border-[#1e3a8a]/30 hover:bg-[#1e3a8a]/5 transition-all cursor-pointer mb-6"
      >
        <p className="text-sm text-gray-500">拖拽文件或 <span className="text-[#1e3a8a] font-medium">点击选择</span></p>
        <p className="text-xs text-gray-400 mt-1">EPUB · DOCX · PDF</p>
        <input ref={fileInputRef} type="file" accept=".epub,.docx,.pdf" multiple onChange={(e) => { if (e.target.files) setFiles((prev) => [...prev, ...Array.from(e.target.files!)]); }} className="hidden" />
      </div>
      {files.length > 0 && (
        <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-4 mb-6">
          <h3 className="text-sm font-medium text-gray-700 mb-3">已选择 {files.length} 个文件</h3>
          {files.map((f, i) => (
            <div key={i} className="flex items-center justify-between py-2 border-b border-gray-50 last:border-0">
              <span className="text-sm text-gray-700 truncate">{f.name}</span>
              <span className="text-xs text-gray-400">{(f.size / 1024).toFixed(0)} KB</span>
              <button onClick={() => setFiles((prev) => prev.filter((_, j) => j !== i))} className="text-xs text-red-400 hover:text-red-600 ml-2">移除</button>
            </div>
          ))}
          <button onClick={handleUpload} disabled={uploading} className="w-full mt-4 py-3 bg-[#1e3a8a] text-white rounded-xl font-medium hover:bg-[#1e3a8a]/90 transition-colors disabled:opacity-50 disabled:cursor-not-allowed">
            {uploading ? '上传解析中...' : `上传 ${files.length} 个文件`}
          </button>
        </div>
      )}
      {result && (
        <div className={`rounded-2xl p-5 ${result.success ? 'bg-green-50 border border-green-100' : 'bg-red-50 border border-red-100'}`}>
          <p className={`text-sm font-medium ${result.success ? 'text-green-700' : 'text-red-700'}`}>{result.success ? '上传成功' : '上传失败'}</p>
          <p className="text-sm text-gray-500 mt-1">{result.message}</p>
          {result.gaNumber && <p className="text-xs text-gray-400 mt-0.5">{result.gaNumber} · {result.chapters} 章节</p>}
        </div>
      )}
    </div>
  );
}
