#!/usr/bin/env python3
"""Test the improved sentence splitter."""

import sys
sys.path.insert(0, '/opt/steiner-reader/scripts')

from pdf_lecture_parser_v2 import split_into_sentences

test_cases = [
    "Am 18. August war es sehr warm. Dann ging es weiter.",
    "Er kam am 1. Januar an. Das war toll.",
    "Z.B. sollte man das machen. Und usw. auch.",
    "Der Vortrag war am 31. Dezember. Es war kalt.",
    "Siehe S. 42. Das ist wichtig.",
    "Er ist ca. 30 Jahre alt. Das ist jung.",
    "Vom 1. bis 3. März war ich weg. Dann zurück.",
    "Dies ist ein Satz. Und ein anderer.",
    "Hallo! Wie geht's? Gut.",
    "Ende.",
]

print("Testing improved sentence splitter:")
print("=" * 60)

for text in test_cases:
    print(f"\nOriginal: {text}")
    sentences = split_into_sentences(text)
    for i, sent in enumerate(sentences):
        print(f"  [{i+1}] {sent}")
    
    # Check if dates were preserved
    if any(str(x) + '.' in text for x in range(1, 32)):
        dates_preserved = all(str(x) + '.' in ' '.join(sentences) for x in range(1, 32) if str(x) + '.' in text)
        print(f"  ✓ Dates preserved: {dates_preserved}")

print("\n" + "=" * 60)
print("Test complete.")