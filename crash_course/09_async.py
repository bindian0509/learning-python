"""
=============================================================================
PYTHON 3 CRASH COURSE - Module 09: Async/Await
=============================================================================
Topics: async/await, asyncio basics, concurrent execution

Run this file: python3 09_async.py
=============================================================================
"""

import asyncio
import time

# =============================================================================
# 1. SYNC VS ASYNC - THE PROBLEM
# =============================================================================

print("=== SYNC VS ASYNC - THE PROBLEM ===")

def sync_task(name: str, duration: float) -> str:
    """Synchronous task that blocks."""
    print(f"  [{name}] Starting (will take {duration}s)")
    time.sleep(duration)  # Blocks the entire program!
    print(f"  [{name}] Completed")
    return f"{name} result"

print("\nRunning 3 sync tasks (total ~3 seconds):")
start = time.time()
result1 = sync_task("Task1", 1)
result2 = sync_task("Task2", 1)
result3 = sync_task("Task3", 1)
print(f"Total time: {time.time() - start:.2f}s")
print(f"Results: {result1}, {result2}, {result3}")


# =============================================================================
# 2. BASIC ASYNC/AWAIT
# =============================================================================

print("\n" + "=" * 50)
print("=== BASIC ASYNC/AWAIT ===")

# async def creates a coroutine function
async def async_task(name: str, duration: float) -> str:
    """Asynchronous task that doesn't block."""
    print(f"  [{name}] Starting (will take {duration}s)")
    await asyncio.sleep(duration)  # Non-blocking sleep!
    print(f"  [{name}] Completed")
    return f"{name} result"

# Running a single coroutine
async def main_single():
    result = await async_task("SingleTask", 0.5)
    print(f"Result: {result}")

print("\nRunning single async task:")
asyncio.run(main_single())


# =============================================================================
# 3. RUNNING TASKS CONCURRENTLY
# =============================================================================

print("\n" + "=" * 50)
print("=== RUNNING TASKS CONCURRENTLY ===")

async def main_concurrent():
    """Run multiple tasks concurrently with gather."""
    print("Starting 3 async tasks concurrently...")
    start = time.time()

    # asyncio.gather runs coroutines concurrently
    results = await asyncio.gather(
        async_task("Task1", 1),
        async_task("Task2", 1),
        async_task("Task3", 1),
    )

    print(f"Total time: {time.time() - start:.2f}s")
    print(f"Results: {results}")
    return results

print("\nRunning 3 async tasks concurrently (total ~1 second):")
asyncio.run(main_concurrent())


# =============================================================================
# 4. CREATING TASKS
# =============================================================================

print("\n" + "=" * 50)
print("=== CREATING TASKS ===")

async def main_tasks():
    """Create and manage individual tasks."""
    print("Creating tasks...")

    # Create tasks (they start running immediately!)
    task1 = asyncio.create_task(async_task("Task1", 0.5))
    task2 = asyncio.create_task(async_task("Task2", 0.3))
    task3 = asyncio.create_task(async_task("Task3", 0.4))

    print("Tasks created, doing other work...")
    await asyncio.sleep(0.1)
    print("Other work done, waiting for tasks...")

    # Wait for all tasks
    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(f"All results: {result1}, {result2}, {result3}")

asyncio.run(main_tasks())


# =============================================================================
# 5. TASK GROUPS (Python 3.11+)
# =============================================================================

print("\n" + "=" * 50)
print("=== TASK GROUPS (Python 3.11+) ===")

async def main_taskgroup():
    """Use TaskGroup for structured concurrency."""
    print("Using TaskGroup...")

    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(async_task("Task1", 0.3))
        task2 = tg.create_task(async_task("Task2", 0.2))
        task3 = tg.create_task(async_task("Task3", 0.4))

    # All tasks guaranteed complete here
    print(f"Results: {task1.result()}, {task2.result()}, {task3.result()}")

try:
    asyncio.run(main_taskgroup())
except AttributeError:
    print("TaskGroup requires Python 3.11+")


# =============================================================================
# 6. HANDLING EXCEPTIONS
# =============================================================================

print("\n" + "=" * 50)
print("=== HANDLING EXCEPTIONS ===")

async def failing_task(name: str, should_fail: bool) -> str:
    await asyncio.sleep(0.1)
    if should_fail:
        raise ValueError(f"{name} failed!")
    return f"{name} succeeded"

