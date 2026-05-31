-- Detailed analysis of empty lectures

-- 1. List all lectures with no paragraphs (with book info)
SELECT l.id, l.book_id, b.ga_number, b.title_de as book_title, l.title_de as lecture_title, l.lecture_date
FROM lectures l
JOIN books b ON b.id = l.book_id
WHERE NOT EXISTS (SELECT 1 FROM paragraphs p WHERE p.lecture_id = l.id)
ORDER BY b.ga_number, l.lecture_date
LIMIT 50;

-- 2. Very long sentences - what do they look like?
SELECT s.id, s.paragraph_id, l.id as lecture_id, l.title_de, length(s.text_de) as len, left(s.text_de, 200) as preview
FROM sentences s
JOIN paragraphs p ON p.id = s.paragraph_id
JOIN lectures l ON l.id = p.lecture_id
WHERE length(s.text_de) > 2000
ORDER BY length(s.text_de) DESC
LIMIT 20;

-- 3. Very short sentences - what do they look like?
SELECT s.id, s.text_de, s.paragraph_id
FROM sentences s
WHERE length(s.text_de) > 0 AND length(text_de) < 5
ORDER BY random()
LIMIT 30;

-- 4. Lectures with very few sentences
SELECT l.id, l.title_de, b.ga_number, count(s.id) as sentence_count
FROM lectures l
JOIN books b ON b.id = l.book_id
JOIN paragraphs p ON p.lecture_id = l.id
JOIN sentences s ON s.paragraph_id = p.id
GROUP BY l.id, l.title_de, b.ga_number
HAVING count(s.id) BETWEEN 1 AND 3
ORDER BY b.ga_number;

-- 5. Distribution of sentences per lecture
SELECT
  CASE
    WHEN cnt = 0 THEN '0 (empty)'
    WHEN cnt BETWEEN 1 AND 10 THEN '1-10'
    WHEN cnt BETWEEN 11 AND 50 THEN '11-50'
    WHEN cnt BETWEEN 51 AND 100 THEN '51-100'
    WHEN cnt BETWEEN 101 AND 500 THEN '101-500'
    WHEN cnt > 500 THEN '500+'
  END as range_label,
  count(*) as lecture_count
FROM (
  SELECT l.id, count(s.id) as cnt
  FROM lectures l
  LEFT JOIN paragraphs p ON p.lecture_id = l.id
  LEFT JOIN sentences s ON s.paragraph_id = p.id
  GROUP BY l.id
) t
GROUP BY range_label
ORDER BY range_label;
