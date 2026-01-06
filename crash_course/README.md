# Python 3 Crash Course for Backend Developers

A hands-on refresher course to get you comfortable writing Python 3 code that is syntax and runtime error-free. Designed for developers who need to quickly get back up to speed with Python fundamentals and modern features.

---

## Course Overview

| Phase | Modules | Focus |
|-------|---------|-------|
| **Phase 1: Fundamentals** | 01-03 | Syntax, data types, control flow |
| **Phase 2: Core Skills** | 04-06 | Functions, OOP, error handling |
| **Phase 3: Backend Ready** | 07-09 | Modules, type hints, async |
| **Phase 4: FastAPI** | 10 | Building APIs with FastAPI |

---

## Quick Start

```bash
# 1. Navigate to the course folder
cd crash_course

# 2. Run any module
python3 01_basics.py

# 3. Complete the exercises (look for # TODO comments)

# 4. Check your answers
python3 solutions/01_basics_solution.py
```

---

## Modules

### Phase 1: Fundamentals

| Module | File | Topics |
|--------|------|--------|
| 01 | `01_basics.py` | Variables, operators, strings, f-strings, walrus operator |
| 02 | `02_data_types.py` | Lists, dicts, sets, tuples, comprehensions, generators |
| 03 | `03_control_flow.py` | if/elif/else, for/while loops, match-case (Python 3.10+) |

### Phase 2: Core Skills

| Module | File | Topics |
|--------|------|--------|
| 04 | `04_functions.py` | Functions, *args/**kwargs, lambda, decorators, closures |
| 05 | `05_oop.py` | Classes, inheritance, properties, dataclasses, ABC |
| 06 | `06_error_handling.py` | try/except/finally, custom exceptions, context managers |

### Phase 3: Backend Ready

| Module | File | Topics |
|--------|------|--------|
| 07 | `07_modules.py` | Imports, packages, stdlib, virtual environments, pip |
| 08 | `08_type_hints.py` | Type annotations, Optional, Union, generics, protocols |
| 09 | `09_async.py` | async/await, asyncio, tasks, semaphores, concurrent execution |

### Phase 4: FastAPI

| Module | File | Topics |
|--------|------|--------|
| 10 | `10_fastapi_intro.py` | Routes, path/query params, Pydantic models, dependencies |

---

## How to Use This Course

### 1. Read & Run
Each module is a standalone Python file with:
- Detailed comments explaining concepts
- Working code examples you can run immediately
- Print statements showing output

```bash
python3 01_basics.py
```

### 2. Complete Exercises
At the bottom of each module, you'll find practice exercises marked with `# TODO`:

```python
# TODO Exercise 1: Create variables for a user profile
# Create: first_name, last_name, email, age, is_premium_user
# Your code here:
```

### 3. Check Solutions
Compare your answers with the solution files:

```bash
python3 solutions/01_basics_solution.py
```

### 4. Reference the Cheatsheet
Use `PYTHON3_CHEATSHEET.md` as a quick reference while coding.

---

## Running the FastAPI Module

Module 10 is a working FastAPI application:

```bash
# Install dependencies (from project root)
pip install fastapi uvicorn pydantic

# Run the API server
cd crash_course
uvicorn 10_fastapi_intro:app --reload

# Or run directly
python3 10_fastapi_intro.py
```

Then visit:
- **API Root**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

---

## File Structure

```
crash_course/
├── README.md                    # This file
├── PYTHON3_CHEATSHEET.md        # Quick reference guide
│
├── 01_basics.py                 # Variables, strings, operators
├── 02_data_types.py             # Collections and comprehensions
├── 03_control_flow.py           # Conditionals and loops
├── 04_functions.py              # Functions and decorators
├── 05_oop.py                    # Object-oriented programming
├── 06_error_handling.py         # Exceptions and context managers
├── 07_modules.py                # Imports and packages
├── 08_type_hints.py             # Type annotations
├── 09_async.py                  # Async programming
├── 10_fastapi_intro.py          # FastAPI basics
│
└── solutions/
    ├── 01_basics_solution.py
    ├── 02_data_types_solution.py
    ├── 03_control_flow_solution.py
    ├── 04_functions_solution.py
    ├── 05_oop_solution.py
    ├── 06_error_handling_solution.py
    ├── 07_modules_solution.py
    ├── 08_type_hints_solution.py
    └── 09_async_solution.py
```

---

## Estimated Time

| Approach | Time |
|----------|------|
| Quick skim (read + run examples) | 2-3 hours |
| With exercises | 4-6 hours |
| Deep practice (build mini-projects) | 8-10 hours |

---

## Prerequisites

- Python 3.10+ recommended (for match-case syntax)
- Python 3.8+ minimum
- Basic programming knowledge

---

## Key Python 3 Features Covered

| Feature | Python Version | Module |
|---------|----------------|--------|
| f-strings | 3.6+ | 01 |
| Walrus operator `:=` | 3.8+ | 01 |
| Positional-only params `/` | 3.8+ | 04 |
| Dataclasses | 3.7+ | 05 |
| match-case | 3.10+ | 03 |
| Type hints `list[str]` | 3.9+ | 08 |
| Union `int \| str` | 3.10+ | 08 |
| TaskGroup | 3.11+ | 09 |
| asyncio.timeout | 3.11+ | 09 |

---

## Tips for Success

1. **Run every example** - Don't just read, execute the code
2. **Modify and experiment** - Change values, break things, learn
3. **Complete all exercises** - Practice is essential
4. **Use the cheatsheet** - Keep it open while coding
5. **Build something** - After finishing, create a small project

---

## Next Steps After This Course

1. Build a REST API with FastAPI
2. Connect to a database (SQLAlchemy, asyncpg)
3. Add authentication (OAuth2, JWT)
4. Write tests (pytest)
5. Deploy to production (Docker, cloud platforms)

---

Happy coding! 🐍

