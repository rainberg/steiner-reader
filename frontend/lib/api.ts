const API_BASE = process.env.NEXT_PUBLIC_API_BASE || process.env.NEXT_PUBLIC_API_URL || '';
const AUTH_BASE = process.env.NEXT_PUBLIC_AUTH_URL || 'https://auth.3mudi.com';
const AUTH_APP = 'steiner';

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
  type?: string | null;
  parent_id?: number | null;
  sentence_count: number;
  paragraph_count?: number;
  translated_count?: number;
  image_count?: number;
  is_published?: boolean;
  edit_translation_cost?: number;
  edit_source_cost?: number;
  paragraphs?: Paragraph[];
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
  is_published?: boolean;
  edit_translation_cost?: number;
  edit_source_cost?: number;
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
  id: string;
  display_name: string;
  email: string | null;
  phone: string | null;
  role: string;
  credits: number;
  username?: string;
  is_active: boolean;
  is_admin?: boolean;
  created_at?: string;
}

export interface AuthResponse {
  access_token: string;
  refresh_token: string;
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
  user_credits: number | null;
  can_afford: boolean | null;
}

export interface TranslationStatus {
  lecture_id: number;
  total: number;
  translated: number;
  completed: boolean;
  is_translating?: boolean;
  is_running?: boolean;
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

export interface SliderCaptcha {
  captcha_id: string;
  bg_image: string;
  slider_image: string;
  y_position: number;
  puzzle_width: number;
}

function getToken(): string | null {
  if (typeof window === 'undefined') return null;
  return localStorage.getItem('access_token');
}

function getRefreshToken(): string | null {
  if (typeof window === 'undefined') return null;
  return localStorage.getItem('refresh_token');
}

function authHeaders(extra: Record<string, string> = {}): Record<string, string> {
  const token = getToken();
  return token ? { ...extra, Authorization: `Bearer ${token}` } : extra;
}

async function refreshAccessToken(): Promise<boolean> {
  const refreshToken = getRefreshToken();
  if (!refreshToken) return false;

  try {
    const res = await fetch(`${AUTH_BASE}/api/auth/refresh`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ refresh_token: refreshToken }),
    });
    if (!res.ok) return false;

    const data = await res.json();
    localStorage.setItem('access_token', data.access_token);
    if (data.refresh_token) {
      localStorage.setItem('refresh_token', data.refresh_token);
    }
    return true;
  } catch {
    return false;
  }
}

async function authFetch(url: string, options: RequestInit = {}): Promise<Response> {
  let res = await fetch(`${API_BASE}${url}`, {
    ...options,
    headers: authHeaders((options.headers as Record<string, string>) || {}),
  });

  if (res.status === 401) {
    const refreshed = await refreshAccessToken();
    if (refreshed) {
      res = await fetch(`${API_BASE}${url}`, {
        ...options,
        headers: authHeaders((options.headers as Record<string, string>) || {}),
      });
    }
  }

  return res;
}

async function authServiceFetch(path: string, options: RequestInit = {}): Promise<Response> {
  const headers = authHeaders((options.headers as Record<string, string>) || {});
  let res = await fetch(`${AUTH_BASE}${path}`, {
    ...options,
    headers,
  });

  if (res.status === 401) {
    const refreshed = await refreshAccessToken();
    if (refreshed) {
      res = await fetch(`${AUTH_BASE}${path}`, {
        ...options,
        headers: authHeaders((options.headers as Record<string, string>) || {}),
      });
    }
  }

  return res;
}

export function getStoredUser(): User | null {
  if (typeof window === 'undefined') return null;
  const raw = localStorage.getItem('auth_user');
  return raw ? JSON.parse(raw) : null;
}

export function getUserCredits(): number {
  const user = getStoredUser();
  if (!user) return 0;
  return typeof user.credits === 'number' ? user.credits : parseFloat(String(user.credits)) || 0;
}

export function isAdmin(): boolean {
  const user = getStoredUser();
  return user?.role === 'admin';
}

export function saveAuth(data: AuthResponse) {
  localStorage.setItem('access_token', data.access_token);
  localStorage.setItem('refresh_token', data.refresh_token);
  localStorage.setItem('auth_user', JSON.stringify(data.user));
}

