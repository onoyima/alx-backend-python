#!/usr/bin/env python3

import asyncio
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())
