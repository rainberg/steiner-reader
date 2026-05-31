-- Check current double hyphen count and patterns
SELECT COUNT(*) AS double_hyphen_count FROM sentences WHERE text_de LIKE '%--%';

-- Show different patterns
SELECT
  CASE
    WHEN text_de ~ E'\\s--\\s' THEN 'space--space (em-dash usage)'
    WHEN text_de ~ E'\\s--' THEN 'space--word'
    WHEN text_de ~ E'--\\s' THEN 'word--space'
    WHEN text_de ~ E'[a-zäöüß]--[a-zäöüß]' THEN 'word--word (compound)'
    WHEN text_de ~ E'---' THEN 'triple+ (separator)'
    ELSE 'other'
  END AS pattern_type,
  COUNT(*) AS cnt
FROM sentences
WHERE text_de LIKE '%--%'
GROUP BY 1
ORDER BY cnt DESC;

-- Convert space--space to space—space (em-dash)
-- This is the safest conversion: " -- " → " — "
UPDATE sentences
SET text_de = regexp_replace(text_de, E'\\s--\\s', ' — ', 'g')
WHERE text_de ~ E'\\s--\\s';

-- Convert word--space to word—space (em-dash at end of clause)
-- Pattern: "word.-- " or "word-- " → "word— "
UPDATE sentences
SET text_de = regexp_replace(text_de, E'\\.\\-\\-\\s', '.— ', 'g')
WHERE text_de ~ E'\\.\\-\\-\\s';

-- Convert space--word to space—word (em-dash at start of clause)
-- Pattern: " --word" → " —word"
UPDATE sentences
SET text_de = regexp_replace(text_de, E'\\s--(?=[A-ZÄÖÜ])', ' —', 'g')
WHERE text_de ~ E'\\s--[A-ZÄÖÜ]';

-- Verify remaining double hyphens
SELECT COUNT(*) AS remaining_double_hyphens FROM sentences WHERE text_de LIKE '%--%';

-- Show remaining patterns
SELECT
  CASE
    WHEN text_de ~ E'---' THEN 'triple+ (separator)'
    WHEN text_de ~ E'[a-zäöüß]--[a-zäöüß]' THEN 'word--word'
    WHEN text_de ~ E'\\s--' THEN 'space--'
    WHEN text_de ~ E'--\\s' THEN '--space'
    ELSE 'other'
  END AS pattern_type,
  COUNT(*) AS cnt
FROM sentences
WHERE text_de LIKE '%--%'
GROUP BY 1
ORDER BY cnt DESC;
