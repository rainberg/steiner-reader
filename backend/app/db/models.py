"""SQLAlchemy ORM models for Steiner Reader."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship

from app.db.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ga_number = Column(String(20), index=True)
    title_de = Column(Text, nullable=False)
    title_zh = Column(Text)
    pdf_filename = Column(Text, nullable=False)
    cover_url = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    lectures = relationship("Lecture", back_populates="book", cascade="all, delete-orphan")
    translation_jobs = relationship("TranslationJob", back_populates="book", cascade="all, delete-orphan")


class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    title_de = Column(Text)
    lecture_date = Column(Date)
    location = Column(String(200))
    order_index = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    book = relationship("Book", back_populates="lectures")
    paragraphs = relationship("Paragraph", back_populates="lecture", cascade="all, delete-orphan")


class Paragraph(Base):
    __tablename__ = "paragraphs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False)
    order_index = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    lecture = relationship("Lecture", back_populates="paragraphs")
    sentences = relationship("Sentence", back_populates="paragraph", cascade="all, delete-orphan")


class Sentence(Base):
    __tablename__ = "sentences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    paragraph_id = Column(Integer, ForeignKey("paragraphs.id", ondelete="CASCADE"), nullable=False)
    order_index = Column(Integer, nullable=False)
    text_de = Column(Text, nullable=False)
    text_zh = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    paragraph = relationship("Paragraph", back_populates="sentences")


class TranslationJob(Base):
    __tablename__ = "translation_jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    status = Column(String(20), default="pending")  # pending/running/completed/failed
    total_sentences = Column(Integer)
    translated_count = Column(Integer, default=0)
    error_message = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    book = relationship("Book", back_populates="translation_jobs")
