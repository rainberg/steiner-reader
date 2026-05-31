-- Delete test data
-- First, find the test book and lecture
SELECT b.id AS book_id, b.title_de AS book_title, l.id AS lecture_id, l.title_de AS lecture_title
FROM books b
LEFT JOIN lectures l ON l.book_id = b.id
WHERE b.title_de ILIKE '%test%' OR l.title_de ILIKE '%test%';

-- Delete sentences in test lecture
DELETE FROM sentences WHERE paragraph_id IN (
    SELECT p.id FROM paragraphs p
    JOIN lectures l ON p.lecture_id = l.id
    JOIN books b ON l.book_id = b.id
    WHERE b.title_de ILIKE '%test%' OR l.title_de ILIKE '%test%'
);

-- Delete paragraphs in test lecture
DELETE FROM paragraphs WHERE lecture_id IN (
    SELECT l.id FROM lectures l
    JOIN books b ON l.book_id = b.id
    WHERE b.title_de ILIKE '%test%' OR l.title_de ILIKE '%test%'
);

-- Delete test lectures
DELETE FROM lectures WHERE book_id IN (
    SELECT id FROM books WHERE title_de ILIKE '%test%'
);

-- Delete test book
DELETE FROM books WHERE title_de ILIKE '%test%';

-- Also check for any other obviously test/placeholder data
SELECT b.id, b.title_de, COUNT(l.id) AS lecture_count
FROM books b
LEFT JOIN lectures l ON l.book_id = b.id
GROUP BY b.id, b.title_de
HAVING COUNT(l.id) = 0
ORDER BY b.title_de;

-- Verify: check for remaining test data
SELECT COUNT(*) AS test_books_remaining FROM books WHERE title_de ILIKE '%test%';
SELECT COUNT(*) AS test_lectures_remaining FROM lectures WHERE title_de ILIKE '%test%';
