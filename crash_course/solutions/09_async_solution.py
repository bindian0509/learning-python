"""
=============================================================================
SOLUTIONS - Module 09: Async/Await
=============================================================================
"""

import asyncio
import time

print("=" * 50)
print("SOLUTIONS - Module 09: Async/Await")
print("=" * 50)

# Exercise 1: Countdown
print("\n--- Exercise 1: Countdown ---")

async def countdown(name: str, n: int) -> None:
    """Count down from n to 1 with delay."""
    for i in range(n, 0, -1):
        print(f"  {name}: {i}")
        await asyncio.sleep(0.5)
    print(f"  {name}: Done!")

async def run_countdowns():
    """Run two countdowns concurrently."""
    await asyncio.gather(
        countdown("Counter A", 3),
        countdown("Counter B", 3),
    )

print("Running concurrent countdowns:")
asyncio.run(run_countdowns())


# Exercise 2: Fetch URLs
print("\n--- Exercise 2: Fetch URLs ---")

async def fetch_url(url: str) -> dict:
    """Simulate fetching a URL."""
    await asyncio.sleep(0.2)  # Simulate network delay
    return {"url": url, "status": 200}

async def fetch_all(urls: list[str]) -> list[dict]:
    """Fetch all URLs concurrently."""
    tasks = [fetch_url(url) for url in urls]
    return await asyncio.gather(*tasks)

async def run_fetch_all():
    urls = [
        "https://api.example.com/users",
        "https://api.example.com/products",
        "https://api.example.com/orders",
        "https://api.example.com/reviews",
        "https://api.example.com/inventory",
    ]

    start = time.time()
    results = await fetch_all(urls)
    elapsed = time.time() - start

    print(f"Fetched {len(results)} URLs in {elapsed:.2f}s")
    for result in results:
        print(f"  {result['url']}: {result['status']}")

asyncio.run(run_fetch_all())


# Exercise 3: Timeout Handling
print("\n--- Exercise 3: Timeout Handling ---")

async def task_with_timeout(duration: float, timeout: float) -> str:
    """Try to complete a task within timeout."""
    try:
        await asyncio.wait_for(asyncio.sleep(duration), timeout=timeout)
        return "Success"
    except asyncio.TimeoutError:
        return "Timed out"

async def run_timeout_tests():
    print("Fast task (0.1s with 1s timeout):")
    result = await task_with_timeout(0.1, 1.0)
    print(f"  Result: {result}")

    print("Slow task (2s with 0.5s timeout):")
    result = await task_with_timeout(2.0, 0.5)
    print(f"  Result: {result}")

asyncio.run(run_timeout_tests())


# Exercise 4: Rate Limiter
print("\n--- Exercise 4: Rate Limiter ---")

async def limited_task(sem: asyncio.Semaphore, task_id: int) -> str:
    """Task that respects rate limiting."""
    async with sem:
        print(f"  Task {task_id} started")
        await asyncio.sleep(0.3)
        print(f"  Task {task_id} completed")
        return f"Result {task_id}"

async def run_rate_limited():
    sem = asyncio.Semaphore(3)  # Max 3 concurrent

    start = time.time()
    results = await asyncio.gather(
        *[limited_task(sem, i) for i in range(1, 11)]
    )
    elapsed = time.time() - start

    print(f"\nCompleted {len(results)} tasks in {elapsed:.2f}s")
    print(f"Expected time: ~{10/3 * 0.3:.2f}s (10 tasks, 3 concurrent, 0.3s each)")

print("Running 10 tasks with max 3 concurrent:")
asyncio.run(run_rate_limited())


# Exercise 5: Async Generator
print("\n--- Exercise 5: Async Generator ---")

async def fetch_pages(total_pages: int):
    """Async generator that yields page data."""
    for page_num in range(1, total_pages + 1):
        await asyncio.sleep(0.1)  # Simulate fetch
        yield {"page": page_num, "data": f"Content {page_num}"}

async def run_async_generator():
    print("Fetching pages:")
    async for page in fetch_pages(5):
        print(f"  Received: {page}")

asyncio.run(run_async_generator())

