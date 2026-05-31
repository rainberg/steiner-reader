-- Check broken hyphenation using a simpler approach
-- Find sentences ending with lowercase + hyphen
SELECT COUNT(*) AS sentences_ending_with_hyphen
FROM sentences
WHERE text_de ~ E'[a-zäöüß]\\-$';

-- Show samples
SELECT s.id, p.lecture_id, s.text_de
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ E'[a-zäöüß]\\-$'
LIMIT 30;

-- Also check for hyphenated compounds that might be broken
-- Pattern: word- at end where the hyphen is part of a compound word
-- e.g. "darwinisti-schen" should be "darwinistischen"
SELECT COUNT(*) AS intra_word_hyphens
FROM sentences
WHERE text_de ~ E'[a-zäöüß]\\-[a-zäöüß]';

-- Check for specific known broken patterns
-- Soft hyphen patterns: words with - in the middle that look like line-break artifacts
-- Common in German: Ent-wicklung, Be-wußtsein, etc. when hyphenated at line breaks
SELECT s.id, p.lecture_id, s.text_de,
  regexp_matches(text_de, E'[a-zäöüß]\\-[a-zäöüß]', 'g') AS match
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ E'[a-zäöüß]\\-[a-zäöüß]'
LIMIT 30;

-- Check for the specific pattern of word- at end of sentence
-- where the next sentence in the same paragraph continues the word
-- Use a simpler join approach instead of window function
SELECT s1.id AS sent_id, s1.text_de AS first_part, s2.text_de AS second_part, s2.id AS next_id
FROM sentences s1
JOIN sentences s2 ON s1.paragraph_id = s2.paragraph_id AND s2.order_index = s1.order_index + 1
WHERE s1.text_de ~ E'[a-zäöüß]\\-$'
  AND s2.text_de ~ E'^[a-zäöüß]'
LIMIT 30;

-- Count total broken hyphenation cases
SELECT COUNT(*) AS broken_hyphen_count
FROM sentences s1
JOIN sentences s2 ON s1.paragraph_id = s2.paragraph_id AND s2.order_index = s1.order_index + 1
WHERE s1.text_de ~ E'[a-zäöüß]\\-$'
  AND s2.text_de ~ E'^[a-zäöüß]';
