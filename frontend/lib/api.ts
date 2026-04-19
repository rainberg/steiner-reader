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

// Full lecture (for reader page)
export interface Lecture {
  id: number;
  book_id: number;
  title_de: string | null;
  lecture_date: string | null;
  location: string | null;
  order_index: number;
  paragraphs: Paragraph[];
}

// Lightweight lecture (for TOC page — no sentences)
export interface LectureListItem {
  id: number;
  book_id: number;
  title_de: string | null;
  lecture_date: string | null;
  location: string | null;
  order_index: number;
  sentence_count: number;
  translated_count: number;
}

export interface LectureSummary {
  id: number;
  title_de: string | null;
  lecture_date: string | null;
  location: string | null;
  order_index: number;
  sentence_count: number;
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
  lectures: LectureListItem[];
}

export interface UploadResponse {
  book_id: number;
  message: string;
  cost?: number;
  credits?: number;
  ga_number: string | null;
  stats: Record<string, number>;
}

export interface TranslateResult {
  lecture_id: number;
  status: string;
  message: string;
  cost?: number;
  credits?: number;
  translated: number;
  total: number;
}

export interface TranslationStatus {
  lecture_id: number;
  total: number;
  translated: number;
  completed: boolean;
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

export async function translateLecture(lectureId: number): Promise<TranslateResult> {
  const res = await fetch(`${API_BASE}/api/lectures/${lectureId}/translate`, { method: 'POST' });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Translation failed' }));
    throw new Error(err.detail || 'Translation failed');
  }
  return res.json();
}

export async function getTranslationStatus(lectureId: number): Promise<TranslationStatus> {
  const res = await fetch(`${API_BASE}/api/lectures/${lectureId}/translation-status`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch status');
  return res.json();
}


export interface LectureImage {
  id: number;
  lecture_id: number;
  filename: string;
  url: string;
  page_number: number;
  width: number;
  height: number;
  after_paragraph_id: number | null;
}

export async function fetchLectureImages(lectureId: number): Promise<LectureImage[]> {
  const res = await fetch(`${API_BASE}/api/lectures/${lectureId}/images`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch images');
  return res.json();
}


// --- Auth ---

export interface User {
  id: number;
  username: string;
  email: string;
  credits: number;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface TranslationCost {
  lecture_id: number;
  total: number;
  translated: number;
  remaining: number;
  cost: number;
  already_translated: boolean;
  user_credits: number | null;
  can_afford: boolean | null;
}

function getToken(): string | null {
  if (typeof window === 'undefined') return null;
  return localStorage.getItem('steiner_token');
}

export function getStoredUser(): User | null {
  if (typeof window === 'undefined') return null;
  const u = localStorage.getItem('steiner_user');
  return u ? JSON.parse(u) : null;
}

export function saveAuth(data: AuthResponse) {
  localStorage.setItem('steiner_token', data.access_token);
  localStorage.setItem('steiner_user', JSON.stringify(data.user));
}

export function clearAuth() {
  localStorage.removeItem('steiner_token');
  localStorage.removeItem('steiner_user');
}

async function authFetch(url: string, options: RequestInit = {}): Promise<Response> {
  const token = getToken();
  const headers: Record<string, string> = {
    ...(options.headers as Record<string, string> || {}),
  };
  if (token) headers['Authorization'] = `Bearer ${token}`;
  return fetch(`${API_BASE}${url}`, { ...options, headers });
}

export async function register(username: string, email: string, password: string): Promise<AuthResponse> {
  const res = await fetch(`${API_BASE}/api/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, email, password }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '注册失败' }));
    throw new Error(err.detail || '注册失败');
  }
  const data = await res.json();
  saveAuth(data);
  return data;
}

export async function login(username: string, password: string): Promise<AuthResponse> {
  const res = await fetch(`${API_BASE}/api/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '登录失败' }));
    throw new Error(err.detail || '登录失败');
  }
  const data = await res.json();
  saveAuth(data);
  return data;
}

export async function fetchMe(): Promise<User> {
  const res = await authFetch('/api/auth/me');
  if (!res.ok) throw new Error('未登录');
  return res.json();
}

export async function getTranslationCost(lectureId: number): Promise<TranslationCost> {
  const res = await authFetch(`/api/lectures/${lectureId}/translation-cost`);
  if (!res.ok) throw new Error('获取翻译费用失败');
  return res.json();
}
