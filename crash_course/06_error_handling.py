"""
=============================================================================
PYTHON 3 CRASH COURSE - Module 06: Error Handling
=============================================================================
Topics: try/except/finally, custom exceptions, context managers

Run this file: python3 06_error_handling.py
=============================================================================
"""

# =============================================================================
# 1. BASIC TRY/EXCEPT
# =============================================================================

print("=== BASIC TRY/EXCEPT ===")

# Without error handling
# result = 10 / 0  # ZeroDivisionError - crashes program!

# With error handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catching the exception object
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# Multiple except blocks
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Invalid types for division")
        return None

print(f"\nsafe_divide(10, 2): {safe_divide(10, 2)}")
print(f"safe_divide(10, 0): {safe_divide(10, 0)}")
print(f"safe_divide('10', 2): {safe_divide('10', 2)}")

# Catching multiple exceptions in one block
try:
    value = int("not a number")
except (ValueError, TypeError) as e:
    print(f"Conversion error: {e}")


# =============================================================================
# 2. COMMON EXCEPTION TYPES
# =============================================================================

print("\n" + "=" * 50)
print("=== COMMON EXCEPTION TYPES ===")

exceptions_demo = [
    ("ZeroDivisionError", "1/0"),
    ("ValueError", "int('abc')"),
    ("TypeError", "'2' + 2"),
    ("IndexError", "[1,2,3][10]"),
    ("KeyError", "{'a': 1}['b']"),
    ("AttributeError", "'hello'.unknown()"),
    ("NameError", "undefined_variable"),
    ("FileNotFoundError", "open('nonexistent.txt')"),
]

for exc_name, code in exceptions_demo:
    try:
        eval(code)
    except Exception as e:
        print(f"{exc_name}: {type(e).__name__} - {e}")


# =============================================================================
# 3. TRY/EXCEPT/ELSE/FINALLY
# =============================================================================

print("\n" + "=" * 50)
print("=== TRY/EXCEPT/ELSE/FINALLY ===")

def read_file_demo(filename):
    """Demonstrate full try/except/else/finally structure."""
    print(f"\nAttempting to read: {filename}")
    try:
        # Code that might raise exception
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        # Runs if exception occurs
        print("  except: File not found!")
        content = None
    else:
        # Runs if NO exception occurs
        print(f"  else: Successfully read {len(content)} characters")
    finally:
        # ALWAYS runs (cleanup)
        print("  finally: Cleanup complete")

    return content

read_file_demo("nonexistent_file.txt")

# else is useful for code that should only run on success
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        # Only runs if division succeeded
        print(f"Division successful: {a}/{b} = {result}")
        return result
    finally:
        print("Division attempt complete")

print("\n")
divide(10, 2)
print()
divide(10, 0)


# =============================================================================
# 4. RAISING EXCEPTIONS
# =============================================================================

print("\n" + "=" * 50)
print("=== RAISING EXCEPTIONS ===")

def validate_age(age):
    """Validate age and raise exception if invalid."""
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

# Test validation
test_ages = [25, -5, 200, "thirty"]
for age in test_ages:
    try:
        validate_age(age)
        print(f"Age {age}: Valid")
    except (TypeError, ValueError) as e:
        print(f"Age {age}: Invalid - {e}")

# Re-raising exceptions
def process_data(data):
    try:
        result = int(data)
        return result * 2
    except ValueError:
        print("Logging: Invalid data received")
        raise  # Re-raise the same exception

try:
    process_data("invalid")
except ValueError as e:
    print(f"Caught re-raised exception: {e}")


# =============================================================================
# 5. CUSTOM EXCEPTIONS
# =============================================================================

print("\n" + "=" * 50)
print("=== CUSTOM EXCEPTIONS ===")

# Basic custom exception
class ValidationError(Exception):
    """Base exception for validation errors."""
    pass

class InvalidEmailError(ValidationError):
    """Raised when email format is invalid."""
    pass

class InvalidPasswordError(ValidationError):
    """Raised when password doesn't meet requirements."""

    def __init__(self, message, requirements=None):
        super().__init__(message)
        self.requirements = requirements or []

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError(f"Email must contain @: {email}")
    if "." not in email.split("@")[1]:
        raise InvalidEmailError(f"Invalid domain in email: {email}")
    return True

def validate_password(password):
    issues = []
    if len(password) < 8:
        issues.append("at least 8 characters")
    if not any(c.isupper() for c in password):
        issues.append("at least one uppercase letter")
    if not any(c.isdigit() for c in password):
        issues.append("at least one digit")

    if issues:
        raise InvalidPasswordError(
            "Password doesn't meet requirements",
            requirements=issues
        )
    return True

# Testing custom exceptions
test_data = [
    ("email", "invalid-email", validate_email),
    ("email", "valid@example.com", validate_email),
    ("password", "weak", validate_password),
    ("password", "StrongPass123", validate_password),
]

for field, value, validator in test_data:
    try:
        validator(value)
        print(f"{field} '{value}': Valid")
    except InvalidEmailError as e:
        print(f"{field} '{value}': {e}")
    except InvalidPasswordError as e:
        print(f"{field} '{value}': {e}")
        print(f"  Missing: {', '.join(e.requirements)}")


