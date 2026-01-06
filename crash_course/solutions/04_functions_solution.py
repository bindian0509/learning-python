"""
=============================================================================
SOLUTIONS - Module 04: Functions
=============================================================================
"""

print("=" * 50)
print("SOLUTIONS - Module 04: Functions")
print("=" * 50)

# Exercise 1: Format Name
print("\n--- Exercise 1: Format Name ---")

def format_name(first: str, last: str, middle: str = "") -> str:
    """Format a full name, optionally including middle name."""
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"

print(f"format_name('John', 'Doe'): {format_name('John', 'Doe')}")
print(f"format_name('John', 'Doe', 'William'): {format_name('John', 'Doe', 'William')}")


# Exercise 2: Average Function
print("\n--- Exercise 2: Average Function ---")

def average(*args: float) -> float:
    """Return the average of all numbers, or 0 if no arguments."""
    if not args:
        return 0
    return sum(args) / len(args)

print(f"average(): {average()}")
print(f"average(10): {average(10)}")
print(f"average(1, 2, 3, 4, 5): {average(1, 2, 3, 4, 5)}")
print(f"average(10, 20): {average(10, 20)}")


# Exercise 3: Build URL
print("\n--- Exercise 3: Build URL ---")

def build_url(base: str, **params) -> str:
    """Build a URL with query parameters."""
    if not params:
        return base
    query_string = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{base}?{query_string}"

print(f"build_url('https://api.example.com'): {build_url('https://api.example.com')}")
print(f"build_url('https://api.example.com', page=1, limit=10): {build_url('https://api.example.com', page=1, limit=10)}")
print(f"build_url('https://api.example.com', q='python', sort='date'): {build_url('https://api.example.com', q='python', sort='date')}")


# Exercise 4: Validation Decorator
print("\n--- Exercise 4: Validation Decorator ---")

from functools import wraps

def validate_positive(func):
    """Decorator that validates all numeric arguments are positive."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i, arg in enumerate(args):
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument {i} must be positive, got {arg}")
        for key, value in kwargs.items():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"Argument '{key}' must be positive, got {value}")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(width, height):
    return width * height

print(f"calculate_area(5, 3): {calculate_area(5, 3)}")
try:
    print(f"calculate_area(-5, 3): {calculate_area(-5, 3)}")
except ValueError as e:
    print(f"calculate_area(-5, 3): Error - {e}")


# Exercise 5: Logger Factory
print("\n--- Exercise 5: Logger Factory ---")

def create_logger(prefix: str):
    """Create a logging function with a specific prefix."""
    def logger(message: str) -> None:
        print(f"{prefix} {message}")
    return logger

info_logger = create_logger("[INFO]")
error_logger = create_logger("[ERROR]")
debug_logger = create_logger("[DEBUG]")

info_logger("System started")
error_logger("Connection failed")
debug_logger("Variable x = 42")


# Exercise 6: Apply All
print("\n--- Exercise 6: Apply All ---")

def apply_all(value, *functions):
    """Apply all functions to value in sequence."""
    result = value
    for func in functions:
        result = func(result)
    return result

result = apply_all(5, lambda x: x * 2, lambda x: x + 3)
print(f"apply_all(5, x*2, x+3): {result}")  # (5*2)+3 = 13

result = apply_all("hello", str.upper, lambda s: s + "!")
print(f"apply_all('hello', upper, add '!'): {result}")  # HELLO!

result = apply_all(10, lambda x: x + 1, lambda x: x * 2, lambda x: x - 5)
print(f"apply_all(10, +1, *2, -5): {result}")  # ((10+1)*2)-5 = 17

