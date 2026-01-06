"""
=============================================================================
PYTHON 3 CRASH COURSE - Module 03: Control Flow
=============================================================================
Topics: if/elif/else, for/while loops, match-case (Python 3.10+)

Run this file: python3 03_control_flow.py
=============================================================================
"""

# =============================================================================
# 1. IF / ELIF / ELSE
# =============================================================================

print("=== IF / ELIF / ELSE ===")

# Basic if statement
age = 25
if age >= 18:
    print("You are an adult")

# if-else
temperature = 15
if temperature > 30:
    print("It's hot!")
else:
    print("It's not that hot")

# if-elif-else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# Nested if
user_role = "admin"
is_active = True

if is_active:
    if user_role == "admin":
        print("Admin dashboard access granted")
    else:
        print("User dashboard access granted")
else:
    print("Account inactive")


# =============================================================================
# 2. TRUTHY AND FALSY VALUES
# =============================================================================

print("\n" + "=" * 50)
print("=== TRUTHY AND FALSY VALUES ===")

# Falsy values in Python:
# - False
# - None
# - 0, 0.0, 0j (zero of any numeric type)
# - "", [], {}, set(), () (empty sequences/collections)

# These are all falsy:
falsy_values = [False, None, 0, 0.0, "", [], {}, set()]

for val in falsy_values:
    if not val:
        print(f"  {repr(val):10} is falsy")

# Practical usage - checking for empty/None
user_input = ""
if user_input:
    print(f"Processing: {user_input}")
else:
    print("No input provided")

# Checking for None vs empty
data = []
if data is None:
    print("Data is None")
elif not data:
    print("Data is empty but not None")
else:
    print(f"Data has {len(data)} items")


# =============================================================================
# 3. TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# =============================================================================

print("\n" + "=" * 50)
print("=== TERNARY OPERATOR ===")

# Syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: {status}")

# Nested ternary (use sparingly - can be hard to read)
score = 75
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Score {score}: Grade {grade}")

# Common pattern: default value
name = None
display_name = name if name else "Anonymous"
print(f"Display name: {display_name}")

# Even better with 'or' for simple cases
display_name = name or "Anonymous"
print(f"Using 'or': {display_name}")


# =============================================================================
# 4. FOR LOOPS
# =============================================================================

print("\n" + "=" * 50)
print("=== FOR LOOPS ===")

# Basic for loop
print("Basic iteration:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  {fruit}")

# range() - generates sequence of numbers
print("\nrange(5):")
for i in range(5):  # 0, 1, 2, 3, 4
    print(f"  {i}", end=" ")
print()

print("\nrange(2, 8):")
for i in range(2, 8):  # 2, 3, 4, 5, 6, 7
    print(f"  {i}", end=" ")
print()

print("\nrange(0, 10, 2):")  # Step by 2
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(f"  {i}", end=" ")
print()

print("\nrange(5, 0, -1):")  # Count down
for i in range(5, 0, -1):  # 5, 4, 3, 2, 1
    print(f"  {i}", end=" ")
print()

# enumerate() - get index and value
print("\nenumerate():")
for idx, fruit in enumerate(fruits):
    print(f"  {idx}: {fruit}")

# Starting from 1
print("\nenumerate(start=1):")
for idx, fruit in enumerate(fruits, start=1):
    print(f"  {idx}: {fruit}")

# zip() - iterate multiple sequences
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

print("\nzip():")
for name, age in zip(names, ages):
    print(f"  {name} is {age}")

# Iterating over dictionary
person = {"name": "Alice", "age": 30, "city": "NYC"}

print("\nDict keys:")
for key in person:
    print(f"  {key}: {person[key]}")

print("\nDict items():")
for key, value in person.items():
    print(f"  {key}: {value}")

# Iterating with index (when you need it)
print("\nWith index using enumerate:")
for i, fruit in enumerate(fruits):
    if i == len(fruits) - 1:
        print(f"  Last item: {fruit}")
    else:
        print(f"  Item {i}: {fruit}")


# =============================================================================
# 5. WHILE LOOPS
# =============================================================================

print("\n" + "=" * 50)
print("=== WHILE LOOPS ===")

# Basic while
count = 0
print("Basic while:")
while count < 5:
    print(f"  Count: {count}")
    count += 1

# While with break condition
print("\nWith break:")
count = 0
while True:
    print(f"  Count: {count}")
    count += 1
    if count >= 3:
        break

# While with continue
print("\nWith continue (skip evens):")
count = 0
while count < 6:
    count += 1
    if count % 2 == 0:
        continue  # Skip even numbers
    print(f"  Odd: {count}")

# While else (executes if loop completes without break)
print("\nWhile-else:")
count = 0
while count < 3:
    print(f"  Count: {count}")
    count += 1
else:
    print("  Loop completed normally!")


# =============================================================================
# 6. BREAK, CONTINUE, PASS
# =============================================================================

print("\n" + "=" * 50)
print("=== BREAK, CONTINUE, PASS ===")

# break - exit the loop entirely
print("break example:")
for i in range(10):
    if i == 5:
        break
    print(f"  {i}", end=" ")
print("\n  Loop stopped at 5")

# continue - skip to next iteration
print("\ncontinue example (skip multiples of 3):")
for i in range(10):
    if i % 3 == 0:
        continue
    print(f"  {i}", end=" ")
print()

# pass - do nothing (placeholder)
print("\npass example:")
for i in range(3):
    if i == 1:
        pass  # TODO: implement later
    else:
        print(f"  Processing {i}")

