"""SQLAlchemy ORM models for Steiner Reader."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Date, Boolean
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

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    credits = Column(Integer, default=100)
    is_admin = Column(Integer, default=0)  # 0=normal, 1=admin
    username_changed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    contributions = relationship("Contribution", back_populates="user", cascade="all, delete-orphan")
    access_grants = relationship("LectureAccess", back_populates="user", cascade="all, delete-orphan")
    edit_audits = relationship("EditAuditLog", back_populates="user", cascade="all, delete-orphan")
    credit_transactions = relationship("CreditTransaction", back_populates="user", cascade="all, delete-orphan")
    recharge_requests = relationship("RechargeRequest", back_populates="user", cascade="all, delete-orphan")


class CreditSetting(Base):
    __tablename__ = "credit_settings"

    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(50), unique=True, nullable=False, index=True)
    value = Column(Integer, nullable=False, default=10)
    description = Column(String(255))
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class CreditTransaction(Base):
    __tablename__ = "credit_transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    amount = Column(Integer, nullable=False)
    balance_after = Column(Integer, nullable=False)
    transaction_type = Column(String(50), nullable=False)
    reference_type = Column(String(50))
    reference_id = Column(Integer)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)

    user = relationship("User", back_populates="credit_transactions", foreign_keys=[user_id])


class Contribution(Base):
    __tablename__ = "contributions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False, index=True)
    contribution_type = Column(String(30), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="contributions", foreign_keys=[user_id])


class LectureAccess(Base):
    __tablename__ = "lecture_access"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    lecture_id = Column(Integer, ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False, index=True)
    access_type = Column(String(30), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="access_grants", foreign_keys=[user_id])


class EditAuditLog(Base):
    __tablename__ = "edit_audit_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    sentence_id = Column(Integer, ForeignKey("sentences.id", ondelete="CASCADE"), nullable=False)
    field_changed = Column(String(20), nullable=False)
    old_value = Column(Text)
    new_value = Column(Text)
    credits_cost = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="edit_audits", foreign_keys=[user_id])


class RechargeRequest(Base):
    __tablename__ = "recharge_requests"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    amount = Column(Integer, nullable=False)
    coefficient = Column(Integer, default=10)
    payment_image = Column(String(255))
    image_hash = Column(String(64))
    status = Column(String(20), default="pending")  # pending, approved, rejected
    admin_note = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="recharge_requests", foreign_keys=[user_id])
