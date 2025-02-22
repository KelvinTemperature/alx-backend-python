#!/usr/bin/env python3
"""Python Async Comprehension"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asyn Generator Function"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
