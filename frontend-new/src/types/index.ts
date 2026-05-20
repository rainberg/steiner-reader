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
  contributors?: ContributionDisplay[];
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

export interface UploadResponse {
  book_id?: number;
  message: string;
  ga_number?: string | null;
  chapters?: number;
  stats?: Record<string, number>;
}

export interface DownloadPermission {
  has_permission: boolean;
  access_types: string[];
}

export interface PurchaseResult {
  success: boolean;
  credits_remaining: number;
  message: string;
}

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

export interface ContributionDisplay {
  username: string;
  contribution_type: string;
  created_at: string;
}

export interface CreditSetting {
  id: number;
  key: string;
  value: number;
  description: string | null;
  updated_at: string | null;
}

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
