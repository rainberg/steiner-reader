#!/usr/bin/env python3
"""
Patch pdf_lecture_parser_v2.py with improved sentence splitting.
"""

import re

OLD_FUNCTION = '''def split_into_sentences(text):
    sentences = re.split(r'(?<=[.!?])\\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 2]'''

NEW_FUNCTION = '''def split_into_sentences(text):
    """
    Improved sentence splitting for German text.
    Handles dates and common abbreviations.
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
    
    # Handle dates: \d{1,2}. followed by capital letter (month)
    # German month names
    months = [
        'Januar', 'Februar', 'März', 'April', 'Mai', 'Juni',
        'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'
    ]
    month_pattern = '|'.join(months)
    
    # Replace "18. August" -> "18###DATE### August"
    text = re.sub(r'(\\b\\d{1,2})\\.\\s+(' + month_pattern + r'\\b)', r'\\1###DATE### \\2', text, flags=re.IGNORECASE)
    
    # Handle standalone dates: "Am 18." -> "Am 18###DATE###"
    text = re.sub(r'(\\b\\d{1,2})\\.(?=\\s|$)', r'\\1###DATE###', text)
    
    # Split sentences
    sentences = re.split(r'(?<=[.!?])\\s+', text)
    
    # Restore abbreviations and dates
    sentences = [s.replace('###ABBR###', '.').replace('###DATE###', '.') for s in sentences]
    
    # Filter
    sentences = [s.strip() for s in sentences if len(s.strip()) > 2]
    
    return sentences'''

def patch_file():
    with open('/opt/steiner-reader/scripts/pdf_lecture_parser_v2.py', 'r') as f:
        content = f.read()
    
    if OLD_FUNCTION in content:
        new_content = content.replace(OLD_FUNCTION, NEW_FUNCTION)
        
        with open('/opt/steiner-reader/scripts/pdf_lecture_parser_v2.py', 'w') as f:
            f.write(new_content)
        
        print("Successfully patched pdf_lecture_parser_v2.py")
        return True
    else:
        print("Old function not found. Checking for alternative formatting...")
        # Try with slightly different formatting
        old_variant = '''def split_into_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if len(s.strip()) > 2]'''
        
        if old_variant in content:
            new_content = content.replace(old_variant, NEW_FUNCTION)
            with open('/opt/steiner-reader/scripts/pdf_lecture_parser_v2.py', 'w') as f:
                f.write(new_content)
            print("Successfully patched (variant)")
            return True
        else:
            print("Could not find split_into_sentences function")
            return False

if __name__ == '__main__':
    patch_file()