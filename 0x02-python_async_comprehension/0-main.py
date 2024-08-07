#!/usr/bin/env python3

import asyncio
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())