# pass is useful for:
# - Empty function bodies
# - Empty class bodies
# - Placeholder in if/else branches

def not_implemented_yet():
    pass  # Will implement later

class EmptyClass:
    pass


# =============================================================================
# 7. FOR-ELSE (Less Common but Useful)
# =============================================================================

print("\n" + "=" * 50)
print("=== FOR-ELSE ===")

# else block runs if loop completes WITHOUT break
# Useful for search patterns

# Example: Search for an item
print("Searching for 'date' in fruits:")
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "date":
        print(f"  Found: {fruit}")
        break
else:
    print("  Item not found!")

# Compare with flag-based approach (less Pythonic)
print("\nSearching for 'banana':")
for fruit in fruits:
    if fruit == "banana":
        print(f"  Found: {fruit}")
        break
else:
    print("  Item not found!")


# =============================================================================
# 8. MATCH-CASE (Python 3.10+)
# =============================================================================

print("\n" + "=" * 50)
print("=== MATCH-CASE (Python 3.10+) ===")

# Structural pattern matching - more powerful than switch statements

# Basic matching
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:  # Default case (wildcard)
            return "Unknown"

print(f"Status 200: {http_status(200)}")
print(f"Status 404: {http_status(404)}")
print(f"Status 999: {http_status(999)}")

# Matching with OR pattern
def get_day_type(day):
    match day.lower():
        case "saturday" | "sunday":
            return "Weekend"
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case _:
            return "Invalid day"

print(f"\nMonday: {get_day_type('Monday')}")
print(f"Saturday: {get_day_type('Saturday')}")

# Matching with guards (if conditions)
def categorize_number(n):
    match n:
        case n if n < 0:
            return "Negative"
        case 0:
            return "Zero"
        case n if n < 10:
            return "Single digit"
        case n if n < 100:
            return "Double digit"
        case _:
            return "Large number"

print(f"\n-5: {categorize_number(-5)}")
print(f"0: {categorize_number(0)}")
print(f"7: {categorize_number(7)}")
print(f"42: {categorize_number(42)}")

# Matching sequences
def analyze_point(point):
    match point:
        case (0, 0):
            return "Origin"
        case (x, 0):
            return f"On X-axis at {x}"
        case (0, y):
            return f"On Y-axis at {y}"
        case (x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Not a point"

print(f"\n(0, 0): {analyze_point((0, 0))}")
print(f"(5, 0): {analyze_point((5, 0))}")
print(f"(0, 3): {analyze_point((0, 3))}")
print(f"(2, 4): {analyze_point((2, 4))}")

# Matching dictionaries
def process_command(cmd):
    match cmd:
        case {"action": "create", "name": name}:
            return f"Creating: {name}"
        case {"action": "delete", "id": id}:
            return f"Deleting ID: {id}"
        case {"action": "list"}:
            return "Listing all items"
        case _:
            return "Unknown command"

print(f"\n{{'action': 'create', 'name': 'test'}}: {process_command({'action': 'create', 'name': 'test'})}")
print(f"{{'action': 'delete', 'id': 42}}: {process_command({'action': 'delete', 'id': 42})}")


# =============================================================================
# 9. NESTED LOOPS
# =============================================================================

print("\n" + "=" * 50)
print("=== NESTED LOOPS ===")

# Multiplication table
print("Multiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i}x{j}={i*j}", end="  ")
    print()

# Breaking out of nested loops
print("\nFinding first match in 2D grid:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5
found = False

for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        if val == target:
            print(f"  Found {target} at position ({i}, {j})")
            found = True
            break
    if found:
        break

# Alternative: Use a function with return
def find_in_matrix(matrix, target):
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == target:
                return (i, j)
    return None

result = find_in_matrix(matrix, 8)
print(f"  Found 8 at position {result}")


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# TODO Exercise 1: FizzBuzz
# Print numbers 1-20, but:
# - For multiples of 3, print "Fizz"
# - For multiples of 5, print "Buzz"
# - For multiples of both, print "FizzBuzz"
print("\n--- Exercise 1: FizzBuzz ---")
# Your code here:


# TODO Exercise 2: Find Prime Numbers
# Find all prime numbers between 2 and 30
# Hint: A prime number is only divisible by 1 and itself
print("\n--- Exercise 2: Prime Numbers ---")
# Your code here:


# TODO Exercise 3: Pattern Printing
# Print this pattern:
# *
# **
# ***
# ****
# *****
print("\n--- Exercise 3: Triangle Pattern ---")
# Your code here:


# TODO Exercise 4: Number Guessing Logic
# Given secret = 42 and guesses = [20, 50, 35, 42, 60]
# For each guess, print "Too low", "Too high", or "Correct!"
# Stop when correct guess is found
print("\n--- Exercise 4: Number Guessing ---")
secret = 42
guesses = [20, 50, 35, 42, 60]
# Your code here:


# TODO Exercise 5: Validate Password
# Check if password meets ALL criteria:
# - At least 8 characters
# - Contains at least one digit
# - Contains at least one uppercase letter
# Print which criteria failed (if any)
print("\n--- Exercise 5: Password Validation ---")
password = "Hello123"
# Your code here:


# TODO Exercise 6: Use match-case
# Create a simple calculator using match-case
# Given: operation = "add", a = 10, b = 5
# Handle: add, subtract, multiply, divide
print("\n--- Exercise 6: Calculator with Match ---")
operation = "multiply"
a, b = 10, 5
# Your code here:


print("\n" + "=" * 50)
print("Run the solution file to check your answers!")
print("=" * 50)

