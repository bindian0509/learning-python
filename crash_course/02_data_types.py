"""
=============================================================================
PYTHON 3 CRASH COURSE - Module 02: Data Types & Collections
=============================================================================
Topics: Lists, dictionaries, sets, tuples, comprehensions

Run this file: python3 02_data_types.py
=============================================================================
"""

# =============================================================================
# 1. LISTS - Ordered, Mutable, Allow Duplicates
# =============================================================================

print("=== LISTS ===")

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]  # Can mix types (but usually don't)
nested = [[1, 2], [3, 4], [5, 6]]       # List of lists

# list() constructor
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']
range_list = list(range(5))  # [0, 1, 2, 3, 4]

print(f"numbers: {numbers}")
print(f"chars from string: {chars}")
print(f"range to list: {range_list}")

# Accessing elements (0-indexed)
print(f"\nnumbers[0] = {numbers[0]}")   # First: 1
print(f"numbers[-1] = {numbers[-1]}")  # Last: 5
print(f"numbers[1:4] = {numbers[1:4]}")  # Slice: [2, 3, 4]

# Modifying lists (mutable)
numbers[0] = 100
print(f"After numbers[0] = 100: {numbers}")

# List methods
fruits = ["apple", "banana"]
fruits.append("cherry")        # Add to end
fruits.insert(1, "blueberry")  # Insert at index
print(f"\nAfter append and insert: {fruits}")

fruits.remove("banana")        # Remove by value (first occurrence)
popped = fruits.pop()          # Remove and return last item
popped_idx = fruits.pop(0)     # Remove and return at index
print(f"After removals: {fruits}, popped: {popped}, popped_idx: {popped_idx}")

# Extending lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # Modifies list1 in place
print(f"Extended list: {list1}")

combined = [1, 2] + [3, 4]  # Creates new list
print(f"Concatenated: {combined}")

# Sorting
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()                    # In-place sort
print(f"Sorted: {nums}")
nums.sort(reverse=True)        # Descending
print(f"Reverse sorted: {nums}")

original = [3, 1, 4]
sorted_copy = sorted(original)  # Returns new list, original unchanged
print(f"Original: {original}, Sorted copy: {sorted_copy}")

# Useful list operations
nums = [1, 2, 3, 4, 5]
print(f"\nlen(nums) = {len(nums)}")
print(f"sum(nums) = {sum(nums)}")
print(f"min(nums) = {min(nums)}")
print(f"max(nums) = {max(nums)}")
print(f"3 in nums = {3 in nums}")
print(f"nums.index(3) = {nums.index(3)}")
print(f"nums.count(3) = {nums.count(3)}")


# =============================================================================
# 2. TUPLES - Ordered, Immutable, Allow Duplicates
# =============================================================================

print("\n" + "=" * 50)
print("=== TUPLES ===")

# Creating tuples
empty_tuple = ()
single = (42,)          # Note the comma! (42) is just an int in parentheses
point = (10, 20)
coordinates = (1.5, 2.5, 3.5)

# Parentheses are optional
another_point = 10, 20  # Also a tuple

print(f"point: {point}")
print(f"type of single (42,): {type(single)}")
print(f"type of (42): {type((42))}")  # int, not tuple!

# Accessing elements (same as lists)
print(f"point[0] = {point[0]}")
print(f"coordinates[1:] = {coordinates[1:]}")

# Tuples are IMMUTABLE
# point[0] = 5  # TypeError: 'tuple' object does not support item assignment

# Tuple unpacking
x, y = point
print(f"Unpacked: x={x}, y={y}")

# Unpacking with * (rest operator)
first, *rest = [1, 2, 3, 4, 5]
print(f"first={first}, rest={rest}")

*beginning, last = [1, 2, 3, 4, 5]
print(f"beginning={beginning}, last={last}")

# Named tuples (more readable)
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'city'])
alice = Person('Alice', 30, 'New York')
print(f"\nNamedTuple: {alice}")
print(f"alice.name = {alice.name}")
print(f"alice[0] = {alice[0]}")  # Also works by index

# Why use tuples?
# 1. Immutability - data won't accidentally change
# 2. Can be used as dictionary keys (lists cannot)
# 3. Slightly faster than lists
# 4. Signals intent: "this data shouldn't change"


# =============================================================================
# 3. DICTIONARIES - Key-Value Pairs, Mutable, Ordered (Python 3.7+)
# =============================================================================

print("\n" + "=" * 50)
print("=== DICTIONARIES ===")

# Creating dictionaries
empty_dict = {}
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# dict() constructor
from_tuples = dict([("a", 1), ("b", 2)])
from_kwargs = dict(name="Bob", age=25)

