"""Translation service — German → Chinese via Google Translate (free)."""

import asyncio
import time
from deep_translator import GoogleTranslator


def translate_sentence_sync(text_de: str) -> str:
    """Translate a single German sentence to Chinese."""
    try:
        translator = GoogleTranslator(source='de', target='zh-CN')
        return translator.translate(text_de)
    except Exception as e:
        return f"[翻译失败: {e}]"


async def translate_sentence_async(text_de: str) -> str:
    """Async wrapper for single sentence translation."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, translate_sentence_sync, text_de)


async def translate_lecture_sentences(sentences: list[str], batch_size: int = 1) -> list[str]:
    """
    Translate sentences for one lecture - each sentence individually.
    No batch translation to avoid line count mismatches.
    """
    results = []
    
    for i, sentence in enumerate(sentences):
        try:
            # Translate each sentence individually
            translator = GoogleTranslator(source='de', target='zh-CN')
            translated = translator.translate(sentence)
            results.append(translated)
            
            # Progress logging every 20 sentences
            if (i + 1) % 20 == 0:
                print(f"[translator] Translated {i+1}/{len(sentences)} sentences")
                
        except Exception as e:
            print(f"[translator] Failed to translate sentence {i+1}: {e}")
            results.append(sentence)  # Fallback to original
            
        # Rate limiting: wait between translations to avoid being blocked
        # Google Translate free tier has limits, so we use a reasonable delay
        if i + 1 < len(sentences):
            await asyncio.sleep(0.3)  # 300ms between requests
    
    return results