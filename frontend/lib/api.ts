// API client for Steiner Reader backend.

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || process.env.NEXT_PUBLIC_API_URL || '';

const REQUEST_TIMEOUT_MS = 12000;

async function timedFetch(url: string, options: RequestInit = {}, timeoutMs: number = REQUEST_TIMEOUT_MS): Promise<Response> {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), timeoutMs);
  try {
    return await fetch(url, { ...options, signal: controller.signal });
  } catch (error) {
    if (error instanceof DOMException && error.name === 'AbortError') {
      throw new Error('Request timeout');
    }
    throw error;
  } finally {
    clearTimeout(timer);
  }
}


export interface Sentence {
  id: number;
  text_de?: string;
  text_zh?: string | null;
  order_index?: number;
  paragraph_id?: number;
  sentence_index?: number;
  content_de?: string;
  content_zh?: string | null;
  is_heading?: boolean;
  image_url?: string | null;
}

export interface Paragraph {
  id: number;
  order_index?: number;
  lecture_id?: number;
  paragraph_index?: number;
  content_de?: string;
  content_zh?: string | null;
  sentences: Sentence[];
}

export interface Lecture {
  id: number;
  book_id: number;
  title_de: string | null;
  title_zh?: string | null;
  lecture_date: string | null;
  location: string | null;
  order_index: number;
  level?: string | null;
  parent_id?: number | null;
  sentence_count: number;
  paragraph_count?: number;
  translated_count?: number;
  image_count?: number;
  paragraphs?: Paragraph[];
  is_published?: boolean;
  contributors?: ContributionDisplay[];
  can_download_pdf?: boolean;
  can_edit?: boolean;
  download_notice?: string;
  download_lecture_cost?: number;
  edit_translation_cost?: number;
  edit_source_cost?: number;
  unlinked_images?: string[];
}

export interface Book {
  id: number;
  ga_number: string | null;
  title_de: string;
  title_zh: string | null;
  subtitle_de?: string | null;
  subtitle_zh?: string | null;
  pdf_filename?: string;
  cover_url?: string | null;
  cover_image_url?: string | null;
  created_at?: string;
  lectures: Lecture[];
  image_count?: number;
  translated_count?: number;
}

export interface BookSummary {
  id: number;
  ga_number: string | null;
  title_de: string;
  title_zh: string | null;
  pdf_filename?: string;
  cover_url?: string | null;
  created_at?: string;
  lecture_count: number;
  sentence_count: number;
  image_count: number;
  translated_count: number;
}

