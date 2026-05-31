-- Check for duplicate lectures (same book, same title, same date)
-- Only consider lectures that actually have content
SELECT b.ga_number, l.title_de, l.lecture_date, l.id, l.location,
       (SELECT count(*) FROM paragraphs p WHERE p.lecture_id = l.id) as para_count,
       (SELECT count(*) FROM paragraphs p JOIN sentences s ON s.paragraph_id = p.id WHERE p.lecture_id = l.id) as sentence_count
FROM lectures l
JOIN books b ON b.id = l.book_id
WHERE EXISTS (
  SELECT 1 FROM lectures l2
  WHERE l2.book_id = l.book_id
    AND l2.title_de = l.title_de
    AND COALESCE(l2.lecture_date, '0001-01-01') = COALESCE(l.lecture_date, '0001-01-01')
    AND l2.id != l.id
)
ORDER BY b.ga_number, l.title_de, l.lecture_date, l.id;
