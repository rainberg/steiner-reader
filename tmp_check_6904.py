import json, urllib.request

lecture_id = 6904

info = json.loads(urllib.request.urlopen(f'http://localhost:8000/api/lectures/{lecture_id}').read())
print("Lecture info:")
print(f"  is_published: {info.get('is_published')}")
print(f"  has_access: {info.get('has_access')}")

paras = json.loads(urllib.request.urlopen(f'http://localhost:8000/api/lectures/{lecture_id}/paragraphs').read())
total = 0
translated = 0
for p in paras:
    for s in p['sentences']:
        total += 1
        if s.get('text_zh'):
            translated += 1
print(f"\nParagraphs (no auth): {len(paras)}")
print(f"Sentences: total={total}, translated={translated}")
print(f"First sentence text_zh: {paras[0]['sentences'][0].get('text_zh')}")
