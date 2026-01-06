"""
=============================================================================
PYTHON 3 CRASH COURSE - Module 08: Type Hints
=============================================================================
Topics: Type annotations, Optional, Union, generics, Pydantic

Run this file: python3 08_type_hints.py
=============================================================================
"""

from typing import (
    List, Dict, Set, Tuple, Optional, Union, Any,
    Callable, TypeVar, Generic, Literal
)

# =============================================================================
# 1. BASIC TYPE HINTS
# =============================================================================

print("=== BASIC TYPE HINTS ===")

# Variable annotations
name: str = "Alice"
age: int = 30
price: float = 19.99
is_active: bool = True

print(f"name: {name} (type hint: str)")
print(f"age: {age} (type hint: int)")
print(f"price: {price} (type hint: float)")

# Function parameters and return types
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def is_even(n: int) -> bool:
    return n % 2 == 0

print(f"\ngreet('World'): {greet('World')}")
print(f"add(3, 5): {add(3, 5)}")
print(f"is_even(4): {is_even(4)}")

# Type hints are NOT enforced at runtime!
# This will run without error:
result = add("3", "5")  # Returns "35" (string concatenation)
print(f"add('3', '5'): {result} (no runtime error!)")


# =============================================================================
# 2. COLLECTION TYPES
# =============================================================================

print("\n" + "=" * 50)
print("=== COLLECTION TYPES ===")

# Python 3.9+: Use built-in types directly
numbers: list[int] = [1, 2, 3, 4, 5]
user_ages: dict[str, int] = {"Alice": 30, "Bob": 25}
unique_ids: set[int] = {1, 2, 3}
point: tuple[float, float] = (3.0, 4.0)

# Python 3.8 and earlier: Use typing module
from typing import List, Dict, Set, Tuple

numbers_old: List[int] = [1, 2, 3]
user_ages_old: Dict[str, int] = {"Alice": 30}

print(f"numbers: {numbers}")
print(f"user_ages: {user_ages}")
print(f"unique_ids: {unique_ids}")
print(f"point: {point}")

# Nested types
matrix: list[list[int]] = [[1, 2], [3, 4], [5, 6]]
user_data: dict[str, list[str]] = {
    "Alice": ["alice@example.com", "alice2@example.com"],
    "Bob": ["bob@example.com"]
}

print(f"\nmatrix: {matrix}")
print(f"user_data: {user_data}")

# Fixed-length tuple vs variable-length
coordinate: tuple[float, float] = (1.0, 2.0)  # Exactly 2 floats
# Variable length tuple
values: tuple[int, ...] = (1, 2, 3, 4, 5)  # Any number of ints

print(f"coordinate: {coordinate}")
print(f"values (variable length): {values}")


# =============================================================================
# 3. OPTIONAL AND UNION
# =============================================================================

print("\n" + "=" * 50)
print("=== OPTIONAL AND UNION ===")

# Optional[X] is shorthand for Union[X, None]
def find_user(user_id: int) -> Optional[str]:
    """Return username or None if not found."""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

print(f"find_user(1): {find_user(1)}")
print(f"find_user(99): {find_user(99)}")

# Union - multiple possible types
def process_id(id_value: Union[int, str]) -> str:
    """Accept either int or string ID."""
    return f"Processing ID: {id_value}"

print(f"\nprocess_id(123): {process_id(123)}")
print(f"process_id('ABC'): {process_id('ABC')}")

# Python 3.10+: Use | for Union
def process_id_new(id_value: int | str) -> str:
    return f"Processing ID: {id_value}"

