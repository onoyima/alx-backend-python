#!/usr/bin/env python3
"""
Module 1-async_comprehension
Contains a coroutine that collects random numbers using async comprehension.
"""

import asyncio
from typing import List
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [number async for number in async_generator()]
