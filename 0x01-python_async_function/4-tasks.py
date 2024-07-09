#!/usr/bin/env python3
"""Concurrent Coroutine"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """concurrent async function"""

    res = await asyncio.gather(
            *tuple(task_wait_random(max_delay) for i in range(n)))
    return sorted(res)
