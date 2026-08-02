#!/usr/bin/env python3
"""
Asinxron generator modulu.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    10 dəfə dövr edir, hər dəfə 1 saniyə gözləyir və
    0-10 arası təsadüfi bir ədəd yield edir.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
