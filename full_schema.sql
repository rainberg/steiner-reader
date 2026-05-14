-- Complete database schema for Steiner Reader
-- Based on SQLAlchemy models

-- Books table
CREATE TABLE IF NOT EXISTS books (
    id            SERIAL PRIMARY KEY,
    ga_number     VARCHAR(20),
    title_de      TEXT NOT NULL,
    title_zh      TEXT,
    pdf_filename  TEXT NOT NULL,
    cover_url     TEXT,
    created_at    TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_books_ga_number ON books(ga_number);

-- Lectures table
CREATE TABLE IF NOT EXISTS lectures (
    id            SERIAL PRIMARY KEY,
    book_id       INTEGER REFERENCES books(id) ON DELETE CASCADE,
    title_de      TEXT,
    lecture_date  DATE,
    location      VARCHAR(200),
    order_index   INTEGER NOT NULL,
    created_at    TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_lectures_book_id ON lectures(book_id);

-- Paragraphs table
CREATE TABLE IF NOT EXISTS paragraphs (
    id            SERIAL PRIMARY KEY,
    lecture_id    INTEGER REFERENCES lectures(id) ON DELETE CASCADE,
    order_index   INTEGER NOT NULL,
    created_at    TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_paragraphs_lecture_id ON paragraphs(lecture_id);

-- Sentences table
CREATE TABLE IF NOT EXISTS sentences (
    id            SERIAL PRIMARY KEY,
    paragraph_id  INTEGER REFERENCES paragraphs(id) ON DELETE CASCADE,
    order_index   INTEGER NOT NULL,
    text_de       TEXT NOT NULL,
    text_zh       TEXT,
    created_at    TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_sentences_paragraph_id ON sentences(paragraph_id);

-- Lecture images table
CREATE TABLE IF NOT EXISTS lecture_images (
    id                SERIAL PRIMARY KEY,
    lecture_id        INTEGER REFERENCES lectures(id) ON DELETE CASCADE,
    filename          VARCHAR(255) NOT NULL,
    page_number       INTEGER NOT NULL,
    width             INTEGER,
    height            INTEGER,
    caption           TEXT,
    order_index       INTEGER DEFAULT 0,
    after_paragraph_id INTEGER REFERENCES paragraphs(id),
    created_at        TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_lecture_images_lecture_id ON lecture_images(lecture_id);

-- Translation jobs table
CREATE TABLE IF NOT EXISTS translation_jobs (
    id                SERIAL PRIMARY KEY,
    book_id           INTEGER REFERENCES books(id) ON DELETE CASCADE,
    status            VARCHAR(20) DEFAULT 'pending',
    total_sentences   INTEGER,
    translated_count  INTEGER DEFAULT 0,
    error_message     TEXT,
    created_at        TIMESTAMP DEFAULT NOW(),
    updated_at        TIMESTAMP DEFAULT NOW()
);

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id            SERIAL PRIMARY KEY,
    username      VARCHAR(50) UNIQUE NOT NULL,
    email         VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    credits       INTEGER DEFAULT 100,
    created_at    TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);