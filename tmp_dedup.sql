-- Delete duplicate lectures, keeping the one with most sentences
WITH ranked AS (
  SELECT l.id,
         ROW_NUMBER() OVER (
           PARTITION BY l.book_id, l.title_de, COALESCE(l.lecture_date, '0001-01-01'::date)
           ORDER BY (SELECT count(*) FROM paragraphs p JOIN sentences s ON s.paragraph_id = p.id WHERE p.lecture_id = l.id) DESC,
                    l.id ASC
         ) as rn
  FROM lectures l
  WHERE EXISTS (
    SELECT 1 FROM lectures l2
    WHERE l2.book_id = l.book_id
      AND l2.title_de = l.title_de
      AND COALESCE(l2.lecture_date, '0001-01-01'::date) = COALESCE(l.lecture_date, '0001-01-01'::date)
      AND l2.id != l.id
  )
)
DELETE FROM lectures WHERE id IN (SELECT id FROM ranked WHERE rn > 1);
