#!/usr/bin/env python3
"""
Dörd asinxron comprehension-ın icra müddətini ölçən modul.
"""
import asyncio
import time

# Əvvəlki tapşırıqdan async_comprehension funksiyasını idxal edirik
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    async_comprehension-ı 4 dəfə paralel şəkildə icra edir
    və ümumi keçən vaxtı ölçüb qaytarır.
    """
    start_time = time.perf_counter()

    # asyncio.gather 4 funksiyanı eyni anda başladır
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.perf_counter()
    return end_time - start_time
