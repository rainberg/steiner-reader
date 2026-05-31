-- Check if encoding issues are real or false positives
-- Compare character length vs byte length for suspected sentences
-- If double-encoded, char_length will be much larger than expected

-- Check specific sentence: "NachlaÃ\u009Fverwaltung" (should be "Nachlassverwaltung")
SELECT id, text_de, char_length(text_de) AS char_len, octet_length(text_de::bytea) AS byte_len
FROM sentences
WHERE text_de LIKE '%Nachla%verwaltung%'
LIMIT 5;

-- Check for actual double-encoding patterns
-- Double-encoded ß: ÃƒÆ'Ã‚ÂŸ or ÃƒÂŸ
-- In UTF-8: Ã = U+00C3 = C3 83, ß = U+00DF = C3 9F
-- Double-encoded: C3 83 C3 83 C2 9F (that would show as ÃƒÆ'Ã‚ÂŸ)
SELECT 'double_encoded_ss' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de LIKE '%Ãƒ%' OR text_de LIKE '%Ã‚%';

-- Check for the specific pattern: Ã followed by a non-ASCII char
-- This would indicate Windows-1252 bytes misread as Latin-1 then UTF-8 encoded
-- Pattern: \xC3\x83 (Ã) followed by more UTF-8 = double encoding
SELECT 'c3_83_pattern' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ E'\\xc3\\x83';

-- Let's check a few specific sentences with get_byte to see actual bytes
SELECT id, text_de,
  substring(text_de from 'Nachla(.{5})') AS sample_bytes,
  char_length(substring(text_de from 'Nachla(.{3})')) AS sample_char_len
FROM sentences
WHERE text_de LIKE 'Nachla%verwaltung%'
LIMIT 3;

-- Check if the 0x80 match is actually em-dash (U+2014 = E2 80 94 in UTF-8)
-- This would be a FALSE POSITIVE in our earlier check
SELECT id, LEFT(text_de, 100) AS sample
FROM sentences
WHERE text_de ~ E'\\xe2\\x80\\x94'
LIMIT 5;

-- Count how many sentences have em-dash (U+2014)
SELECT 'em_dash_u2014' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ E'\\u2014' OR text_de LIKE '%—%';

-- Count how many have en-dash (U+2013)
SELECT 'en_dash_u2013' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ E'\\u2013' OR text_de LIKE '%–%';

-- Check for actual mojibake patterns that indicate real encoding problems
-- Windows-1252 0x80 (€) misread as Latin-1 and encoded to UTF-8 = C2 80
-- This would show as Â€ or a control char after Â
SELECT 'euro_misread' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ E'\\xc2\\x80';

-- Check for 0x85 (…) misread = C2 85
SELECT 'ellipsis_misread' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ E'\\xc2\\x85';

-- Check for 0x84 („) misread = C2 84
SELECT 'double_low_quote_misread' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ E'\\xc2\\x84';

-- Check for 0x93 (") misread = C2 93
SELECT 'left_double_quote_misread' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ E'\\xc2\\x93';

-- Check for 0x94 (") misread = C2 94
SELECT 'right_double_quote_misread' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ E'\\xc2\\x94';

-- The real test: check for C2 80 through C2 9F (Latin-1 control range in UTF-8)
-- These are NOT valid text characters and indicate encoding problems
SELECT 'c2_80_9f_range' AS check_type, COUNT(*) AS cnt
FROM sentences
WHERE text_de ~ E'\\xc2[\\x80-\\x9f]';

-- Show samples of C2 80-9F matches
SELECT s.id, p.lecture_id, LEFT(s.text_de, 150) AS sample
FROM sentences s
JOIN paragraphs p ON s.paragraph_id = p.id
WHERE s.text_de ~ E'\\xc2[\\x80-\\x9f]'
LIMIT 20;
