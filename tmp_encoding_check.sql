-- Check for Windows-1252 special characters that may have been imported incorrectly
-- \x96 = en-dash in Windows-1252 (should be – in UTF-8)
-- \x97 = em-dash in Windows-1252 (should be — in UTF-8)
-- \x85 = ellipsis in Windows-1252 (should be … in UTF-8)
-- \x91 = left single quote in Windows-1252
-- \x92 = right single quote in Windows-1252
-- \x93 = left double quote in Windows-1252
-- \x94 = right double quote in Windows-1252
-- \x80 = Euro sign in Windows-1252
-- \x84 = double low-9 quotation mark

-- Count sentences with Windows-1252 byte sequences
SELECT 'win1252_chars' AS check_type,
  COUNT(*) AS affected_sentences,
  SUM(LENGTH(text_de)) AS total_chars_affected
FROM sentences
WHERE text_de ~ E'[\\x80-\\x9f]'
   OR text_de ~ E'\\u0096'
   OR text_de ~ E'\\u0097'
   OR text_de ~ E'\\u0085';

-- Show samples of affected sentences
SELECT s.id, s.lecture_id, LEFT(s.text_de, 120) AS sample
FROM sentences s
WHERE s.text_de ~ E'[\\x80-\\x9f]'
LIMIT 20;

-- Check for common encoding artifacts
SELECT 'double_hyphen_dash' AS check_type, COUNT(*) AS cnt
FROM sentences WHERE text_de LIKE '%--%';

SELECT 'triple_dot' AS check_type, COUNT(*) AS cnt
FROM sentences WHERE text_de LIKE '%...%' OR text_de LIKE '%…%';

-- Check for stray angle brackets (potential HTML/XML remnants)
SELECT 'angle_brackets' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '<[a-zA-Z/]' OR text_de ~ '</[a-zA-Z]';

-- Show samples of angle bracket sentences
SELECT s.id, s.lecture_id, LEFT(s.text_de, 150) AS sample
FROM sentences s
WHERE s.text_de ~ '<[a-zA-Z/]' OR s.text_de ~ '</[a-zA-Z]'
LIMIT 20;

-- Check for other common import artifacts
SELECT 'nbsp' AS check_type, COUNT(*) AS cnt
FROM sentences WHERE text_de ~ E'\\u00a0';

SELECT 'bom' AS check_type, COUNT(*) AS cnt
FROM sentences WHERE text_de ~ E'\\ufeff';

SELECT 'carriage_return' AS check_type, COUNT(*) AS cnt
FROM sentences WHERE text_de ~ E'\\r';

SELECT 'tab_chars' AS check_type, COUNT(*) AS cnt
FROM sentences WHERE text_de ~ E'\\t';

-- Check for multiple consecutive spaces (potential formatting issue)
SELECT 'multi_spaces' AS check_type, COUNT(*) AS cnt
FROM sentences WHERE text_de ~ '  ';

-- Show samples of multi-space sentences
SELECT s.id, s.lecture_id, LEFT(s.text_de, 150) AS sample
FROM sentences s
WHERE s.text_de ~ '  '
LIMIT 20;

-- Check for leading/trailing whitespace
SELECT 'leading_whitespace' AS check_type, COUNT(*) AS cnt
FROM sentences WHERE text_de ~ E'^\\s' AND text_de != '';

SELECT 'trailing_whitespace' AS check_type, COUNT(*) AS cnt
FROM sentences WHERE text_de ~ E'\\s$' AND text_de != '';

-- Check for standalone numbers that might be page numbers or section numbers
SELECT 'standalone_number' AS check_type, COUNT(*) AS cnt
FROM sentences WHERE text_de ~ '^[0-9]+$' AND LENGTH(text_de) <= 4;

-- Show distribution of standalone numbers
SELECT text_de, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '^[0-9]+$' AND LENGTH(text_de) <= 4
GROUP BY text_de
ORDER BY cnt DESC
LIMIT 20;
