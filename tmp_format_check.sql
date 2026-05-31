-- Detailed check of angle brackets - are they HTML tags or typographic?
-- Check for actual HTML tags (with closing tags or self-closing)
SELECT 'html_tags' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '<[a-zA-Z][a-zA-Z0-9]*[^>]*>' OR text_de ~ '</[a-zA-Z]+>';

-- Show HTML tag samples
SELECT s.id, p.lecture_id, LEFT(s.text_de, 200) AS sample
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ '<[a-zA-Z][a-zA-Z0-9]*[^>]*>' OR s.text_de ~ '</[a-zA-Z]+>'
LIMIT 20;

-- Check for unclosed angle brackets (potential import issues)
SELECT 'unclosed_angle' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE (text_de ~ '<[^>]+$') OR (text_de ~ '^[^<]+>');

-- Check for angle brackets used as German quotation marks
-- In German, << and >> or « and » are used for quotes
-- <word> pattern is common for emphasis in Steiner texts
SELECT 'angle_as_quote' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '<[A-ZÄÖÜ][a-zäöüß]+>' OR text_de ~ '<[a-zäöüß]+>';

-- Check for guillemets (proper German quotation marks)
SELECT 'guillemets' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de LIKE '%«%' OR text_de LIKE '%»%' OR text_de LIKE '%‹%' OR text_de LIKE '%›%';

-- Check for stray punctuation-only sentences
SELECT 'punctuation_only' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '^[^a-zA-ZÄÖÜäöüß0-9]+$' AND text_de != '';

-- Show punctuation-only sentences
SELECT s.id, p.lecture_id, s.text_de, LENGTH(s.text_de) AS len
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ '^[^a-zA-ZÄÖÜäöüß0-9]+$' AND s.text_de != ''
ORDER BY LENGTH(s.text_de) DESC
LIMIT 20;

-- Check for sentences that are just dashes or separators
SELECT 'dash_only' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '^[-—–_]+$';

-- Check for sentences with only numbers and punctuation
SELECT 'num_punct_only' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '^[0-9\s.,;:!\?\-—–/()]+$' AND text_de != '';

-- Show samples
SELECT s.id, p.lecture_id, s.text_de
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ '^[0-9\s.,;:!\?\-—–/()]+$' AND text_de != ''
ORDER BY LENGTH(s.text_de) DESC
LIMIT 20;

-- Check for paragraphs with no sentences
SELECT 'empty_paragraphs' AS check_type, COUNT(*) AS cnt
FROM paragraphs par
WHERE NOT EXISTS (SELECT 1 FROM sentences s WHERE s.paragraph_id = par.id);

-- Check for lectures with no paragraphs
SELECT 'empty_lectures' AS check_type, COUNT(*) AS cnt
FROM lectures l
WHERE NOT EXISTS (SELECT 1 FROM paragraphs p WHERE p.lecture_id = l.id);

-- Check for books with no lectures
SELECT 'empty_books' AS check_type, COUNT(*) AS cnt
FROM books b
WHERE NOT EXISTS (SELECT 1 FROM lectures l WHERE l.book_id = b.id);

-- Check for duplicate lecture titles within same book
SELECT b.title_de AS book, l.title_de AS lecture, COUNT(*) AS cnt
FROM lectures l
JOIN books b ON l.book_id = b.id
GROUP BY b.title_de, l.title_de, l.book_id
HAVING COUNT(*) > 1
ORDER BY cnt DESC
LIMIT 20;

-- Check for lectures with very few sentences (potential import issues)
SELECT l.id, l.title_de, b.title_de AS book, COUNT(s.id) AS sent_count
FROM lectures l
JOIN books b ON l.book_id = b.id
LEFT JOIN paragraphs p ON p.lecture_id = l.id
LEFT JOIN sentences s ON s.paragraph_id = p.id
GROUP BY l.id, l.title_de, b.title_de
HAVING COUNT(s.id) BETWEEN 1 AND 5
ORDER BY COUNT(s.id)
LIMIT 20;
