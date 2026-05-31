-- Check remaining markers
SELECT s.id, substring(s.text_de from '#SE[^ ]*') as marker, left(s.text_de, 200) as preview
FROM sentences s
WHERE s.text_de LIKE '%#SE%'
LIMIT 30;

-- Clean remaining markers with a broader pattern
UPDATE sentences
SET text_de = regexp_replace(text_de, '#SE[^a-zA-ZäöüÄÖÜß ]+', '', 'g')
WHERE text_de LIKE '%#SE%';

-- Final cleanup of double spaces
UPDATE sentences
SET text_de = regexp_replace(text_de, '  +', ' ', 'g')
WHERE text_de LIKE '%  %';

-- Final verification
SELECT count(*) as remaining_markers FROM sentences WHERE text_de LIKE '%#SE%';
