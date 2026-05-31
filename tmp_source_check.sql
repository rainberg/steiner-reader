-- Check GA266 details - what does this book look like?
SELECT l.id, l.title_de, l.lecture_date, l.location
FROM lectures l
JOIN books b ON b.id = l.book_id
WHERE b.ga_number = 'GA266'
ORDER BY l.lecture_date
LIMIT 30;

-- Check if GA044 has any content at all in its lectures
SELECT l.id, l.title_de, (SELECT count(*) FROM paragraphs p WHERE p.lecture_id = l.id) as para_count
FROM lectures l
JOIN books b ON b.id = l.book_id
WHERE b.ga_number = 'GA044'
ORDER BY l.id;

-- Check duplicate lectures more carefully - are they from different imports?
SELECT b.ga_number, l.title_de, l.lecture_date, l.id, l.location,
       (SELECT count(*) FROM paragraphs p WHERE p.lecture_id = l.id) as para_count
FROM lectures l
JOIN books b ON b.id = l.book_id
WHERE b.ga_number = 'GA072'
ORDER BY l.title_de, l.lecture_date;

-- Check how many books are from DOCX vs PDF
SELECT
  CASE
    WHEN title_de LIKE '%(from DOCX)%' THEN 'DOCX'
    WHEN title_de LIKE '%(from PDF)%' THEN 'PDF'
    ELSE 'Other'
  END as source,
  count(*) as book_count
FROM books
GROUP BY source;
