export interface Book {
  id: number;
  ga_number: string | null;
  title_de: string;
  title_zh: string | null;
  pdf_filename?: string;
  cover_url?: string | null;
  created_at?: string;
  lectures?: LectureSummary[];
  image_count?: number;
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

export interface BookGroup {
  group: string;
  book_count: number;
  lecture_count: number;
  sentence_count: number;
  books: BookSummary[];
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
  can_download_pdf?: boolean;
  can_edit?: boolean;
  download_notice?: string;
  download_lecture_cost?: number;
  edit_translation_cost?: number;
  edit_source_cost?: number;
}

export interface LectureSummary {
  id: number;
  title_de: string | null;
  title_zh?: string | null;
  lecture_date: string | null;
  location: string | null;
  order_index: number;
  sentence_count: number;
  image_count: number;
  translated_count: number;
  level?: string | null;
  parent_id?: number | null;
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

export interface User {
  id: number;
  username: string;
  email: string;
  credits: number;
  is_admin?: number;
  created_at?: string;
}
