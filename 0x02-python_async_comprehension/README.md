# Async Comprehension Project

This project contains a series of tasks to practice asynchronous programming with Python using async comprehensions.

## Requirements
- All files should end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- Code should adhere to the pycodestyle style.
- All modules and functions must have documentation.
- All functions and coroutines must be type-annotated.

## Tasks

### Task 0: Async Generator
- Write a coroutine called `async_generator` that loops 10 times, waits 1 second asynchronously each time, and yields a random number between 0 and 10.

### Task 1: Async Comprehensions
- Write a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`, then returns the 10 random numbers.

### Task 2: Run time for four parallel comprehensions
- Write a coroutine called `measure_runtime` that will execute `async_comprehension` four times in parallel using `asyncio.gather` and measure the total runtime.

## Usage
To run the project, use the following commands:

```sh
chmod +x *.py
./0-main.py
./1-main.py
./2-main.py

