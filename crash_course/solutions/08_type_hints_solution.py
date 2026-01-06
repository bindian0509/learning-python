"""
=============================================================================
SOLUTIONS - Module 08: Type Hints
=============================================================================
"""

from typing import (
    List, Dict, Any, Optional, Callable, TypeVar,
    TypedDict, Protocol, Sequence
)

print("=" * 50)
print("SOLUTIONS - Module 08: Type Hints")
print("=" * 50)

# Exercise 1: Add Type Hints
print("\n--- Exercise 1: Add Type Hints ---")

def get_items(data: dict[str, list[Any]], key: str) -> list[Any]:
    """Extract items from dict, return empty list if key missing."""
    return data.get(key, [])

def merge_dicts(dict1: dict[str, Any], dict2: dict[str, Any]) -> dict[str, Any]:
    """Merge two dictionaries."""
    return {**dict1, **dict2}

def filter_by_length(words: list[str], min_length: int) -> list[str]:
    """Filter words longer than min_length."""
    return [w for w in words if len(w) >= min_length]

# Test
data = {"fruits": ["apple", "banana"], "colors": ["red", "blue"]}
print(f"get_items(data, 'fruits'): {get_items(data, 'fruits')}")
print(f"get_items(data, 'missing'): {get_items(data, 'missing')}")

d1, d2 = {"a": 1}, {"b": 2}
print(f"merge_dicts({d1}, {d2}): {merge_dicts(d1, d2)}")

words = ["hi", "hello", "hey", "greetings"]
print(f"filter_by_length({words}, 4): {filter_by_length(words, 4)}")


# Exercise 2: Generic Function
print("\n--- Exercise 2: Generic Function ---")

T = TypeVar('T')

def second(items: Sequence[T]) -> T:
    """Return the second item of any sequence."""
    if len(items) < 2:
        raise IndexError("Sequence must have at least 2 items")
    return items[1]

print(f"second([1, 2, 3]): {second([1, 2, 3])}")
print(f"second(('a', 'b', 'c')): {second(('a', 'b', 'c'))}")
print(f"second('hello'): {second('hello')}")


# Exercise 3: TypedDict
print("\n--- Exercise 3: TypedDict ---")

class APIResponseRequired(TypedDict):
    status: str
    data: dict

class APIResponse(APIResponseRequired, total=False):
    error: str
    count: int

def handle_response(response: APIResponse) -> None:
    print(f"  Status: {response['status']}")
    if 'error' in response:
        print(f"  Error: {response['error']}")
    if 'count' in response:
        print(f"  Count: {response['count']}")

# Test
success_response: APIResponse = {
    "status": "success",
    "data": {"users": ["Alice", "Bob"]},
    "count": 2
}

error_response: APIResponse = {
    "status": "error",
    "data": {},
    "error": "Not found"
}

print("Success response:")
handle_response(success_response)
print("\nError response:")
handle_response(error_response)


# Exercise 4: Callable Type Hint
print("\n--- Exercise 4: Callable Type Hint ---")

def transform_all(
    items: list[str],
    transformer: Callable[[str], str]
) -> list[str]:
    """Transform all strings using the provided function."""
    return [transformer(item) for item in items]

words = ["hello", "world", "python"]
print(f"Original: {words}")
print(f"Upper: {transform_all(words, str.upper)}")
print(f"Title: {transform_all(words, str.title)}")
print(f"Reverse: {transform_all(words, lambda s: s[::-1])}")


# Exercise 5: Protocol
print("\n--- Exercise 5: Protocol ---")

class Serializable(Protocol):
    """Protocol for objects that can be serialized to dict."""

    def to_dict(self) -> dict:
        ...

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def to_dict(self) -> dict:
        return {"name": self.name, "email": self.email}

class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def to_dict(self) -> dict:
        return {"name": self.name, "price": self.price}

def serialize(obj: Serializable) -> dict:
    """Serialize any object that implements to_dict()."""
    return obj.to_dict()

# Both User and Product satisfy Serializable protocol
user = User("Alice", "alice@example.com")
product = Product("Laptop", 999.99)

print(f"Serialized user: {serialize(user)}")
print(f"Serialized product: {serialize(product)}")

