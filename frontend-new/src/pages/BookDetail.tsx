import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ArrowLeft, BookOpen } from 'lucide-react';
import { api } from '../lib/api';
import type { Book, Lecture } from '../types';

export default function BookDetail() {
  const { bookId } = useParams<{ bookId: string }>();
  const [book, setBook] = useState<Book | null>(null);
  const [lectures, setLectures] = useState<Lecture[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const loadData = async () => {
      if (!bookId) return;
      setIsLoading(true);
      try {
        const bookData = await api.getBook(parseInt(bookId));
        setBook(bookData);
        setLectures(bookData.lectures || []);
      } catch (error) {
        console.error('Failed to load book:', error);
        // Mock data for demo
        setBook({
          id: parseInt(bookId),
          ga_number: 'GA001',
          title_de: 'Die Philosophie der Freiheit',
          title_zh: '自由的哲学',
          lectures: [],
        });
        setLectures([
          { id: 1, book_id: parseInt(bookId), title_de: 'Introduction', title_zh: '导言', order_index: 1, lecture_date: null, location: null, sentence_count: 120 },
          { id: 2, book_id: parseInt(bookId), title_de: 'Knowledge of Freedom', title_zh: '自由的知识', order_index: 2, lecture_date: null, location: null, sentence_count: 200 },
          { id: 3, book_id: parseInt(bookId), title_de: 'Moral Imagination', title_zh: '道德想象力', order_index: 3, lecture_date: null, location: null, sentence_count: 180 },
          { id: 4, book_id: parseInt(bookId), title_de: 'Ethical Individualism', title_zh: '伦理个人主义', order_index: 4, lecture_date: null, location: null, sentence_count: 150 },
        ]);
      } finally {
        setIsLoading(false);
      }
    };

    loadData();
  }, [bookId]);

  if (isLoading) {
    return (
      <div className="min-h-screen pt-24 pb-16">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="animate-pulse">
            <div className="h-8 bg-gray-200 rounded w-32 mb-8" />
            <div className="flex gap-8 mb-12">
              <div className="w-64 h-96 bg-gray-200 rounded-2xl flex-shrink-0" />
              <div className="flex-1">
                <div className="h-12 bg-gray-200 rounded w-3/4 mb-4" />
                <div className="h-6 bg-gray-200 rounded w-1/2 mb-6" />
                <div className="h-4 bg-gray-200 rounded w-full mb-2" />
                <div className="h-4 bg-gray-200 rounded w-full mb-2" />
                <div className="h-4 bg-gray-200 rounded w-2/3" />
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (!book) {
    return (
      <div className="min-h-screen pt-24 pb-16 flex items-center justify-center">
        <p className="text-gray-500 text-lg">书籍未找到</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen pt-24 pb-16">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <Link
          to="/"
          className="inline-flex items-center gap-2 text-gray-600 hover:text-[#1e3a8a] transition-colors mb-8"
        >
          <ArrowLeft className="h-4 w-4" />
          返回
        </Link>

        <div className="flex flex-col lg:flex-row gap-8 mb-12">
          <div className="w-full lg:w-64 flex-shrink-0">
            <div className="aspect-[3/4] bg-gradient-to-br from-[#e0e7ff] to-[#f8f5f0] rounded-2xl shadow-lg overflow-hidden">
              {book.cover_url ? (
                <img
                  src={book.cover_url}
                  alt={book.title_de}
                  className="w-full h-full object-cover"
                />
              ) : (
                <div className="w-full h-full flex items-center justify-center">
                  <BookOpen className="h-24 w-24 text-[#1e3a8a] opacity-30" />
                </div>
              )}
            </div>
          </div>

          <div className="flex-1">
            <span className="inline-block px-3 py-1 bg-[#e0e7ff] text-[#1e3a8a] text-sm rounded-full mb-4">
              {book.ga_number || 'GA'}
            </span>
            <h1 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4 font-['Playfair_Display']">
              {book.title_de}
            </h1>
            {book.title_zh && (
              <p className="text-xl text-gray-600 mb-6">{book.title_zh}</p>
            )}
            <p className="text-gray-700 leading-relaxed">
              {book.title_de} 是鲁道夫·施泰纳的重要著作之一。
            </p>
          </div>
        </div>

        <div className="bg-white rounded-2xl shadow-sm p-6 md:p-8">
          <h2 className="text-2xl font-bold text-gray-900 mb-6 font-['Playfair_Display']">
            章节列表
          </h2>
          {lectures.length > 0 ? (
            <div className="space-y-3">
              {lectures.map((lecture) => (
                <Link
                  key={lecture.id}
                  to={`/books/${book.id}/lectures/${lecture.id}`}
                  className="flex items-center gap-4 p-4 rounded-xl hover:bg-[#f8f5f0] transition-colors group"
                >
                  <div className="w-10 h-10 bg-[#1e3a8a] text-white rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0">
                    {lecture.order_index}
                  </div>
                  <div className="flex-1">
                    <h3 className="text-lg font-semibold text-gray-900 group-hover:text-[#1e3a8a] transition-colors">
                      {lecture.title_de}
                    </h3>
                    {lecture.title_zh && (
                      <p className="text-sm text-gray-500">{lecture.title_zh}</p>
                    )}
                    {lecture.lecture_date && (
                      <p className="text-sm text-gray-400">{lecture.lecture_date}</p>
                    )}
                  </div>
                  <ArrowLeft className="h-5 w-5 text-gray-400 group-hover:text-[#1e3a8a] group-hover:translate-x-1 transition-all rotate-180" />
                </Link>
              ))}
            </div>
          ) : (
            <p className="text-gray-500 text-center py-8">暂无章节</p>
          )}
        </div>
      </div>
    </div>
  );
}
