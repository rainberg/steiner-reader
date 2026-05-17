export interface Book {
  id: number;
  title: string;
  author: string;
  description: string;
  cover_image?: string;
  category: string;
  created_at?: string;
  updated_at?: string;
}

export interface Lecture {
  id: number;
  book_id: number;
  title: string;
  number: number;
  date?: string;
  created_at?: string;
}

export interface Paragraph {
  id: number;
  lecture_id: number;
  original_text: string;
  translated_text?: string;
  order: number;
  created_at?: string;
  updated_at?: string;
}

export interface User {
  id: number;
  email: string;
  name?: string;
  credits: number;
  is_admin: boolean;
  created_at?: string;
}
