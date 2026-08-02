#!/usr/bin/env python3
"""
Asinxron siyahı toplama) modulu.
"""
from typing import List

# Əvvəlki tapşırıqdan generatoru idxal edirik
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asinxron generatorun bütün elementlərini async comprehension
    vasitəsilə toplayır və siyahı kimi qaytarır.
    """
    return [i async for i in async_generator()]
