-- Second pass cleanup for remaining #Bild patterns
-- Pattern: #Bild [a-z] [sS][,.]?\s*\d+ (with letter prefix)
UPDATE sentences
SET text_de = regexp_replace(text_de, '#Bild\s+[a-z]\s+[sS][,.]?\s*\d+\s*', ' ', 'g')
WHERE text_de ~ '#Bild\s+[a-z]\s+[sS][,.]?\s*\d+';

-- Pattern: #Bild [sS][,.]?\s*\d+ (uppercase S or comma)
UPDATE sentences
SET text_de = regexp_replace(text_de, '#Bild\s+[sS][,.]?\s*\d+\s*', ' ', 'g')
WHERE text_de ~ '#Bild\s+[sS][,.]?\s*\d+';

-- Pattern: #Bild s. (truncated, no number - just remove the marker)
UPDATE sentences
SET text_de = regexp_replace(text_de, '#Bild\s+[sS]\.?\s*', ' ', 'g')
WHERE text_de ~ '#Bild\s+[sS]\.?\s*';

-- Pattern: #Bild followed by anything else (catch-all)
UPDATE sentences
SET text_de = regexp_replace(text_de, '#Bild\s*', ' ', 'g')
WHERE text_de ~ '#Bild';

-- Fix remaining #G pattern
UPDATE sentences
SET text_de = regexp_replace(text_de, '#G\d+[-,]\d+[-,]-*SE\d+\s*', ' ', 'g')
WHERE text_de ~ '#G\d+[-,]\d+[-,]-*SE\d+';

-- Fix #A pattern (question marker)
UPDATE sentences
SET text_de = regexp_replace(text_de, '#A\s*', ' ', 'g')
WHERE text_de ~ '#A\s';

-- Clean up multiple spaces again
UPDATE sentences
SET text_de = regexp_replace(text_de, '  +', ' ', 'g')
WHERE text_de ~ '  ';

-- Trim again
UPDATE sentences
SET text_de = trim(text_de)
WHERE text_de != trim(text_de);

-- Delete sentences that became empty
DELETE FROM sentences
WHERE text_de = '' OR text_de IS NULL;

-- Final verification
SELECT
  CASE
    WHEN text_de ~ '#Bild' THEN '#Bild'
    WHEN text_de ~ '#G\d+' THEN '#G'
    WHEN text_de ~ '#TI' THEN '#TI'
    WHEN text_de ~ '#Tafel' THEN '#Tafel'
    WHEN text_de ~ '#BV' THEN '#BV'
    WHEN text_de ~ '#EE' THEN '#EE'
    WHEN text_de ~ '#SW' THEN '#SW'
    WHEN text_de ~ '#A' THEN '#A'
    ELSE 'other'
  END AS pattern_type,
  COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '#[A-Z]'
GROUP BY 1
ORDER BY cnt DESC;

-- Total sentence count after cleanup
SELECT COUNT(*) AS total_sentences FROM sentences;
