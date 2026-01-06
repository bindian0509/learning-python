"""
=============================================================================
SOLUTIONS - Module 07: Modules and Packages
=============================================================================
"""

import json
import os
from pathlib import Path
from datetime import datetime, date
import re
from collections import defaultdict

print("=" * 50)
print("SOLUTIONS - Module 07: Modules")
print("=" * 50)

# Exercise 1: JSON File Operations
print("\n--- Exercise 1: JSON File Operations ---")

def save_json(data: dict, filename: str) -> bool:
    """Save dictionary to JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except (IOError, TypeError) as e:
        print(f"Error saving JSON: {e}")
        return False

def load_json(filename: str) -> dict | None:
    """Load dictionary from JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return None

# Test
test_data = {"name": "Alice", "scores": [95, 87, 92]}
save_json(test_data, "test_data.json")
loaded = load_json("test_data.json")
print(f"Saved and loaded: {loaded}")
os.remove("test_data.json")  # Cleanup


# Exercise 2: Path Operations
print("\n--- Exercise 2: Path Operations ---")

current_dir = Path(".")
py_files = list(current_dir.glob("*.py"))

print(f"Python files in current directory:")
for py_file in py_files[:5]:  # Limit to 5 for display
    size = py_file.stat().st_size
    print(f"  {py_file.name}: {size:,} bytes")

if len(py_files) > 5:
    print(f"  ... and {len(py_files) - 5} more files")


# Exercise 3: Date Calculations
print("\n--- Exercise 3: Date Calculations ---")

def days_until(date_string: str) -> int:
    """
    Calculate days until a date.

    Args:
        date_string: Date in YYYY-MM-DD format

    Returns:
        Days until date (negative if in past)
    """
    target_date = datetime.strptime(date_string, "%Y-%m-%d").date()
    today = date.today()
    delta = target_date - today
    return delta.days

# Test with various dates
test_dates = [
    "2025-12-25",  # Christmas
    "2025-01-01",  # New Year
    "2024-01-01",  # Past date
]

for date_str in test_dates:
    days = days_until(date_str)
    if days > 0:
        print(f"  {date_str}: {days} days from now")
    elif days < 0:
        print(f"  {date_str}: {abs(days)} days ago")
    else:
        print(f"  {date_str}: Today!")


# Exercise 4: Text Processing
print("\n--- Exercise 4: Text Processing ---")

sample_text = """
Check out https://python.org and http://example.com
Join us at #Python #Programming #100DaysOfCode
Also visit https://fastapi.tiangolo.com/tutorial/
"""

# Extract URLs
url_pattern = r'https?://[^\s]+'
urls = re.findall(url_pattern, sample_text)
print(f"URLs found: {urls}")

# Extract hashtags
hashtag_pattern = r'#\w+'
hashtags = re.findall(hashtag_pattern, sample_text)
print(f"Hashtags found: {hashtags}")


# Exercise 5: Data Processing
print("\n--- Exercise 5: Data Processing ---")

orders = [
    {"customer": "Alice", "amount": 100},
    {"customer": "Bob", "amount": 50},
    {"customer": "Alice", "amount": 75},
    {"customer": "Charlie", "amount": 200},
    {"customer": "Bob", "amount": 125},
]

# Group orders by customer
customer_orders = defaultdict(list)
for order in orders:
    customer_orders[order["customer"]].append(order["amount"])

print("Orders by customer:")
for customer, amounts in customer_orders.items():
    print(f"  {customer}: {amounts}")

# Calculate totals
customer_totals = {
    customer: sum(amounts)
    for customer, amounts in customer_orders.items()
}
print(f"\nTotals: {customer_totals}")

# Find top customer
top_customer = max(customer_totals, key=customer_totals.get)
print(f"Top customer: {top_customer} (${customer_totals[top_customer]})")

