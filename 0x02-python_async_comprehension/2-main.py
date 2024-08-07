#!/usr/bin/env python3

import asyncio
from 2_measure_runtime import measure_runtime

async def main():
    return await measure_runtime()

print(asyncio.run(main()))
