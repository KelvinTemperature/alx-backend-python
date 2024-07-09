#!/usr/bin/env python3
"""Basic Async Function"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Async function"""
    waitTime = random.random() * max_delay
    await asyncio.sleep(waitTime)
    return waitTime
