import { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { BookOpen, User, Menu, X, Coins, Shield, Upload, LogOut } from 'lucide-react';
import { useStore } from '../hooks/useStore';
import { api, clearAuth, getStoredUser } from '../lib/api';

export default function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const { user, setUser, clearUser } = useStore();
  const location = useLocation();

  useEffect(() => {
    const stored = getStoredUser();
    if (stored) {
      setUser(stored);
      api.fetchMe().then(u => {
        setUser(u);
      }).catch(() => {
        clearAuth();
        clearUser();
      });
    }
  }, [setUser, clearUser]);

  useEffect(() => {
    setIsMenuOpen(false);
  }, [location.pathname]);

  const handleLogout = () => {
    clearAuth();
    clearUser();
  };

  const navLink = (to: string, label: string, icon?: React.ReactNode) => (
    <Link
      to={to}
      className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-sm font-medium transition-colors ${
        location.pathname === to
          ? 'bg-[#1e3a8a]/10 text-[#1e3a8a]'
          : 'text-gray-600 hover:text-[#1e3a8a] hover:bg-[#1e3a8a]/5'
      }`}
    >
      {icon}
      {label}
    </Link>
  );

  return (
    <nav className="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-gray-200/80 shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-14">
          <Link to="/" className="flex items-center gap-2 shrink-0">
            <BookOpen className="h-6 w-6 text-[#1e3a8a]" />
            <span className="text-lg font-bold text-[#1e3a8a]">
              Steiner Reader
            </span>
            <span className="hidden sm:inline text-xs text-gray-400 mt-0.5">施泰纳著作</span>
          </Link>

          <div className="hidden md:flex items-center gap-1">
            {navLink('/', '首页')}
            {user ? (
              <>
                {navLink('/recharge', '充值', <Coins className="h-3.5 w-3.5" />)}
                {user.is_admin === 1 && (
                  <>
                    {navLink('/upload', '上传', <Upload className="h-3.5 w-3.5" />)}
                    {navLink('/admin', '管理', <Shield className="h-3.5 w-3.5" />)}
                  </>
                )}
                <div className="w-px h-5 bg-gray-200 mx-1" />
                <Link to="/profile" className="flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm hover:bg-gray-50 transition-colors">
                  <User className="h-4 w-4 text-gray-500" />
                  <span className="text-gray-700 font-medium">{user.username}</span>
                  <span className="text-xs bg-amber-50 text-amber-700 border border-amber-200/60 px-1.5 py-0.5 rounded-full">
                    {user.credits} 点
                  </span>
                </Link>
                <button
                  onClick={handleLogout}
                  className="p-1.5 rounded-lg text-gray-400 hover:text-gray-600 hover:bg-gray-50 transition-colors"
                  title="退出登录"
                >
                  <LogOut className="h-4 w-4" />
                </button>
              </>
            ) : (
              <>
                <div className="w-px h-5 bg-gray-200 mx-1" />
                <Link
                  to="/login"
                  className="px-4 py-1.5 bg-[#1e3a8a] text-white text-sm font-medium rounded-lg hover:bg-[#163272] transition-colors"
                >
                  登录
                </Link>
              </>
            )}
          </div>

          <button
            className="md:hidden p-1.5 rounded-lg text-gray-600 hover:bg-gray-50"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            {isMenuOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
          </button>
        </div>

        {isMenuOpen && (
          <div className="md:hidden py-3 border-t border-gray-100 space-y-1">
            {navLink('/', '首页')}
            {user ? (
              <>
                {navLink('/recharge', '充值', <Coins className="h-3.5 w-3.5" />)}
                {user.is_admin === 1 && (
                  <>
                    {navLink('/upload', '上传', <Upload className="h-3.5 w-3.5" />)}
                    {navLink('/admin', '管理', <Shield className="h-3.5 w-3.5" />)}
                  </>
                )}
                {navLink('/profile', user.username || '个人中心', <User className="h-3.5 w-3.5" />)}
                <button
                  onClick={handleLogout}
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-sm text-red-500 hover:bg-red-50 w-full"
                >
                  <LogOut className="h-3.5 w-3.5" />
                  退出登录
                </button>
              </>
            ) : (
              <Link
                to="/login"
                className="block px-3 py-1.5 rounded-lg text-sm font-medium text-[#1e3a8a] hover:bg-[#1e3a8a]/5"
              >
                登录
              </Link>
            )}
          </div>
        )}
      </div>
    </nav>
  );
}
