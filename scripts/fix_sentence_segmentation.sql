-- Fix broken sentence segmentation caused by German ordinal abbreviations
-- Pattern: "Im 17." + "Jahrhundert" → "Im 17. Jahrhundert"
-- Also handles: Auflage, Band, Teil, Jahrgang, Seite, etc.
--
-- This script is idempotent and can be re-run safely.

BEGIN;

-- ============================================================
-- PHASE 1: Forward merges (current ends with ordinal + next starts with keyword)
-- ============================================================
DROP TABLE IF EXISTS merge_pairs;
CREATE TEMP TABLE merge_pairs AS
WITH broken AS (
    SELECT s.id, s.text_de, s.order_index, s.paragraph_id,
           LEAD(s.text_de) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS next_text,
           LEAD(s.id) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS next_id
    FROM sentences s
)
SELECT b.id AS current_id, b.text_de AS current_text, b.next_id, b.next_text
FROM broken b
WHERE b.text_de ~ '\d+\.$'
  AND b.text_de !~ '^\d+\.$'
  AND b.next_text IS NOT NULL
  AND (
    b.next_text ~ '^[a-zäöüß]'
    OR b.next_text ~ '^(Jahrhundert|Jahrhunderts|Jahrhundert\s|Jahres|Jahrgang|Jahrgangs|Jahrestag|Jahrestages|Jahr|Auflage|Auflage\)|Band|Bandes|Bande|Bands|Teil|Teils|Kapitel|Abschnitt|Seite|S\.|Nr\.|Tausend|Mitte|Ende|Anfang|Dezember|Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November)'
  );

SELECT 'Forward merge pairs: ' || COUNT(*) FROM merge_pairs;

-- ============================================================
-- PHASE 2: Standalone ordinal merges (standalone number like "17." merged with previous)
-- ============================================================
DROP TABLE IF EXISTS standalone_merge;
CREATE TEMP TABLE standalone_merge AS
WITH broken AS (
    SELECT s.id, s.text_de, s.order_index, s.paragraph_id,
           LAG(s.text_de) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS prev_text,
           LAG(s.id) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS prev_id
    FROM sentences s
    WHERE s.text_de ~ '^\d+\.$'
)
SELECT b.id AS current_id, b.text_de AS current_text, b.prev_id, b.prev_text
FROM broken b
WHERE b.prev_id IS NOT NULL
  AND b.prev_text IS NOT NULL
  AND (
    b.prev_text ~ '\d+\.$'
    OR b.prev_text ~ '[a-zäöüß]\s*$'
    OR b.prev_text ~ '(Band|Teil|Auflage|Jahrgang|Jahrhundert|Jahr|Kapitel|Abschnitt|Seite|S\.|Nr\.)\s*$'
  );

SELECT 'Standalone ordinal merges: ' || COUNT(*) FROM standalone_merge;

-- ============================================================
-- PHASE 3: Merge text (update existing sentences)
-- ============================================================
-- Forward: current absorbs next
UPDATE sentences s
SET text_de = mp.current_text || ' ' || mp.next_text,
    text_zh = NULL
FROM merge_pairs mp
WHERE s.id = mp.current_id;

-- Standalone: previous absorbs standalone number
UPDATE sentences s
SET text_de = sm.prev_text || ' ' || sm.current_text,
    text_zh = NULL
FROM standalone_merge sm
WHERE s.id = sm.prev_id;

-- ============================================================
-- PHASE 4: Collect all IDs to delete and clear FK references
-- ============================================================
DROP TABLE IF EXISTS ids_to_delete;
CREATE TEMP TABLE ids_to_delete AS
SELECT next_id AS id FROM merge_pairs
UNION
SELECT current_id AS id FROM standalone_merge;

SELECT 'Total sentences to delete: ' || COUNT(*) FROM ids_to_delete;

-- Clear FK references (set to NULL for safety)
UPDATE lecture_images SET after_sentence_id = NULL
WHERE after_sentence_id IN (SELECT id FROM ids_to_delete);

UPDATE edit_audit_log SET sentence_id = NULL
WHERE sentence_id IN (SELECT id FROM ids_to_delete)
  AND sentence_id IS NOT NULL;

DELETE FROM sentence_revisions
WHERE sentence_id IN (SELECT id FROM ids_to_delete);

-- ============================================================
-- PHASE 5: Delete the merged-into sentences
-- ============================================================
DELETE FROM sentences WHERE id IN (SELECT id FROM ids_to_delete);

COMMIT;

-- Verify
SELECT 'Remaining broken patterns: ' AS label, COUNT(*) AS count
FROM (
    SELECT s.id, s.text_de,
           LEAD(s.text_de) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS next_text
    FROM sentences s
) sub
WHERE sub.text_de ~ '\d+\.$'
  AND sub.text_de !~ '^\d+\.$'
  AND sub.next_text IS NOT NULL
  AND sub.next_text ~ '^[a-zäöüß]';
