import { Link } from 'react-router-dom';
import type { Book } from '../types';

interface BookCardProps {
  book: Book;
}

export default function BookCard({ book }: BookCardProps) {
  return (
    <Link
      to={`/books/${book.id}`}
      className="group bg-white rounded-2xl shadow-sm hover:shadow-lg transition-all duration-300 overflow-hidden"
    >
      <div className="aspect-[3/4] bg-gradient-to-br from-[#e0e7ff] to-[#f8f5f0] relative overflow-hidden">
        {book.cover_image ? (
          <img
            src={book.cover_image}
            alt={book.title}
            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
          />
        ) : (
          <div className="w-full h-full flex items-center justify-center">
            <div className="text-[#1e3a8a] text-4xl font-['Playfair_Display'] opacity-30">
              {book.title.charAt(0)}
            </div>
          </div>
        )}
      </div>
      <div className="p-5">
        <div className="flex items-center gap-2 mb-2">
          <span className="px-2 py-1 bg-[#e0e7ff] text-[#1e3a8a] text-xs rounded-full">
            {book.category}
          </span>
        </div>
        <h3 className="text-lg font-bold text-gray-900 mb-1 line-clamp-2 group-hover:text-[#1e3a8a] transition-colors">
          {book.title}
        </h3>
        <p className="text-gray-500 text-sm">{book.author}</p>
      </div>
    </Link>
  );
}
