-- Distribution of empty lectures by book (fixed)
SELECT b.ga_number, b.title_de, count(l.id) as empty_lectures,
       (SELECT count(*) FROM lectures l2 WHERE l2.book_id = b.id) as total_lectures_in_book
FROM books b
JOIN lectures l ON l.book_id = b.id
WHERE NOT EXISTS (SELECT 1 FROM paragraphs p WHERE p.lecture_id = l.id)
GROUP BY b.id, b.ga_number, b.title_de
ORDER BY empty_lectures DESC;