export interface User {
  id: number;
  username: string;
  email: string;
  credits: number;
  is_admin?: number;
  created_at?: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface UploadResponse {
  book_id?: number;
  message: string;
  ga_number?: string | null;
  chapters?: number;
  stats?: Record<string, number>;
}

export interface TranslationCost {
  lecture_id: number;
  total: number;
  translated: number;
  remaining: number;
  cost: number;
  already_translated: boolean;
  is_published: boolean;
  user_credits: number | null;
  can_afford: boolean | null;
}

export interface TranslationStatus {
  lecture_id: number;
  total: number;
  translated: number;
  completed: boolean;
  is_translating?: boolean;
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

export interface LectureImage {
  id: number;
  lecture_id?: number;
  filename: string;
  url: string;
  page_number?: number;
  width?: number;
  height?: number;
  after_paragraph_id?: number | null;
  paragraph_index?: number | null;
}

function getToken(): string | null {
  if (typeof window === 'undefined') return null;
  return localStorage.getItem('steiner_token');
}

function authHeaders(extra: Record<string, string> = {}): Record<string, string> {
  const token = getToken();
  return token ? { ...extra, Authorization: `Bearer ${token}` } : extra;
}

async function authFetch(url: string, options: RequestInit = {}): Promise<Response> {
  return timedFetch(`${API_BASE}${url}`, {
    ...options,
    headers: authHeaders((options.headers as Record<string, string>) || {}),
  });
}

export function getStoredUser(): User | null {
  if (typeof window === 'undefined') return null;
  const raw = localStorage.getItem('steiner_user');
  return raw ? JSON.parse(raw) : null;
}

export function saveAuth(data: AuthResponse) {
  localStorage.setItem('steiner_token', data.access_token);
  localStorage.setItem('steiner_user', JSON.stringify(data.user));
}

export function clearAuth() {
  localStorage.removeItem('steiner_token');
  localStorage.removeItem('steiner_user');
}

export async function fetchBooks(): Promise<Book[]> {
  const res = await timedFetch(`${API_BASE}/api/books`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch books');
  return res.json();
}

export async function fetchBookSummaries(): Promise<BookSummary[]> {
  const res = await timedFetch(`${API_BASE}/api/books/summary`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch book summaries');
  return res.json();
}

export interface BookGroup {
  group: string;
  book_count: number;
  lecture_count: number;
  sentence_count: number;
  books: BookSummary[];
}

export async function fetchBookGroups(): Promise<BookGroup[]> {
  const res = await timedFetch(`${API_BASE}/api/books/groups`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch book groups');
  return res.json();
}

export async function fetchBookSummariesPaginated(params: {
  page?: number;
  page_size?: number;
  search?: string;
  sort_by?: string;
  sort_dir?: string;
}): Promise<BookSummary[]> {
  const qs = new URLSearchParams();
  if (params.page) qs.set('page', String(params.page));
  if (params.page_size) qs.set('page_size', String(params.page_size));
  if (params.search) qs.set('search', params.search);
  if (params.sort_by) qs.set('sort_by', params.sort_by);
  if (params.sort_dir) qs.set('sort_dir', params.sort_dir);
  const res = await timedFetch(`${API_BASE}/api/books/summary?${qs}`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch books');
  return res.json();
}

export async function fetchBookCount(search: string = ''): Promise<number> {
  const qs = search ? `?search=${encodeURIComponent(search)}` : '';
  const res = await timedFetch(`${API_BASE}/api/books/summary/count${qs}`, { cache: 'no-store' });
  if (!res.ok) return 0;
  const data = await res.json();
  return data.count;
}

export async function fetchBook(bookId: number): Promise<Book> {
  const res = await timedFetch(`${API_BASE}/api/books/${bookId}`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch book');
  return res.json();
}

export async function fetchLecture(bookIdOrLectureId: number, maybeLectureId?: number): Promise<Lecture> {
  const url = maybeLectureId === undefined
    ? `${API_BASE}/api/lectures/${bookIdOrLectureId}`
    : `${API_BASE}/api/books/${bookIdOrLectureId}/lectures/${maybeLectureId}`;
  const res = await timedFetch(url, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch lecture');
  return res.json();
}

export async function fetchParagraphs(lectureId: number): Promise<Paragraph[]> {
  const res = await timedFetch(`${API_BASE}/api/lectures/${lectureId}/paragraphs`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch paragraphs');
  return res.json();
}

export async function fetchSentences(paragraphId: number): Promise<Sentence[]> {
  const res = await timedFetch(`${API_BASE}/api/paragraphs/${paragraphId}/sentences`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch sentences');
  return res.json();
}

export async function uploadPdf(file: File): Promise<UploadResponse> {
  const formData = new FormData();
  formData.append('file', file);
  const res = await authFetch('/api/books/upload', {
    method: 'POST',
    body: formData,
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Upload failed' }));
    throw new Error(err.detail || 'Upload failed');
  }
  return res.json();
}

export async function register(username: string, email: string, password: string): Promise<AuthResponse> {
  const res = await timedFetch(`${API_BASE}/api/auth/register`, {
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

export async function login(email: string, password: string): Promise<AuthResponse> {
  const res = await timedFetch(`${API_BASE}/api/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
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
  const res = await authFetch('/api/auth/me', { cache: 'no-store' });
  if (!res.ok) throw new Error('未登录');
  return res.json();
}

export async function getTranslationCost(lectureId: number): Promise<TranslationCost> {
  const res = await authFetch(`/api/lectures/${lectureId}/translation-cost`, { cache: 'no-store' });
  if (!res.ok) throw new Error('获取翻译费用失败');
  return res.json();
}

export async function getTranslationStatus(lectureId: number): Promise<TranslationStatus> {
  const res = await timedFetch(`${API_BASE}/api/lectures/${lectureId}/translation-status`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch status');
  return res.json();
}

export async function translateLecture(lectureId: number): Promise<TranslateResult> {
  const res = await authFetch(`/api/lectures/${lectureId}/translate`, { method: 'POST' });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Translation failed' }));
    throw new Error(err.detail || 'Translation failed');
  }
  return res.json();
}

export async function fetchLectureImages(lectureId: number): Promise<LectureImage[]> {
  const res = await timedFetch(`${API_BASE}/api/lectures/${lectureId}/images`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch images');
  return res.json();
}

export async function changePassword(oldPassword: string, newPassword: string): Promise<void> {
  const res = await authFetch('/api/auth/change-password', {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ old_password: oldPassword, new_password: newPassword }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '修改密码失败' }));
    throw new Error(err.detail || '修改密码失败');
  }
}

export async function changeEmail(email: string, password: string): Promise<void> {
  const res = await authFetch('/api/auth/change-email', {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '修改邮箱失败' }));
    throw new Error(err.detail || '修改邮箱失败');
  }
}

export async function changeUsername(username: string, password: string): Promise<{ success: boolean; message: string; username: string }> {
  const res = await authFetch('/api/auth/change-username', {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '修改用户名失败' }));
    throw new Error(err.detail || '修改用户名失败');
  }
  return res.json();
}

// --- Admin API ---

export async function adminAddCredits(userId: number, amount: number): Promise<{ success: boolean; username: string; added: number; new_credits: number }> {
  const res = await authFetch(`/api/admin/users/${userId}/credits/add`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ amount }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '充值失败' }));
    throw new Error(err.detail || '充值失败');
  }
  return res.json();
}

export async function adminUpdateUser(userId: number, data: { username?: string; email?: string }): Promise<{ success: boolean; user_id: number; username: string; email: string }> {
  const res = await authFetch(`/api/admin/users/${userId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '更新失败' }));
    throw new Error(err.detail || '更新失败');
  }
  return res.json();
}

export async function adminResetPassword(userId: number, newPassword: string): Promise<{ success: boolean; message: string }> {
  const res = await authFetch(`/api/admin/users/${userId}/reset-password`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ new_password: newPassword }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '重置密码失败' }));
    throw new Error(err.detail || '重置密码失败');
  }
  return res.json();
}

// --- Download ---

export interface DownloadPermission {
  has_permission: boolean;
  access_types: string[];
}

export interface PurchaseResult {
  success: boolean;
  credits_remaining: number;
  message: string;
}

export async function getDownloadPermission(lectureId: number): Promise<DownloadPermission> {
  const res = await authFetch(`/api/lectures/${lectureId}/download-permission`, { cache: 'no-store' });
  if (!res.ok) return { has_permission: false, access_types: [] };
  return res.json();
}

export async function purchaseDownloadAccess(lectureId: number): Promise<PurchaseResult> {
  const res = await authFetch(`/api/lectures/${lectureId}/purchase-download`, { method: 'POST' });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '购买失败' }));
    throw new Error(err.detail || '购买失败');
  }
  return res.json();
}

export function getDownloadUrl(lectureId: number): string {
  return `${API_BASE}/api/lectures/${lectureId}/download`;
}

// --- Sentence Editing ---

export interface EditSentenceRequest {
  field: 'text_de' | 'text_zh';
  new_value: string;
}

export interface EditSentenceResult {
  success: boolean;
  new_text: string;
  cost: number;
  credits_remaining: number;
}

export async function editSentence(sentenceId: number, data: EditSentenceRequest): Promise<EditSentenceResult> {
  const res = await authFetch(`/api/sentences/${sentenceId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '编辑失败' }));
    throw new Error(err.detail || '编辑失败');
  }
  return res.json();
}

export interface EditLogEntry {
  id: number;
  user_id: number;
  username: string;
  sentence_id: number;
  field_changed: string;
  old_value: string | null;
  new_value: string | null;
  credits_cost: number;
  created_at: string;
}

export async function fetchSentenceEdits(sentenceId: number): Promise<EditLogEntry[]> {
  const res = await timedFetch(`${API_BASE}/api/sentences/${sentenceId}/edits`, { cache: 'no-store' });
  if (!res.ok) return [];
  return res.json();
}

// --- Contributions ---

export interface ContributionDisplay {
  username: string;
  contribution_type: string;
  count: number;
  created_at: string;
}

export async function fetchContributions(lectureId: number): Promise<ContributionDisplay[]> {
  const res = await timedFetch(`${API_BASE}/api/lectures/${lectureId}/contributions`, { cache: 'no-store' });
  if (!res.ok) return [];
  const data = await res.json();
  return data.contributions || [];
}

// --- Credit Settings (Admin) ---

export interface CreditSetting {
  id: number;
  key: string;
  value: number;
  description: string | null;
  updated_at: string | null;
}

export async function fetchCreditSettings(): Promise<CreditSetting[]> {
  const res = await authFetch('/api/admin/credit-settings', { cache: 'no-store' });
  if (!res.ok) throw new Error('获取积分设置失败');
  return res.json();
}

export async function updateCreditSetting(key: string, value: number): Promise<CreditSetting> {
  const res = await authFetch(`/api/admin/credit-settings/${key}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ value }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '更新失败' }));
    throw new Error(err.detail || '更新失败');
  }
  return res.json();
}

// --- Credit Transactions ---

export interface CreditTransaction {
  id: number;
  user_id: number;
  amount: number;
  balance_after: number;
  transaction_type: string;
  reference_type: string | null;
  reference_id: number | null;
  description: string | null;
  created_at: string;
}

export async function fetchMyTransactions(userId: number, page: number = 1): Promise<{ transactions: CreditTransaction[]; total: number }> {
  const res = await authFetch(`/api/users/${userId}/transactions?page=${page}&limit=50`, { cache: 'no-store' });
  if (!res.ok) throw new Error('获取交易记录失败');
  return res.json();
}
