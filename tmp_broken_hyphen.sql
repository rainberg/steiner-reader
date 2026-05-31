-- Check sentences table column names
SELECT column_name FROM information_schema.columns
WHERE table_name = 'sentences' ORDER BY ordinal_position;

-- Check broken hyphenation with correct column names
WITH next_sent AS (
  SELECT s.id, s.text_de, s.paragraph_id, s.order_index,
    LEAD(s.text_de) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS next_text,
    LEAD(s.id) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS next_id
  FROM sentences s
)
SELECT id, text_de, next_text, next_id
FROM next_sent
WHERE text_de ~ E'[a-zäöüß]\\-$'
  AND next_text ~ E'^[a-zäöüß]'
LIMIT 30;

-- Count total broken hyphenation cases
SELECT COUNT(*) AS broken_hyphen_count
FROM (
  WITH next_sent AS (
    SELECT s.id, s.text_de, s.paragraph_id, s.order_index,
      LEAD(s.text_de) OVER (PARTITION BY s.paragraph_id ORDER BY s.order_index) AS next_text
    FROM sentences s
  )
  SELECT id
  FROM next_sent
  WHERE text_de ~ E'[a-zäöüß]\\-$'
    AND next_text ~ E'^[a-zäöüß]'
) sub;

-- Check #G and #TI patterns - are they at the start of lectures?
SELECT s.id, p.lecture_id, LEFT(s.text_de, 200) AS sample, s.order_index
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de LIKE '%#G%' OR s.text_de LIKE '%#TI%'
ORDER BY p.lecture_id, s.order_index
LIMIT 20;

-- Check #Tafel patterns
SELECT s.id, p.lecture_id, s.text_de
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de LIKE '%#Tafel%'
LIMIT 10;

-- Check #BV patterns
SELECT s.id, p.lecture_id, s.text_de
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de LIKE '%#BV%'
LIMIT 10;

-- Check for #EE and #SW patterns
SELECT s.id, p.lecture_id, s.text_de
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de LIKE '%#EE%' OR s.text_de LIKE '%#SW%'
LIMIT 10;

-- Count all hash-tag patterns
SELECT
  CASE
    WHEN text_de ~ '#Bild' THEN '#Bild'
    WHEN text_de ~ '#G[0-9]' THEN '#G (GA number)'
    WHEN text_de ~ '#TI' THEN '#TI (title)'
    WHEN text_de ~ '#Tafel' THEN '#Tafel'
    WHEN text_de ~ '#BV' THEN '#BV'
    WHEN text_de ~ '#EE' THEN '#EE'
    WHEN text_de ~ '#SW' THEN '#SW'
    WHEN text_de ~ '#Das' THEN '#Das'
    ELSE 'other_hash'
  END AS pattern_type,
  COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '#[A-Z]'
GROUP BY 1
ORDER BY cnt DESC;