# =============================================================================
# 6. EXCEPTION CHAINING
# =============================================================================

print("\n" + "=" * 50)
print("=== EXCEPTION CHAINING ===")

class DatabaseError(Exception):
    pass

def get_user_from_db(user_id):
    # Simulate database lookup
    if user_id < 0:
        raise ValueError("Invalid user ID")
    raise KeyError(f"User {user_id} not found")

def fetch_user(user_id):
    try:
        return get_user_from_db(user_id)
    except KeyError as e:
        # Chain the exception - preserves original cause
        raise DatabaseError(f"Failed to fetch user {user_id}") from e

try:
    fetch_user(42)
except DatabaseError as e:
    print(f"DatabaseError: {e}")
    print(f"Original cause: {e.__cause__}")


# =============================================================================
# 7. CONTEXT MANAGERS (with statement)
# =============================================================================

print("\n" + "=" * 50)
print("=== CONTEXT MANAGERS ===")

# File handling with context manager (automatic cleanup)
print("File handling with 'with':")

# Create a test file
with open("test_file.txt", "w") as f:
    f.write("Hello, World!")
    print("  File written successfully")
# File is automatically closed here, even if exception occurs

with open("test_file.txt", "r") as f:
    content = f.read()
    print(f"  File content: {content}")

# Multiple context managers
# with open("file1.txt") as f1, open("file2.txt") as f2:
#     pass

# Custom context manager using class
class Timer:
    """Context manager to measure execution time."""

    def __enter__(self):
        import time
        self.start = time.time()
        print("  Timer started")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        self.end = time.time()
        self.elapsed = self.end - self.start
        print(f"  Timer stopped: {self.elapsed:.4f} seconds")
        return False  # Don't suppress exceptions

print("\nCustom context manager (Timer):")
with Timer() as timer:
    import time
    time.sleep(0.1)
    print("  Doing some work...")

# Custom context manager using contextlib
from contextlib import contextmanager

@contextmanager
def managed_resource(name):
    """Context manager using decorator."""
    print(f"  Acquiring resource: {name}")
    try:
        yield name  # This is what 'as' receives
    finally:
        print(f"  Releasing resource: {name}")

print("\nContext manager with @contextmanager:")
with managed_resource("database_connection") as resource:
    print(f"  Using resource: {resource}")

# Cleanup test file
import os
os.remove("test_file.txt")


# =============================================================================
# 8. EXCEPTION HANDLING BEST PRACTICES
# =============================================================================

print("\n" + "=" * 50)
print("=== BEST PRACTICES ===")

print("""
1. Be specific with exceptions:
   BAD:  except Exception:  # Catches everything
   GOOD: except ValueError:  # Catches only what you expect

2. Don't use bare except:
   BAD:  except:  # Catches even KeyboardInterrupt!
   GOOD: except Exception:  # At minimum

3. Use else for success code:
   try:
       result = operation()
   except SomeError:
       handle_error()
   else:
       process(result)  # Only runs on success

4. Use finally for cleanup:
   try:
       resource = acquire()
       use(resource)
   finally:
       release(resource)  # Always runs

5. Prefer context managers for resources:
   with open(file) as f:  # Auto-closes
       process(f)

6. Create custom exceptions for your domain:
   class UserNotFoundError(Exception):
       pass

7. Include helpful error messages:
   raise ValueError(f"Expected positive, got {value}")

8. Log exceptions before re-raising:
   except SomeError as e:
       logger.error(f"Failed: {e}")
       raise
""")


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# TODO Exercise 1: Safe Type Conversion
# Create a function safe_convert(value, target_type) that:
# - Converts value to target_type (int, float, str)
# - Returns None if conversion fails
# - Works for: safe_convert("42", int) -> 42
#              safe_convert("hello", int) -> None
print("\n--- Exercise 1: Safe Convert ---")
# Your code here:


# TODO Exercise 2: Custom Exception Hierarchy
# Create exceptions for an API:
# - APIError (base)
# - AuthenticationError
# - RateLimitError (include retry_after attribute)
# - NotFoundError
print("\n--- Exercise 2: API Exceptions ---")
# Your code here:


# TODO Exercise 3: Retry Decorator
# Create a decorator retry(max_attempts=3) that:
# - Retries a function if it raises an exception
# - Gives up after max_attempts
# - Raises the last exception if all attempts fail
print("\n--- Exercise 3: Retry Decorator ---")
# Your code here:


# TODO Exercise 4: Context Manager
# Create a context manager temporary_file(filename) that:
# - Creates a file when entering
# - Yields the file object
# - Deletes the file when exiting (even if exception)
print("\n--- Exercise 4: Temporary File Manager ---")
# Your code here:


# TODO Exercise 5: Input Validation
# Create validate_user_input(data) that validates a dict:
# Required: name (str, non-empty), email (str, contains @)
# Optional: age (int, 0-150)
# Raise appropriate exceptions with helpful messages
print("\n--- Exercise 5: Input Validation ---")
# Your code here:


print("\n" + "=" * 50)
print("Run the solution file to check your answers!")
print("=" * 50)

