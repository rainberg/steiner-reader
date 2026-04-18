"""Translation service — German → Chinese via api2d.net (OpenAI-compatible)."""

import asyncio
from openai import AsyncOpenAI

from app.config import settings

# Async OpenAI client pointed at api2d.net
_client = None


def get_client() -> AsyncOpenAI:
    global _client
    if _client is None:
        _client = AsyncOpenAI(
            api_key=settings.DEEPSEEK_API_KEY,
            base_url=settings.DEEPSEEK_BASE_URL,
        )
    return _client


# Translation prompt optimized for Steiner's anthroposophical texts
SYSTEM_PROMPT = """你是一位精通德语和中文的翻译专家，擅长翻译鲁道夫·施泰纳的人智学著作。
翻译要求：
1. 准确传达原文含义，保持学术严谨性
2. 人智学专有名词使用通用译法（如"人智学"Anthroposophie，"以太体"Ätherleib）
3. 语言自然流畅，符合中文阅读习惯
4. 只输出译文，不要任何解释或注释"""


async def translate_sentence(text_de: str) -> str:
    """Translate a single German sentence to Chinese."""
    client = get_client()
    
    response = await client.chat.completions.create(
        model=settings.TRANSLATION_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text_de},
        ],
        temperature=0.3,
        max_tokens=1024,
    )
    
    return response.choices[0].message.content.strip()


async def translate_batch(texts: list[str], concurrency: int = 5) -> list[str]:
    """Translate a batch of sentences with concurrency control."""
    semaphore = asyncio.Semaphore(concurrency)
    
    async def translate_one(text: str) -> str:
        async with semaphore:
            return await translate_sentence(text)
    
    tasks = [translate_one(text) for text in texts]
    return await asyncio.gather(*tasks, return_exceptions=False)
