# learning-python

A personal Python playground: a deployed Flask branding site, a self-paced **Python 3 crash course** for backend developers, and a handful of standalone utility scripts.

Live site: https://mavenguy.pythonanywhere.com/

---

## Contents

| Area | Path | What it is |
|------|------|------------|
| Flask branding page | `app.py`, `templates/index.html` | Single-page personal profile site rendered with Jinja2 |
| Python 3 crash course | `crash_course/` | 10 runnable modules + exercises + solutions + cheatsheet |
| Salary/tax calculator | `salaries-post-tax.py` | India new-regime take-home calculator with pandas/matplotlib output |
| Secret message decoder | `print-secret-message.py` | Scrapes a published doc and renders an ASCII grid |
| AWS architecture diagram | `diagram.py` | Generates a Graphviz diagram via `diagrams` |
| Small katas | `even_or_odd.py`, `photos-sorter.py`, `test.py` | Interview-style puzzles |

---

## Setup

Requires **Python 3.10+** (developed on 3.12).

```bash
git clone <repo-url> && cd learning-python

python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

Optional system dependency — only needed for `diagram.py`:

```bash
sudo apt install graphviz          # macOS: brew install graphviz
```

---

## Running the Flask app

```bash
FLASK_APP=app FLASK_ENV=development FLASK_RUN_PORT=8000 flask run
# or
PORT=8000 python app.py
```

Then open http://localhost:8000. The convenience script `run.python.flask.app.sh` contains the same steps.

All page content (profile, skills, experience, education) lives in the route handler in `app.py`; styling and layout live in `templates/index.html`.

---

## The crash course

A structured refresher covering fundamentals through async and FastAPI. Each module is a standalone, runnable file with inline explanations, `# TODO` exercises, and a matching solution file.

```bash
cd crash_course
python3 01_basics.py                       # read & run
python3 solutions/01_basics_solution.py    # check your answers
```

| Phase | Modules | Focus |
|-------|---------|-------|
| Fundamentals | 01–03 | Syntax, data types, control flow |
| Core skills | 04–06 | Functions, OOP, error handling |
| Backend ready | 07–09 | Modules, type hints, async |
| FastAPI | 10 | Routes, Pydantic models, dependencies |

Module 10 is a working API server:

```bash
cd crash_course
uvicorn 10_fastapi_intro:app --reload
```

Docs at http://localhost:8000/docs. See `crash_course/README.md` for the full module breakdown and `crash_course/PYTHON3_CHEATSHEET.md` for quick reference.

---

## Utility scripts

```bash
python3 salaries-post-tax.py      # writes take_home_salary_regime.csv + take_home_salary.png
python3 print-secret-message.py   # fetches a published doc and prints the decoded grid
python3 diagram.py                # writes a web service diagram (needs graphviz installed)
python3 photos-sorter.py          # photo renaming kata
```

`salaries-post-tax.py` models the Indian new tax regime including standard deduction, surcharge slabs, and marginal relief, then charts net monthly take-home against gross annual income.

---

## Dependencies

Declared in `requirements.txt`:

- **Flask** — branding site
- **fastapi**, **uvicorn**, **pydantic**, **email-validator** — crash course module 10
- **pandas**, **matplotlib** — salary calculator and charts
- **requests**, **beautifulsoup4** — scraping script
- **diagrams** — AWS architecture diagram (plus system `graphviz`)

---

## Deployment

The Flask site is hosted on PythonAnywhere. To redeploy, sync `app.py`, `templates/`, and `requirements.txt` to the host and reload the web app.
