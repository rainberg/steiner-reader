import { useState } from 'react';
import { Link } from 'react-router-dom';
import { BookOpen, User, Search, Menu, X } from 'lucide-react';
import { useStore } from '../hooks/useStore';

export default function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const { user } = useStore();

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-white/90 backdrop-blur-md border-b border-gray-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <Link to="/" className="flex items-center gap-2">
            <BookOpen className="h-8 w-8 text-[#1e3a8a]" />
            <span className="text-xl font-bold text-[#1e3a8a] font-['Playfair_Display']">
              Steiner Library
            </span>
          </Link>

          <div className="hidden md:flex items-center gap-8">
            <Link to="/" className="text-gray-700 hover:text-[#1e3a8a] transition-colors">
              首页
            </Link>
            <Link to="/search" className="text-gray-700 hover:text-[#1e3a8a] transition-colors flex items-center gap-1">
              <Search className="h-4 w-4" />
              搜索
            </Link>
            {user ? (
              <>
                <Link to="/profile" className="text-gray-700 hover:text-[#1e3a8a] transition-colors flex items-center gap-1">
                  <User className="h-4 w-4" />
                  {user.username || user.email}
                </Link>
                {user.is_admin === 1 && (
                  <Link to="/admin" className="text-gray-700 hover:text-[#1e3a8a] transition-colors">
                    管理
                  </Link>
                )}
              </>
            ) : (
              <Link to="/login" className="text-gray-700 hover:text-[#1e3a8a] transition-colors">
                登录
              </Link>
            )}
          </div>

          <button
            className="md:hidden text-gray-700"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            {isMenuOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
          </button>
        </div>

        {isMenuOpen && (
          <div className="md:hidden py-4 border-t border-gray-100">
            <div className="flex flex-col gap-4">
              <Link
                to="/"
                className="text-gray-700 hover:text-[#1e3a8a] transition-colors"
                onClick={() => setIsMenuOpen(false)}
              >
                首页
              </Link>
              <Link
                to="/search"
                className="text-gray-700 hover:text-[#1e3a8a] transition-colors"
                onClick={() => setIsMenuOpen(false)}
              >
                搜索
              </Link>
              {user ? (
                <>
                  <Link
                    to="/profile"
                    className="text-gray-700 hover:text-[#1e3a8a] transition-colors"
                    onClick={() => setIsMenuOpen(false)}
                  >
                    个人中心
                  </Link>
                  {user.is_admin === 1 && (
                    <Link
                      to="/admin"
                      className="text-gray-700 hover:text-[#1e3a8a] transition-colors"
                      onClick={() => setIsMenuOpen(false)}
                    >
                      管理后台
                    </Link>
                  )}
                </>
              ) : (
                <Link
                  to="/login"
                  className="text-gray-700 hover:text-[#1e3a8a] transition-colors"
                  onClick={() => setIsMenuOpen(false)}
                >
                  登录
                </Link>
              )}
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}
