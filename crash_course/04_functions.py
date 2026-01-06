"""
=============================================================================
PYTHON 3 CRASH COURSE - Module 04: Functions
=============================================================================
Topics: Functions, *args/**kwargs, lambda, decorators, closures

Run this file: python3 04_functions.py
=============================================================================
"""

# =============================================================================
# 1. BASIC FUNCTIONS
# =============================================================================

print("=== BASIC FUNCTIONS ===")

# Simple function
def greet():
    """A simple greeting function."""
    print("Hello, World!")

greet()

# Function with parameters
def greet_person(name):
    """Greet a specific person."""
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with return value
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add(3, 5)
print(f"3 + 5 = {result}")

# Multiple return values (returns a tuple)
def get_min_max(numbers):
    """Return both min and max of a list."""
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9])
print(f"Min: {minimum}, Max: {maximum}")

# Early return
def is_even(n):
    """Check if a number is even."""
    if n % 2 == 0:
        return True
    return False

# Simpler version
def is_even_v2(n):
    return n % 2 == 0

print(f"is_even(4): {is_even(4)}")
print(f"is_even(7): {is_even(7)}")


# =============================================================================
# 2. FUNCTION PARAMETERS
# =============================================================================

print("\n" + "=" * 50)
print("=== FUNCTION PARAMETERS ===")

# Positional arguments
def power(base, exponent):
    return base ** exponent

print(f"power(2, 3) = {power(2, 3)}")

# Keyword arguments (order doesn't matter)
print(f"power(exponent=3, base=2) = {power(exponent=3, base=2)}")

# Default parameters
def greet_with_default(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet_with_default("Alice"))  # Uses default
print(greet_with_default("Bob", "Hi"))  # Override default

# IMPORTANT: Default mutable arguments - GOTCHA!
# DON'T do this:
def bad_append(item, lst=[]):  # Same list is reused!
    lst.append(item)
    return lst

# print(bad_append(1))  # [1]
# print(bad_append(2))  # [1, 2] - Unexpected!