export function clearAuth() {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  localStorage.removeItem('auth_user');
}

export function updateStoredCredits(credits: number) {
  const user = getStoredUser();
  if (!user) return;
  user.credits = credits;
  localStorage.setItem('auth_user', JSON.stringify(user));
  window.dispatchEvent(new Event('storage'));
}

export async function generateCaptcha(): Promise<SliderCaptcha> {
  const res = await fetch(`${AUTH_BASE}/api/auth/captcha/generate`);
  if (!res.ok) throw new Error('获取滑块验证码失败');
  return res.json();
}

export async function verifyCaptcha(captchaId: string, xPos: number): Promise<{ success: boolean; message: string }> {
  const res = await fetch(`${AUTH_BASE}/api/auth/captcha/verify`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ captcha_id: captchaId, x_position: xPos }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '滑块验证失败' }));
    throw new Error(err.detail || '滑块验证失败');
  }
  return res.json();
}

export async function sendSmsCode(phone: string, captchaId: string, captchaX: number): Promise<{ message: string }> {
  const res = await fetch(`${AUTH_BASE}/api/auth/sms/send`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ phone, captcha_id: captchaId, captcha_x: captchaX }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '发送验证码失败' }));
    throw new Error(err.detail || '发送验证码失败');
  }
  return res.json();
}

async function handleAuthResponse(res: Response): Promise<AuthResponse> {
  const data = await res.json();
  const authData: AuthResponse = {
    access_token: data.access_token,
    refresh_token: data.refresh_token,
    token_type: data.token_type,
    user: data.user,
  };
  saveAuth(authData);
  return authData;
}

async function throwAuthError(res: Response, fallbackMsg: string): Promise<never> {
  const err = await res.json().catch(() => ({ detail: fallbackMsg }));
  throw new Error(err.detail || fallbackMsg);
}

export async function register(email: string, password: string, displayName?: string): Promise<AuthResponse> {
  const res = await fetch(`${AUTH_BASE}/api/auth/register/email`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password, display_name: displayName, app: AUTH_APP }),
  });
  if (!res.ok) return throwAuthError(res, '注册失败');
  return handleAuthResponse(res);
}

export async function login(account: string, password: string): Promise<AuthResponse> {
  const res = await fetch(`${AUTH_BASE}/api/auth/login/password`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ account, password, app: AUTH_APP }),
  });
  if (!res.ok) return throwAuthError(res, '登录失败');
  return handleAuthResponse(res);
}

export async function loginByPhone(phone: string, code: string): Promise<AuthResponse> {
  const res = await fetch(`${AUTH_BASE}/api/auth/login/phone`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ phone, code, app: AUTH_APP }),
  });
  if (!res.ok) return throwAuthError(res, '登录失败');
  return handleAuthResponse(res);
}

export async function registerByPhone(phone: string, code: string, password: string, displayName?: string): Promise<AuthResponse> {
  const res = await fetch(`${AUTH_BASE}/api/auth/register/phone`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ phone, code, password, display_name: displayName, app: AUTH_APP }),
  });
  if (!res.ok) return throwAuthError(res, '注册失败');
  return handleAuthResponse(res);
}

export async function refreshAuth(): Promise<AuthResponse> {
  const refreshToken = getRefreshToken();
  if (!refreshToken) throw new Error('无刷新令牌');
  const res = await fetch(`${AUTH_BASE}/api/auth/refresh`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ refresh_token: refreshToken }),
  });
  if (!res.ok) return throwAuthError(res, '刷新令牌失败');
  return handleAuthResponse(res);
}

export async function fetchMe(): Promise<User> {
  const res = await authFetch('/api/auth/me', { cache: 'no-store' });
  if (!res.ok) throw new Error('未登录');
  const data = await res.json();
  const updatedUser: User = {
    id: data.id,
    display_name: data.display_name,
    email: data.email,
    phone: data.phone,
    role: data.role,
    credits: data.credits,
    is_active: data.is_active,
    is_admin: data.role === 'admin',
    created_at: data.created_at,
  };
  localStorage.setItem('auth_user', JSON.stringify(updatedUser));
  return updatedUser;
}

