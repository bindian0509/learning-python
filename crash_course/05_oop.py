"""
=============================================================================
PYTHON 3 CRASH COURSE - Module 05: Object-Oriented Programming
=============================================================================
Topics: Classes, inheritance, dataclasses, special methods

Run this file: python3 05_oop.py
=============================================================================
"""

# =============================================================================
# 1. BASIC CLASSES
# =============================================================================

print("=== BASIC CLASSES ===")

class Dog:
    """A simple Dog class."""

    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor / Initializer
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

    # Another instance method
    def get_info(self):
        return f"{self.name} is {self.age} years old"

# Creating instances
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"dog1.name: {dog1.name}")
print(f"dog1.bark(): {dog1.bark()}")
print(f"dog1.get_info(): {dog1.get_info()}")
print(f"Dog.species: {Dog.species}")
print(f"dog1.species: {dog1.species}")  # Can also access via instance


# =============================================================================
# 2. SPECIAL METHODS (DUNDER METHODS)
# =============================================================================

print("\n" + "=" * 50)
print("=== SPECIAL METHODS ===")

class Point:
    """A 2D point with special methods."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # String representation for users (print, str)
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # String representation for developers (repr, debugging)
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    # Equality comparison
    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    # Hash (needed if you want to use as dict key or in sets)
    def __hash__(self):
        return hash((self.x, self.y))

    # Addition
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # Length (optional - could be distance from origin)
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

    # Boolean value
    def __bool__(self):
        return self.x != 0 or self.y != 0

    # Make it callable
    def __call__(self, scale=1):
        return Point(self.x * scale, self.y * scale)

p1 = Point(3, 4)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(f"str(p1): {str(p1)}")
print(f"repr(p1): {repr(p1)}")
print(f"p1 == p3: {p1 == p3}")
print(f"p1 == p2: {p1 == p2}")
print(f"p1 + p2: {p1 + p2}")
print(f"len(p1): {len(p1)}")  # Distance from origin (int)
print(f"bool(Point(0, 0)): {bool(Point(0, 0))}")
print(f"p1(2): {p1(2)}")  # Callable - scales the point


# =============================================================================
# 3. CLASS METHODS AND STATIC METHODS
# =============================================================================

print("\n" + "=" * 50)
print("=== CLASS AND STATIC METHODS ===")

class Employee:
    """Employee class with different method types."""

    # Class attribute
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    # Instance method - has access to self
    def give_raise(self, amount):
        self.salary += amount
        return self.salary

    # Class method - has access to cls, not self
    @classmethod
    def from_string(cls, employee_string):
        """Alternative constructor from string."""
        name, salary = employee_string.split("-")
        return cls(name, int(salary))

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    # Static method - no access to self or cls
    @staticmethod
    def is_valid_salary(salary):
        """Validate salary without needing instance or class."""
        return salary > 0 and salary < 10000000

# Using instance method
emp1 = Employee("Alice", 50000)
print(f"emp1.salary after raise: {emp1.give_raise(5000)}")

# Using class method (alternative constructor)
emp2 = Employee.from_string("Bob-60000")
print(f"emp2 created from string: {emp2.name}, ${emp2.salary}")

# Using class method
print(f"Total employees: {Employee.get_employee_count()}")

# Using static method
print(f"Is 50000 valid? {Employee.is_valid_salary(50000)}")
print(f"Is -1000 valid? {Employee.is_valid_salary(-1000)}")


# =============================================================================
# 4. INHERITANCE
# =============================================================================

print("\n" + "=" * 50)
print("=== INHERITANCE ===")

class Animal:
    """Base class for animals."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement speak()")

    def info(self):
        return f"I am {self.name}"

class Dog(Animal):
    """Dog inherits from Animal."""

    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"

    def fetch(self):
        return f"{self.name} is fetching!"

class Cat(Animal):
    """Cat inherits from Animal."""

    def speak(self):
        return f"{self.name} says Meow!"

    def purr(self):
        return f"{self.name} is purring..."

