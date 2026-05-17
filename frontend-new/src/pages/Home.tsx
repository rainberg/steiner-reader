import { useEffect, useMemo } from 'react';
import { Search, Grid, Layers } from 'lucide-react';
import BookCard from '../components/BookCard';
import { useStore } from '../hooks/useStore';
import { api } from '../lib/api';
import type { Book } from '../types';

export default function Home() {
  const {
    books,
    setBooks,
    isLoading,
    setIsLoading,
    searchQuery,
    setSearchQuery,
    viewMode,
    setViewMode,
  } = useStore();

  useEffect(() => {
    const loadBooks = async () => {
      setIsLoading(true);
      try {
        const data = await api.getBooks();
        setBooks(data);
      } catch (error) {
        console.error('Failed to load books:', error);
        // Mock data for demo
        setBooks([
          {
            id: 1,
            title: 'The Philosophy of Freedom',
            author: 'Rudolf Steiner',
            description: 'A fundamental work on epistemology and the philosophy of freedom.',
            category: 'Philosophy',
          },
          {
            id: 2,
            title: 'How to Know Higher Worlds',
            author: 'Rudolf Steiner',
            description: 'A guide to spiritual development and higher knowledge.',
            category: 'Spirituality',
          },
          {
            id: 3,
            title: 'Theosophy',
            author: 'Rudolf Steiner',
            description: 'An introduction to anthroposophy and spiritual science.',
            category: 'Theosophy',
          },
          {
            id: 4,
            title: 'Knowledge of the Higher Worlds',
            author: 'Rudolf Steiner',
            description: 'Methods for attaining spiritual perception.',
            category: 'Spirituality',
          },
          {
            id: 5,
            title: 'Occult Science',
            author: 'Rudolf Steiner',
            description: 'An outline of esoteric knowledge and spiritual science.',
            category: 'Science',
          },
          {
            id: 6,
            title: 'The Fourth Dimension',
            author: 'Rudolf Steiner',
            description: 'Explorations of space, time, and higher dimensions.',
            category: 'Science',
          },
        ]);
      } finally {
        setIsLoading(false);
      }
    };

    loadBooks();
  }, [setBooks, setIsLoading]);

  const filteredBooks = useMemo(() => {
    if (!searchQuery) return books;
    const query = searchQuery.toLowerCase();
    return books.filter(
      (book) =>
        book.title.toLowerCase().includes(query) ||
        book.author.toLowerCase().includes(query) ||
        book.category.toLowerCase().includes(query)
    );
  }, [books, searchQuery]);

  const groupedBooks = useMemo(() => {
    const groups: Record<string, Book[]> = {};
    books.forEach((book) => {
      if (!groups[book.category]) {
        groups[book.category] = [];
      }
      groups[book.category].push(book);
    });
    return groups;
  }, [books]);

  return (
    <div className="min-h-screen pt-24 pb-16">
      {/* Hero Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-16">
        <div className="text-center max-w-3xl mx-auto">
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold text-gray-900 mb-6 font-['Playfair_Display']">
            施泰纳著作库
          </h1>
          <p className="text-lg text-gray-600 mb-8">
            Rudolf Steiner Gesamtausgabe 在线阅读与检索
          </p>
          <div className="relative max-w-xl mx-auto">
            <Search className="absolute left-4 top-1/2 -translate-y-1/2 h-5 w-5 text-gray-400" />
            <input
              type="text"
              placeholder="搜索书籍、作者..."
              value={searchQuery}
              onChange={(e) => {
                setSearchQuery(e.target.value);
                if (e.target.value) {
                  setViewMode('search');
                }
              }}
              className="w-full pl-12 pr-4 py-4 bg-white border border-gray-200 rounded-2xl shadow-sm focus:outline-none focus:ring-2 focus:ring-[#1e3a8a] focus:border-transparent transition-all"
            />
          </div>
        </div>
      </section>

      {/* View Toggle */}
      {!searchQuery && (
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mb-8">
          <div className="flex items-center gap-2 bg-gray-100 p-1 rounded-xl w-fit">
            <button
              onClick={() => setViewMode('group')}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                viewMode === 'group'
                  ? 'bg-white text-gray-900 shadow-sm'
                  : 'text-gray-500 hover:text-gray-700'
              }`}
            >
              <Layers className="h-4 w-4" />
              分类
            </button>
            <button
              onClick={() => setViewMode('grid')}
              className={`flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition-all ${
                viewMode === 'grid'
                  ? 'bg-white text-gray-900 shadow-sm'
                  : 'text-gray-500 hover:text-gray-700'
              }`}
            >
              <Grid className="h-4 w-4" />
              网格
            </button>
          </div>
        </section>
      )}

      {/* Books Content */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {isLoading ? (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {[...Array(8)].map((_, i) => (
              <div
                key={i}
                className="bg-white rounded-2xl shadow-sm overflow-hidden"
              >
                <div className="aspect-[3/4] bg-gray-100 animate-pulse" />
                <div className="p-5">
                  <div className="h-3 bg-gray-100 rounded w-16 mb-3 animate-pulse" />
                  <div className="h-5 bg-gray-100 rounded w-3/4 mb-2 animate-pulse" />
                  <div className="h-4 bg-gray-100 rounded w-1/2 animate-pulse" />
                </div>
              </div>
            ))}
          </div>
        ) : viewMode === 'group' && !searchQuery ? (
          Object.entries(groupedBooks).map(([category, categoryBooks]) => (
            <div key={category} className="mb-12">
              <h2 className="text-2xl font-bold text-gray-900 mb-6 font-['Playfair_Display']">
                {category}
              </h2>
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                {categoryBooks.map((book) => (
                  <BookCard key={book.id} book={book} />
                ))}
              </div>
            </div>
          ))
        ) : (
          <>
            {searchQuery && (
              <h2 className="text-xl font-bold text-gray-900 mb-6">
                搜索结果 ({filteredBooks.length})
              </h2>
            )}
            {filteredBooks.length > 0 ? (
              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                {filteredBooks.map((book) => (
                  <BookCard key={book.id} book={book} />
                ))}
              </div>
            ) : (
              <div className="text-center py-16">
                <p className="text-gray-500 text-lg">未找到相关书籍</p>
              </div>
            )}
          </>
        )}
      </section>
    </div>
  );
}