export async function updateUserProfile(displayName?: string, oldPassword?: string, password?: string): Promise<User> {
  const body: Record<string, string> = {};
  if (displayName !== undefined) body.display_name = displayName;
  if (oldPassword !== undefined) body.old_password = oldPassword;
  if (password !== undefined) body.password = password;
  const res = await authServiceFetch('/api/auth/me', {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) return throwAuthError(res, '更新失败');
  const data = await res.json();
  const updatedUser: User = {
    id: data.id,
    display_name: data.display_name,
    email: data.email,
    phone: data.phone,
    role: data.role,
    credits: data.credits,
    is_active: data.is_active,
    is_admin: data.role === 'admin',
    created_at: data.created_at,
  };
  localStorage.setItem('auth_user', JSON.stringify(updatedUser));
  return updatedUser;
}

export async function changePassword(oldPassword: string, newPassword: string): Promise<User> {
  return updateUserProfile(undefined, oldPassword, newPassword);
}

export async function changeEmail(email: string, password?: string): Promise<User> {
  const res = await authServiceFetch('/api/auth/me', {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, old_password: password }),
  });
  if (!res.ok) return throwAuthError(res, '修改邮箱失败');
  const data = await res.json();
  const updatedUser: User = {
    id: data.id,
    display_name: data.display_name,
    email: data.email,
    phone: data.phone,
    role: data.role,
    credits: data.credits,
    is_active: data.is_active,
    is_admin: data.role === 'admin',
    created_at: data.created_at,
  };
  localStorage.setItem('auth_user', JSON.stringify(updatedUser));
  return updatedUser;
}

export async function changeUsername(displayName: string, password?: string): Promise<User> {
  return updateUserProfile(displayName, password);
}

export async function fetchMyTransactions(page: number = 1, pageSize: number = 20) {
  const params = new URLSearchParams({ page: String(page), page_size: String(pageSize) });
  const res = await authServiceFetch(`/api/credits/logs?${params}`, { cache: 'no-store' });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '获取积分记录失败' }));
    throw new Error(err.detail || '获取积分记录失败');
  }
  return res.json();
}

export async function fetchCreditBalance(): Promise<{ credits: number }> {
  const res = await authServiceFetch('/api/credits/balance', { cache: 'no-store' });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '获取积分余额失败' }));
    throw new Error(err.detail || '获取积分余额失败');
  }
  return res.json();
}

export async function adminListUsers(page: number = 1, pageSize: number = 20, search: string = '') {
  const params = new URLSearchParams({ page: String(page), page_size: String(pageSize) });
  if (search) params.set('search', search);
  const res = await authServiceFetch(`/api/admin/users?${params}`);
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '获取用户列表失败' }));
    throw new Error(err.detail || '获取用户列表失败');
  }
  return res.json();
}

export async function adminSetCredits(userId: string | number, credits: number, remark?: string) {
  const res = await authServiceFetch(`/api/admin/users/${userId}/set-credits`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ credits, remark }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '设置积分失败' }));
    throw new Error(err.detail || '设置积分失败');
  }
  return res.json();
}

export async function adminAddCredits(userId: string | number, amount: number, remark?: string) {
  const res = await authServiceFetch(`/api/admin/users/${userId}/add-credits`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ credits: amount, remark }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: '充值失败' }));
    throw new Error(err.detail || '充值失败');
  }
  return res.json();
}