# Using inheritance
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

print(f"dog.info(): {dog.info()}")  # Inherited method
print(f"dog.speak(): {dog.speak()}")  # Overridden method
print(f"dog.fetch(): {dog.fetch()}")  # Dog-specific method
print(f"cat.speak(): {cat.speak()}")

# Polymorphism - treating different types uniformly
animals = [dog, cat]
print("\nPolymorphism:")
for animal in animals:
    print(f"  {animal.speak()}")

# isinstance and issubclass
print(f"\nisinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")


# =============================================================================
# 5. MULTIPLE INHERITANCE AND MRO
# =============================================================================

print("\n" + "=" * 50)
print("=== MULTIPLE INHERITANCE ===")

class Flyable:
    """Mixin for flying capability."""

    def fly(self):
        return f"{self.name} is flying!"

class Swimmable:
    """Mixin for swimming capability."""

    def swim(self):
        return f"{self.name} is swimming!"

class Duck(Animal, Flyable, Swimmable):
    """Duck can walk, fly, and swim."""

    def speak(self):
        return f"{self.name} says Quack!"

duck = Duck("Donald")
print(f"duck.speak(): {duck.speak()}")
print(f"duck.fly(): {duck.fly()}")
print(f"duck.swim(): {duck.swim()}")

# Method Resolution Order (MRO)
print(f"\nDuck MRO: {Duck.__mro__}")


# =============================================================================
# 6. PROPERTIES (GETTERS/SETTERS)
# =============================================================================

print("\n" + "=" * 50)
print("=== PROPERTIES ===")

class Circle:
    """Circle with computed properties."""

    def __init__(self, radius):
        self._radius = radius  # Convention: _ prefix for "private"

    @property
    def radius(self):
        """Get the radius."""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set the radius with validation."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self):
        """Computed property - diameter."""
        return self._radius * 2

    @property
    def area(self):
        """Computed property - area."""
        import math
        return math.pi * self._radius ** 2

circle = Circle(5)
print(f"radius: {circle.radius}")
print(f"diameter: {circle.diameter}")
print(f"area: {circle.area:.2f}")

# Using setter
circle.radius = 10
print(f"new radius: {circle.radius}")
print(f"new diameter: {circle.diameter}")

# Validation works
try:
    circle.radius = -5
except ValueError as e:
    print(f"Error: {e}")


# =============================================================================
# 7. DATACLASSES (Python 3.7+)
# =============================================================================

print("\n" + "=" * 50)
print("=== DATACLASSES ===")

from dataclasses import dataclass, field
from typing import List

# Basic dataclass
@dataclass
class User:
    """User dataclass - generates __init__, __repr__, __eq__ automatically."""
    name: str
    email: str
    age: int

user1 = User("Alice", "alice@example.com", 30)
user2 = User("Alice", "alice@example.com", 30)

print(f"user1: {user1}")
print(f"user1 == user2: {user1 == user2}")

# Dataclass with defaults and field options
@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: List[str] = field(default_factory=list)  # Mutable default
    _id: int = field(default=0, repr=False)  # Hidden from repr

product = Product("Laptop", 999.99, 5, ["electronics", "sale"])
print(f"\nproduct: {product}")

# Immutable dataclass
@dataclass(frozen=True)
class Point3D:
    x: float
    y: float
    z: float

point = Point3D(1, 2, 3)
print(f"\nfrozen point: {point}")
# point.x = 5  # FrozenInstanceError!

# Dataclass with methods
@dataclass
class Rectangle:
    width: float
    height: float

    @property
    def area(self):
        return self.width * self.height

    def scale(self, factor):
        return Rectangle(self.width * factor, self.height * factor)

rect = Rectangle(5, 3)
print(f"\nrect: {rect}")
print(f"rect.area: {rect.area}")
print(f"rect.scale(2): {rect.scale(2)}")

