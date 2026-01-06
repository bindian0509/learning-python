"""
=============================================================================
PYTHON 3 CRASH COURSE - Module 07: Modules and Packages
=============================================================================
Topics: Imports, packages, virtual environments, common stdlib

Run this file: python3 07_modules.py
=============================================================================
"""

# =============================================================================
# 1. IMPORTING MODULES
# =============================================================================

print("=== IMPORTING MODULES ===")

# Import entire module
import math
print(f"math.pi: {math.pi}")
print(f"math.sqrt(16): {math.sqrt(16)}")

# Import with alias
import datetime as dt
now = dt.datetime.now()
print(f"Current time: {now}")

# Import specific items
from random import randint, choice
print(f"Random int 1-10: {randint(1, 10)}")
print(f"Random choice: {choice(['apple', 'banana', 'cherry'])}")

# Import with alias
from collections import Counter as C
word_counts = C("mississippi")
print(f"Letter counts: {dict(word_counts)}")

# Import all (avoid in production code!)
# from math import *  # Pollutes namespace


# =============================================================================
# 2. COMMON STANDARD LIBRARY MODULES
# =============================================================================

print("\n" + "=" * 50)
print("=== COMMON STANDARD LIBRARY ===")

# os - Operating system interface
import os

print("\n--- os module ---")
print(f"Current directory: {os.getcwd()}")
print(f"Directory contents: {os.listdir('.')[:5]}...")  # First 5
print(f"Environment var HOME: {os.environ.get('HOME', 'Not set')}")
print(f"Path separator: {os.sep}")
print(f"Join paths: {os.path.join('folder', 'subfolder', 'file.txt')}")

# pathlib - Modern path handling (Python 3.4+)
from pathlib import Path

print("\n--- pathlib module ---")
current = Path.cwd()
print(f"Current path: {current}")
print(f"Home directory: {Path.home()}")

# Path operations
p = Path("/usr/local/bin/python")
print(f"Name: {p.name}")
print(f"Stem: {p.stem}")
print(f"Suffix: {p.suffix}")
print(f"Parent: {p.parent}")
print(f"Parts: {p.parts}")

# sys - System-specific parameters
import sys

print("\n--- sys module ---")
print(f"Python version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Path: {sys.path[:2]}...")  # First 2 paths

# json - JSON encoding/decoding
import json

print("\n--- json module ---")
data = {"name": "Alice", "age": 30, "active": True}

# Serialize to JSON string
json_string = json.dumps(data, indent=2)
print(f"JSON string:\n{json_string}")

# Parse JSON string
parsed = json.loads(json_string)
print(f"Parsed back: {parsed}")

# datetime - Date and time handling
from datetime import datetime, date, timedelta

print("\n--- datetime module ---")
now = datetime.now()
print(f"Now: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Today: {date.today()}")
print(f"Tomorrow: {date.today() + timedelta(days=1)}")

# Parse date string
date_str = "2024-12-25"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print(f"Parsed date: {parsed_date}")

# collections - Specialized containers
from collections import defaultdict, namedtuple, deque, OrderedDict

print("\n--- collections module ---")

# defaultdict - dict with default value
word_groups = defaultdict(list)
for word in ["apple", "banana", "apricot", "blueberry"]:
    word_groups[word[0]].append(word)
print(f"Word groups: {dict(word_groups)}")

# namedtuple - tuple with named fields
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(f"Named tuple: {p}, x={p.x}, y={p.y}")

# deque - double-ended queue (efficient append/pop from both ends)
d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
print(f"Deque: {d}")

# itertools - Iterator building blocks
import itertools

print("\n--- itertools module ---")
print(f"count: {list(itertools.islice(itertools.count(1), 5))}")
print(f"cycle: {list(itertools.islice(itertools.cycle('AB'), 6))}")
print(f"chain: {list(itertools.chain([1, 2], [3, 4]))}")
print(f"combinations: {list(itertools.combinations('ABC', 2))}")
print(f"permutations: {list(itertools.permutations('AB'))}")

# functools - Higher-order functions
from functools import reduce, partial

print("\n--- functools module ---")
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Product with reduce: {product}")

# re - Regular expressions
import re

print("\n--- re module ---")
text = "Contact us at support@example.com or sales@example.com"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(f"Found emails: {emails}")

pattern = re.compile(r'\d+')
print(f"Find all numbers in 'abc123def456': {pattern.findall('abc123def456')}")


# =============================================================================
# 3. CREATING YOUR OWN MODULE
# =============================================================================

print("\n" + "=" * 50)
print("=== CREATING MODULES ===")

print("""
To create a module, simply create a .py file:

# mymodule.py
'''My custom module.'''

PI = 3.14159

def greet(name):
    return f"Hello, {name}!"

class Calculator:
    def add(self, a, b):
        return a + b

# Usage:
import mymodule
print(mymodule.greet("Alice"))
print(mymodule.PI)
""")


# =============================================================================
# 4. PACKAGES (Directories of Modules)
# =============================================================================

print("\n" + "=" * 50)
print("=== PACKAGES ===")

print("""
Package structure:

mypackage/
    __init__.py      # Makes it a package (can be empty)
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py

# Usage:
from mypackage import module1
from mypackage.module2 import some_function
from mypackage.subpackage import module3

# __init__.py can define:
# - What gets imported with 'from package import *'
# - Package-level variables and functions
# - Convenient imports

# Example __init__.py:
from .module1 import important_function
from .module2 import ImportantClass

__all__ = ['important_function', 'ImportantClass']
""")