export async function fetchBooks(): Promise<Book[]> {
  const res = await fetch(`${API_BASE}/api/books`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch books');
  return res.json();
}

export async function fetchBookSummaries(): Promise<BookSummary[]> {
  const res = await fetch(`${API_BASE}/api/books/summary`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch book summaries');
  return res.json();
}

export async function fetchBook(bookId: number): Promise<Book> {
  const res = await fetch(`${API_BASE}/api/books/${bookId}`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch book');
  return res.json();
}

export async function fetchLecture(bookIdOrLectureId: number, maybeLectureId?: number): Promise<Lecture> {
  const url = maybeLectureId === undefined
    ? `/api/lectures/${bookIdOrLectureId}`
    : `/api/books/${bookIdOrLectureId}/lectures/${maybeLectureId}`;
  const res = await authFetch(url, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch lecture');
  return res.json();
}

export async function fetchParagraphs(lectureId: number): Promise<Paragraph[]> {
  const res = await authFetch(`/api/lectures/${lectureId}/paragraphs`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch paragraphs');
  return res.json();
}

export async function fetchSentences(paragraphId: number): Promise<Sentence[]> {
  const res = await fetch(`${API_BASE}/api/paragraphs/${paragraphId}/sentences`, { cache: 'no-store' });
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

export async function getTranslationCost(lectureId: number): Promise<TranslationCost> {
  const res = await authFetch(`/api/lectures/${lectureId}/translation-cost`, { cache: 'no-store' });
  if (!res.ok) throw new Error('获取翻译费用失败');
  return res.json();
}

export async function getTranslationStatus(lectureId: number): Promise<TranslationStatus> {
  const res = await authFetch(`/api/lectures/${lectureId}/translation-status?_t=${Date.now()}`, { cache: 'no-store' });
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
  const res = await fetch(`${API_BASE}/api/lectures/${lectureId}/images`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch images');
  return res.json();
}


export interface BookGroup {
  id: string;
  ga_prefix: string;
  title_de: string;
  title_zh: string | null;
  cover_url: string | null;
  book_count: number;
  group?: string;
  lecture_count?: number;
  books?: BookSummary[];
  sentence_count: number;
  translated_count: number;
}

export interface CreditSetting {
  key?: string;
  value?: number;
  id: number;
  action: string;
  price: number;
  description: string | null;
  updated_at: string | null;
}

export interface CreditTransaction {
  id: number;
  user_id: string;
  amount: number;
  balance_after: number;
  transaction_type: string;
  reference_type: string | null;
  reference_id: number | null;
  description: string | null;
  created_at: string;
}

export interface DownloadPermission {
  has_permission: boolean;
  access_types: string[];
}

export interface ContributionDisplay {
  user_id?: string;
  display_name: string;
  contribution_type: string;
  cost?: number;
  grants_download?: boolean;
  created_at: string | null;
}

export interface EditLogEntry {
  id: number;
  user_id: string;
  username: string;
  sentence_id: number;
  field_changed: string;
  old_value: string | null;
  new_value: string | null;
  credits_cost: number;
  created_at: string;
}

export interface RevisionItem {
  id: number;
  field: string;
  new_value: string;
  user_id: string;
  username: string;
  vote_count: number;
  created_at: string;
}

export async function fetchBookGroups(): Promise<BookGroup[]> {
  const res = await fetch(`${API_BASE}/api/books/groups`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch book groups');
  return res.json();
}

export async function fetchBookSummariesPaginated(
  pageOrOpts: number | { page: number; page_size: number; search?: string; sort_by?: string; sort_dir?: string } = 1,
  pageSize: number = 20,
): Promise<any> {
  const opts = typeof pageOrOpts === 'number'
    ? { page: pageOrOpts, page_size: pageSize }
    : pageOrOpts;
  const params = new URLSearchParams({
    page: String(opts.page),
    page_size: String(opts.page_size),
  });
  if (opts.sort_by) params.set('sort_by', opts.sort_by);
  if (opts.sort_dir) params.set('sort_dir', opts.sort_dir);
  const res = await fetch(`${API_BASE}/api/books/summary?${params}`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch book summaries');
  return res.json();
}

export async function fetchBookCount(search?: string): Promise<number> {
  const res = await fetch(`${API_BASE}/api/books/count`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch book count');
  const data = await res.json();
  return data.count;
}

export async function getDownloadPermission(lectureId: number): Promise<DownloadPermission> {
  const res = await authFetch(`/api/lectures/${lectureId}/download-permission`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to check download permission');
  return res.json();
}

export async function downloadLecturePdf(lectureId: number): Promise<Blob> {
  const res = await authFetch(`/api/lectures/${lectureId}/download-pdf`, { cache: 'no-store' });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'PDF 下载失败' }));
    throw new Error(err.detail || 'PDF 下载失败');
  }
  return res.blob();
}

export async function editSentence(
  sentenceId: number,
  fieldOrObj: string | { field: string; new_value: string },
  newValue?: string,
): Promise<{ success: boolean; new_text: string; cost: number; credits_remaining: number }> {
  const body = typeof fieldOrObj === 'string'
    ? { field: fieldOrObj, new_value: newValue || '' }
    : fieldOrObj;
  const res = await authFetch(`/api/sentences/${sentenceId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Edit failed' }));
    throw new Error(err.detail || 'Edit failed');
  }
  return res.json();
}

export async function fetchSentenceEdits(sentenceId: number): Promise<EditLogEntry[]> {
  const res = await fetch(`${API_BASE}/api/sentences/${sentenceId}/edits`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch sentence edits');
  return res.json();
}

export async function fetchContributions(lectureId: number): Promise<ContributionDisplay[]> {
  const res = await authFetch(`/api/lectures/${lectureId}/contributions`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch contributions');
  return res.json();
}

export async function fetchSentenceRevisions(sentenceId: number): Promise<RevisionItem[]> {
  const res = await fetch(`${API_BASE}/api/sentences/${sentenceId}/revisions`, { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch revisions');
  return res.json();
}

export async function voteRevision(
  sentenceId: number,
  revisionId: number,
): Promise<{ success: boolean; vote_count: number; credits_remaining: number }> {
  const res = await authFetch(`/api/sentences/${sentenceId}/revisions/${revisionId}/vote`, {
    method: 'POST',
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Vote failed' }));
    throw new Error(err.detail || 'Vote failed');
  }
  return res.json();
}

export async function fetchCreditSettings(): Promise<CreditSetting[]> {
  const res = await authFetch('/api/admin/credit-settings', { cache: 'no-store' });
  if (!res.ok) throw new Error('Failed to fetch credit settings');
  return res.json();
}

export async function updateCreditSetting(
  settingId: string | number,
  dataOrValue: { price?: number; description?: string } | number,
): Promise<CreditSetting> {
  const body = typeof dataOrValue === 'number'
    ? { price: dataOrValue }
    : dataOrValue;
  const res = await authFetch(`/api/admin/credit-settings/${settingId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error('Failed to update credit setting');
  return res.json();
}

export async function adminUpdateUser(
  userId: string | number,
  data: { role?: string; is_active?: boolean; username?: string; email?: string; display_name?: string },
): Promise<User> {
  const updates: Promise<any>[] = [];
  if (data.role !== undefined) {
    updates.push(
      authServiceFetch(`/api/admin/users/${userId}/role`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ role: data.role }),
      })
    );
  }
  if (data.is_active !== undefined) {
    updates.push(
      authServiceFetch(`/api/admin/users/${userId}/toggle-active`, {
        method: 'PUT',
      })
    );
  }
  await Promise.all(updates);
  return (await fetchMe());
}

export async function adminResetPassword(
  userId: string | number,
  newPassword: string,
): Promise<{ success: boolean; message?: string }> {
  const res = await authServiceFetch(`/api/admin/users/${userId}/reset-password`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ new_password: newPassword }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({ detail: 'Reset failed' }));
    throw new Error(err.detail || 'Reset failed');
  }
  return res.json();
}

export async function generateSliderCaptcha(): Promise<SliderCaptcha> {
  return generateCaptcha();
}

export async function verifySliderCaptcha(
  captchaId: string,
  xPos: number,
): Promise<{ success: boolean; message: string }> {
  return verifyCaptcha(captchaId, xPos);
}

export async function loginWithPassword(
  account: string,
  password: string,
): Promise<AuthResponse> {
  return login(account, password);
}

export async function loginWithPhone(phone: string, code: string): Promise<AuthResponse> {
  return loginByPhone(phone, code);
}

export async function registerWithEmail(
  email: string,
  password: string,
  displayName?: string,
): Promise<AuthResponse> {
  return register(email, password, displayName);
}

export async function registerWithPhone(
  phone: string,
  code: string,
  password: string,
  displayName?: string,
): Promise<AuthResponse> {
  return registerByPhone(phone, code, password, displayName);
}