# Dataclass with __post_init__ for validation/computation
@dataclass
class Person:
    first_name: str
    last_name: str
    birth_year: int
    full_name: str = field(init=False)  # Computed, not in __init__

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"
        if self.birth_year < 1900:
            raise ValueError("Birth year must be >= 1900")

person = Person("John", "Doe", 1990)
print(f"\nperson: {person}")
print(f"person.full_name: {person.full_name}")


# =============================================================================
# 8. ABSTRACT BASE CLASSES
# =============================================================================

print("\n" + "=" * 50)
print("=== ABSTRACT BASE CLASSES ===")

from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area - must be implemented by subclasses."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter - must be implemented by subclasses."""
        pass

    def describe(self):
        """Concrete method - inherited by subclasses."""
        return f"Shape with area {self.area():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius

# Cannot instantiate abstract class
# shape = Shape()  # TypeError!

rect = Rectangle(5, 3)
circle = Circle(4)

print(f"Rectangle area: {rect.area()}, perimeter: {rect.perimeter()}")
print(f"Circle area: {circle.area():.2f}, perimeter: {circle.perimeter():.2f}")
print(f"rect.describe(): {rect.describe()}")


# =============================================================================
# 9. COMPOSITION VS INHERITANCE
# =============================================================================

print("\n" + "=" * 50)
print("=== COMPOSITION VS INHERITANCE ===")

# Composition: "has-a" relationship (often preferred over inheritance)

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"

class Wheels:
    def __init__(self, count):
        self.count = count

    def rotate(self):
        return f"{self.count} wheels rotating"

class Car:
    """Car composed of engine and wheels."""

    def __init__(self, model, horsepower, wheel_count=4):
        self.model = model
        self.engine = Engine(horsepower)  # Composition
        self.wheels = Wheels(wheel_count)  # Composition

    def start(self):
        return f"{self.model}: {self.engine.start()}, {self.wheels.rotate()}"

    def stop(self):
        return f"{self.model}: {self.engine.stop()}"

car = Car("Tesla Model 3", 300)
print(f"car.start(): {car.start()}")
print(f"car.stop(): {car.stop()}")
print(f"car.engine.horsepower: {car.engine.horsepower}")


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# TODO Exercise 1: Create a BankAccount Class
# - Attributes: account_number, holder_name, balance (default 0)
# - Methods: deposit(amount), withdraw(amount), get_balance()
# - withdraw should not allow negative balance (raise ValueError)
print("\n--- Exercise 1: BankAccount Class ---")
# Your code here:


# TODO Exercise 2: Create Special Methods
# Create a Vector class with x, y attributes
# Implement: __str__, __eq__, __add__, __mul__ (scalar multiplication)
print("\n--- Exercise 2: Vector Class ---")
# Your code here:


# TODO Exercise 3: Inheritance
# Create a base class Vehicle with name and max_speed
# Create Car and Motorcycle subclasses with additional attributes
# Implement a describe() method in each
print("\n--- Exercise 3: Vehicle Inheritance ---")
# Your code here:


# TODO Exercise 4: Properties
# Create a Temperature class that stores temperature in Celsius
# Add properties for fahrenheit and kelvin (computed)
# Add setters that convert back to Celsius
print("\n--- Exercise 4: Temperature Class ---")
# Your code here:


# TODO Exercise 5: Dataclass
# Create a Book dataclass with:
# - title, author, year, isbn
# - pages (default 0)
# - genres (list, default empty)
# Add a property `age` that returns years since publication
print("\n--- Exercise 5: Book Dataclass ---")
# Your code here:


# TODO Exercise 6: Abstract Base Class
# Create an abstract PaymentProcessor with methods:
# - process_payment(amount) -> bool
# - refund(amount) -> bool
# Implement CreditCardProcessor and PayPalProcessor
print("\n--- Exercise 6: Payment Processor ---")
# Your code here:


print("\n" + "=" * 50)
print("Run the solution file to check your answers!")
print("=" * 50)

