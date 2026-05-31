-- Step 1: Delete empty lectures (lectures with no paragraphs)
-- These are from failed DOCX/PDF imports that only created lecture headers

-- First, count what we'll delete
SELECT count(*) as empty_lectures_to_delete
FROM lectures l
WHERE NOT EXISTS (SELECT 1 FROM paragraphs p WHERE p.lecture_id = l.id);

-- Delete empty lectures (CASCADE will handle any related records)
DELETE FROM lectures l
WHERE NOT EXISTS (SELECT 1 FROM paragraphs p WHERE p.lecture_id = l.id);

-- Step 2: Check if any books are now empty (no lectures left)
SELECT b.id, b.ga_number, b.title_de, count(l.id) as remaining_lectures
FROM books b
LEFT JOIN lectures l ON l.book_id = b.id
GROUP BY b.id, b.ga_number, b.title_de
HAVING count(l.id) = 0;

-- Step 3: Delete empty books
DELETE FROM books b
WHERE NOT EXISTS (SELECT 1 FROM lectures l WHERE l.book_id = b.id);