# =============================================================================
# 5. VIRTUAL ENVIRONMENTS
# =============================================================================

print("\n" + "=" * 50)
print("=== VIRTUAL ENVIRONMENTS ===")

print("""
Virtual environments isolate project dependencies.

# Create virtual environment
python3 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\\Scripts\\activate

# Deactivate
deactivate

# Install packages
pip install package_name
pip install package_name==1.2.3  # Specific version
pip install -r requirements.txt  # From file

# Save dependencies
pip freeze > requirements.txt

# Common requirements.txt format:
flask>=2.0.0
requests==2.28.1
numpy~=1.24.0  # Compatible release (1.24.x)
""")


# =============================================================================
# 6. PACKAGE MANAGEMENT WITH PIP
# =============================================================================

print("\n" + "=" * 50)
print("=== PIP COMMANDS ===")

print("""
# Install
pip install package_name
pip install package_name==1.0.0
pip install -e .  # Install current directory in editable mode

# Upgrade
pip install --upgrade package_name
pip install -U pip  # Upgrade pip itself

# Uninstall
pip uninstall package_name

# Information
pip list                  # List installed packages
pip show package_name     # Package details
pip search package_name   # Search PyPI (deprecated)

# Requirements
pip freeze > requirements.txt
pip install -r requirements.txt

# Cache
pip cache purge  # Clear cache
""")


# =============================================================================
# 7. __name__ AND __main__
# =============================================================================

print("\n" + "=" * 50)
print("=== __name__ AND __main__ ===")

print(f"Current __name__: {__name__}")

print("""
When a Python file runs:
- If run directly: __name__ == '__main__'
- If imported: __name__ == 'module_name'

Common pattern:

def main():
    # Main program logic
    print("Running as main program")

if __name__ == '__main__':
    main()

This allows:
1. Running the file directly as a script
2. Importing functions without running main code
""")

# Demo
def main():
    print("This would be the main entry point")

if __name__ == '__main__':
    print("This file is being run directly")


# =============================================================================
# 8. USEFUL THIRD-PARTY PACKAGES
# =============================================================================

print("\n" + "=" * 50)
print("=== POPULAR THIRD-PARTY PACKAGES ===")

print("""
Web Development:
- fastapi - Modern async API framework
- flask - Lightweight web framework
- django - Full-featured web framework
- requests - HTTP library
- httpx - Async HTTP client

Data:
- pandas - Data analysis
- numpy - Numerical computing
- sqlalchemy - Database ORM

Testing:
- pytest - Testing framework
- coverage - Code coverage

Utilities:
- python-dotenv - Environment variables
- pydantic - Data validation
- click - CLI applications
- rich - Beautiful terminal output

Async:
- asyncio (stdlib) - Async programming
- aiohttp - Async HTTP
- uvicorn - ASGI server
""")


# =============================================================================
# 9. RELATIVE VS ABSOLUTE IMPORTS
# =============================================================================

print("\n" + "=" * 50)
print("=== RELATIVE VS ABSOLUTE IMPORTS ===")

print("""
Given package structure:
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py

# ABSOLUTE IMPORTS (Recommended)
from mypackage.module1 import func1
from mypackage.subpackage.module3 import func3

# RELATIVE IMPORTS (Within package)
# In module2.py:
from .module1 import func1  # Same directory
from . import module1

# In subpackage/module3.py:
from .. import module1  # Parent directory
from ..module2 import func2

Best Practice:
- Use absolute imports for clarity
- Use relative imports sparingly within packages
- Never use relative imports in scripts meant to run directly
""")


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================

print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

# TODO Exercise 1: JSON File Operations
# Create functions:
# - save_json(data, filename) - save dict to JSON file
# - load_json(filename) - load dict from JSON file
# Handle errors appropriately
print("\n--- Exercise 1: JSON File Operations ---")
# Your code here:


# TODO Exercise 2: Path Operations
# Using pathlib:
# - List all .py files in current directory
# - Get the size of each file
# - Print formatted output
print("\n--- Exercise 2: Path Operations ---")
# Your code here:


# TODO Exercise 3: Date Calculations
# Create a function days_until(date_string) that:
# - Takes a date string "YYYY-MM-DD"
# - Returns days until that date (negative if past)
print("\n--- Exercise 3: Date Calculations ---")
# Your code here:


# TODO Exercise 4: Text Processing
# Using re (regex):
# - Extract all URLs from a text
# - Extract all hashtags (#something)
print("\n--- Exercise 4: Text Processing ---")
sample_text = """
Check out https://python.org and http://example.com
Join us at #Python #Programming #100DaysOfCode
"""
# Your code here:


# TODO Exercise 5: Data Processing with Collections
# Given a list of orders (dicts with 'customer' and 'amount'):
# - Group orders by customer using defaultdict
# - Calculate total per customer
# - Find top customer
print("\n--- Exercise 5: Data Processing ---")
orders = [
    {"customer": "Alice", "amount": 100},
    {"customer": "Bob", "amount": 50},
    {"customer": "Alice", "amount": 75},
    {"customer": "Charlie", "amount": 200},
    {"customer": "Bob", "amount": 125},
]
# Your code here:


print("\n" + "=" * 50)
print("Run the solution file to check your answers!")
print("=" * 50)

