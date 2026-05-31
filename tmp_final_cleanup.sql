-- Clean up remaining issues

-- Find and show the 4 empty lectures
SELECT l.id, l.title_de, b.title_de AS book
FROM lectures l
JOIN books b ON l.book_id = b.id
WHERE NOT EXISTS (SELECT 1 FROM paragraphs p WHERE p.lecture_id = l.id);

-- Delete the empty lectures (they have no paragraphs/sentences)
DELETE FROM lectures WHERE id IN (
    SELECT l.id
    FROM lectures l
    WHERE NOT EXISTS (SELECT 1 FROM paragraphs p WHERE p.lecture_id = l.id)
);

-- Fix the 1 trailing whitespace
UPDATE sentences SET text_de = trim(text_de)
WHERE text_de != trim(text_de);

-- Check for empty books after deleting empty lectures
SELECT COUNT(*) AS empty_books_after FROM books b
WHERE NOT EXISTS (SELECT 1 FROM lectures l WHERE l.book_id = b.id);

-- Delete any newly empty books
DELETE FROM books WHERE id IN (
    SELECT b.id FROM books b
    WHERE NOT EXISTS (SELECT 1 FROM lectures l WHERE l.book_id = b.id)
);

-- Final counts
SELECT 'books' AS entity, COUNT(*) AS total FROM books
UNION ALL
SELECT 'lectures', COUNT(*) FROM lectures
UNION ALL
SELECT 'paragraphs', COUNT(*) FROM paragraphs
UNION ALL
SELECT 'sentences', COUNT(*) FROM sentences;

-- Check the 1 remaining hash pattern
SELECT s.id, p.lecture_id, LEFT(s.text_de, 100) AS sample
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ '#[A-Z]'
LIMIT 5;
