-- Fix: sentences table uses paragraph_id, not lecture_id
-- Get samples of Windows-1252 characters
SELECT s.id, p.lecture_id, LEFT(s.text_de, 150) AS sample
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ E'[\\x80-\\x9f]'
LIMIT 30;

-- Get samples of angle bracket sentences
SELECT s.id, p.lecture_id, LEFT(s.text_de, 200) AS sample
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ '<[a-zA-Z/]' OR s.text_de ~ '</[a-zA-Z]'
LIMIT 30;

-- Get samples of double hyphen sentences
SELECT s.id, p.lecture_id, LEFT(s.text_de, 200) AS sample
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de LIKE '%--%'
LIMIT 20;

-- Get samples of leading/trailing whitespace
SELECT s.id, p.lecture_id, LEFT(s.text_de, 100) AS sample, LENGTH(s.text_de) AS len
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE (s.text_de ~ E'^\\s' OR s.text_de ~ E'\\s$') AND s.text_de != ''
LIMIT 20;

-- Check what specific Windows-1252 chars appear and their frequency
SELECT
  CASE
    WHEN text_de ~ E'\\x80' THEN '0x80 Euro'
    WHEN text_de ~ E'\\x85' THEN '0x85 Ellipsis'
    WHEN text_de ~ E'\\x91' THEN '0x91 Left Single Quote'
    WHEN text_de ~ E'\\x92' THEN '0x92 Right Single Quote'
    WHEN text_de ~ E'\\x93' THEN '0x93 Left Double Quote'
    WHEN text_de ~ E'\\x94' THEN '0x94 Right Double Quote'
    WHEN text_de ~ E'\\x96' THEN '0x96 En-dash'
    WHEN text_de ~ E'\\x97' THEN '0x97 Em-dash'
    WHEN text_de ~ E'\\x99' THEN '0x99 Trademark'
    ELSE 'other'
  END AS char_type,
  COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ E'[\\x80-\\x9f]'
GROUP BY 1
ORDER BY cnt DESC;

-- Check standalone numbers - are they page numbers from import?
SELECT s.id, p.lecture_id, s.text_de, p.position AS para_pos, s.position AS sent_pos
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ '^[0-9]+$' AND LENGTH(s.text_de) <= 4
ORDER BY p.lecture_id, p.position, s.position
LIMIT 30;