async def main_exceptions():
    """Handle exceptions in async code."""

    # Method 1: try/except around gather
    print("\nMethod 1: try/except with return_exceptions=False")
    try:
        results = await asyncio.gather(
            failing_task("Task1", False),
            failing_task("Task2", True),  # Will fail
            failing_task("Task3", False),
        )
    except ValueError as e:
        print(f"  Caught exception: {e}")

    # Method 2: return_exceptions=True
    print("\nMethod 2: return_exceptions=True")
    results = await asyncio.gather(
        failing_task("Task1", False),
        failing_task("Task2", True),  # Returns exception instead of raising
        failing_task("Task3", False),
        return_exceptions=True
    )

    for i, result in enumerate(results, 1):
        if isinstance(result, Exception):
            print(f"  Task{i}: Exception - {result}")
        else:
            print(f"  Task{i}: Success - {result}")

asyncio.run(main_exceptions())


# =============================================================================
# 7. TIMEOUTS
# =============================================================================

print("\n" + "=" * 50)
print("=== TIMEOUTS ===")

async def slow_task():
    print("  Slow task starting...")
    await asyncio.sleep(5)  # Takes 5 seconds
    return "Slow task complete"

async def main_timeout():
    """Demonstrate timeout handling."""

    # Method 1: wait_for with timeout
    print("\nUsing wait_for with 1s timeout:")
    try:
        result = await asyncio.wait_for(slow_task(), timeout=1.0)
        print(f"  Result: {result}")
    except asyncio.TimeoutError:
        print("  Task timed out!")

    # Method 2: timeout context manager (Python 3.11+)
    print("\nUsing timeout context manager:")
    try:
        async with asyncio.timeout(1.0):
            result = await slow_task()
    except asyncio.TimeoutError:
        print("  Task timed out!")
    except AttributeError:
        print("  asyncio.timeout requires Python 3.11+")

asyncio.run(main_timeout())


# =============================================================================
# 8. ASYNC ITERATORS AND GENERATORS
# =============================================================================

print("\n" + "=" * 50)
print("=== ASYNC ITERATORS AND GENERATORS ===")

async def async_range(start: int, stop: int, delay: float = 0.1):
    """Async generator that yields numbers with delay."""
    for i in range(start, stop):
        await asyncio.sleep(delay)
        yield i

async def main_async_iter():
    """Demonstrate async iteration."""
    print("Async for loop:")
    async for num in async_range(1, 5):
        print(f"  Got: {num}")

    # Async comprehension
    print("\nAsync comprehension:")
    squares = [x**2 async for x in async_range(1, 5)]
    print(f"  Squares: {squares}")

asyncio.run(main_async_iter())


# =============================================================================
# 9. ASYNC CONTEXT MANAGERS
# =============================================================================

print("\n" + "=" * 50)
print("=== ASYNC CONTEXT MANAGERS ===")

class AsyncResource:
    """Example async context manager."""

    def __init__(self, name: str):
        self.name = name

    async def __aenter__(self):
        print(f"  Acquiring {self.name}...")
        await asyncio.sleep(0.1)  # Simulate async setup
        print(f"  {self.name} acquired")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"  Releasing {self.name}...")
        await asyncio.sleep(0.1)  # Simulate async cleanup
        print(f"  {self.name} released")
        return False

async def main_async_context():
    """Demonstrate async context manager."""
    async with AsyncResource("DatabaseConnection") as resource:
        print(f"  Using {resource.name}")
        await asyncio.sleep(0.1)

asyncio.run(main_async_context())


# =============================================================================
# 10. PRACTICAL EXAMPLE: CONCURRENT API CALLS
# =============================================================================

print("\n" + "=" * 50)
print("=== PRACTICAL EXAMPLE: CONCURRENT API CALLS ===")

async def fetch_user(user_id: int) -> dict:
    """Simulate API call to fetch user."""
    await asyncio.sleep(0.2)  # Simulate network delay
    return {"id": user_id, "name": f"User{user_id}"}

async def fetch_posts(user_id: int) -> list:
    """Simulate API call to fetch user's posts."""
    await asyncio.sleep(0.3)  # Simulate network delay
    return [{"id": i, "title": f"Post {i}"} for i in range(1, 4)]

