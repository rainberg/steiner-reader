"""Pydantic schemas for API request/response validation."""

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


# --- Sentence ---

class SentenceBase(BaseModel):
    text_de: str
    text_zh: Optional[str] = None
    order_index: int


class SentenceCreate(BaseModel):
    text_de: str
    order_index: int


class SentenceResponse(SentenceBase):
    id: int
    content_de: str = ""
    content_zh: Optional[str] = None
    paragraph_id: int = 0
    sentence_index: int = 0
    is_heading: bool = False
    image_url: Optional[str] = None

    class Config:
        from_attributes = True


# --- Paragraph ---

class ParagraphBase(BaseModel):
    order_index: int


class ParagraphResponse(ParagraphBase):
    id: int
    content_de: str = ""
    content_zh: Optional[str] = None
    lecture_id: int = 0
    paragraph_index: int = 0
    sentences: list[SentenceResponse] = []

    class Config:
        from_attributes = True


# --- Lecture ---

class LectureBase(BaseModel):
    title_de: Optional[str] = None
    title_zh: Optional[str] = None
    lecture_date: Optional[date | str] = None
    location: Optional[str] = None
    order_index: int


class LectureCreate(LectureBase):
    pass


class LectureResponse(LectureBase):
    """Full lecture with all paragraphs and sentences (for reader page)."""
    id: int
    book_id: int
    paragraphs: list[ParagraphResponse] = []

    class Config:
        from_attributes = True


class LectureListItem(LectureBase):
    """Lightweight lecture for book detail / TOC — no paragraphs/sentences."""
    id: int
    book_id: int
    sentence_count: int = 0
    level: Optional[str] = "lecture"
    parent_id: Optional[int] = None
    image_count: int = 0
    translated_count: int = 0

    class Config:
        from_attributes = True


class LectureSummary(BaseModel):
    """Lecture list item (without paragraphs for performance)."""
    id: int
    title_de: Optional[str]
    title_zh: Optional[str] = None
    lecture_date: Optional[date | str] = None
    location: Optional[str]
    order_index: int
    sentence_count: int = 0
    paragraph_count: int = 0
    image_count: int = 0
    translated_count: int = 0
    level: Optional[str] = "lecture"
    parent_id: Optional[int] = None

    class Config:
        from_attributes = True


# --- Book ---

class BookBase(BaseModel):
    ga_number: Optional[str] = None
    title_de: str
    title_zh: Optional[str] = None
    pdf_filename: str


class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    cover_url: Optional[str]
    created_at: datetime
    lectures: list[LectureSummary] = []
    image_count: int = 0
    translated_count: int = 0

    class Config:
        from_attributes = True


class BookSummary(BaseModel):
    """Very small book row for the homepage."""
    id: int
    ga_number: Optional[str] = None
    title_de: str
    title_zh: Optional[str] = None
    pdf_filename: str
    cover_url: Optional[str] = None
    created_at: datetime
    lecture_count: int = 0
    sentence_count: int = 0
    image_count: int = 0
    translated_count: int = 0

    class Config:
        from_attributes = True


class BookDetail(BookResponse):
    """Book detail for TOC page — lectures include translation counts but no sentences."""
    lectures: list[LectureListItem] = []




# --- Translation ---

class TranslationJobResponse(BaseModel):
    id: int
    book_id: int
    status: str
    total_sentences: Optional[int]
    translated_count: int
    error_message: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TranslateRequest(BaseModel):
    book_id: int


class UploadResponse(BaseModel):
    book_id: Optional[int] = None
    message: str
    ga_number: Optional[str] = None
    stats: Optional[dict] = None


# --- Credit Settings ---

class CreditSettingResponse(BaseModel):
    id: int
    key: str
    value: int
    description: Optional[str] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class CreditSettingUpdateRequest(BaseModel):
    value: int


# --- Credit Transactions ---

class CreditTransactionResponse(BaseModel):
    id: int
    user_id: int
    amount: int
    balance_after: int
    transaction_type: str
    reference_type: Optional[str] = None
    reference_id: Optional[int] = None
    description: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


# --- Contributions ---

class ContributionDisplay(BaseModel):
    username: str
    contribution_type: str
    created_at: datetime


# --- Downloads ---

class DownloadPermission(BaseModel):
    has_permission: bool
    access_types: list[str] = []


class PurchaseResult(BaseModel):
    success: bool
    credits_remaining: int
    message: str


# --- Sentence Editing ---

class EditSentenceRequest(BaseModel):
    field: str  # "text_de" or "text_zh"
    new_value: str


class EditSentenceResult(BaseModel):
    success: bool
    new_text: str
    cost: int
    credits_remaining: int


class EditLogEntry(BaseModel):
    id: int
    user_id: int
    username: str
    sentence_id: int
    field_changed: str
    old_value: Optional[str] = None
    new_value: Optional[str] = None
    credits_cost: int
    created_at: datetime

    class Config:
        from_attributes = True
