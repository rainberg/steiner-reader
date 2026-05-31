-- Clean up #SE page markers from text_de
-- These are page number references like #SE281-221 that were embedded in the text during PDF import
-- They should be removed as they are not part of the original text

-- First count how many will be affected
SELECT count(*) as sentences_to_clean FROM sentences WHERE text_de LIKE '%#SE%';

-- Show the pattern of these markers
SELECT substring(text_de from '#SE[0-9]+-[0-9]+') as marker_sample, count(*)
FROM sentences
WHERE text_de LIKE '%#SE%'
GROUP BY marker_sample
LIMIT 20;

-- Remove the #SE markers using regexp
UPDATE sentences
SET text_de = regexp_replace(text_de, '#SE[0-9]+-[0-9]+', '', 'g')
WHERE text_de LIKE '%#SE%';

-- Also clean up any resulting double spaces
UPDATE sentences
SET text_de = regexp_replace(text_de, '  +', ' ', 'g')
WHERE text_de LIKE '%  %';

-- Verify
SELECT count(*) as remaining_markers FROM sentences WHERE text_de LIKE '%#SE%';
