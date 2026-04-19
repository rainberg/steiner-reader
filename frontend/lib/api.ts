// API client for Steiner Reader backend

const API_BASE = process.env.NEXT_PUBLIC_API_URL || '';

export interface Sentence {
  id: number;
  text_de: string;
  text_zh: string | null;
  order_index: number;
}

export interface Paragraph {
  id: number;
  order_index: number;
  sentences: Sentence[];
}

export interface LectureSummary {
  id: number;
  title_de: string | null;
  lecture_date: string | null;
  location: string | null;
  order_index: number;
  sentence_count: number;
}

export interface Lecture {
  id: number;
  book_id: number;
  title_de: string | null;
  lecture_date: string | null;
  location: string | null;
  order_index: number;
  paragraphs: Paragraph[];
}

export interface Book {
  id: number;
  ga_number: string | null;
  title_de: string;
  title_zh: string | null;
  pdf_filename: string;
  cover_url: string | null;
  created_at: string;
  lectures: LectureSummary[];
}

export interface BookDetail {
  id: number;
  ga_number: string | null;
  title_de: string;
  title_zh: string | null;
  pdf_filename: string;
  cover_url: string | null;
  created_at: string;
  lectures: Lecture[];
}

export interface UploadResponse {
  book_id: number;
  message: string;
  ga_number: string | null;
  stats: Record<string, number>;
}

export interface TranslationJob {
  id: number;
  book_id: number;
  status: string;
  total_sentences: number | null;
  translated_count: number;
  error_message: string | null;
  created_at: string;
  updated_at: string;
}

export async function fetchBooks(): Promise<Book[]> {
  const res = await fetch(`${API_BASE}/api/books`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch books');
  return res.json();
}

export async function fetchBook(bookId: number): Promise<BookDetail> {
  const res = await fetch(`${API_BASE}/api/books/${bookId}`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch book');
  return res.json();
}

export async function fetchLecture(bookId: number, lectureId: number): Promise<Lecture> {
  const res = await fetch(`${API_BASE}/api/books/${bookId}/lectures/${lectureId}`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch lecture');
  return res.json();
}

export async function uploadPdf(file: File): Promise<UploadResponse> {
  const formData = new FormData();
  formData.append('file', file);
  const res = await fetch(`${API_BASE}/api/books/upload`, {
    method: 'POST',
    body: formData,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Upload failed' }));
    throw new Error(err.detail || 'Upload failed');
  }
  return res.json();
}

export async function translateLecture(lectureId: number): Promise<{ translated: number; total: number; message: string }> {
  const res = await fetch(`${API_BASE}/api/lectures/${lectureId}/translate`, { method: 'POST' });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Translation failed' }));
    throw new Error(err.detail || 'Translation failed');
  }
  return res.json();
}

export async function getJobStatus(jobId: number): Promise<TranslationJob> {
  const res = await fetch(`${API_BASE}/api/jobs/${jobId}`);
  if (!res.ok) throw new Error('Failed to fetch job');
  return res.json();
}
