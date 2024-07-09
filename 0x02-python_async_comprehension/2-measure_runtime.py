#!/usr/bin/env python3
"""TASK 2 Module"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure Runtime Function"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return (time.time() - start_time)
