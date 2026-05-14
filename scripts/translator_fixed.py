"""
Translation service — German → Chinese via Google Translate (free).
"""

import asyncio
from deep_translator import GoogleTranslator


def translate_sentence(text_de: str) -> str:
    """Translate a single German sentence to Chinese."""
    try:
        translator = GoogleTranslator(source='de', target='zh-CN')
        return translator.translate(text_de)
    except Exception as e:
        return f"[翻译失败: {e}]"


async def translate_sentence_async(text_de: str) -> str:
    """Async wrapper."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, translate_sentence, text_de)


async def translate_lecture_sentences(sentences: list[str], batch_size: int = 10) -> list[str]:
    """
    Translate sentences for one lecture in small batches.
    Google Translate limit: ~5000 chars per request.
    batch_size=10 sentences per request keeps us well under the limit.
    """
    results = []
    
    for i in range(0, len(sentences), batch_size):
        batch = sentences[i:i + batch_size]
        
        # Join with newlines for batch translation
        joined = "\n".join(batch)
        
        # Truncate if too long (safety)
        if len(joined) > 4500:
            joined = joined[:4500]
        
        try:
            translator = GoogleTranslator(source='de', target='zh-CN')
            translated = translator.translate(joined)
            
            # Split back into individual translations
            parts = translated.split("\n")
            
            # CRITICAL FIX: If line count doesn't match, fallback to sentence-by-sentence
            if len(parts) != len(batch):
                print(f"[translator] Batch {i//batch_size}: Got {len(parts)} lines, expected {len(batch)}. Falling back to sentence-by-sentence.")
                # Translate each sentence individually for this batch
                batch_results = []
                for sent in batch:
                    try:
                        batch_results.append(translate_sentence(sent))
                        await asyncio.sleep(0.2)  # Small delay between sentences
                    except Exception as e:
                        batch_results.append(sent)  # Fallback to original
                results.extend(batch_results)
            else:
                # Line count matches, use batch results
                for j, sent in enumerate(batch):
                    if j < len(parts):
                        results.append(parts[j].strip())
                    else:
                        results.append(sent)  # Fallback to original
        
        except Exception as e:
            print(f"[translator] Batch translation failed: {e}. Falling back to sentence-by-sentence.")
            # On failure, translate each sentence individually
            batch_results = []
            for sent in batch:
                try:
                    batch_results.append(translate_sentence(sent))
                    await asyncio.sleep(0.2)
                except Exception as e2:
                    batch_results.append(sent)
            results.extend(batch_results)
        
        # Small delay to avoid rate limiting
        if i + batch_size < len(sentences):
            await asyncio.sleep(0.5)
    
    return results