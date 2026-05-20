import type {
  Book,
  BookSummary,
  BookGroup,
  Lecture,
  Paragraph,
  User,
  AuthResponse,
  TranslationCost,
  TranslationStatus,
  TranslateResult,
  LectureImage,
  UploadResponse,
  DownloadPermission,
  PurchaseResult,
  EditSentenceRequest,
  EditSentenceResult,
  EditLogEntry,
  ContributionDisplay,
  CreditSetting,
  CreditTransaction,
} from '../types';

const API_BASE = '';

function getToken(): string | null {
  return localStorage.getItem('steiner_token');
}

function authHeaders(extra: Record<string, string> = {}): Record<string, string> {
  const token = getToken();
  return token ? { ...extra, Authorization: `Bearer ${token}` } : extra;
}

export function getStoredUser(): User | null {
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

class ApiClient {
  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const headers = authHeaders((options.headers as Record<string, string>) || {});
    if (!headers['Content-Type'] && !(options.body instanceof FormData)) {
      headers['Content-Type'] = 'application/json';
    }

    const response = await fetch(`${API_BASE}${endpoint}`, {
      headers,
      ...options,
    });

    if (!response.ok) {
      if (response.status === 401) {
        clearAuth();
      }
      const err = await response.json().catch(() => ({ detail: `请求失败 (${response.status})` }));
      throw new Error(err.detail || `请求失败 (${response.status})`);
    }

    return response.json();
  }

  async login(email: string, password: string): Promise<AuthResponse> {
    const data = await this.request<AuthResponse>('/api/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
    saveAuth(data);
    return data;
  }

  async register(username: string, email: string, password: string): Promise<AuthResponse> {
    const data = await this.request<AuthResponse>('/api/auth/register', {
      method: 'POST',
      body: JSON.stringify({ username, email, password }),
    });
    saveAuth(data);
    return data;
  }

  async fetchMe(): Promise<User> {
    return this.request<User>('/api/auth/me');
  }

  async getCurrentUser(): Promise<User | null> {
    try {
      return await this.request<User>('/api/auth/me');
    } catch {
      return null;
    }
  }

  logout() {
    clearAuth();
  }

  async changePassword(oldPassword: string, newPassword: string): Promise<void> {
    await this.request<void>('/api/auth/change-password', {
      method: 'PUT',
      body: JSON.stringify({ old_password: oldPassword, new_password: newPassword }),
    });
  }

  async changeEmail(email: string, password: string): Promise<void> {
    await this.request<void>('/api/auth/change-email', {
      method: 'PUT',
      body: JSON.stringify({ email, password }),
    });
  }

  async changeUsername(username: string, password: string): Promise<{ success: boolean; message: string; username: string }> {
    return this.request<{ success: boolean; message: string; username: string }>('/api/auth/change-username', {
      method: 'PUT',
      body: JSON.stringify({ username, password }),
    });
  }

  async getBooks(): Promise<Book[]> {
    return this.request<Book[]>('/api/books');
  }

  async getBookSummaries(): Promise<BookSummary[]> {
    return this.request<BookSummary[]>('/api/books/summary');
  }

  async getBookGroups(): Promise<BookGroup[]> {
    return this.request<BookGroup[]>('/api/books/groups');
  }

  async getBook(id: number): Promise<Book> {
    return this.request<Book>(`/api/books/${id}`);
  }

  async uploadPdf(file: File): Promise<UploadResponse> {
    const formData = new FormData();
    formData.append('file', file);
    return this.request<UploadResponse>('/api/books/upload', {
      method: 'POST',
      body: formData,
    });
  }

  async getLecture(bookId: number, lectureId: number): Promise<Lecture> {
    return this.request<Lecture>(`/api/books/${bookId}/lectures/${lectureId}`);
  }

  async getTranslationCost(lectureId: number): Promise<TranslationCost> {
    return this.request<TranslationCost>(`/api/lectures/${lectureId}/translation-cost`);
  }

  async getTranslationStatus(lectureId: number): Promise<TranslationStatus> {
    return this.request<TranslationStatus>(`/api/lectures/${lectureId}/translation-status`);
  }

  async translateLecture(lectureId: number): Promise<TranslateResult> {
    return this.request<TranslateResult>(`/api/lectures/${lectureId}/translate`, {
      method: 'POST',
    });
  }

  async fetchLectureImages(lectureId: number): Promise<LectureImage[]> {
    return this.request<LectureImage[]>(`/api/lectures/${lectureId}/images`);
  }

  async getParagraphs(lectureId: number): Promise<Paragraph[]> {
    return this.request<Paragraph[]>(`/api/lectures/${lectureId}/paragraphs`);
  }

  async getDownloadPermission(lectureId: number): Promise<DownloadPermission> {
    try {
      return await this.request<DownloadPermission>(`/api/lectures/${lectureId}/download-permission`);
    } catch {
      return { has_permission: false, access_types: [] };
    }
  }

  async purchaseDownloadAccess(lectureId: number): Promise<PurchaseResult> {
    return this.request<PurchaseResult>(`/api/lectures/${lectureId}/purchase-download`, {
      method: 'POST',
    });
  }

  async editSentence(sentenceId: number, data: EditSentenceRequest): Promise<EditSentenceResult> {
    return this.request<EditSentenceResult>(`/api/sentences/${sentenceId}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  }

  async fetchSentenceEdits(sentenceId: number): Promise<EditLogEntry[]> {
    try {
      return await this.request<EditLogEntry[]>(`/api/sentences/${sentenceId}/edits`);
    } catch {
      return [];
    }
  }

  async fetchContributions(lectureId: number): Promise<ContributionDisplay[]> {
    try {
      const data = await this.request<{ contributions: ContributionDisplay[] }>(`/api/lectures/${lectureId}/contributions`);
      return data.contributions || [];
    } catch {
      return [];
    }
  }

  async fetchCreditSettings(): Promise<CreditSetting[]> {
    return this.request<CreditSetting[]>('/api/admin/credit-settings');
  }

  async updateCreditSetting(key: string, value: number): Promise<CreditSetting> {
    return this.request<CreditSetting>(`/api/admin/credit-settings/${key}`, {
      method: 'PUT',
      body: JSON.stringify({ value }),
    });
  }

  async adminAddCredits(userId: number, amount: number): Promise<{ success: boolean; username: string; added: number; new_credits: number }> {
    return this.request<{ success: boolean; username: string; added: number; new_credits: number }>(`/api/admin/users/${userId}/credits/add`, {
      method: 'POST',
      body: JSON.stringify({ amount }),
    });
  }

  async adminUpdateUser(userId: number, data: { username?: string; email?: string }): Promise<{ success: boolean; user_id: number; username: string; email: string }> {
    return this.request<{ success: boolean; user_id: number; username: string; email: string }>(`/api/admin/users/${userId}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  }

  async adminResetPassword(userId: number, newPassword: string): Promise<{ success: boolean; message: string }> {
    return this.request<{ success: boolean; message: string }>(`/api/admin/users/${userId}/reset-password`, {
      method: 'POST',
      body: JSON.stringify({ new_password: newPassword }),
    });
  }

  async fetchMyTransactions(userId: number, page: number = 1): Promise<{ transactions: CreditTransaction[]; total: number }> {
    return this.request<{ transactions: CreditTransaction[]; total: number }>(`/api/users/${userId}/transactions?page=${page}&limit=50`);
  }
}

export const api = new ApiClient();
