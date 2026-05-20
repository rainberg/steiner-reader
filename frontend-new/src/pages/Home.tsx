import { useEffect, useMemo } from 'react';
import { Search, Grid, Layers } from 'lucide-react';
import BookCard from '../components/BookCard';
import { useStore } from '../hooks/useStore';
import { api } from '../lib/api';
import type { BookSummary } from '../types';

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
        const data = await api.getBookSummaries();
        setBooks(data);
      } catch (error) {
        console.error('Failed to load books:', error);
        // Mock data for demo
        setBooks([
          {
            id: 1,
            ga_number: 'GA001',
            title_de: 'Die Philosophie der Freiheit',
            title_zh: '自由的哲学',
            lecture_count: 12,
            sentence_count: 3456,
            image_count: 0,
            translated_count: 1200,
          },
          {
            id: 2,
            ga_number: 'GA002',
            title_de: 'Wie erlangt man Erkenntnisse der höheren Welten?',
            title_zh: '如何认识高层世界',
            lecture_count: 8,
            sentence_count: 2345,
            image_count: 0,
            translated_count: 800,
          },
          {
            id: 3,
            ga_number: 'GA003',
            title_de: 'Theosophie',
            title_zh: '神智学',
            lecture_count: 10,
            sentence_count: 2890,
            image_count: 0,
            translated_count: 1500,
          },
          {
            id: 4,
            ga_number: 'GA004',
            title_de: 'Die Geheimwissenschaft im Umriß',
            title_zh: '奥秘科学大纲',
            lecture_count: 15,
            sentence_count: 4567,
            image_count: 0,
            translated_count: 2000,
          },
          {
            id: 5,
            ga_number: 'GA005',
            title_de: 'Von Seelenrätseln',
            title_zh: '灵魂之谜',
            lecture_count: 6,
            sentence_count: 1876,
            image_count: 0,
            translated_count: 600,
          },
          {
            id: 6,
            ga_number: 'GA006',
            title_de: 'Das Christentum als mystische Tatsache',
            title_zh: '基督教作为神秘事实',
            lecture_count: 9,
            sentence_count: 2789,
            image_count: 0,
            translated_count: 900,
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
        book.title_de.toLowerCase().includes(query) ||
        (book.title_zh && book.title_zh.toLowerCase().includes(query)) ||
        (book.ga_number && book.ga_number.toLowerCase().includes(query))
    );
  }, [books, searchQuery]);

  const groupedBooks = useMemo(() => {
    const groups: Record<string, BookSummary[]> = {};
    books.forEach((book) => {
      const ga = book.ga_number || '';
      let prefix = '其他';
      if (ga.startsWith('GA')) {
        const num = parseInt(ga.substring(2)) || 0;
        const decade = Math.floor(num / 10) * 10;
        prefix = `GA${String(decade).padStart(3, '0')}-${String(decade + 9).padStart(3, '0')}`;
      }
      if (!groups[prefix]) {
        groups[prefix] = [];
      }
      groups[prefix].push(book);
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
              placeholder="搜索书籍、GA编号..."
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
