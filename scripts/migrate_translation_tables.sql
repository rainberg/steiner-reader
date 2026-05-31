-- Migration: Add translation_publications and user_translation_jobs tables
-- Generated: 2026-05-31
--
-- Purpose:
--   1. Replace the boolean Lecture.is_published with a three-state
--      translation_publications table (translating / published / failed).
--   2. Replace in-memory _running_tasks with persistent
--      user_translation_jobs table (pending / running / completed / failed).
--
-- Back-fill strategy:
--   - Lectures where is_published = TRUE  → translation_publications.status = 'published'
--   - Lectures where is_translating = TRUE → translation_publications.status = 'translating'
--   - The old is_published / is_translating columns are kept for backward
--     compatibility during the transition period.

BEGIN;

-- ============================================================
-- 1. Create translation_publications table
-- ============================================================
CREATE TABLE IF NOT EXISTS translation_publications (
    id            SERIAL PRIMARY KEY,
    lecture_id    INTEGER NOT NULL REFERENCES lectures(id) ON DELETE CASCADE,
    status        VARCHAR(20) NOT NULL DEFAULT 'translating',
    user_id       VARCHAR(36),
    display_name  VARCHAR(100),
    published_at  TIMESTAMP,
    created_at    TIMESTAMP DEFAULT NOW(),
    updated_at    TIMESTAMP DEFAULT NOW()
);

CREATE UNIQUE INDEX IF NOT EXISTS ix_translation_publications_lecture_id
    ON translation_publications (lecture_id);
CREATE INDEX IF NOT EXISTS ix_translation_publications_user_id
    ON translation_publications (user_id);

-- ============================================================
-- 2. Create user_translation_jobs table
-- ============================================================
CREATE TABLE IF NOT EXISTS user_translation_jobs (
    id            SERIAL PRIMARY KEY,
    lecture_id    INTEGER NOT NULL REFERENCES lectures(id) ON DELETE CASCADE,
    user_id       VARCHAR(36),
    display_name  VARCHAR(100),
    status        VARCHAR(20) NOT NULL DEFAULT 'pending',
    error_message TEXT,
    created_at    TIMESTAMP DEFAULT NOW(),
    updated_at    TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS ix_user_translation_jobs_lecture_id
    ON user_translation_jobs (lecture_id);
CREATE INDEX IF NOT EXISTS ix_user_translation_jobs_user_id
    ON user_translation_jobs (user_id);
CREATE INDEX IF NOT EXISTS ix_user_translation_jobs_status
    ON user_translation_jobs (status);

-- ============================================================
-- 3. Back-fill translation_publications from existing lectures
-- ============================================================

-- Published lectures → status = 'published'
INSERT INTO translation_publications (lecture_id, status, published_at, created_at, updated_at)
SELECT l.id, 'published', l.created_at, l.created_at, NOW()
FROM lectures l
WHERE l.is_published = TRUE
  AND NOT EXISTS (
      SELECT 1 FROM translation_publications tp WHERE tp.lecture_id = l.id
  );

-- Translating (but not yet published) lectures → status = 'translating'
INSERT INTO translation_publications (lecture_id, status, created_at, updated_at)
SELECT l.id, 'translating', l.created_at, NOW()
FROM lectures l
WHERE l.is_translating = TRUE
  AND l.is_published = FALSE
  AND NOT EXISTS (
      SELECT 1 FROM translation_publications tp WHERE tp.lecture_id = l.id
  );

COMMIT;
