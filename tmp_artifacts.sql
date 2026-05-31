-- Check for residual page markers like #SE281-221 in text
SELECT count(*) as sentences_with_page_markers
FROM sentences
WHERE text_de LIKE '%#SE%';

-- Show some examples
SELECT s.id, left(s.text_de, 200) as preview
FROM sentences s
WHERE text_de LIKE '%#SE%'
LIMIT 10;

-- Check for other common import artifacts
SELECT
  CASE
    WHEN text_de LIKE '%#SE%' THEN 'page_marker_#SE'
    WHEN text_de LIKE '%\u0096%' THEN 'special_dash_96'
    WHEN text_de LIKE '%\u0097%' THEN 'special_dash_97'
    WHEN text_de LIKE '%>%' AND text_de NOT LIKE '%<%' THEN 'stray_angle_bracket'
    ELSE 'other'
  END as artifact_type,
  count(*) as cnt
FROM sentences
WHERE text_de LIKE '%#SE%'
   OR text_de LIKE E'%\x96%'
   OR text_de LIKE E'%\x97%'
   OR (text_de LIKE '%>%' AND text_de NOT LIKE '%<%')
GROUP BY artifact_type
ORDER BY cnt DESC;