# DO this instead:
def good_append(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(f"good_append(1): {good_append(1)}")
print(f"good_append(2): {good_append(2)}")

# Keyword-only arguments (after *)
def create_user(name, *, email, is_admin=False):
    """email must be passed as keyword argument."""
    return {"name": name, "email": email, "is_admin": is_admin}

# create_user("Alice", "alice@example.com")  # TypeError!
user = create_user("Alice", email="alice@example.com")
print(f"User: {user}")

# Positional-only arguments (Python 3.8+, before /)
def calculate(x, y, /, operation="add"):
    """x and y must be positional arguments."""
    if operation == "add":
        return x + y
    return x - y

print(f"calculate(5, 3): {calculate(5, 3)}")
# calculate(x=5, y=3)  # TypeError!


# =============================================================================
# 3. *ARGS AND **KWARGS
# =============================================================================

print("\n" + "=" * 50)
print("=== *ARGS AND **KWARGS ===")

# *args - variable number of positional arguments (tuple)
def sum_all(*args):
    """Sum any number of arguments."""
    print(f"  args type: {type(args)}, value: {args}")
    return sum(args)

print(f"sum_all(1, 2, 3): {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5): {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - variable number of keyword arguments (dict)
def print_info(**kwargs):
    """Print any keyword arguments."""
    print(f"  kwargs type: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("\nprint_info(name='Alice', age=30):")
print_info(name="Alice", age=30, city="NYC")

# Combining *args and **kwargs
def flexible_function(required, *args, **kwargs):
    """Accept required, variable positional, and variable keyword args."""
    print(f"  required: {required}")
    print(f"  args: {args}")
    print(f"  kwargs: {kwargs}")

print("\nflexible_function(1, 2, 3, x=10, y=20):")
flexible_function(1, 2, 3, x=10, y=20)

# Unpacking arguments
def multiply(a, b, c):
    return a * b * c

numbers = [2, 3, 4]
print(f"\nmultiply(*[2, 3, 4]): {multiply(*numbers)}")

params = {"a": 2, "b": 3, "c": 4}
print(f"multiply(**{{'a': 2, 'b': 3, 'c': 4}}): {multiply(**params)}")


# =============================================================================
# 4. LAMBDA FUNCTIONS
# =============================================================================

print("\n" + "=" * 50)
print("=== LAMBDA FUNCTIONS ===")

# Lambda = anonymous, single-expression function
# Syntax: lambda arguments: expression

# Basic lambda
square = lambda x: x ** 2
print(f"square(5): {square(5)}")

# Multiple arguments
add = lambda x, y: x + y
print(f"add(3, 4): {add(3, 4)}")

# Common use: sorting with key
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_by_age = sorted(people, key=lambda person: person[1])
print(f"\nSorted by age: {sorted_by_age}")

# With filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# With map
doubled = list(map(lambda x: x * 2, numbers))
print(f"Doubled: {doubled}")

# Lambda vs regular function - when to use each:
# Lambda: Simple, one-off operations (sorting keys, filter/map)
# Regular: Complex logic, multiple statements, reusability, documentation


# =============================================================================
# 5. HIGHER-ORDER FUNCTIONS
# =============================================================================

print("\n" + "=" * 50)
print("=== HIGHER-ORDER FUNCTIONS ===")

# Functions that take functions as arguments or return functions

# Function as argument
def apply_operation(x, y, operation):
    """Apply any operation to x and y."""
    return operation(x, y)

def multiply(a, b):
    return a * b

print(f"apply_operation(5, 3, multiply): {apply_operation(5, 3, multiply)}")
print(f"apply_operation(5, 3, lambda a, b: a - b): {apply_operation(5, 3, lambda a, b: a - b)}")

# Function returning a function (factory pattern)
def create_multiplier(factor):
    """Create a function that multiplies by factor."""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(f"\ndouble(5): {double(5)}")
print(f"triple(5): {triple(5)}")


# =============================================================================
# 6. CLOSURES
# =============================================================================

print("\n" + "=" * 50)
print("=== CLOSURES ===")

# A closure is a function that remembers values from its enclosing scope

def make_counter():
    """Create a counter function with its own state."""
    count = 0

    def counter():
        nonlocal count  # Access variable from enclosing scope
        count += 1
        return count

    return counter

counter1 = make_counter()
counter2 = make_counter()

print(f"counter1(): {counter1()}")  # 1
print(f"counter1(): {counter1()}")  # 2
print(f"counter2(): {counter2()}")  # 1 (separate state)
print(f"counter1(): {counter1()}")  # 3

# Closure with parameters
def make_greeting(greeting):
    """Create a greeter function with a specific greeting."""
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

say_hello = make_greeting("Hello")
say_hi = make_greeting("Hi")

print(f"\nsay_hello('Alice'): {say_hello('Alice')}")
print(f"say_hi('Bob'): {say_hi('Bob')}")


# =============================================================================
# 7. DECORATORS
# =============================================================================

print("\n" + "=" * 50)
print("=== DECORATORS ===")

# Decorators wrap functions to add behavior
# VERY important for FastAPI!

# Basic decorator
def my_decorator(func):
    """A simple decorator that prints before/after."""
    def wrapper(*args, **kwargs):
        print("  Before function call")
        result = func(*args, **kwargs)
        print("  After function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"  Hello, {name}!")

print("Calling say_hello('Alice'):")
say_hello("Alice")

# Without @ syntax (equivalent)
def say_goodbye(name):
    print(f"  Goodbye, {name}!")

say_goodbye = my_decorator(say_goodbye)
print("\nCalling decorated say_goodbye('Bob'):")
say_goodbye("Bob")

# Decorator with arguments
def repeat(times):
    """Decorator that repeats function call."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(times=3)
def get_greeting(name):
    return f"Hello, {name}!"

print(f"\nget_greeting('Alice'): {get_greeting('Alice')}")

# Practical decorator: Timing
import time

def timer(func):
    """Measure execution time of a function."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"  {func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(0.1)
    return "Done"

print("\nCalling slow_function():")
slow_function()

# Practical decorator: Logging
def log_calls(func):
    """Log function calls with arguments."""
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(repr, args))
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"  Calling {func.__name__}({all_args})")
        result = func(*args, **kwargs)
        print(f"  {func.__name__} returned {result!r}")
        return result
    return wrapper

@log_calls
def add_numbers(a, b):
    return a + b

print("\nCalling add_numbers(3, 5):")
add_numbers(3, 5)

# Preserving function metadata with functools.wraps
from functools import wraps

def better_decorator(func):
    @wraps(func)  # Preserves __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@better_decorator
def my_function():
    """This is my function's docstring."""
    pass

print(f"\nFunction name: {my_function.__name__}")
print(f"Function doc: {my_function.__doc__}")

# Stacking decorators
@timer
@log_calls
def compute(x, y):
    return x * y

print("\nStacked decorators on compute(4, 5):")
compute(4, 5)


# =============================================================================
# 8. FUNCTOOLS UTILITIES
# =============================================================================

print("\n" + "=" * 50)
print("=== FUNCTOOLS UTILITIES ===")

from functools import partial, reduce, lru_cache

# partial - freeze some arguments
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"square(5): {square(5)}")
print(f"cube(5): {cube(5)}")

# reduce - reduce sequence to single value
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"\nProduct of {numbers}: {product}")

# lru_cache - memoization decorator
@lru_cache(maxsize=128)
def fibonacci(n):
    """Calculate fibonacci number (with caching)."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\nfibonacci(30): {fibonacci(30)}")
print(f"Cache info: {fibonacci.cache_info()}")


# =============================================================================
# 9. DOCSTRINGS AND TYPE HINTS (PREVIEW)
# =============================================================================

print("\n" + "=" * 50)
print("=== DOCSTRINGS AND TYPE HINTS ===")

def calculate_area(width: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.

    Returns:
        The area of the rectangle.

    Raises:
        ValueError: If width or height is negative.

    Example:
        >>> calculate_area(5, 3)
        15.0
    """
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return width * height

print(f"calculate_area(5, 3): {calculate_area(5, 3)}")
print(f"\nDocstring:\n{calculate_area.__doc__}")


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# TODO Exercise 1: Function with Default Parameters
# Create a function `format_name(first, last, middle="")` that returns
# "First Middle Last" or "First Last" if no middle name
print("\n--- Exercise 1: Format Name ---")
# Your code here:


# TODO Exercise 2: *args Function
# Create a function `average(*args)` that returns the average of all numbers
# Handle the case when no arguments are provided (return 0)
print("\n--- Exercise 2: Average Function ---")
# Your code here:


# TODO Exercise 3: **kwargs Function
# Create a function `build_url(base, **params)` that builds a URL
# Example: build_url("https://api.example.com", page=1, limit=10)
# Returns: "https://api.example.com?page=1&limit=10"
print("\n--- Exercise 3: Build URL ---")
# Your code here:


# TODO Exercise 4: Create a Decorator
# Create a decorator `validate_positive` that checks if all numeric arguments
# are positive. If not, raise ValueError.
print("\n--- Exercise 4: Validation Decorator ---")
# Your code here:


# TODO Exercise 5: Closure for Configuration
# Create a function `create_logger(prefix)` that returns a logging function
# The returned function should print messages with the prefix
# Example: logger = create_logger("[INFO]"); logger("System started")
# Output: "[INFO] System started"
print("\n--- Exercise 5: Logger Factory ---")
# Your code here:


# TODO Exercise 6: Higher-Order Function
# Create a function `apply_all(value, *functions)` that applies all functions
# to the value in sequence and returns the final result
# Example: apply_all(5, lambda x: x*2, lambda x: x+3) -> 13
print("\n--- Exercise 6: Apply All ---")
# Your code here:


print("\n" + "=" * 50)
print("Run the solution file to check your answers!")
print("=" * 50)

