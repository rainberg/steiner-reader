-- Fix broken hyphenation by merging split sentences
-- This handles cases where a word was split across a line break during PDF import
-- e.g., "stre-" at end of sentence + "ben danach" at start of next → "streben danach"

DO $$
DECLARE
    rec RECORD;
    merged_count INTEGER := 0;
    deleted_count INTEGER := 0;
    new_text TEXT;
    new_text_zh TEXT;
    hyphen_word_part TEXT;
    next_word_part TEXT;
BEGIN
    -- Process each broken hyphenation case
    FOR rec IN
        SELECT s1.id AS first_id, s1.text_de AS first_text, s1.text_zh AS first_zh,
               s1.paragraph_id, s1.order_index AS first_order,
               s2.id AS second_id, s2.text_de AS second_text, s2.text_zh AS second_zh,
               s2.order_index AS second_order
        FROM sentences s1
        JOIN sentences s2 ON s1.paragraph_id = s2.paragraph_id
            AND s2.order_index = s1.order_index + 1
        WHERE s1.text_de ~ E'[a-zäöüß]\\-$'
          AND s2.text_de ~ E'^[a-zäöüß]'
        ORDER BY s1.paragraph_id, s1.order_index
    LOOP
        -- Extract the word parts to determine how to join
        hyphen_word_part := substring(rec.first_text from E'([a-zäöüß])\\-$');
        next_word_part := substring(rec.second_text from E'^([a-zäöüß])');

        -- Check if this is a compound enumeration (e.g., "sach-, berufs-" + "und")
        -- Pattern: comma or enumeration before the hyphenated word
        IF rec.first_text ~ E',[\s]*[a-zäöüß]+\\-$' THEN
            -- Compound enumeration: keep hyphen, add space
            new_text := regexp_replace(rec.first_text, E'\\-$', '- ') || rec.second_text;
        ELSE
            -- Line break artifact: remove hyphen, join directly
            new_text := regexp_replace(rec.first_text, E'\\-$', '') || rec.second_text;
        END IF;

        -- Merge Chinese translations if both exist
        IF rec.first_zh IS NOT NULL AND rec.second_zh IS NOT NULL THEN
            new_text_zh := rec.first_zh || rec.second_zh;
        ELSIF rec.first_zh IS NOT NULL THEN
            new_text_zh := rec.first_zh;
        ELSIF rec.second_zh IS NOT NULL THEN
            new_text_zh := rec.second_zh;
        ELSE
            new_text_zh := NULL;
        END IF;

        -- Update the first sentence with merged text
        UPDATE sentences
        SET text_de = new_text, text_zh = new_text_zh
        WHERE id = rec.first_id;

        -- Delete the second sentence
        DELETE FROM sentences WHERE id = rec.second_id;

        -- Renumber subsequent sentences in the same paragraph
        UPDATE sentences
        SET order_index = order_index - 1
        WHERE paragraph_id = rec.paragraph_id
          AND order_index > rec.second_order;

        merged_count := merged_count + 1;
    END LOOP;

    RAISE NOTICE 'Merged % broken hyphenation cases', merged_count;
END $$;

-- Clean up any resulting double spaces
UPDATE sentences
SET text_de = regexp_replace(text_de, '  +', ' ', 'g')
WHERE text_de ~ '  ';

-- Trim whitespace
UPDATE sentences
SET text_de = trim(text_de)
WHERE text_de != trim(text_de);

-- Delete any sentences that became empty
DELETE FROM sentences WHERE text_de = '' OR text_de IS NULL;

-- Verify: count remaining broken hyphenation cases
SELECT COUNT(*) AS remaining_broken_hyphens
FROM sentences s1
JOIN sentences s2 ON s1.paragraph_id = s2.paragraph_id
    AND s2.order_index = s1.order_index + 1
WHERE s1.text_de ~ E'[a-zäöüß]\\-$'
  AND s2.text_de ~ E'^[a-zäöüß]';
