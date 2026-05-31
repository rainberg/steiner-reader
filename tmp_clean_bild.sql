-- Comprehensive cleanup of import artifacts
-- Step 1: Remove #Bild references (image placeholders)
-- Pattern: #Bild [sS]. NUMBER or #Bild NUMBER
UPDATE sentences
SET text_de = regexp_replace(text_de, '#Bild\s*[sS]\.?\s*\d+[a-z]*\s*', ' ', 'g')
WHERE text_de ~ '#Bild';

-- Step 2: Remove #G references (GA number metadata)
-- Pattern: #G123-YYYY-SE000 or #G123,YYYY,SE000 or #G123x-YYYY-SE000
UPDATE sentences
SET text_de = regexp_replace(text_de, '#G\d+[a-z]?[-,]\d+[-,]\w+\s*', ' ', 'g')
WHERE text_de ~ '#G\d+';

-- Step 3: Remove #TI references (title markers)
-- Pattern: #TI or #TI followed by text
UPDATE sentences
SET text_de = regexp_replace(text_de, '#TI\s*', ' ', 'g')
WHERE text_de ~ '#TI';

-- Step 4: Remove #Tafel references (blackboard/plate references)
-- Pattern: #Tafel NUMBER
UPDATE sentences
SET text_de = regexp_replace(text_de, '#Tafel\s+\d+[a-z]?\s*', ' ', 'g')
WHERE text_de ~ '#Tafel';

-- Step 5: Remove #BV references
UPDATE sentences
SET text_de = regexp_replace(text_de, '#BV\s*', ' ', 'g')
WHERE text_de ~ '#BV';

-- Step 6: Remove #EE and #SW references
UPDATE sentences
SET text_de = regexp_replace(text_de, '#EE\d+\s*', ' ', 'g')
WHERE text_de ~ '#EE';

UPDATE sentences
SET text_de = regexp_replace(text_de, '#SW\d+\s*', ' ', 'g')
WHERE text_de ~ '#SW';

-- Step 7: Clean up multiple spaces created by removals
UPDATE sentences
SET text_de = regexp_replace(text_de, '  +', ' ', 'g')
WHERE text_de ~ '  ';

-- Step 8: Trim leading/trailing whitespace
UPDATE sentences
SET text_de = trim(text_de)
WHERE text_de != trim(text_de);

-- Step 9: Delete sentences that became empty after cleanup
DELETE FROM sentences
WHERE text_de = '' OR text_de IS NULL;

-- Verify: count remaining hash patterns
SELECT
  CASE
    WHEN text_de ~ '#Bild' THEN '#Bild'
    WHEN text_de ~ '#G\d+' THEN '#G'
    WHEN text_de ~ '#TI' THEN '#TI'
    WHEN text_de ~ '#Tafel' THEN '#Tafel'
    WHEN text_de ~ '#BV' THEN '#BV'
    WHEN text_de ~ '#EE' THEN '#EE'
    WHEN text_de ~ '#SW' THEN '#SW'
    ELSE 'other_hash'
  END AS pattern_type,
  COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ '#[A-Z]'
GROUP BY 1
ORDER BY cnt DESC;