async def fetch_user_with_posts(user_id: int) -> dict:
    """Fetch user and their posts concurrently."""
    user, posts = await asyncio.gather(
        fetch_user(user_id),
        fetch_posts(user_id)
    )
    user["posts"] = posts
    return user

async def main_api_example():
    """Demonstrate concurrent API pattern."""
    print("Fetching data for users 1, 2, 3 concurrently...")
    start = time.time()

    users = await asyncio.gather(
        fetch_user_with_posts(1),
        fetch_user_with_posts(2),
        fetch_user_with_posts(3),
    )

    print(f"Time taken: {time.time() - start:.2f}s")
    for user in users:
        print(f"  User {user['id']}: {user['name']}, {len(user['posts'])} posts")

asyncio.run(main_api_example())


# =============================================================================
# 11. SEMAPHORES - LIMITING CONCURRENCY
# =============================================================================

print("\n" + "=" * 50)
print("=== SEMAPHORES - LIMITING CONCURRENCY ===")

async def rate_limited_task(sem: asyncio.Semaphore, task_id: int):
    """Task that respects rate limiting."""
    async with sem:
        print(f"  Task {task_id} acquired semaphore")
        await asyncio.sleep(0.5)
        print(f"  Task {task_id} releasing semaphore")
    return f"Task {task_id} done"

async def main_semaphore():
    """Limit concurrent tasks with semaphore."""
    # Only allow 2 concurrent tasks
    sem = asyncio.Semaphore(2)

    print("Running 5 tasks with max 2 concurrent:")
    start = time.time()

    results = await asyncio.gather(
        *[rate_limited_task(sem, i) for i in range(1, 6)]
    )

    print(f"Time taken: {time.time() - start:.2f}s")
    print(f"Results: {results}")

asyncio.run(main_semaphore())


# =============================================================================
# 12. ASYNC DEF VS DEF IN FASTAPI
# =============================================================================

print("\n" + "=" * 50)
print("=== ASYNC DEF VS DEF IN FASTAPI ===")

print("""
FastAPI handles both async and sync functions:

# Async endpoint - for I/O-bound operations
@app.get("/async-endpoint")
async def async_endpoint():
    result = await some_async_operation()
    return {"result": result}

# Sync endpoint - for CPU-bound or blocking operations
@app.get("/sync-endpoint")
def sync_endpoint():
    result = some_blocking_operation()
    return {"result": result}

When to use async def:
- Database queries (async drivers)
- HTTP requests to other services
- File I/O (async file operations)
- Any operation using await

When to use def:
- CPU-intensive calculations
- Using libraries without async support
- Simple operations with no I/O

FastAPI runs sync functions in a thread pool automatically!
""")


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# TODO Exercise 1: Basic Async Function
# Create an async function `countdown(name, n)` that:
# - Counts down from n to 1 with 0.5s delay between numbers
# - Prints each number with the name
# Run two countdowns concurrently
print("\n--- Exercise 1: Countdown ---")
# Your code here:


# TODO Exercise 2: Fetch Multiple URLs
# Create async functions:
# - fetch_url(url) - simulate fetching (0.2s delay), return {"url": url, "status": 200}
# - fetch_all(urls) - fetch all URLs concurrently, return list of results
# Test with 5 URLs
print("\n--- Exercise 2: Fetch URLs ---")
# Your code here:


# TODO Exercise 3: Timeout Handling
# Create an async function that:
# - Tries to complete a task within a timeout
# - Returns "Success" if completed
# - Returns "Timed out" if timeout exceeded
# Test with both fast and slow tasks
print("\n--- Exercise 3: Timeout Handling ---")
# Your code here:


# TODO Exercise 4: Rate Limiter
# Create a rate limiter that:
# - Allows max 3 concurrent operations
# - Run 10 tasks through it
# - Each task takes 0.3s
# Measure total time (should be ~1.2s with 3 concurrent)
print("\n--- Exercise 4: Rate Limiter ---")
# Your code here:


# TODO Exercise 5: Async Generator
# Create an async generator `fetch_pages(total_pages)` that:
# - Simulates fetching pages (0.1s per page)
# - Yields {"page": n, "data": f"Content {n}"}
# Use async for to consume it
print("\n--- Exercise 5: Async Generator ---")
# Your code here:


print("\n" + "=" * 50)
print("Run the solution file to check your answers!")
print("=" * 50)