print(f"person: {person}")
print(f"from_kwargs: {from_kwargs}")

# Accessing values
print(f"\nperson['name'] = {person['name']}")
# person['country']  # KeyError if key doesn't exist!

# Safe access with .get()
print(f"person.get('country') = {person.get('country')}")  # None
print(f"person.get('country', 'USA') = {person.get('country', 'USA')}")  # Default

# Adding/Updating values
person["email"] = "alice@example.com"  # Add new key
person["age"] = 31                      # Update existing
print(f"Updated person: {person}")

# Update multiple at once
person.update({"age": 32, "phone": "555-1234"})
print(f"After update(): {person}")

# Removing items
del person["phone"]                     # Remove by key
email = person.pop("email")             # Remove and return value
print(f"After removals: {person}")

# Dictionary methods
print(f"\nKeys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Iterating over dictionaries
print("\nIterating:")
for key in person:
    print(f"  {key}: {person[key]}")

print("\nWith items():")
for key, value in person.items():
    print(f"  {key}: {value}")

# Check if key exists
print(f"\n'name' in person: {'name' in person}")
print(f"'country' in person: {'country' in person}")

# Merging dictionaries (Python 3.9+)
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged = dict1 | dict2  # dict2 values override dict1 for conflicts
print(f"\nMerged (|): {merged}")

# Update in place
dict1 |= {"d": 5}
print(f"After |=: {dict1}")

# setdefault - get value or set default if missing
data = {}
data.setdefault("counter", 0)
data["counter"] += 1
print(f"setdefault example: {data}")


# =============================================================================
# 4. SETS - Unordered, Mutable, NO Duplicates
# =============================================================================

print("\n" + "=" * 50)
print("=== SETS ===")

# Creating sets
empty_set = set()  # NOT {} - that's an empty dict!
numbers = {1, 2, 3, 4, 5}
from_list = set([1, 2, 2, 3, 3, 3])  # Duplicates removed

print(f"numbers: {numbers}")
print(f"from_list (duplicates removed): {from_list}")

# Adding/Removing
numbers.add(6)
numbers.discard(1)  # Remove if exists, no error if not
numbers.remove(2)   # Remove, raises KeyError if not found
print(f"After modifications: {numbers}")

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"\na = {a}")
print(f"b = {b}")
print(f"Union (a | b): {a | b}")              # {1, 2, 3, 4, 5, 6}
print(f"Intersection (a & b): {a & b}")       # {3, 4}
print(f"Difference (a - b): {a - b}")         # {1, 2}
print(f"Symmetric diff (a ^ b): {a ^ b}")     # {1, 2, 5, 6}

# Subset and superset
print(f"\n{{1, 2}} <= {{1, 2, 3}}: {({1, 2} <= {1, 2, 3})}")  # True (subset)
print(f"{{1, 2, 3}} >= {{1, 2}}: {({1, 2, 3} >= {1, 2})}")    # True (superset)

# Frozen set (immutable set)
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # AttributeError: frozenset has no attribute 'add'
print(f"\nfrozenset: {frozen}")

# Common use case: Remove duplicates from list while preserving order
items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique_ordered = list(dict.fromkeys(items))  # Python 3.7+ trick
print(f"Unique (preserving order): {unique_ordered}")


# =============================================================================
# 5. LIST COMPREHENSIONS
# =============================================================================

print("\n" + "=" * 50)
print("=== LIST COMPREHENSIONS ===")

# Basic syntax: [expression for item in iterable]
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(20) if x % 2 == 0]
print(f"Evens: {evens}")

# With if-else (note position!)
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(f"Labels: {labels}")

# Nested loops
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# Creating a matrix
matrix = [[i + j*3 for i in range(3)] for j in range(3)]
print(f"Created matrix: {matrix}")

# With function calls
words = ["hello", "WORLD", "Python"]
lower_words = [word.lower() for word in words]
print(f"Lowercased: {lower_words}")


# =============================================================================
# 6. DICTIONARY COMPREHENSIONS
# =============================================================================

print("\n" + "=" * 50)
print("=== DICTIONARY COMPREHENSIONS ===")

# Basic syntax: {key_expr: value_expr for item in iterable}
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
print(f"Combined: {combined}")

# With condition
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Inverting a dictionary
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(f"Inverted: {inverted}")

# Filtering a dictionary
prices = {"apple": 0.50, "banana": 0.25, "cherry": 0.75, "date": 1.00}
expensive = {k: v for k, v in prices.items() if v >= 0.50}
print(f"Expensive items: {expensive}")


# =============================================================================
# 7. SET COMPREHENSIONS
# =============================================================================

print("\n" + "=" * 50)
print("=== SET COMPREHENSIONS ===")

