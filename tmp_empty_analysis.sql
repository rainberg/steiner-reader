-- Distribution of empty lectures by book
SELECT b.ga_number, b.title_de, count(l.id) as empty_lectures,
       (SELECT count(*) FROM lectures l2 WHERE l2.book_id = b.id) as total_lectures
FROM books b
JOIN lectures l ON l.book_id = b.id
WHERE NOT EXISTS (SELECT 1 FROM paragraphs p WHERE p.lecture_id = l.id)
GROUP BY b.ga_number, b.title_de
ORDER BY empty_lectures DESC;

-- Check if these books have source DOCX files available
-- Also check: are there duplicate lectures (same book, same title)?
SELECT b.ga_number, l.title_de, l.lecture_date, count(*) as dup_count
FROM lectures l
JOIN books b ON b.id = l.book_id
GROUP BY b.ga_number, l.title_de, l.lecture_date
HAVING count(*) > 1
ORDER BY dup_count DESC, b.ga_number
LIMIT 30;
