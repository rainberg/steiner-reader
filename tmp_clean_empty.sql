-- Clean up sentences that are now empty after removing #SE markers
SELECT count(*) as empty_after_cleanup FROM sentences WHERE text_de IS NOT NULL AND length(trim(text_de)) = 0;

-- Delete these empty sentences
DELETE FROM sentences WHERE text_de IS NOT NULL AND length(trim(text_de)) = 0;

-- Also check for sentences that are just whitespace
SELECT count(*) as whitespace_only FROM sentences WHERE text_de IS NOT NULL AND length(text_de) > 0 AND length(trim(text_de)) = 0;
