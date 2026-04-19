"""Translation service — German → Chinese via Google Translate (free)."""

import asyncio
from deep_translator import GoogleTranslator

# Google Translate is free, no API key needed
_translator = GoogleTranslator(source='de', target='zh-CN')


def translate_sentence(text_de: str) -> str:
    """Translate a single German sentence to Chinese (synchronous)."""
    try:
        result = _translator.translate(text_de)
        return result if result else text_de
    except Exception as e:
        return f"[翻译失败: {e}]"


async def translate_sentence_async(text_de: str) -> str:
    """Async wrapper for translate_sentence."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, translate_sentence, text_de)


async def translate_batch(texts: list[str], concurrency: int = 5) -> list[str]:
    """Translate a batch of sentences. Google Translate handles batching well."""
    # Google Translate has a limit of ~5000 chars per request
    # Split into chunks if needed
    results = []
    chunk = []
    chunk_len = 0
    
    for text in texts:
        if chunk_len + len(text) > 4500 and chunk:
            # Translate current chunk
            try:
                joined = "\n".join(chunk)
                translated = await translate_sentence_async(joined)
                results.extend(translated.split("\n"))
            except Exception:
                results.extend(chunk)  # Fallback to original text
            chunk = []
            chunk_len = 0
        
        chunk.append(text)
        chunk_len += len(text)
    
    # Translate remaining
    if chunk:
        try:
            joined = "\n".join(chunk)
            translated = await translate_sentence_async(joined)
            results.extend(translated.split("\n"))
        except Exception:
            results.extend(chunk)
    
    return results
