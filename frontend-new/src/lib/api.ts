import type { Book, Lecture, Paragraph, User } from '../types';

const API_BASE = 'http://localhost:8000/api';

class ApiClient {
  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const response = await fetch(`${API_BASE}${endpoint}`, {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });

    if (!response.ok) {
      throw new Error(`API Error: ${response.status}`);
    }

    return response.json();
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

  // Auth
  async login(email: string, password: string): Promise<User> {
    return this.request<User>('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });
  }

  async register(email: string, password: string, name?: string): Promise<User> {
    return this.request<User>('/auth/register', {
      method: 'POST',
      body: JSON.stringify({ email, password, name }),
    });
  }

  async getCurrentUser(): Promise<User | null> {
    try {
      return await this.request<User>('/auth/me');
    } catch {
      return null;
    }
  }

  // Translation
  async translateParagraph(paragraphId: number): Promise<Paragraph> {
    return this.request<Paragraph>(`/translate/paragraph/${paragraphId}`, {
      method: 'POST',
    });
  }
}

export const api = new ApiClient();
