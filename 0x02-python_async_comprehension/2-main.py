#!/usr/bin/env python3

import asyncio
from importlib import import_module as using

measure_runtime = using('2-measure_runtime').measure_runtime

async def main():
    return await measure_runtime()

print(asyncio.run(main()))
