"""
=============================================================================
PYTHON 3 CRASH COURSE - Module 01: Basics
=============================================================================
Topics: Variables, operators, strings, f-strings, basic I/O

Run this file: python3 01_basics.py
=============================================================================
"""

# =============================================================================
# 1. VARIABLES AND NAMING CONVENTIONS
# =============================================================================

# Python uses snake_case for variables and functions (PEP 8 style guide)
user_name = "Alice"
user_age = 30
is_active = True

# Constants are UPPERCASE (convention, not enforced)
MAX_CONNECTIONS = 100
API_VERSION = "v2"

# Python is dynamically typed - no need to declare types
x = 10          # x is an int
x = "hello"     # x is now a string (perfectly valid, but be careful!)

# Multiple assignment
a, b, c = 1, 2, 3
x = y = z = 0   # All three variables are 0

# Swap variables (Pythonic way)
a, b = b, a     # a is now 2, b is now 1

print("=== Variables Demo ===")
print(f"user_name: {user_name}, user_age: {user_age}, is_active: {is_active}")
print(f"After swap: a={a}, b={b}")


# =============================================================================
# 2. BASIC DATA TYPES
# =============================================================================

# Integer - unlimited precision in Python 3
integer_num = 42
big_number = 10_000_000  # Underscores for readability (Python 3.6+)

# Float - double precision
float_num = 3.14159
scientific = 1.5e-10  # Scientific notation

# Boolean
is_valid = True
is_empty = False

# None - represents absence of value (like null in other languages)
result = None

# String - immutable sequence of characters
name = "Python"
multiline = """This is a
multiline string"""

# Check types with type()
print("\n=== Data Types ===")
print(f"type(42) = {type(42)}")
print(f"type(3.14) = {type(3.14)}")
print(f"type(True) = {type(True)}")
print(f"type(None) = {type(None)}")
print(f"type('hello') = {type('hello')}")


# =============================================================================
# 3. ARITHMETIC OPERATORS
# =============================================================================

print("\n=== Arithmetic Operators ===")

a, b = 17, 5

print(f"a = {a}, b = {b}")
print(f"a + b  = {a + b}")    # Addition: 22
print(f"a - b  = {a - b}")    # Subtraction: 12
print(f"a * b  = {a * b}")    # Multiplication: 85
print(f"a / b  = {a / b}")    # Division (always returns float): 3.4
print(f"a // b = {a // b}")   # Floor division (integer): 3
print(f"a % b  = {a % b}")    # Modulo (remainder): 2
print(f"a ** b = {a ** b}")   # Exponentiation: 1419857

# Augmented assignment
x = 10
x += 5   # Same as x = x + 5
x *= 2   # Same as x = x * 2
print(f"After x=10, x+=5, x*=2: x = {x}")


# =============================================================================
# 4. COMPARISON OPERATORS
# =============================================================================

print("\n=== Comparison Operators ===")

x, y = 10, 20

print(f"x = {x}, y = {y}")
print(f"x == y: {x == y}")   # Equal: False
print(f"x != y: {x != y}")   # Not equal: True
print(f"x < y:  {x < y}")    # Less than: True
print(f"x > y:  {x > y}")    # Greater than: False
print(f"x <= y: {x <= y}")   # Less than or equal: True
print(f"x >= y: {x >= y}")   # Greater than or equal: False

# Chained comparisons (Pythonic!)
age = 25
print(f"\nChained comparison: 18 <= {age} <= 65 is {18 <= age <= 65}")


# =============================================================================
# 5. LOGICAL OPERATORS
# =============================================================================

print("\n=== Logical Operators ===")

a, b = True, False

print(f"a = {a}, b = {b}")
print(f"a and b: {a and b}")  # False
print(f"a or b:  {a or b}")   # True
print(f"not a:   {not a}")    # False

# Short-circuit evaluation
# 'and' returns first falsy value or last value
# 'or' returns first truthy value or last value
print(f"\n0 or 'default': {0 or 'default'}")     # 'default'
print(f"'value' or 'default': {'value' or 'default'}")  # 'value'
print(f"None and 'hello': {None and 'hello'}")  # None


# =============================================================================
# 6. IDENTITY AND MEMBERSHIP OPERATORS
# =============================================================================

print("\n=== Identity and Membership ===")

# Identity operators: is, is not
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")  # True (same value)
print(f"a is b: {a is b}")  # False (different objects)
print(f"a is c: {a is c}")  # True (same object)

# Always use 'is' for None comparison
value = None
print(f"value is None: {value is None}")  # Preferred
print(f"value == None: {value == None}")  # Works but not recommended

