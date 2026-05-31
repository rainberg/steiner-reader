-- Check remaining #Bild patterns
SELECT DISTINCT
  substring(text_de from '#Bild[^ a-z]*') AS bild_pattern,
  COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '#Bild'
GROUP BY 1
ORDER BY cnt DESC
LIMIT 30;

-- Show remaining #Bild samples
SELECT s.id, p.lecture_id, LEFT(s.text_de, 200) AS sample
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ '#Bild'
LIMIT 20;

-- Check remaining #G
SELECT s.id, p.lecture_id, s.text_de
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ '#G\d+'
LIMIT 5;

-- Check other_hash
SELECT s.id, p.lecture_id, s.text_de
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ '#[A-Z]' AND text_de !~ '#Bild' AND text_de !~ '#G\d+'
LIMIT 10;