# Optional with default None
def greet_optional(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, stranger!"
    return f"Hello, {name}!"

print(f"\ngreet_optional(): {greet_optional()}")
print(f"greet_optional('Alice'): {greet_optional('Alice')}")


# =============================================================================
# 4. ANY AND CALLABLE
# =============================================================================

print("\n" + "=" * 50)
print("=== ANY AND CALLABLE ===")

# Any - opt out of type checking
def process_anything(data: Any) -> Any:
    """Accept any type, return any type."""
    return data

print(f"process_anything(42): {process_anything(42)}")
print(f"process_anything('hello'): {process_anything('hello')}")

# Callable - function types
# Callable[[arg_types], return_type]

def apply_operation(
    x: int,
    y: int,
    operation: Callable[[int, int], int]
) -> int:
    """Apply a function to two integers."""
    return operation(x, y)

def multiply(a: int, b: int) -> int:
    return a * b

result = apply_operation(5, 3, multiply)
print(f"\napply_operation(5, 3, multiply): {result}")

# Callable with no arguments
def run_task(task: Callable[[], None]) -> None:
    """Run a function that takes no args and returns nothing."""
    task()

def say_hello() -> None:
    print("  Hello from task!")

print("\nrun_task(say_hello):")
run_task(say_hello)


# =============================================================================
# 5. TYPE ALIASES
# =============================================================================

print("\n" + "=" * 50)
print("=== TYPE ALIASES ===")

# Simple type alias
UserId = int
Username = str

def get_username(user_id: UserId) -> Username:
    return f"user_{user_id}"

print(f"get_username(42): {get_username(42)}")

# Complex type aliases
JsonDict = dict[str, Any]
Matrix = list[list[float]]
Handler = Callable[[str], None]

def process_json(data: JsonDict) -> None:
    print(f"  Processing: {data}")

print("\nprocess_json with JsonDict alias:")
process_json({"name": "Alice", "age": 30})

# Python 3.10+: TypeAlias for explicit declaration
from typing import TypeAlias

Vector: TypeAlias = list[float]

def normalize(v: Vector) -> Vector:
    magnitude = sum(x**2 for x in v) ** 0.5
    return [x / magnitude for x in v] if magnitude else v

print(f"\nnormalize([3, 4]): {normalize([3.0, 4.0])}")


# =============================================================================
# 6. LITERAL AND FINAL
# =============================================================================

print("\n" + "=" * 50)
print("=== LITERAL AND FINAL ===")

# Literal - specific allowed values
def set_mode(mode: Literal["read", "write", "append"]) -> str:
    return f"Mode set to: {mode}"

print(f"set_mode('read'): {set_mode('read')}")
print(f"set_mode('write'): {set_mode('write')}")
# set_mode('delete')  # Type checker would flag this

# Final - constant that shouldn't be reassigned
from typing import Final

MAX_CONNECTIONS: Final = 100
API_VERSION: Final[str] = "v2"

print(f"\nMAX_CONNECTIONS: {MAX_CONNECTIONS}")
print(f"API_VERSION: {API_VERSION}")


# =============================================================================
# 7. GENERICS
# =============================================================================

print("\n" + "=" * 50)
print("=== GENERICS ===")

# TypeVar - generic type variable
T = TypeVar('T')

def first(items: list[T]) -> T:
    """Return first item of any list type."""
    return items[0]

print(f"first([1, 2, 3]): {first([1, 2, 3])}")
print(f"first(['a', 'b', 'c']): {first(['a', 'b', 'c'])}")

# Bounded TypeVar
from typing import Sequence

T_num = TypeVar('T_num', int, float)

def add_numbers(a: T_num, b: T_num) -> T_num:
    return a + b

print(f"\nadd_numbers(1, 2): {add_numbers(1, 2)}")
print(f"add_numbers(1.5, 2.5): {add_numbers(1.5, 2.5)}")

# Generic class
class Stack(Generic[T]):
    """Generic stack implementation."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def __repr__(self) -> str:
        return f"Stack({self._items})"

# Using generic class
int_stack: Stack[int] = Stack()
int_stack.push(1)
int_stack.push(2)
int_stack.push(3)
print(f"\nint_stack: {int_stack}")
print(f"int_stack.pop(): {int_stack.pop()}")

str_stack: Stack[str] = Stack()
str_stack.push("a")
str_stack.push("b")
print(f"str_stack: {str_stack}")


# =============================================================================
# 8. TYPED DICT (Python 3.8+)
# =============================================================================

print("\n" + "=" * 50)
print("=== TYPED DICT ===")

from typing import TypedDict

# Define structure of dictionary
class User(TypedDict):
    name: str
    email: str
    age: int

class UserOptional(TypedDict, total=False):
    name: str
    email: str
    age: int  # All fields optional with total=False

# Mix required and optional
class UserMixed(TypedDict):
    name: str  # Required
    email: str  # Required

class UserMixedExtended(UserMixed, total=False):
    age: int  # Optional
    phone: str  # Optional

def create_user(user: User) -> str:
    return f"Created user: {user['name']} ({user['email']})"

user_data: User = {"name": "Alice", "email": "alice@example.com", "age": 30}
print(f"create_user result: {create_user(user_data)}")


# =============================================================================
# 9. PROTOCOLS (STRUCTURAL SUBTYPING)
# =============================================================================

print("\n" + "=" * 50)
print("=== PROTOCOLS ===")

from typing import Protocol

# Define a protocol (interface)
class Drawable(Protocol):
    def draw(self) -> str:
        ...

# Any class with draw() method satisfies the protocol
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self) -> str:
        return f"Drawing circle with radius {self.radius}"

class Square:
    def __init__(self, side: float):
        self.side = side

    def draw(self) -> str:
        return f"Drawing square with side {self.side}"

def render(shape: Drawable) -> None:
    """Works with any object that has draw() method."""
    print(f"  {shape.draw()}")

print("Using Protocol:")
render(Circle(5))
render(Square(4))


# =============================================================================
# 10. PYDANTIC - RUNTIME VALIDATION (FastAPI uses this!)
# =============================================================================

print("\n" + "=" * 50)
print("=== PYDANTIC PREVIEW ===")

print("""
Pydantic provides runtime data validation using type hints.
FastAPI uses Pydantic extensively!

# Install: pip install pydantic

from pydantic import BaseModel, Field, validator
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    age: int = Field(ge=0, le=150)
    is_active: bool = True

# Automatic validation
user = User(name="Alice", email="alice@example.com", age=30)
print(user.model_dump())  # Convert to dict

# Validation error example
try:
    bad_user = User(name="Bob", email="bob@example.com", age=-5)
except ValidationError as e:
    print(e)

# From JSON
user_json = '{"name": "Charlie", "email": "c@example.com", "age": 25}'
user = User.model_validate_json(user_json)

See Module 10 (FastAPI) for more Pydantic examples!
""")


# =============================================================================
# 11. TYPE CHECKING TOOLS
# =============================================================================

print("\n" + "=" * 50)
print("=== TYPE CHECKING TOOLS ===")

print("""
Type hints are NOT checked at runtime!
Use these tools to check types:

1. mypy - Most popular type checker
   pip install mypy
   mypy your_file.py

2. pyright - Microsoft's type checker (faster)
   pip install pyright
   pyright your_file.py

3. IDE Integration
   - VS Code: Pylance extension
   - PyCharm: Built-in type checking

Common mypy flags:
   mypy --strict your_file.py  # Strict mode
   mypy --ignore-missing-imports your_file.py

# mypy.ini configuration example:
[mypy]
python_version = 3.10
warn_return_any = True
warn_unused_ignores = True
disallow_untyped_defs = True
""")


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# TODO Exercise 1: Add Type Hints
# Add proper type hints to these functions:
print("\n--- Exercise 1: Add Type Hints ---")

def get_items(data, key):
    """Extract items from dict, return empty list if key missing."""
    return data.get(key, [])

def merge_dicts(dict1, dict2):
    """Merge two dictionaries."""
    return {**dict1, **dict2}

def filter_by_length(words, min_length):
    """Filter words longer than min_length."""
    return [w for w in words if len(w) >= min_length]

# Your type-hinted versions here:


# TODO Exercise 2: Generic Function
# Create a generic function `second(items)` that returns
# the second item of any sequence (list, tuple, string)
print("\n--- Exercise 2: Generic Function ---")
# Your code here:


# TODO Exercise 3: TypedDict
# Create a TypedDict for an API response:
# - status: str (required)
# - data: dict (required)
# - error: str (optional)
# - count: int (optional)
print("\n--- Exercise 3: TypedDict ---")
# Your code here:


# TODO Exercise 4: Callable Type Hint
# Create a function `transform_all(items, transformer)` that:
# - Takes a list of strings
# - Takes a function that transforms string -> string
# - Returns transformed list
# Add proper type hints
print("\n--- Exercise 4: Callable Type Hint ---")
# Your code here:


# TODO Exercise 5: Protocol
# Create a protocol `Serializable` with method `to_dict() -> dict`
# Create two classes that implement this protocol
# Create a function that accepts any Serializable
print("\n--- Exercise 5: Protocol ---")
# Your code here:


print("\n" + "=" * 50)
print("Run the solution file to check your answers!")
print("=" * 50)

