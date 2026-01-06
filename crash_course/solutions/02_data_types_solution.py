"""
=============================================================================
SOLUTIONS - Module 02: Data Types & Collections
=============================================================================
"""

print("=" * 50)
print("SOLUTIONS - Module 02: Data Types")
print("=" * 50)

# Exercise 1: Filter and Transform
print("\n--- Exercise 1: Filter and Transform ---")
numbers = [-3, -1, 0, 2, 4, -5, 6]
positive_squares = [x**2 for x in numbers if x > 0]
print(f"Original: {numbers}")
print(f"Positive squares: {positive_squares}")


# Exercise 2: Word Count
print("\n--- Exercise 2: Word Count ---")
sentence = "the quick brown fox jumps over the lazy dog the fox"
words = sentence.split()

# Method 1: Using dict comprehension and count
word_count = {word: words.count(word) for word in set(words)}
print(f"Word count: {word_count}")

# Method 2: Using collections.Counter (better for large texts)
from collections import Counter
word_count_v2 = dict(Counter(words))
print(f"Using Counter: {word_count_v2}")


# Exercise 3: Passing Students
print("\n--- Exercise 3: Passing Students ---")
grades = {
    "Alice": 85,
    "Bob": 55,
    "Charlie": 72,
    "Diana": 48,
    "Eve": 91
}
passing = {name: grade for name, grade in grades.items() if grade >= 60}
print(f"All grades: {grades}")
print(f"Passing students: {passing}")


# Exercise 4: Set Operations
print("\n--- Exercise 4: Set Operations ---")
team_a = {"Alice", "Bob", "Charlie", "Diana"}
team_b = {"Charlie", "Diana", "Eve", "Frank"}

common = team_a & team_b
only_a = team_a - team_b
only_b = team_b - team_a

print(f"Team A: {team_a}")
print(f"Team B: {team_b}")
print(f"Common members: {common}")
print(f"Only in Team A: {only_a}")
print(f"Only in Team B: {only_b}")


# Exercise 5: Extract Emails
print("\n--- Exercise 5: Extract Emails ---")
users = [
    {"name": "Alice", "email": "alice@example.com", "active": True},
    {"name": "Bob", "email": "bob@example.com", "active": False},
    {"name": "Charlie", "email": "charlie@example.com", "active": True}
]

active_emails = [user["email"] for user in users if user["active"]]
print(f"Active user emails: {active_emails}")


# Exercise 6: Calculate Distances
print("\n--- Exercise 6: Calculate Distances ---")
points = [(3, 4), (5, 12), (8, 15)]
distances = [(x**2 + y**2)**0.5 for x, y in points]
print(f"Points: {points}")
print(f"Distances from origin: {distances}")

# More detailed output
for (x, y), dist in zip(points, distances):
    print(f"  Point ({x}, {y}): distance = {dist:.2f}")