# Basic syntax: {expression for item in iterable}
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}
print(f"Unique squares: {unique_squares}")  # {0, 1, 4}

# Extract unique characters
text = "hello world"
unique_chars = {char for char in text if char != " "}
print(f"Unique chars: {unique_chars}")


# =============================================================================
# 8. GENERATOR EXPRESSIONS (Memory Efficient)
# =============================================================================

print("\n" + "=" * 50)
print("=== GENERATOR EXPRESSIONS ===")

# Like list comprehension but with () - doesn't create list in memory
# Useful for large datasets

# Generator expression
gen = (x**2 for x in range(1000000))
print(f"Generator: {gen}")
print(f"First value: {next(gen)}")
print(f"Second value: {next(gen)}")

# Memory comparison
import sys
list_comp = [x**2 for x in range(1000)]
gen_expr = (x**2 for x in range(1000))

print(f"\nList size: {sys.getsizeof(list_comp)} bytes")
print(f"Generator size: {sys.getsizeof(gen_expr)} bytes")

# Using with functions that accept iterables
total = sum(x**2 for x in range(100))  # No extra [] needed!
print(f"Sum of squares: {total}")


# =============================================================================
# 9. USEFUL BUILT-IN FUNCTIONS FOR COLLECTIONS
# =============================================================================

print("\n" + "=" * 50)
print("=== USEFUL BUILT-INS ===")

# zip - combine iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age}, {city}")

# enumerate - get index and value
print("\nenumerate:")
for i, name in enumerate(names):
    print(f"  {i}: {name}")

# Starting from different index
for i, name in enumerate(names, start=1):
    print(f"  {i}: {name}")

# any / all
numbers = [2, 4, 6, 8]
print(f"\nall even: {all(n % 2 == 0 for n in numbers)}")  # True
print(f"any > 5: {any(n > 5 for n in numbers)}")         # True

# filter and map
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
doubled = list(map(lambda x: x * 2, numbers))
print(f"\nfilter evens: {evens}")
print(f"map doubled: {doubled}")

# sorted with key
words = ["banana", "Apple", "cherry"]
print(f"\nSorted (case-insensitive): {sorted(words, key=str.lower)}")

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
print(f"Sorted by age: {sorted(people, key=lambda p: p[1])}")

# reversed
nums = [1, 2, 3, 4, 5]
print(f"Reversed: {list(reversed(nums))}")


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# TODO Exercise 1: List Operations
# Given a list of numbers, create a new list with only positive numbers, squared
print("\n--- Exercise 1: Filter and Transform ---")
numbers = [-3, -1, 0, 2, 4, -5, 6]
# Create: positive_squares (should be [4, 16, 36])
# Your code here:


# TODO Exercise 2: Word Count
# Count the frequency of each word in the sentence
print("\n--- Exercise 2: Word Count ---")
sentence = "the quick brown fox jumps over the lazy dog the fox"
# Create: word_count dict (should be {'the': 3, 'quick': 1, ...})
# Hint: Use dict comprehension or a loop
# Your code here:


# TODO Exercise 3: Dictionary Manipulation
# Given student grades, find students who passed (grade >= 60)
print("\n--- Exercise 3: Passing Students ---")
grades = {
    "Alice": 85,
    "Bob": 55,
    "Charlie": 72,
    "Diana": 48,
    "Eve": 91
}
# Create: passing dict with only passing students
# Your code here:


# TODO Exercise 4: Set Operations
# Find common and unique elements
print("\n--- Exercise 4: Set Operations ---")
team_a = {"Alice", "Bob", "Charlie", "Diana"}
team_b = {"Charlie", "Diana", "Eve", "Frank"}
# Find: common members (both teams), only_a (only in team_a), only_b (only in team_b)
# Your code here:


# TODO Exercise 5: Nested Data
# Extract all email addresses from users
print("\n--- Exercise 5: Extract Emails ---")
users = [
    {"name": "Alice", "email": "alice@example.com", "active": True},
    {"name": "Bob", "email": "bob@example.com", "active": False},
    {"name": "Charlie", "email": "charlie@example.com", "active": True}
]
# Create: active_emails (list of emails for active users only)
# Your code here:


# TODO Exercise 6: Tuple Unpacking
# Given a list of (x, y) coordinates, calculate distances from origin
print("\n--- Exercise 6: Calculate Distances ---")
points = [(3, 4), (5, 12), (8, 15)]
# Create: distances list with distance from origin for each point
# Hint: distance = sqrt(x² + y²), use x**0.5 for square root
# Your code here:


print("\n" + "=" * 50)
print("Run the solution file to check your answers!")
print("=" * 50)

