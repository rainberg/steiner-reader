import { Link } from 'react-router-dom';
import type { BookSummary } from '../types';

interface BookCardProps {
  book: BookSummary;
}

export default function BookCard({ book }: BookCardProps) {
  return (
    <Link
      to={`/books/${book.id}`}
      className="group bg-white rounded-2xl shadow-sm hover:shadow-lg transition-all duration-300 overflow-hidden"
    >
      <div className="aspect-[3/4] bg-gradient-to-br from-[#e0e7ff] to-[#f8f5f0] relative overflow-hidden">
        {book.cover_url ? (
          <img
            src={book.cover_url}
            alt={book.title_de}
            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
          />
        ) : (
          <div className="w-full h-full flex items-center justify-center">
            <div className="text-[#1e3a8a] text-4xl font-['Playfair_Display'] opacity-30">
              {book.ga_number || book.title_de.charAt(0)}
            </div>
          </div>
        )}
      </div>
      <div className="p-5">
        <div className="flex items-center gap-2 mb-2">
          <span className="px-2 py-1 bg-[#e0e7ff] text-[#1e3a8a] text-xs rounded-full">
            {book.ga_number || 'GA'}
          </span>
        </div>
        <h3 className="text-lg font-bold text-gray-900 mb-1 line-clamp-2 group-hover:text-[#1e3a8a] transition-colors">
          {book.title_de}
        </h3>
        {book.title_zh && (
          <p className="text-gray-500 text-sm mb-1">{book.title_zh}</p>
        )}
        <p className="text-gray-400 text-xs">{book.lecture_count} 章节 · {book.sentence_count} 句子</p>
      </div>
    </Link>
  );
}
