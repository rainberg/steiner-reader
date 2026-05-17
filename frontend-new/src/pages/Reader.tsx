import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { ArrowLeft, Languages, Loader2 } from 'lucide-react';
import { api } from '../lib/api';
import type { Book, Lecture, Paragraph } from '../types';

export default function Reader() {
  const { bookId, lectureId } = useParams<{ bookId: string; lectureId: string }>();
  const [book, setBook] = useState<Book | null>(null);
  const [lecture, setLecture] = useState<Lecture | null>(null);
  const [paragraphs, setParagraphs] = useState<Paragraph[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [showTranslation, setShowTranslation] = useState(true);
  const [translatingId, setTranslatingId] = useState<number | null>(null);

  useEffect(() => {
    const loadData = async () => {
      if (!bookId || !lectureId) return;
      setIsLoading(true);
      try {
        const [bookData, lectureData, paragraphsData] = await Promise.all([
          api.getBook(parseInt(bookId)),
          api.getLecture(parseInt(bookId), parseInt(lectureId)),
          api.getParagraphs(parseInt(lectureId)),
        ]);
        setBook(bookData);
        setLecture(lectureData);
        setParagraphs(paragraphsData);
      } catch (error) {
        console.error('Failed to load content:', error);
        // Mock data for demo
        setBook({
          id: parseInt(bookId),
          title: 'The Philosophy of Freedom',
          author: 'Rudolf Steiner',
          description: 'A fundamental work on epistemology and the philosophy of freedom.',
          category: 'Philosophy',
        });
        setLecture({
          id: parseInt(lectureId),
          book_id: parseInt(bookId),
          title: 'Introduction',
          number: 1,
        });
        setParagraphs([
          {
            id: 1,
            lecture_id: parseInt(lectureId),
            original_text: 'There is a fundamental question which dominates all others in the spiritual life of humanity. It is the question of freedom.',
            translated_text: '有一个问题支配着人类精神生活中的所有其他问题。那就是自由的问题。',
            order: 1,
          },
          {
            id: 2,
            lecture_id: parseInt(lectureId),
            original_text: 'All other questions recede into the background when this one is raised in the human soul.',
            translated_text: '当这个问题在人类灵魂中被提出时，所有其他问题都退居次要地位。',
            order: 2,
          },
          {
            id: 3,
            lecture_id: parseInt(lectureId),
            original_text: 'The question of freedom is the central question of all spiritual life.',
            order: 3,
          },
        ]);
      } finally {
        setIsLoading(false);
      }
    };

    loadData();
  }, [bookId, lectureId]);

  const handleTranslate = async (paragraphId: number) => {
    setTranslatingId(paragraphId);
    try {
      const updated = await api.translateParagraph(paragraphId);
      setParagraphs((prev) => prev.map((p) => (p.id === paragraphId ? updated : p)));
    } catch (error) {
      console.error('Failed to translate:', error);
      // Mock translation for demo
      setParagraphs((prev) =>
        prev.map((p) =>
          p.id === paragraphId
            ? { ...p, translated_text: '这是该段落的翻译内容。' }
            : p
        )
      );
    } finally {
      setTranslatingId(null);
    }
  };

  if (isLoading) {
    return (
      <div className="min-h-screen pt-24 pb-16">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="animate-pulse space-y-6">
            <div className="h-8 bg-gray-200 rounded w-32" />
            <div className="h-12 bg-gray-200 rounded w-1/2" />
            {[...Array(5)].map((_, i) => (
              <div key={i} className="space-y-3">
                <div className="h-4 bg-gray-200 rounded w-full" />
                <div className="h-4 bg-gray-200 rounded w-full" />
                <div className="h-4 bg-gray-200 rounded w-3/4" />
              </div>
            ))}
          </div>
        </div>
      </div>
    );
  }

  if (!book || !lecture) {
    return (
      <div className="min-h-screen pt-24 pb-16 flex items-center justify-center">
        <p className="text-gray-500 text-lg">内容未找到</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen pt-24 pb-16">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between mb-8">
          <Link
            to={`/books/${book.id}`}
            className="inline-flex items-center gap-2 text-gray-600 hover:text-[#1e3a8a] transition-colors"
          >
            <ArrowLeft className="h-4 w-4" />
            返回书籍
          </Link>
          <button
            onClick={() => setShowTranslation(!showTranslation)}
            className="flex items-center gap-2 px-4 py-2 bg-[#1e3a8a] text-white rounded-xl hover:bg-[#1e3a8a]/90 transition-colors"
          >
            <Languages className="h-4 w-4" />
            {showTranslation ? '隐藏翻译' : '显示翻译'}
          </button>
        </div>

        <div className="mb-12 text-center">
          <p className="text-[#1e3a8a] font-medium mb-2">{book.title}</p>
          <h1 className="text-3xl md:text-4xl font-bold text-gray-900 mb-2 font-['Playfair_Display']">
            {lecture.title}
          </h1>
        </div>

        <div className="space-y-8">
          {paragraphs.map((paragraph) => (
            <div key={paragraph.id} className="group">
              <div className="bg-white rounded-2xl p-6 md:p-8 shadow-sm">
                <p className="text-lg text-gray-900 leading-relaxed mb-4">
                  {paragraph.original_text}
                </p>
                {showTranslation && (
                  <div className="border-t border-gray-100 pt-4">
                    {paragraph.translated_text ? (
                      <p className="text-gray-600 leading-relaxed">
                        {paragraph.translated_text}
                      </p>
                    ) : (
                      <button
                        onClick={() => handleTranslate(paragraph.id)}
                        disabled={translatingId === paragraph.id}
                        className="flex items-center gap-2 text-[#d4a574] hover:text-[#d4a574]/80 transition-colors disabled:opacity-50"
                      >
                        {translatingId === paragraph.id ? (
                          <Loader2 className="h-4 w-4 animate-spin" />
                        ) : (
                          <Languages className="h-4 w-4" />
                        )}
                        {translatingId === paragraph.id ? '翻译中...' : '翻译此段落'}
                      </button>
                    )}
                  </div>
                )}
              </div>
            </div>
          ))}
        </div>

        {paragraphs.length === 0 && (
          <div className="text-center py-16">
            <p className="text-gray-500 text-lg">暂无内容</p>
          </div>
        )}
      </div>
    </div>
  );
}