# Membership operators: in, not in
fruits = ["apple", "banana", "cherry"]
print(f"\n'banana' in fruits: {'banana' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# Works with strings too
print(f"'Py' in 'Python': {'Py' in 'Python'}")


# =============================================================================
# 7. STRING OPERATIONS
# =============================================================================

print("\n=== String Operations ===")

# String creation
single = 'Hello'
double = "World"
triple = '''Multi
line'''

# Concatenation
greeting = single + " " + double
print(f"Concatenation: {greeting}")

# Repetition
line = "-" * 20
print(f"Repetition: {line}")

# Indexing (0-based)
text = "Python"
print(f"\ntext = '{text}'")
print(f"text[0] = '{text[0]}'")   # 'P'
print(f"text[-1] = '{text[-1]}'") # 'n' (last character)

# Slicing [start:end:step] - end is exclusive
print(f"text[0:3] = '{text[0:3]}'")    # 'Pyt'
print(f"text[2:] = '{text[2:]}'")      # 'thon'
print(f"text[:3] = '{text[:3]}'")      # 'Pyt'
print(f"text[::2] = '{text[::2]}'")    # 'Pto' (every 2nd char)
print(f"text[::-1] = '{text[::-1]}'")  # 'nohtyP' (reversed)

# String methods (strings are immutable, methods return new strings)
text = "  Hello World  "
print(f"\nOriginal: '{text}'")
print(f"strip(): '{text.strip()}'")
print(f"lower(): '{text.lower()}'")
print(f"upper(): '{text.upper()}'")
print(f"replace(): '{text.replace('World', 'Python')}'")
print(f"split(): {text.split()}")  # ['Hello', 'World']

# Useful string methods for validation
print(f"\n'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")


# =============================================================================
# 8. STRING FORMATTING (F-STRINGS - MODERN WAY)
# =============================================================================

print("\n=== F-Strings (Python 3.6+) ===")

name = "Alice"
age = 30
salary = 75000.50

# Basic f-string
print(f"Name: {name}, Age: {age}")

# Expressions inside f-strings
print(f"Next year, {name} will be {age + 1}")

# Formatting numbers
print(f"Salary: ${salary:,.2f}")          # $75,000.50
print(f"Percentage: {0.856:.1%}")         # 85.6%
print(f"Binary: {42:b}, Hex: {42:x}")     # Binary: 101010, Hex: 2a

# Padding and alignment
print(f"Left:   |{name:<10}|")   # |Alice     |
print(f"Right:  |{name:>10}|")   # |     Alice|
print(f"Center: |{name:^10}|")   # |  Alice   |
print(f"Padded: |{42:05d}|")     # |00042|

# Debug mode (Python 3.8+) - shows variable name and value
x = 42
print(f"{x=}")  # x=42

# Multiline f-strings
message = f"""
User Report
-----------
Name: {name}
Age: {age}
Salary: ${salary:,.2f}
"""
print(message)


# =============================================================================
# 9. WALRUS OPERATOR := (Python 3.8+)
# =============================================================================

print("\n=== Walrus Operator := ===")

# Assign and use in one expression
# Traditional way:
data = "Hello World"
n = len(data)
if n > 5:
    print(f"Traditional: String has {n} characters")

# With walrus operator:
if (n := len(data)) > 5:
    print(f"Walrus: String has {n} characters")

# Useful in while loops
import random
print("\nRandom numbers until we get > 0.9:")
while (num := random.random()) <= 0.9:
    print(f"  Got {num:.3f}, trying again...")
print(f"  Success! Got {num:.3f}")


# =============================================================================
# 10. INPUT AND OUTPUT
# =============================================================================

print("\n=== Input/Output ===")

# print() with multiple arguments
print("Hello", "World", "!")  # Separated by space
print("One", "Two", "Three", sep=" | ")  # Custom separator
print("No newline", end=" -> ")
print("Same line")

# Input from user (commented out - uncomment to test interactively)
# user_input = input("Enter your name: ")
# print(f"Hello, {user_input}!")

# Note: input() always returns a string
# number = int(input("Enter a number: "))  # Convert to int


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# TODO Exercise 1: Create variables for a user profile
# Create: first_name, last_name, email, age, is_premium_user
# Print them using an f-string in a nice format
print("\n--- Exercise 1: User Profile ---")
# Your code here:


# TODO Exercise 2: Temperature converter
# Given celsius = 25, convert to Fahrenheit using: F = C * 9/5 + 32
# Print the result formatted to 1 decimal place
print("\n--- Exercise 2: Temperature Converter ---")
celsius = 25
# Your code here:


# TODO Exercise 3: String manipulation
# Given the string "  PyTHon ProGRAMming  "
# Clean it up: remove whitespace, convert to title case
# Print the result
print("\n--- Exercise 3: String Manipulation ---")
messy_string = "  PyTHon ProGRAMming  "
# Your code here:


# TODO Exercise 4: Calculate discount
# Given price = 99.99 and discount_percent = 15
# Calculate the final price after discount
# Print: "Original: $99.99, Discount: 15%, Final: $84.99"
print("\n--- Exercise 4: Calculate Discount ---")
price = 99.99
discount_percent = 15
# Your code here:


# TODO Exercise 5: Check if a number is in range
# Given a number, check if it's between 1 and 100 (inclusive)
# Use chained comparison
print("\n--- Exercise 5: Range Check ---")
number = 42
# Your code here:


print("\n" + "=" * 50)
print("Run the solution file to check your answers!")
print("=" * 50)

