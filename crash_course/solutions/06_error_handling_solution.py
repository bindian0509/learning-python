"""
=============================================================================
SOLUTIONS - Module 06: Error Handling
=============================================================================
"""

print("=" * 50)
print("SOLUTIONS - Module 06: Error Handling")
print("=" * 50)

# Exercise 1: Safe Convert
print("\n--- Exercise 1: Safe Convert ---")

def safe_convert(value, target_type):
    """Safely convert value to target type, return None on failure."""
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return None

print(f"safe_convert('42', int): {safe_convert('42', int)}")
print(f"safe_convert('3.14', float): {safe_convert('3.14', float)}")
print(f"safe_convert('hello', int): {safe_convert('hello', int)}")
print(f"safe_convert(123, str): {safe_convert(123, str)}")
print(f"safe_convert(None, int): {safe_convert(None, int)}")


# Exercise 2: API Exceptions
print("\n--- Exercise 2: API Exceptions ---")

class APIError(Exception):
    """Base exception for API errors."""
    pass

class AuthenticationError(APIError):
    """Raised when authentication fails."""
    pass

class RateLimitError(APIError):
    """Raised when rate limit is exceeded."""

    def __init__(self, message: str, retry_after: int = 60):
        super().__init__(message)
        self.retry_after = retry_after

class NotFoundError(APIError):
    """Raised when resource is not found."""
    pass

# Demonstrate usage
def make_api_request(endpoint: str, authenticated: bool = True):
    if not authenticated:
        raise AuthenticationError("Invalid API key")
    if endpoint == "/rate-limited":
        raise RateLimitError("Too many requests", retry_after=30)
    if endpoint == "/missing":
        raise NotFoundError(f"Resource not found: {endpoint}")
    return {"status": "success"}

test_cases = [
    ("/users", True),
    ("/users", False),
    ("/rate-limited", True),
    ("/missing", True),
]

for endpoint, authenticated in test_cases:
    try:
        result = make_api_request(endpoint, authenticated)
        print(f"  {endpoint}: {result}")
    except AuthenticationError as e:
        print(f"  {endpoint}: Auth Error - {e}")
    except RateLimitError as e:
        print(f"  {endpoint}: Rate Limit - {e} (retry in {e.retry_after}s)")
    except NotFoundError as e:
        print(f"  {endpoint}: Not Found - {e}")


# Exercise 3: Retry Decorator
print("\n--- Exercise 3: Retry Decorator ---")

import time
from functools import wraps

def retry(max_attempts: int = 3):
    """Decorator that retries a function on exception."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"  Attempt {attempt}/{max_attempts} failed: {e}")
                    if attempt < max_attempts:
                        time.sleep(0.1)  # Brief delay
            raise last_exception
        return wrapper
    return decorator

# Test the retry decorator
attempt_count = 0

@retry(max_attempts=3)
def flaky_function():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ValueError(f"Failed on attempt {attempt_count}")
    return "Success!"

print("Testing flaky_function:")
try:
    result = flaky_function()
    print(f"Result: {result}")
except ValueError as e:
    print(f"All attempts failed: {e}")


# Exercise 4: Temporary File Manager
print("\n--- Exercise 4: Temporary File Manager ---")

import os
from contextlib import contextmanager

@contextmanager
def temporary_file(filename: str):
    """Context manager that creates and cleans up a temporary file."""
    try:
        # Create file
        f = open(filename, 'w')
        print(f"  Created: {filename}")
        yield f
    finally:
        # Close if still open
        if not f.closed:
            f.close()
        # Delete file
        if os.path.exists(filename):
            os.remove(filename)
            print(f"  Deleted: {filename}")

# Test the context manager
print("Testing temporary_file:")
with temporary_file("test_temp.txt") as f:
    f.write("Hello, World!")
    print(f"  Wrote to file")
print(f"  File exists after context: {os.path.exists('test_temp.txt')}")


# Exercise 5: Input Validation
print("\n--- Exercise 5: Input Validation ---")

class ValidationError(Exception):
    """Base validation error."""
    pass

class MissingFieldError(ValidationError):
    """Raised when required field is missing."""
    pass

class InvalidFieldError(ValidationError):
    """Raised when field value is invalid."""
    pass

def validate_user_input(data: dict) -> bool:
    """
    Validate user input data.

    Required: name (str, non-empty), email (str, contains @)
    Optional: age (int, 0-150)
    """
    # Check for required fields
    if "name" not in data:
        raise MissingFieldError("Field 'name' is required")
    if "email" not in data:
        raise MissingFieldError("Field 'email' is required")

    # Validate name
    if not isinstance(data["name"], str) or not data["name"].strip():
        raise InvalidFieldError("'name' must be a non-empty string")

    # Validate email
    if not isinstance(data["email"], str) or "@" not in data["email"]:
        raise InvalidFieldError("'email' must contain '@'")

    # Validate optional age
    if "age" in data:
        age = data["age"]
        if not isinstance(age, int):
            raise InvalidFieldError("'age' must be an integer")
        if not 0 <= age <= 150:
            raise InvalidFieldError("'age' must be between 0 and 150")

    return True

# Test cases
test_inputs = [
    {"name": "Alice", "email": "alice@example.com", "age": 30},
    {"name": "", "email": "test@test.com"},
    {"email": "no-name@test.com"},
    {"name": "Bob", "email": "invalid-email"},
    {"name": "Charlie", "email": "c@test.com", "age": 200},
]

for data in test_inputs:
    try:
        validate_user_input(data)
        print(f"  {data}: Valid")
    except (MissingFieldError, InvalidFieldError) as e:
        print(f"  {data}: {type(e).__name__} - {e}")

