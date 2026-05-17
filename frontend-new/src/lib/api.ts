import type { Book, Lecture, Paragraph, User } from '../types';

const API_BASE = 'http://localhost:8000/api';

function getToken(): string | null {
  return localStorage.getItem('token');
}

function setToken(token: string) {
  localStorage.setItem('token', token);
}

function removeToken() {
  localStorage.removeItem('token');
}

class ApiClient {
  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const token = getToken();
    const headers: Record<string, string> = {
      'Content-Type': 'application/json',
      ...options.headers as Record<string, string>,
    };
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
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
    const data = await this.request<{ access_token: string; user: User }>('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
    setToken(data.access_token);
    return data;
  }

  async register(username: string, email: string, password: string): Promise<{ access_token: string; user: User }> {
    const data = await this.request<{ access_token: string; user: User }>('/auth/register', {
      method: 'POST',
      body: JSON.stringify({ username, email, password }),
    });
    setToken(data.access_token);
    return data;
  }

  async getCurrentUser(): Promise<User | null> {
    try {
      return await this.request<User>('/auth/me');
    } catch {
      return null;
    }
  }

  logout() {
    removeToken();
  }

  // Books
  async getBooks(): Promise<Book[]> {
    return this.request<Book[]>('/books');
  }

  async getBook(id: number): Promise<Book> {
    return this.request<Book>(`/books/${id}`);
  }

  // Lectures
  async getLectures(bookId: number): Promise<Lecture[]> {
    return this.request<Lecture[]>(`/books/${bookId}/lectures`);
  }

  async getLecture(bookId: number, lectureId: number): Promise<Lecture> {
    return this.request<Lecture>(`/books/${bookId}/lectures/${lectureId}`);
  }

  // Paragraphs
  async getParagraphs(lectureId: number): Promise<Paragraph[]> {
    return this.request<Paragraph[]>(`/lectures/${lectureId}/paragraphs`);
  }

  // Translation
  async translateParagraph(paragraphId: number): Promise<Paragraph> {
    return this.request<Paragraph>(`/translate/paragraph/${paragraphId}`, {
      method: 'POST',
    });
  }
}

export const api = new ApiClient();
