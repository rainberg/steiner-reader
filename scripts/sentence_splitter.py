import re

def split_into_sentences_v2(text):
    """
    Improved sentence splitting for German text.
    Handles dates, abbreviations, and common German patterns.
    """
    if not text or not text.strip():
        return []
    
    # Clean text
    text = text.strip()
    
    # Patterns where period should NOT split sentences
    # 1. Dates: "18. August", "1. Januar", "31." (standalone date)
    date_pattern = r'\b(\d{1,2}\.)\s+[A-ZÄÖÜ][a-zäöüß]+'
    
    # 2. Common German abbreviations (case-insensitive)
    abbreviations = [
        r'z\.B\.', r'd\.h\.', r'u\.a\.', r'v\.a\.', r'usw\.', r'etc\.',
        r'ca\.', r'Nr\.', r'Dr\.', r'Prof\.', r'bspw\.', r'evtl\.',
        r'ggf\.', r'inkl\.', r'exkl\.', r'sog\.', r'bzw\.', r'insb\.',
        r'min\.', r'max\.', r'S\.', r's\.', r'f\.', r'ff\.'
    ]
    
    # 3. Ordinal numbers: "1. Vortrag", "zweiter.", "dritter."
    ordinal_pattern = r'\b(\d{1,2}\.)\s+[A-ZÄÖÜ]'
    
    # Combine patterns where period should not cause split
    non_splitting_patterns = '|'.join(abbreviations) + '|' + date_pattern + '|' + ordinal_pattern
    
    # Temporary replacement: replace problematic periods with a placeholder
    placeholder = '###PERIOD###'
    
    # Find all matches of non-splitting patterns and replace periods with placeholder
    import re
    positions = []
    
    # First, mark positions where we have dates like "18. August"
    for match in re.finditer(r'\b\d{1,2}\.\s+[A-ZÄÖÜ][a-zäöüß]+', text):
        start, end = match.span()
        # Replace the period within this match
        match_text = text[start:end]
        modified = match_text.replace('.', placeholder)
        text = text[:start] + modified + text[end:]
        # Adjust positions for future matches
        length_diff = len(modified) - len(match_text)
        end += length_diff
    
    # Mark common abbreviations
    for abbr in abbreviations:
        pattern = abbr.replace(r'\.', r'\.')  # Ensure literal period in pattern
        for match in re.finditer(pattern, text, re.IGNORECASE):
            start, end = match.span()
            match_text = text[start:end]
            modified = match_text.replace('.', placeholder)
            text = text[:start] + modified + text[end:]
            length_diff = len(modified) - len(match_text)
            end += length_diff
    
    # Now split on periods, exclamation marks, question marks
    # Use regex that looks for these punctuation marks followed by whitespace
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Restore original periods
    sentences = [s.replace(placeholder, '.') for s in sentences]
    
    # Filter empty or very short sentences
    sentences = [s.strip() for s in sentences if len(s.strip()) > 2]
    
    return sentences


def split_into_sentences_simple(text):
    """
    Simple sentence splitting for German text with basic abbreviation handling.
    This is a more practical approach than the complex placeholder method.
    """
    if not text or not text.strip():
        return []
    
    text = text.strip()
    
    # Common German abbreviations that end with period but don't end sentences
    abbreviations = [
        'z.B.', 'd.h.', 'u.a.', 'v.a.', 'usw.', 'etc.',
        'ca.', 'Nr.', 'Dr.', 'Prof.', 'bspw.', 'evtl.',
        'ggf.', 'inkl.', 'exkl.', 'sog.', 'bzw.', 'insb.',
        'min.', 'max.', 'S.', 's.', 'f.', 'ff.'
    ]
    
    # Add space after abbreviations to prevent splitting
    for abbr in abbreviations:
        # Case insensitive replacement
        pattern = re.compile(re.escape(abbr), re.IGNORECASE)
        replacement = abbr.replace('.', '###ABBR###')
        text = pattern.sub(replacement, text)
    
    # Also handle dates: \d{1,2}. followed by capital letter (month)
    # Replace "18. August" -> "18###DATE### August"
    text = re.sub(r'(\b\d{1,2})\.\s+([A-ZÄÖÜ][a-zäöüß]+)', r'\1###DATE### \2', text)
    
    # Handle standalone dates: "Am 18." -> "Am 18###DATE###"
    text = re.sub(r'(\b\d{1,2})\.(?=\s|$)', r'\1###DATE###', text)
    
    # Split sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Restore abbreviations and dates
    sentences = [s.replace('###ABBR###', '.').replace('###DATE###', '.') for s in sentences]
    
    # Filter
    sentences = [s.strip() for s in sentences if len(s.strip()) > 2]
    
    return sentences


if __name__ == '__main__':
    # Test cases
    test_texts = [
        "Am 18. August war es sehr warm. Dann ging es weiter.",
        "Er kam am 1. Januar an. Das war toll.",
        "Z.B. sollte man das machen. Und usw. auch.",
        "Der Vortrag war am 31. Dezember. Es war kalt.",
        "Siehe S. 42. Das ist wichtig.",
        "Er ist ca. 30 Jahre alt. Das ist jung.",
        "Vom 1. bis 3. März war ich weg. Dann zurück."
    ]
    
    print("Testing split_into_sentences_simple:")
    for text in test_texts:
        print(f"\nOriginal: {text}")
        sentences = split_into_sentences_simple(text)
        for i, sent in enumerate(sentences):
            print(f"  Sentence {i+1}: {sent}")