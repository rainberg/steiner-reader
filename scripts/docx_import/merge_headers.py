"""Merge .docx header blocks: header ordinals, subtitles, and date lines into one paragraph.

The reimport creates separate paragraphs for each .docx line. This script finds
header paragraphs (ERSTER VORTRAG, etc.) and merges them with the following
subtitle and date/location lines into a single paragraph with newlines.

Does NOT touch body text — use merge_body.py for that.
"""
import psycopg2, re, sys

conn = psycopg2.connect("host=localhost port=5432 dbname=steiner_reader user=steiner password=Dd08120@")
cur = conn.cursor()

HEADER_KEYS = [
    "ERSTER VORTRAG", "ZWEITER VORTRAG", "DRITTER VORTRAG",
    "VIERTER VORTRAG", "FUNFTER VORTRAG", "FUNFTER VORTRAG",
    "SECHSTER VORTRAG", "SIEBENTER VORTRAG", "ACHTER VORTRAG",
    "NEUNTER VORTRAG", "ZEHNTER VORTRAG",
]
HEADER_PAT = re.compile(r'^(' + '|'.join(HEADER_KEYS) + r')\b')

MONTH_PAT = re.compile(
    r'(Januar|Februar|März|April|Mai|Juni|Juli|August|'
    r'September|Oktober|November|Dezember|19\d{2}|20\d{2})'
)

# Common body text starters — if a paragraph starts like this, it's body, not header metadata
BODY_STARTERS = re.compile(
    r'^(Meine|Wir|Ich|Die|Das|Es|In|Auf|Aus|Bei|Mit|Nach|Von|Zu|'
    r'Diese|Dieser|Dieses|Welche|Welcher|Welches|'
    r'So|Da|Nun|Denn|Aber|Und|Oder|Doch|'
    r'Man|Wer|Was|Wie|Wann|Wo|Warum|Weshalb|'
    r'Wenn|Weil|Obwohl|Während|Bevor|Nachdem|Seit|'
    r'Durch|Für|Gegen|Ohne|Um|'
    r'Eine|Einer|Einem|Einen|'
    r'Kann|Können|Muss|Müssen|Soll|Sollen|Will|Wollen|'
    r'Hat|Habe|Haben|Ist|Sind|War|Waren|Wird|Werden)'
)

def is_all_caps_or_mostly(text):
    """Check if text is mostly ALL CAPS (subtitle style)."""
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return False
    caps = sum(1 for c in letters if c == c.upper())
    return caps / len(letters) > 0.8

def looks_like_date_or_location(text):
    """Check if text looks like a date/location line."""
    return bool(MONTH_PAT.search(text)) or bool(re.search(r'\b\d{4}\b', text))

def looks_like_body(text):
    """Check if text looks like body text (should NOT be merged with header)."""
    return bool(BODY_STARTERS.match(text.strip()))

merged_count = 0
book_id = int(sys.argv[1]) if len(sys.argv) > 1 else 302  # default GA083

cur.execute("SELECT id FROM lectures WHERE book_id=%s ORDER BY order_index", (book_id,))
for (lec_id,) in cur.fetchall():
    cur.execute(
        "SELECT p.id, s.text_de, s.id as sid "
        "FROM sentences s JOIN paragraphs p ON s.paragraph_id = p.id "
        "WHERE p.lecture_id = %s ORDER BY p.order_index",
        (lec_id,)
    )
    paras = cur.fetchall()  # (pid, text_de, sid)

    i = 0
    while i < len(paras):
        pid, text, sid = paras[i]
        t = (text or "").strip()

        if not HEADER_PAT.match(t):
            i += 1
            continue

        # Found a header paragraph. Try to merge with next 1-2 paras.
        merged_lines = [t]
        ids_to_delete = []

        # Look ahead for subtitle (ALL CAPS) and date/location
        for offset in range(1, min(4, len(paras) - i)):
            next_pid, next_text, next_sid = paras[i + offset]
            nt = (next_text or "").strip()

            # Stop if this looks like body text or another header
            if HEADER_PAT.match(nt) or looks_like_body(nt):
                break

            # Accept if ALL CAPS (subtitle) or date-like
            if is_all_caps_or_mostly(nt) or looks_like_date_or_location(nt):
                merged_lines.append(nt)
                ids_to_delete.append((next_pid, next_sid))
            else:
                break

        if ids_to_delete:
            header_block = "\n".join(merged_lines)
            print(f"  Lecture {lec_id}: merged {len(merged_lines)} lines → header block")
            print(f"    {header_block[:120]}")

            cur.execute(
                "UPDATE sentences SET text_de=%s, text_zh=NULL WHERE id=%s",
                (header_block, sid)
            )
            for del_pid, del_sid in ids_to_delete:
                cur.execute("DELETE FROM sentences WHERE id=%s", (del_sid,))
                cur.execute("DELETE FROM paragraphs WHERE id=%s", (del_pid,))
            merged_count += len(ids_to_delete)

            # Update paras list for subsequent iterations
            paras = [p for p in paras if p[2] not in [s for _, s in ids_to_delete]]

        i += 1

conn.commit()

# Renumber paragraph order_index per lecture
print("\nRenumbering paragraphs...")
cur.execute("SELECT id FROM lectures WHERE book_id=%s ORDER BY order_index", (book_id,))
for (lec_id,) in cur.fetchall():
    cur.execute(
        "SELECT id FROM paragraphs WHERE lecture_id=%s ORDER BY order_index, id",
        (lec_id,)
    )
    pids = [r[0] for r in cur.fetchall()]
    for idx, pid in enumerate(pids):
        cur.execute("UPDATE paragraphs SET order_index=%s WHERE id=%s", (idx, pid))

conn.commit()

# Report
cur.execute(
    "SELECT COUNT(*) FROM sentences s JOIN paragraphs p ON s.paragraph_id=p.id "
    "WHERE p.lecture_id IN (SELECT id FROM lectures WHERE book_id=%s)", (book_id,)
)
total = cur.fetchone()[0]
print(f"Merged {merged_count} header-adjacent paragraphs into header blocks.")
print(f"Total paragraphs: {total}")

cur.close(); conn.close()
