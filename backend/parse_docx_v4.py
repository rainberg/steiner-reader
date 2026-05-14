#!/usr/bin/env python3
"""
docx 解析器 v4：
- 用 Heading 1 样式精确识别章节
- 过滤 Vorrede/Nachwort/Einleitung 等非正文章节
- 从文件名提取 GA 编号
- 正确获取书名
"""
import sys, json, re, os
from docx import Document

def main():
    path = sys.argv[1]
    doc = Document(path)
    
    # 从文件名提取 GA 编号
    basename = os.path.basename(path)  # e.g. GA010.docx
    ga_match = re.search(r"GA(\d+)", basename, re.IGNORECASE)
    ga_number = "GA %s" % ga_match.group(1) if ga_match else ""
    
    # 跳过的章节标题
    SKIP_PREFIXES = [
        "inhalt", "contents", "table of contents",
        "vorrede", "preface", "foreword",
        "vorwort",
        "einleitung", "introduction",
        "vorbemerkung",
        "register", "index", "literaturverzeichnis",
        "anhang", "appendix",
        "nachwort", "afterword",
    ]
    
    def is_skip_title(title):
        t = title.lower().strip()
        for prefix in SKIP_PREFIXES:
            if t.startswith(prefix):
                return True
        return False
    
    def clean_text(t):
        t = re.sub(r"[¹²³⁴⁵⁶⁷⁸⁹⁰]+|\(\d+\)", "", t)
        t = re.sub(r"-\n(\w)", r"\1", t)
        t = re.sub(r"\s+", " ", t)
        return t.strip()
    
    def split_sentences(text):
        text = text.strip()
        if len(text) < 10:
            return []
        parts = re.split(r'(?<=[.!?])\s+(?=[A-ZÄÖÜ"\'])', text)
        sentences = [s.strip() for s in parts if s.strip() and len(s.strip()) > 5]
        return sentences if sentences else [text]
    
    # ===== 遍历段落 =====
    lectures = []
    cur_lecture = None
    lorder = 0
    pcounter = 0
    skip_section = False
    title_de = ""
    first_content_heading = True
    
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        
        style_name = para.style.name if para.style else ""
        is_h1 = style_name == "Heading 1"
        
        # ===== Heading 1 → 章节标题 =====
        if is_h1:
            cleaned = clean_text(text)
            if not cleaned:
                continue
            
            # 跳过非正文章节
            if is_skip_title(cleaned):
                skip_section = True
                cur_lecture = None
                continue
            
            skip_section = False
            
            # 第一个非跳过的 Heading 1 作为书名（如果还没有）
            if not title_de:
                title_de = cleaned
            
            # 提取地点和日期
            location = ""
            date = ""
            dm = re.search(
                r"([A-ZÄÖÜa-zäöüß][A-ZÄÖÜa-zäöüß\s\-/]+?),\s+"
                r"(\d{1,2}\.\s*(?:Januar|Februar|März|April|Mai|Juni|Juli|"
                r"August|September|Oktober|November|Dezember)\s+\d{4})",
                cleaned
            )
            if dm:
                location = dm.group(1).strip()
                date = dm.group(2).strip()
            
            cur_lecture = {
                "title_de": cleaned[:200],
                "location": location,
                "date": date,
                "order_index": lorder,
                "paragraphs": []
            }
            lectures.append(cur_lecture)
            lorder += 1
            pcounter = 0
            continue
        
        # 跳过非正文区域
        if skip_section:
            continue
        
        # 只处理 Normal 样式的正文
        if style_name not in ("Normal", "Обычный (веб)", "fnt"):
            continue
        
        # ===== 处理正文段落 =====
        cleaned = clean_text(text)
        if not cleaned or len(cleaned) < 15:
            continue
        
        # 跳过页码
        if re.match(r"^\s*\d{1,4}\s*$", cleaned):
            continue
        
        # 跳过目录行
        if re.match(r".+\.{2,}\s*\d+\s*$", cleaned):
            continue
        
        # 跳过元数据
        if any(cleaned.startswith(x) for x in [
            "Rudolf Steiner Online", "Seitennummern", "Anmerkungen, angegeben",
            "Steiner, Rudolf:", "Dornach (CH)", "Rudolf-Steiner-Verlag",
        ]):
            continue
        if re.match(r"^(Rudolf Steiner|Rudolf Steiner Online)\s*$", cleaned):
            continue
        
        # 还没遇到标题，创建默认章节
        if cur_lecture is None:
            cur_lecture = {
                "title_de": title_de or ga_number or "Gesamtwerk",
                "location": "",
                "date": "",
                "order_index": 0,
                "paragraphs": []
            }
            lectures.append(cur_lecture)
            lorder = 1
            pcounter = 0
        
        # 拆分句子
        sents = split_sentences(cleaned)
        if not sents:
            continue
        
        para_obj = {"order_index": pcounter, "sentences": []}
        pcounter += 1
        
        for idx, st in enumerate(sents):
            if len(st) > 5:
                para_obj["sentences"].append({"text_de": st, "order_index": idx})
        
        if para_obj["sentences"]:
            cur_lecture["paragraphs"].append(para_obj)
    
    # 如果没找到书名，用 GA 编号
    if not title_de:
        title_de = ga_number or "Unbekannt"
    
    result = {
        "title_de": title_de,
        "ga_number": ga_number,
        "lectures": lectures
    }
    
    json.dump(result, sys.stdout, ensure_ascii=False)

if __name__ == "__main__":
    main()
