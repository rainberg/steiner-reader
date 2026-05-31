"""SQLAlchemy ORM models for Steiner Reader."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Date, Boolean, Numeric
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

    lectures = relationship("Lecture", back_populates="book", cascade="all, delete-orphan",
                            foreign_keys="Lecture.book_id")
    translation_jobs = relationship("TranslationJob", back_populates="book", cascade="all, delete-orphan")


class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    title_de = Column(Text)
    title_zh = Column(String(200))
    lecture_date = Column(Date)
    location = Column(String(200))
    order_index = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    parent_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=True)
    level = Column(String(10), default="lecture")
    is_published = Column(Boolean, default=False, server_default="false")
    is_translating = Column(Boolean, default=False, server_default="false")
    translate_progress = Column(Integer, default=0, server_default="0")
    translate_total = Column(Integer, default=0, server_default="0")

    book = relationship("Book", back_populates="lectures", foreign_keys=[book_id])
    paragraphs = relationship("Paragraph", back_populates="lecture", cascade="all, delete-orphan",
                              foreign_keys="Paragraph.lecture_id")
    images = relationship("LectureImage", back_populates="lecture", cascade="all, delete-orphan",
                          foreign_keys="LectureImage.lecture_id")
    children = relationship("Lecture", back_populates="parent", foreign_keys=[parent_id])
    parent = relationship("Lecture", back_populates="children", remote_side="Lecture.id", foreign_keys=[parent_id])


class Paragraph(Base):
    __tablename__ = "paragraphs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False)
    order_index = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    lecture = relationship("Lecture", back_populates="paragraphs", foreign_keys=[lecture_id])
    sentences = relationship("Sentence", back_populates="paragraph", cascade="all, delete-orphan",
                             foreign_keys="Sentence.paragraph_id")


class Sentence(Base):
    __tablename__ = "sentences"

    id = Column(Integer, primary_key=True, autoincrement=True)
    paragraph_id = Column(Integer, ForeignKey("paragraphs.id", ondelete="CASCADE"), nullable=False)
    order_index = Column(Integer, nullable=False)
    text_de = Column(Text, nullable=False)
    text_zh = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    paragraph = relationship("Paragraph", back_populates="sentences", foreign_keys=[paragraph_id])


class LectureImage(Base):
    __tablename__ = "lecture_images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False, index=True)
    filename = Column(String(255), nullable=False)
    page_number = Column(Integer, nullable=False)
    width = Column(Integer)
    height = Column(Integer)
    caption = Column(Text)
    order_index = Column(Integer, default=0)
    after_paragraph_id = Column(Integer, ForeignKey("paragraphs.id"), nullable=True)
    after_sentence_id = Column(Integer, ForeignKey("sentences.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    lecture = relationship("Lecture", back_populates="images", foreign_keys=[lecture_id])


class TranslationJob(Base):
    __tablename__ = "translation_jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    status = Column(String(20), default="pending")
    total_sentences = Column(Integer)
    translated_count = Column(Integer, default=0)
    error_message = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    book = relationship("Book", back_populates="translation_jobs")


class CreditSetting(Base):
    __tablename__ = "credit_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    action = Column(String(50), unique=True, nullable=False, index=True)
    price = Column(Numeric(10, 2), nullable=False)
    description = Column(String(255))
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Contribution(Base):
    __tablename__ = "contributions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), nullable=False, index=True)
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False)
    contribution_type = Column(String(30), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=True)
    cost = Column(Integer, default=0, server_default="0")
    grants_download = Column(Boolean, default=False, server_default="false")
    display_name = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class LectureAccess(Base):
    __tablename__ = "lecture_access"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), nullable=False, index=True)
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False)
    access_type = Column(String(30), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class EditAuditLog(Base):
    __tablename__ = "edit_audit_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), nullable=False)
    sentence_id = Column(Integer, ForeignKey("sentences.id", ondelete="CASCADE"), nullable=False)
    field_changed = Column(String(20), nullable=False)
    old_value = Column(Text)
    new_value = Column(Text)
    credits_cost = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)


class SentenceRevision(Base):
    __tablename__ = "sentence_revisions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence_id = Column(Integer, ForeignKey("sentences.id", ondelete="CASCADE"), nullable=False, index=True)
    field = Column(String(10), nullable=False)
    new_value = Column(Text, nullable=False)
    user_id = Column(String(36), nullable=False)
    status = Column(String(20), default="active")
    vote_count = Column(Integer, default=0)
    text_hash = Column(String(64))
    text_anchor = Column(String(200))
    created_at = Column(DateTime, default=datetime.utcnow, index=True)


class RevisionVote(Base):
    __tablename__ = "revision_votes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    revision_id = Column(Integer, ForeignKey("sentence_revisions.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(String(36), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class TranslationFix(Base):
    __tablename__ = "translation_fixes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pattern = Column(Text, nullable=False)
    replacement = Column(Text, nullable=False)
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class RechargeRequest(Base):
    __tablename__ = "recharge_requests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), nullable=False, index=True)
    amount = Column(Integer, nullable=False)
    coefficient = Column(Integer, default=10)
    payment_image = Column(String(255), nullable=True)
    image_hash = Column(String(64), nullable=True)
    status = Column(String(20), default="pending", server_default="pending", index=True)
    admin_note = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class TranslationPublication(Base):
    __tablename__ = "translation_publications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False, index=True)
    scope = Column(String(20), default="lecture", server_default="lecture")
    status = Column(String(20), default="translating", server_default="translating", nullable=False, index=True)
    first_contributor_user_id = Column(String(36), nullable=True)
    published_at = Column(DateTime, nullable=True)
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    lecture = relationship("Lecture", foreign_keys=[lecture_id])
    book = relationship("Book", foreign_keys=[book_id])


class UserTranslationJob(Base):
    __tablename__ = "user_translation_jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(36), nullable=False, index=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False, index=True)
    mode = Column(String(20), default="simulate", server_default="simulate")
    status = Column(String(20), default="running", server_default="running", nullable=False, index=True)
    total_sentences = Column(Integer, default=0, server_default="0")
    completed_sentences = Column(Integer, default=0, server_default="0")
    error_message = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    lecture = relationship("Lecture", foreign_keys=[lecture_id])
    book = relationship("Book", foreign_keys=[book_id])
