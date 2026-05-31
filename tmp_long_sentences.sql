-- Check very long sentences (>1000 chars) that are NOT index/register content
-- These are the ones that likely need sentence splitting
SELECT s.id, s.paragraph_id, l.title_de as lecture_title, b.ga_number,
       length(s.text_de) as len,
       left(s.text_de, 300) as preview
FROM sentences s
JOIN paragraphs p ON p.id = s.paragraph_id
JOIN lectures l ON l.id = p.lecture_id
JOIN books b ON b.id = l.book_id
WHERE length(s.text_de) > 1000
  AND l.title_de NOT LIKE '%REGISTER%'
  AND l.title_de NOT LIKE '%HINWEISE%'
  AND l.title_de NOT LIKE '%VERZEICHNIS%'
  AND l.title_de NOT LIKE '%ANHANG%'
  AND s.text_de NOT LIKE '%BILDERWERZEICHNIS%'
ORDER BY length(s.text_de) DESC
LIMIT 30;
