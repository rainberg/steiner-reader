-- Check for broken hyphenation (words split across line breaks)
-- Pattern: word ending with - at end of sentence, next sentence starts with lowercase
SELECT 'broken_hyphenation' AS check_type, COUNT(*) AS cnt
FROM sentences s
WHERE s.text_de ~ E'[a-zäöüß]\\-$';

-- Show samples of broken hyphenation
SELECT s.id, p.lecture_id, s.text_de
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ E'[a-zäöüß]\\-$'
LIMIT 30;

-- Check for "Test" data that should be removed
SELECT l.id, l.title_de, b.title_de AS book, b.id AS book_id
FROM lectures l
JOIN books b ON l.book_id = b.id
WHERE l.title_de ILIKE '%test%' OR b.title_de ILIKE '%test%';

-- Check for leading/trailing whitespace details
SELECT s.id, p.lecture_id, '>' || s.text_de || '<' AS with_markers, LENGTH(s.text_de) AS len
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE (s.text_de ~ E'^\\s' OR s.text_de ~ E'\\s$') AND s.text_de != ''
LIMIT 20;

-- Check for double hyphens that should be em-dashes
-- Pattern: word--word or space--space
SELECT s.id, p.lecture_id, s.text_de
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de LIKE '%--%'
AND s.text_de NOT LIKE '%---%'
LIMIT 30;

-- Check for triple+ hyphens (section dividers)
SELECT 'triple_hyphens' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '---';

-- Check for sentences with mixed < and » or « (inconsistent quotation marks)
SELECT 'mixed_quotes' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE (text_de LIKE '%<%' OR text_de LIKE '%>%')
  AND (text_de LIKE '%«%' OR text_de LIKE '%»%');

-- Show samples of mixed quotes
SELECT s.id, p.lecture_id, LEFT(s.text_de, 200) AS sample
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE (s.text_de LIKE '%<%' OR text_de LIKE '%>%')
  AND (text_de LIKE '%«%' OR text_de LIKE '%»%')
LIMIT 15;

-- Check for sentences with only underscores (section dividers)
SELECT 'underscore_dividers' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '^_+$';

-- Check for Faksimile/Bild references that might be empty placeholders
SELECT 'faksimile_refs' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ILIKE '%faksimile%' OR text_de ILIKE '%bild s.%' OR text_de ILIKE '%#Bild%';

-- Show Faksimile/Bild samples
SELECT s.id, p.lecture_id, s.text_de
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE text_de ILIKE '%faksimile%' OR text_de ILIKE '%bild s.%' OR text_de ILIKE '%#Bild%'
LIMIT 15;

-- Check for "Seite X, Zeile Y" errata references
SELECT 'errata_refs' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ILIKE '%seite%, zeile%';

-- Show errata samples
SELECT s.id, p.lecture_id, LEFT(s.text_de, 200) AS sample
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE text_de ILIKE '%seite%, zeile%'
LIMIT 10;
