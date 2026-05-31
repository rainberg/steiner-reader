-- Migration: Back-fill translation_publications from existing lectures
-- Generated: 2026-05-31
--
-- The translation_publications and user_translation_jobs tables already exist
-- in production. This script only back-fills data from lectures.is_published.

BEGIN;

-- Published lectures → status = 'published'
INSERT INTO translation_publications (lecture_id, book_id, status, published_at, created_at, updated_at)
SELECT l.id, l.book_id, 'published', l.created_at, l.created_at, NOW()
FROM lectures l
WHERE l.is_published = TRUE
  AND NOT EXISTS (
      SELECT 1 FROM translation_publications tp WHERE tp.lecture_id = l.id
  );

-- Translating (but not yet published) lectures → status = 'translating'
INSERT INTO translation_publications (lecture_id, book_id, status, created_at, updated_at)
SELECT l.id, l.book_id, 'translating', l.created_at, NOW()
FROM lectures l
WHERE l.is_translating = TRUE
  AND l.is_published = FALSE
  AND NOT EXISTS (
      SELECT 1 FROM translation_publications tp WHERE tp.lecture_id = l.id
  );

COMMIT;
