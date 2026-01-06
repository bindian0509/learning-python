"""
=============================================================================
SOLUTIONS - Module 05: Object-Oriented Programming
=============================================================================
"""

print("=" * 50)
print("SOLUTIONS - Module 05: OOP")
print("=" * 50)

# Exercise 1: BankAccount Class
print("\n--- Exercise 1: BankAccount Class ---")

class BankAccount:
    """A simple bank account class."""

    def __init__(self, account_number: str, holder_name: str, balance: float = 0):
        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = balance

    def deposit(self, amount: float) -> float:
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Withdraw money from the account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds. Balance: {self._balance}")
        self._balance -= amount
        return self._balance

    def get_balance(self) -> float:
        """Get current balance."""
        return self._balance

    def __str__(self) -> str:
        return f"BankAccount({self.account_number}, {self.holder_name}, ${self._balance:.2f})"

account = BankAccount("12345", "Alice")
print(f"Created: {account}")
print(f"Deposit $100: ${account.deposit(100):.2f}")
print(f"Withdraw $30: ${account.withdraw(30):.2f}")
print(f"Balance: ${account.get_balance():.2f}")

try:
    account.withdraw(100)
except ValueError as e:
    print(f"Withdraw $100: Error - {e}")


# Exercise 2: Vector Class
print("\n--- Exercise 2: Vector Class ---")

class Vector:
    """A 2D vector class with special methods."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)

v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = Vector(3, 4)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 == v3: {v1 == v3}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 * 2: {v1 * 2}")


# Exercise 3: Vehicle Inheritance
print("\n--- Exercise 3: Vehicle Inheritance ---")

class Vehicle:
    """Base class for vehicles."""

    def __init__(self, name: str, max_speed: int):
        self.name = name
        self.max_speed = max_speed

    def describe(self) -> str:
        return f"{self.name} with max speed {self.max_speed} km/h"

class Car(Vehicle):
    """Car inherits from Vehicle."""

    def __init__(self, name: str, max_speed: int, num_doors: int):
        super().__init__(name, max_speed)
        self.num_doors = num_doors

    def describe(self) -> str:
        return f"Car: {self.name}, {self.num_doors} doors, max {self.max_speed} km/h"

class Motorcycle(Vehicle):
    """Motorcycle inherits from Vehicle."""

    def __init__(self, name: str, max_speed: int, engine_cc: int):
        super().__init__(name, max_speed)
        self.engine_cc = engine_cc

    def describe(self) -> str:
        return f"Motorcycle: {self.name}, {self.engine_cc}cc engine, max {self.max_speed} km/h"

car = Car("Tesla Model 3", 250, 4)
bike = Motorcycle("Ducati", 280, 1200)

print(car.describe())
print(bike.describe())


# Exercise 4: Temperature Class
print("\n--- Exercise 4: Temperature Class ---")

class Temperature:
    """Temperature class with Celsius storage and computed properties."""

    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self._celsius = (value - 32) * 5/9

    @property
    def kelvin(self) -> float:
        return self._celsius + 273.15

    @kelvin.setter
    def kelvin(self, value: float):
        self._celsius = value - 273.15

temp = Temperature(25)
print(f"Celsius: {temp.celsius}°C")
print(f"Fahrenheit: {temp.fahrenheit}°F")
print(f"Kelvin: {temp.kelvin}K")

temp.fahrenheit = 100
print(f"\nAfter setting 100°F:")
print(f"Celsius: {temp.celsius:.2f}°C")

temp.kelvin = 300
print(f"\nAfter setting 300K:")
print(f"Celsius: {temp.celsius:.2f}°C")


# Exercise 5: Book Dataclass
print("\n--- Exercise 5: Book Dataclass ---")

from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Book:
    """Book dataclass with computed age property."""
    title: str
    author: str
    year: int
    isbn: str
    pages: int = 0
    genres: List[str] = field(default_factory=list)

    @property
    def age(self) -> int:
        return datetime.now().year - self.year

book = Book(
    title="The Pragmatic Programmer",
    author="David Thomas",
    year=2019,
    isbn="978-0135957059",
    pages=352,
    genres=["Programming", "Software Engineering"]
)

print(f"Book: {book}")
print(f"Age: {book.age} years")


# Exercise 6: Payment Processor
print("\n--- Exercise 6: Payment Processor ---")

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Abstract base class for payment processors."""

    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Process a payment."""
        pass

    @abstractmethod
    def refund(self, amount: float) -> bool:
        """Process a refund."""
        pass

class CreditCardProcessor(PaymentProcessor):
    """Credit card payment processor."""

    def __init__(self, card_number: str):
        self.card_number = card_number

    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount:.2f} via credit card {self.card_number[-4:]}")
        return True

    def refund(self, amount: float) -> bool:
        print(f"Refunding ${amount:.2f} to credit card {self.card_number[-4:]}")
        return True

class PayPalProcessor(PaymentProcessor):
    """PayPal payment processor."""

    def __init__(self, email: str):
        self.email = email

    def process_payment(self, amount: float) -> bool:
        print(f"Processing ${amount:.2f} via PayPal ({self.email})")
        return True

    def refund(self, amount: float) -> bool:
        print(f"Refunding ${amount:.2f} to PayPal ({self.email})")
        return True

# Usage
cc = CreditCardProcessor("4111111111111234")
paypal = PayPalProcessor("user@example.com")

cc.process_payment(99.99)
cc.refund(50.00)
paypal.process_payment(49.99)
paypal.refund(25.00)

