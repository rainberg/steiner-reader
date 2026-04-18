"""Pydantic schemas for API request/response validation."""

from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


# ─── Sentence ──

class SentenceBase(BaseModel):
    text_de: str
    text_zh: Optional[str] = None
    order_index: int


class SentenceCreate(BaseModel):
    text_de: str
    order_index: int


class SentenceResponse(SentenceBase):
    id: int

    class Config:
        from_attributes = True


# ─── Paragraph ──

class ParagraphBase(BaseModel):
    order_index: int


class ParagraphResponse(ParagraphBase):
    id: int
    sentences: list[SentenceResponse] = []

    class Config:
        from_attributes = True


# ─── Lecture ──

class LectureBase(BaseModel):
    title_de: Optional[str] = None
    lecture_date: Optional[date] = None
    location: Optional[str] = None
    order_index: int


class LectureCreate(LectureBase):
    pass


class LectureResponse(LectureBase):
    id: int
    book_id: int
    paragraphs: list[ParagraphResponse] = []

    class Config:
        from_attributes = True


class LectureSummary(BaseModel):
    """Lecture list item (without paragraphs for performance)."""
    id: int
    title_de: Optional[str]
    lecture_date: Optional[date]
    location: Optional[str]
    order_index: int
    sentence_count: int = 0

    class Config:
        from_attributes = True


# ─── Book ──

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

    class Config:
        from_attributes = True


class BookDetail(BookResponse):
    """Full book with all lectures, paragraphs, sentences."""
    lectures: list[LectureResponse] = []


# ─── Upload ──

class UploadResponse(BaseModel):
    book_id: int
    message: str
    ga_number: Optional[str] = None
    stats: dict = {}


# ─── Translation ──

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
