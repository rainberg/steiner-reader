#!/usr/bin/env python3
"""
PDF parser using pymupdf (fitz) - much lighter than pdfplumber.
Outputs JSON to stdout. Runs as subprocess.
"""
import sys, json, re, gc

def main():
    import fitz  # pymupdf

    path = sys.argv[1]
    doc = fitz.open(path)

    LECTURE_RE = re.compile(
        r"(ERSTER|ZWEITER|DRITTER|VIERTER|FUENFTER|SECHSTER|SIEBENTER|"
        r"ACHTER|NEUNTER|ZEHNTER|ELFTER|ZWOELFTER|DREIZEHNTER|VIERZEHNTER|"
        r"FUENFZEHNTER|SECHZEHNTER|SIEBZEHNTER|ACHTZEHNTER|NEUNZEHNTER|"
        r"ZWANZIGSTER)\s+VORTRAG", re.IGNORECASE
    )
    GA_RE = re.compile(r"(?:GA|Band)\s*(\d+)", re.IGNORECASE)
    DATE_RE = re.compile(
        r"([A-ZÄÖÜa-zäöüß][A-ZÄÖÜa-zäöüß\s\-]+?),\s+"
        r"(\d{1,2}\.\s*(?:Januar|Februar|März|April|Mai|Juni|Juli|"
        r"August|September|Oktober|November|Dezember)\s+\d{4})"
    )

    def clean(t):
        t = re.sub(r"[¹²³⁴⁵⁶⁷⁸⁹⁰]+|\(\d+\)", "", t)
        t = re.sub(r"-\n(\w)", r"\1", t)
        t = re.sub(r"\s+", " ", t)
        return t.strip()

    def paras(t):
        t = t.replace("\r\n","\n").replace("\r","\n")
        return [p.strip() for p in re.split(r"\n\s*\n", t) if p.strip() and len(p.strip())>15]

    def sents(t):
        t = t.strip()
        if len(t)<5: return []
        p = re.split(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ])', t)
        r = [s.strip() for s in p if s.strip() and len(s.strip())>5]
        return r if r else [t]

    # Metadata
    meta = doc.metadata or {}
    book_title = meta.get("title", "")
    ga_number = ""
    if book_title:
        m = GA_RE.search(book_title)
        if m: ga_number = f"GA {m.group(1)}"

    lectures = []
    cur = None
    lorder = 0
    pcounter = 0

    for i in range(len(doc)):
        page = doc[i]
        text = page.get_text("text")
        page = None  # release

        if not text or len(text.strip()) < 30:
            del text; gc.collect(); continue

        cleaned = clean(text); del text
        header = cleaned[:500]
        lm = LECTURE_RE.search(header)
        dm = DATE_RE.search(header)

        if lm or dm:
            title = lm.group(0).strip() if lm else "Vortrag"
            loc = dm.group(1).strip() if dm else ""
            dt = dm.group(2).strip() if dm else ""
            cur = {"title_de":title,"location":loc,"date":dt,"order_index":lorder,"paragraphs":[]}
            lectures.append(cur)
            lorder += 1; pcounter = 0

        if i < 5:
            del cleaned; gc.collect(); continue

        if cur is None:
            cur = {"title_de":book_title or "Gesamtwerk","location":"","date":"","order_index":0,"paragraphs":[]}
            lectures.append(cur); lorder=1; pcounter=0

        for pt in paras(cleaned):
            if re.match(r"^\s*\d{1,3}\s*$", pt): continue
            s = sents(pt)
            para = {"order_index":pcounter,"sentences":[]}
            pcounter += 1
            for idx,st in enumerate(s):
                if len(st) > 5:
                    para["sentences"].append({"text_de":st,"order_index":idx})
            if para["sentences"]:
                cur["paragraphs"].append(para)

        del cleaned; gc.collect()

    doc.close()
    json.dump({"title_de":book_title,"ga_number":ga_number,"lectures":lectures}, sys.stdout, ensure_ascii=False)

if __name__=="__main__":
    main()
