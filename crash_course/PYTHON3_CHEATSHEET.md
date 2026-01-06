# Python 3 Cheat Sheet for Backend Developers

A quick reference guide for Python 3 syntax, patterns, and best practices.

---

## Table of Contents

1. [Variables & Data Types](#variables--data-types)
2. [Strings](#strings)
3. [Collections](#collections)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Classes & OOP](#classes--oop)
7. [Error Handling](#error-handling)
8. [Type Hints](#type-hints)
9. [Async/Await](#asyncawait)
10. [Common Gotchas](#common-gotchas)
11. [FastAPI Quick Reference](#fastapi-quick-reference)

---

## Variables & Data Types

### Basic Types

```python
# Numbers
x = 42              # int
y = 3.14            # float
z = 1_000_000       # int with separator (Python 3.6+)

# Strings
name = "Alice"
name = 'Alice'      # Same thing
multi = """Multi
line string"""

# Boolean
is_active = True
is_empty = False

# None (null equivalent)
result = None
```

### Type Checking

```python
type(42)           # <class 'int'>
isinstance(42, int)  # True
isinstance(42, (int, float))  # True (multiple types)
```

### Type Conversion

```python
int("42")          # 42
float("3.14")      # 3.14
str(42)            # "42"
bool(0)            # False
bool("hello")      # True
list("abc")        # ['a', 'b', 'c']
```

---

## Strings

### F-Strings (Python 3.6+)

```python
name = "Alice"
age = 30

# Basic interpolation
f"Hello, {name}!"

# Expressions
f"Next year: {age + 1}"

# Formatting
f"Price: ${99.99:.2f}"        # Price: $99.99
f"Percent: {0.856:.1%}"       # Percent: 85.6%
f"Padded: {42:05d}"           # Padded: 00042
f"Left: {name:<10}"           # Left: Alice
f"Right: {name:>10}"          # Right:      Alice
f"Center: {name:^10}"         # Center:   Alice

# Debug mode (Python 3.8+)
f"{name=}"                    # name='Alice'
```

### Common String Methods

```python
s = "  Hello World  "

s.strip()              # "Hello World"
s.lower()              # "  hello world  "
s.upper()              # "  HELLO WORLD  "
s.title()              # "  Hello World  "
s.replace("World", "Python")
s.split()              # ["Hello", "World"]
s.split(",")           # Split by delimiter
"-".join(["a", "b"])   # "a-b"

# Validation
"123".isdigit()        # True
"abc".isalpha()        # True
"abc123".isalnum()     # True

# Search
"Hello" in s           # True
s.startswith("  He")   # True
s.find("World")        # Index or -1
```

### String Slicing

```python
s = "Python"
s[0]       # 'P' (first)
s[-1]      # 'n' (last)
s[0:3]     # 'Pyt' (start:end)
s[2:]      # 'thon' (from index)
s[:3]      # 'Pyt' (until index)
s[::2]     # 'Pto' (every 2nd)
s[::-1]    # 'nohtyP' (reversed)
```

---

## Collections

### Lists (Mutable, Ordered)

```python
# Create
nums = [1, 2, 3]
nums = list(range(5))  # [0, 1, 2, 3, 4]

# Access
nums[0]        # First
nums[-1]       # Last
nums[1:3]      # Slice

# Modify
nums.append(4)          # Add to end
nums.insert(0, -1)      # Insert at index
nums.extend([5, 6])     # Add multiple
nums.remove(2)          # Remove by value
nums.pop()              # Remove last
nums.pop(0)             # Remove at index
nums.sort()             # Sort in place
nums.reverse()          # Reverse in place

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
```

### Dictionaries (Key-Value)

```python
# Create
d = {"name": "Alice", "age": 30}
d = dict(name="Alice", age=30)

# Access
d["name"]              # "Alice" (KeyError if missing)
d.get("name")          # "Alice" (None if missing)
d.get("city", "N/A")   # Default value

# Modify
d["email"] = "a@b.com"  # Add/Update
del d["email"]          # Delete
d.pop("age")            # Remove and return
d.update({"x": 1})      # Update multiple

# Iterate
for key in d: ...
for key, value in d.items(): ...
for value in d.values(): ...

# Dict comprehension
squares = {x: x**2 for x in range(5)}

# Merge (Python 3.9+)
merged = d1 | d2
```

### Sets (Unique, Unordered)

```python
# Create
s = {1, 2, 3}
s = set([1, 2, 2, 3])  # {1, 2, 3}

# Operations
s.add(4)
s.remove(1)     # KeyError if missing
s.discard(1)    # No error if missing

# Set math
a | b   # Union
a & b   # Intersection
a - b   # Difference
a ^ b   # Symmetric difference
```

### Tuples (Immutable)

```python
# Create
t = (1, 2, 3)
single = (42,)   # Note the comma!

# Unpacking
x, y, z = t
first, *rest = [1, 2, 3, 4]  # first=1, rest=[2,3,4]
```

---

## Control Flow

### Conditionals

```python
if condition:
    pass
elif other_condition:
    pass
else:
    pass

# Ternary
result = "yes" if condition else "no"

# Chained comparison
if 0 <= x <= 100:
    pass
```

### Loops

```python
# For loop
for item in collection:
    pass

for i in range(10):           # 0-9
for i in range(1, 10):        # 1-9
for i in range(0, 10, 2):     # 0, 2, 4, 6, 8

for i, item in enumerate(lst):          # Index + value
for a, b in zip(list1, list2):          # Parallel iteration
for key, value in dict.items():         # Dict iteration

# While loop
while condition:
    pass

# Control
break       # Exit loop
continue    # Skip to next iteration
pass        # Do nothing (placeholder)
```

### Match-Case (Python 3.10+)

```python
match value:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or three")
    case str() as s:
        print(f"String: {s}")
    case _:
        print("Default")
```

---

## Functions

### Basic Functions

```python
def greet(name):
    """Docstring describing the function."""
    return f"Hello, {name}!"

# Default arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Multiple return values
def get_stats(nums):
    return min(nums), max(nums), sum(nums)

minimum, maximum, total = get_stats([1, 2, 3])
```

### *args and **kwargs

```python
def func(*args, **kwargs):
    print(args)    # Tuple of positional args
    print(kwargs)  # Dict of keyword args

func(1, 2, 3, x=10, y=20)
# args = (1, 2, 3)
# kwargs = {'x': 10, 'y': 20}

# Unpacking
nums = [1, 2, 3]
func(*nums)           # Same as func(1, 2, 3)

params = {"a": 1, "b": 2}
func(**params)        # Same as func(a=1, b=2)
```

### Lambda Functions

```python
square = lambda x: x ** 2
add = lambda x, y: x + y

# Common with sorted, filter, map
sorted(items, key=lambda x: x["name"])
list(filter(lambda x: x > 0, nums))
list(map(lambda x: x * 2, nums))
```

### Decorators

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before")
        result = func(*args, **kwargs)
        print("After")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hi!")
```

---

## Classes & OOP

### Basic Class

```python
class Person:
    # Class attribute
    species = "Human"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name}"

    @classmethod
    def from_string(cls, s):
        name, age = s.split("-")
        return cls(name, int(age))

    @staticmethod
    def is_adult(age):
        return age >= 18

    def __str__(self):
        return f"Person({self.name})"

    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"
```

### Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"
```

### Properties

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Negative radius")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```

### Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class User:
    name: str
    email: str
    age: int = 0
    tags: List[str] = field(default_factory=list)

# Auto-generates __init__, __repr__, __eq__
user = User("Alice", "alice@example.com", 30)
```

---

## Error Handling

### Try/Except

```python
try:
    result = risky_operation()
except ValueError as e:
    print(f"Value error: {e}")
except (TypeError, KeyError):
    print("Type or key error")
except Exception as e:
    print(f"Unexpected: {e}")
else:
    print("No exception occurred")
finally:
    print("Always runs")
```

### Raising Exceptions

```python
raise ValueError("Invalid input")
raise ValueError("Invalid input") from original_error

# Re-raise current exception
except Exception:
    logging.error("Failed")
    raise
```

### Custom Exceptions

```python
class APIError(Exception):
    pass

class NotFoundError(APIError):
    def __init__(self, resource_id):
        self.resource_id = resource_id
        super().__init__(f"Resource {resource_id} not found")
```

### Context Managers

```python
# File handling
with open("file.txt", "r") as f:
    content = f.read()

# Custom context manager
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Elapsed: {time.time() - start}")

with timer():
    do_something()
```

---

## Type Hints

### Basic Types

```python
from typing import Optional, Union, List, Dict, Any, Callable

def greet(name: str) -> str:
    return f"Hello, {name}"

# Variables
count: int = 0
names: list[str] = ["Alice", "Bob"]
config: dict[str, Any] = {}

# Optional (can be None)
def find(id: int) -> Optional[str]:
    ...

# Union (multiple types)
def process(id: int | str) -> None:  # Python 3.10+
    ...
```

### Complex Types

```python
from typing import TypedDict, Protocol, Literal

# TypedDict
class User(TypedDict):
    name: str
    email: str

# Protocol
class Drawable(Protocol):
    def draw(self) -> None: ...

# Literal
def set_mode(mode: Literal["read", "write"]) -> None:
    ...

# Callable
def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
```

---

## Async/Await

### Basic Async

```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return "data"

# Run single coroutine
asyncio.run(fetch_data())

# Run multiple concurrently
async def main():
    results = await asyncio.gather(
        fetch_data(),
        fetch_data(),
        fetch_data(),
    )
    return results
```

### Tasks and Timeouts

```python
async def main():
    # Create task
    task = asyncio.create_task(fetch_data())
    result = await task

    # Timeout
    try:
        result = await asyncio.wait_for(fetch_data(), timeout=5.0)
    except asyncio.TimeoutError:
        print("Timed out")
```

### Rate Limiting

```python
sem = asyncio.Semaphore(3)  # Max 3 concurrent

async def limited_fetch(url):
    async with sem:
        return await fetch(url)
```

---

## Common Gotchas

### 1. Mutable Default Arguments

```python
# BAD - same list shared between calls!
def append(item, lst=[]):
    lst.append(item)
    return lst

# GOOD
def append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### 2. Variable Scope in Loops

```python
# BAD - all lambdas reference same i
funcs = [lambda: i for i in range(3)]
[f() for f in funcs]  # [2, 2, 2]

# GOOD - capture i's value
funcs = [lambda i=i: i for i in range(3)]
[f() for f in funcs]  # [0, 1, 2]
```

### 3. Modifying List While Iterating

```python
# BAD
for item in items:
    if condition:
        items.remove(item)  # Skips items!

# GOOD
items = [item for item in items if not condition]
```

### 4. Integer Division

```python
# Python 3
5 / 2   # 2.5 (float division)
5 // 2  # 2 (integer division)
```

### 5. is vs ==

```python
# Use == for value comparison
if x == 5: ...

# Use is for identity (None, True, False)
if x is None: ...
if x is not None: ...
```

---

## FastAPI Quick Reference

### Basic App

```python
from fastapi import FastAPI, HTTPException, Query, Path, Depends
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}
```

### Path and Query Parameters

```python
@app.get("/items/{item_id}")
async def get_item(
    item_id: int = Path(..., ge=1),
    q: Optional[str] = Query(None, max_length=50),
    skip: int = 0,
    limit: int = 10
):
    return {"item_id": item_id, "q": q}
```

### Request Body (Pydantic)

```python
class Item(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    description: Optional[str] = None

@app.post("/items")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}
```

### Response Model

```python
class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    # password NOT included

@app.post("/items", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    return created_item  # FastAPI filters output
```

### Error Handling

```python
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id not in db:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )
    return db[item_id]
```

### Dependencies

```python
async def get_db():
    db = Database()
    try:
        yield db
    finally:
        db.close()

@app.get("/items")
async def list_items(db = Depends(get_db)):
    return db.get_all()
```

### Async vs Sync

```python
# Use async for I/O-bound operations
@app.get("/async")
async def async_endpoint():
    result = await fetch_from_api()
    return result

# Use sync for CPU-bound or blocking operations
@app.get("/sync")
def sync_endpoint():
    result = compute_something()
    return result
```

---

## Quick Commands

```bash
# Virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Package management
pip install package_name
pip install -r requirements.txt
pip freeze > requirements.txt

# Run FastAPI
uvicorn main:app --reload

# Type checking
pip install mypy
mypy your_file.py
```

---

Happy coding! 🐍

