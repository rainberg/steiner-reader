-- Quality check queries for Steiner Reader data

-- 1. Lectures with empty titles
SELECT 'empty_title_lectures' as issue, count(*) as cnt FROM lectures WHERE title_de IS NULL OR title_de = '';

-- 2. Lectures with no paragraphs
SELECT 'no_paragraph_lectures' as issue, count(*) as cnt FROM lectures l WHERE NOT EXISTS (SELECT 1 FROM paragraphs p WHERE p.lecture_id = l.id);

-- 3. Paragraphs with no sentences
SELECT 'no_sentence_paragraphs' as issue, count(*) as cnt FROM paragraphs p WHERE NOT EXISTS (SELECT 1 FROM sentences s WHERE s.paragraph_id = p.id);

-- 4. Sentences with empty German text
SELECT 'empty_de_sentences' as issue, count(*) as cnt FROM sentences WHERE text_de IS NULL OR text_de = '';

-- 5. Very short sentences (possible parsing issues)
SELECT 'very_short_sentences' as issue, count(*) as cnt FROM sentences WHERE length(text_de) > 0 AND length(text_de) < 5;

-- 6. Very long sentences (possible missing sentence breaks)
SELECT 'very_long_sentences' as issue, count(*) as cnt FROM sentences WHERE length(text_de) > 2000;

-- 7. Duplicate sentences within same paragraph
SELECT 'duplicate_sentences' as issue, count(*) as cnt FROM (SELECT text_de, paragraph_id, count(*) as c FROM sentences WHERE text_de != '' GROUP BY text_de, paragraph_id HAVING count(*) > 1) t;

-- 8. Lectures with suspiciously few sentences
SELECT 'few_sentence_lectures' as issue, count(*) as cnt FROM lectures l WHERE (SELECT count(*) FROM paragraphs p JOIN sentences s ON s.paragraph_id = p.id WHERE p.lecture_id = l.id) BETWEEN 1 AND 3;

-- 9. Books with no lectures
SELECT 'no_lecture_books' as issue, count(*) as cnt FROM books b WHERE NOT EXISTS (SELECT 1 FROM lectures l WHERE l.book_id = b.id);

-- 10. Sentences with only whitespace or special chars
SELECT 'whitespace_sentences' as issue, count(*) as cnt FROM sentences WHERE length(trim(text_de)) = 0 AND text_de IS NOT NULL;
