-- =============================================
-- FINAL DATA QUALITY REPORT
-- =============================================

-- 1. Overall statistics
SELECT 'books' AS entity, COUNT(*) AS total FROM books
UNION ALL
SELECT 'lectures', COUNT(*) FROM lectures
UNION ALL
SELECT 'paragraphs', COUNT(*) FROM paragraphs
UNION ALL
SELECT 'sentences', COUNT(*) FROM sentences;

-- 2. Check for empty entities
SELECT 'empty_books' AS check_type, COUNT(*) AS cnt FROM books b
WHERE NOT EXISTS (SELECT 1 FROM lectures l WHERE l.book_id = b.id)
UNION ALL
SELECT 'empty_lectures', COUNT(*) FROM lectures l
WHERE NOT EXISTS (SELECT 1 FROM paragraphs p WHERE p.lecture_id = l.id)
UNION ALL
SELECT 'empty_paragraphs', COUNT(*) FROM paragraphs p
WHERE NOT EXISTS (SELECT 1 FROM sentences s WHERE s.paragraph_id = p.id)
UNION ALL
SELECT 'empty_sentences', COUNT(*) FROM sentences WHERE text_de = '' OR text_de IS NULL;

-- 3. Check for remaining import artifacts
SELECT '#SE markers' AS check_type, COUNT(*) AS cnt FROM sentences WHERE text_de LIKE '%#SE%'
UNION ALL
SELECT '#Bild markers', COUNT(*) FROM sentences WHERE text_de LIKE '%#Bild%'
UNION ALL
SELECT '#G markers', COUNT(*) FROM sentences WHERE text_de ~ '#G\d+'
UNION ALL
SELECT '#TI markers', COUNT(*) FROM sentences WHERE text_de LIKE '%#TI%'
UNION ALL
SELECT '#Tafel markers', COUNT(*) FROM sentences WHERE text_de LIKE '%#Tafel%'
UNION ALL
SELECT '#BV markers', COUNT(*) FROM sentences WHERE text_de LIKE '%#BV%'
UNION ALL
SELECT 'any hash pattern', COUNT(*) FROM sentences WHERE text_de ~ '#[A-Z]';

-- 4. Check for broken hyphenation
SELECT 'broken_hyphenation' AS check_type, COUNT(*) AS cnt
FROM sentences s1
JOIN sentences s2 ON s1.paragraph_id = s2.paragraph_id
    AND s2.order_index = s1.order_index + 1
WHERE s1.text_de ~ E'[a-zäöüß]\\-$'
  AND s2.text_de ~ E'^[a-zäöüß]';

-- 5. Check for whitespace issues
SELECT 'leading_whitespace' AS check_type, COUNT(*) AS cnt FROM sentences WHERE text_de ~ E'^\\s' AND text_de != ''
UNION ALL
SELECT 'trailing_whitespace', COUNT(*) FROM sentences WHERE text_de ~ E'\\s$' AND text_de != ''
UNION ALL
SELECT 'multiple_spaces', COUNT(*) FROM sentences WHERE text_de ~ '  ';

-- 6. Sentence length distribution
SELECT
  CASE
    WHEN LENGTH(text_de) = 0 THEN '0 (empty)'
    WHEN LENGTH(text_de) < 5 THEN '1-4 (very short)'
    WHEN LENGTH(text_de) < 20 THEN '5-19 (short)'
    WHEN LENGTH(text_de) < 100 THEN '20-99 (normal)'
    WHEN LENGTH(text_de) < 500 THEN '100-499 (long)'
    WHEN LENGTH(text_de) < 2000 THEN '500-1999 (very long)'
    ELSE '2000+ (extreme)'
  END AS length_category,
  COUNT(*) AS cnt,
  MIN(LENGTH(text_de)) AS min_len,
  MAX(LENGTH(text_de)) AS max_len
FROM sentences
GROUP BY 1
ORDER BY 1;

-- 7. Translation coverage
SELECT
  COUNT(*) AS total_sentences,
  COUNT(text_zh) AS translated_sentences,
  ROUND(COUNT(text_zh) * 100.0 / COUNT(*), 2) AS translation_pct
FROM sentences;

-- 8. Published lectures
SELECT
  COUNT(*) AS total_lectures,
  SUM(CASE WHEN is_published THEN 1 ELSE 0 END) AS published_lectures,
  ROUND(SUM(CASE WHEN is_published THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS published_pct
FROM lectures;

-- 9. Check for orphan paragraphs (paragraphs with no lecture)
SELECT 'orphan_paragraphs' AS check_type, COUNT(*) AS cnt
FROM paragraphs p
WHERE NOT EXISTS (SELECT 1 FROM lectures l WHERE l.id = p.lecture_id);

-- 10. Check for orphan sentences (sentences with no paragraph)
SELECT 'orphan_sentences' AS check_type, COUNT(*) AS cnt
FROM sentences s
WHERE NOT EXISTS (SELECT 1 FROM paragraphs p WHERE p.id = s.paragraph_id);

-- 11. Books with most sentences (top 10)
SELECT b.title_de, COUNT(s.id) AS sentence_count
FROM books b
JOIN lectures l ON l.book_id = b.id
JOIN paragraphs p ON p.lecture_id = l.id
JOIN sentences s ON s.paragraph_id = p.id
GROUP BY b.title_de
ORDER BY sentence_count DESC
LIMIT 10;

-- 12. Check for duplicate lecture titles within same book
SELECT b.title_de AS book, l.title_de AS lecture, COUNT(*) AS cnt
FROM lectures l
JOIN books b ON l.book_id = b.id
GROUP BY b.title_de, l.title_de, l.book_id
HAVING COUNT(*) > 1
ORDER BY cnt DESC;
