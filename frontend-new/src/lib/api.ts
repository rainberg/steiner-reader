import type { Book, Lecture, Paragraph, User } from '../types';

const API_BASE = '';

function getToken(): string | null {
  return localStorage.getItem('steiner_token');
}

function setToken(token: string) {
  localStorage.setItem('steiner_token', token);
}

function removeToken() {
  localStorage.removeItem('steiner_token');
}

function authHeaders(extra: Record<string, string> = {}): Record<string, string> {
  const token = getToken();
  return token ? { ...extra, Authorization: `Bearer ${token}` } : extra;
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
        removeToken();
      }
      throw new Error(`API Error: ${response.status}`);
    }

    return response.json();
  }

  // Auth
  async login(email: string, password: string): Promise<{ access_token: string; user: User }> {
    const data = await this.request<{ access_token: string; user: User }>('/api/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
    setToken(data.access_token);
    localStorage.setItem('steiner_user', JSON.stringify(data.user));
    return data;
  }

  async register(username: string, email: string, password: string): Promise<{ access_token: string; user: User }> {
    const data = await this.request<{ access_token: string; user: User }>('/api/auth/register', {
      method: 'POST',
      body: JSON.stringify({ username, email, password }),
    });
    setToken(data.access_token);
    localStorage.setItem('steiner_user', JSON.stringify(data.user));
    return data;
  }

  async getCurrentUser(): Promise<User | null> {
    try {
      return await this.request<User>('/api/auth/me');
    } catch {
      return null;
    }
  }

  logout() {
    removeToken();
    localStorage.removeItem('steiner_user');
  }

  // Books
  async getBooks(): Promise<Book[]> {
    return this.request<Book[]>('/api/books');
  }

  async getBook(id: number): Promise<Book> {
    return this.request<Book>(`/api/books/${id}`);
  }

  // Lectures
  async getLectures(bookId: number): Promise<Lecture[]> {
    return this.request<Lecture[]>(`/api/books/${bookId}/lectures`);
  }

  async getLecture(bookId: number, lectureId: number): Promise<Lecture> {
    return this.request<Lecture>(`/api/books/${bookId}/lectures/${lectureId}`);
  }

  // Paragraphs
  async getParagraphs(lectureId: number): Promise<Paragraph[]> {
    return this.request<Paragraph[]>(`/api/lectures/${lectureId}/paragraphs`);
  }

  // Translation
  async translateParagraph(paragraphId: number): Promise<Paragraph> {
    return this.request<Paragraph>(`/api/translate/paragraph/${paragraphId}`, {
      method: 'POST',
    });
  }
}

export const api = new ApiClient();
