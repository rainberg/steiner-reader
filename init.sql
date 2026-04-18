-- Database schema initialization
-- This runs automatically when PostgreSQL container starts for the first time

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

CREATE TABLE IF NOT EXISTS paragraphs (
    id            SERIAL PRIMARY KEY,
    lecture_id    INTEGER REFERENCES lectures(id) ON DELETE CASCADE,
    order_index   INTEGER NOT NULL,
    created_at    TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_paragraphs_lecture_id ON paragraphs(lecture_id);

CREATE TABLE IF NOT EXISTS sentences (
    id            SERIAL PRIMARY KEY,
    paragraph_id  INTEGER REFERENCES paragraphs(id) ON DELETE CASCADE,
    order_index   INTEGER NOT NULL,
    text_de       TEXT NOT NULL,
    text_zh       TEXT,
    created_at    TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_sentences_paragraph_id ON sentences(paragraph_id);

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
