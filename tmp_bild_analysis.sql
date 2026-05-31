-- Analyze #Bild patterns in detail
-- Count different #Bild patterns
SELECT
  CASE
    WHEN text_de ~ '#Bild [sS]\.\s*\d+' THEN 'Bild s. NUMBER'
    WHEN text_de ~ '#Bild\s+\d+' THEN 'Bild NUMBER'
    WHEN text_de ~ '#Bild' THEN 'Other Bild'
    ELSE 'No Bild'
  END AS pattern_type,
  COUNT(*) AS cnt
FROM sentences
WHERE text_de LIKE '%#Bild%'
GROUP BY 1
ORDER BY cnt DESC;

-- Show the exact #Bild patterns found
SELECT DISTINCT
  substring(text_de from '#Bild[^ ]*') AS bild_pattern,
  COUNT(*) AS cnt
FROM sentences
WHERE text_de LIKE '%#Bild%'
GROUP BY 1
ORDER BY cnt DESC
LIMIT 30;

-- Check how #Bild appears in context (before and after)
SELECT
  LEFT(s.text_de, 80) AS before_bild,
  substring(s.text_de from '#Bild[^\n]*') AS bild_ref,
  RIGHT(s.text_de, 80) AS after_bild,
  LENGTH(s.text_de) AS total_len
FROM sentences s
WHERE s.text_de LIKE '%#Bild%'
LIMIT 20;

-- Check if #Bild is at the end, middle, or beginning of sentence
SELECT
  CASE
    WHEN text_de ~ '#Bild.*$' AND text_de !~ '#Bild.+.+$' THEN 'Bild at end'
    WHEN text_de ~ '^#Bild' THEN 'Bild at start'
    ELSE 'Bild in middle'
  END AS position_type,
  COUNT(*) AS cnt
FROM sentences
WHERE text_de LIKE '%#Bild%'
GROUP BY 1;

-- Check for #G (GA number) references too
SELECT 'g_refs' AS check_type, COUNT(*) AS cnt
FROM sentences WHERE text_de LIKE '%#G%';

-- Show #G samples
SELECT s.id, p.lecture_id, LEFT(s.text_de, 150) AS sample
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de LIKE '%#G%'
LIMIT 10;

-- Check for other # patterns
SELECT DISTINCT
  substring(text_de from '#[A-Z][A-Za-z]*') AS hash_pattern,
  COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '#[A-Z][A-Za-z]'
GROUP BY 1
ORDER BY cnt DESC
LIMIT 20;

-- Check for broken hyphenation more carefully
-- Pattern: lowercase letter + hyphen at end of sentence, next sentence starts with lowercase
WITH next_sent AS (
  SELECT s.id, s.text_de, s.paragraph_id, s.position,
    LEAD(s.text_de) OVER (PARTITION BY s.paragraph_id ORDER BY s.position) AS next_text,
    LEAD(s.id) OVER (PARTITION BY s.paragraph_id ORDER BY s.position) AS next_id
  FROM sentences s
)
SELECT id, text_de, next_text, next_id
FROM next_sent
WHERE text_de ~ E'[a-zäöüß]\\-$'
  AND next_text ~ E'^[a-zäöüß]'
LIMIT 30;

-- Also check for hyphenated words that look like they should be joined
-- Pattern: word- at end, next word continues
SELECT COUNT(*) AS broken_hyphen_count
FROM (
  WITH next_sent AS (
    SELECT s.id, s.text_de, s.paragraph_id, s.position,
      LEAD(s.text_de) OVER (PARTITION BY s.paragraph_id ORDER BY s.position) AS next_text
    FROM sentences s
  )
  SELECT id
  FROM next_sent
  WHERE text_de ~ E'[a-zäöüß]\\-$'
    AND next_text ~ E'^[a-zäöüß]'
) sub;
