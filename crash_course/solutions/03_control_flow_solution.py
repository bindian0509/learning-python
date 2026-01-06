"""
=============================================================================
SOLUTIONS - Module 03: Control Flow
=============================================================================
"""

print("=" * 50)
print("SOLUTIONS - Module 03: Control Flow")
print("=" * 50)

# Exercise 1: FizzBuzz
print("\n--- Exercise 1: FizzBuzz ---")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()


# Exercise 2: Prime Numbers
print("\n--- Exercise 2: Prime Numbers ---")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(2, 31) if is_prime(n)]
print(f"Primes between 2 and 30: {primes}")


# Exercise 3: Triangle Pattern
print("\n--- Exercise 3: Triangle Pattern ---")
for i in range(1, 6):
    print("*" * i)


# Exercise 4: Number Guessing
print("\n--- Exercise 4: Number Guessing ---")
secret = 42
guesses = [20, 50, 35, 42, 60]

for guess in guesses:
    if guess < secret:
        print(f"  Guess {guess}: Too low")
    elif guess > secret:
        print(f"  Guess {guess}: Too high")
    else:
        print(f"  Guess {guess}: Correct!")
        break


# Exercise 5: Password Validation
print("\n--- Exercise 5: Password Validation ---")
password = "Hello123"

def validate_password(pwd):
    issues = []

    if len(pwd) < 8:
        issues.append("at least 8 characters")

    if not any(c.isdigit() for c in pwd):
        issues.append("at least one digit")

    if not any(c.isupper() for c in pwd):
        issues.append("at least one uppercase letter")

    return issues

issues = validate_password(password)
if issues:
    print(f"Password '{password}' is invalid:")
    for issue in issues:
        print(f"  - Missing: {issue}")
else:
    print(f"Password '{password}' is valid!")

# Test with an invalid password
weak_password = "weak"
issues = validate_password(weak_password)
if issues:
    print(f"\nPassword '{weak_password}' is invalid:")
    for issue in issues:
        print(f"  - Missing: {issue}")


# Exercise 6: Calculator with Match
print("\n--- Exercise 6: Calculator with Match ---")
operation = "multiply"
a, b = 10, 5

match operation:
    case "add":
        result = a + b
    case "subtract":
        result = a - b
    case "multiply":
        result = a * b
    case "divide":
        result = a / b if b != 0 else "Cannot divide by zero"
    case _:
        result = "Unknown operation"

print(f"{a} {operation} {b} = {result}")

# Test all operations
operations = ["add", "subtract", "multiply", "divide"]
for op in operations:
    match op:
        case "add":
            result = a + b
        case "subtract":
            result = a - b
        case "multiply":
            result = a * b
        case "divide":
            result = a / b if b != 0 else "Error"
        case _:
            result = "Unknown"
    print(f"  {a} {op} {b} = {result}")

