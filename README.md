# Bharat Verma – Flask Branding Page

Live site: https://mavenguy.pythonanywhere.com/

## Overview

A lightweight Flask app that serves a personal branding page for Bharat Verma, highlighting leadership profile, experience, and skills. The page is rendered from `templates/index.html` and populated by `app.py`.

## Getting Started

1. Create/activate a virtual environment (optional):
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run locally (defaults to port 8000):
   ```bash
   FLASK_APP=app FLASK_ENV=development FLASK_RUN_PORT=8000 flask run
   # or
   PORT=8000 python app.py
   ```
4. Open http://localhost:8000

## Project Structure

- `app.py` – Flask app and route data (profile, skills, experience, etc.)
- `templates/index.html` – Jinja2 template for the branding page
- `requirements.txt` – Python dependencies
- `run.python.flask.app.sh` – helper script to set env vars and run Flask

## Customizing

- Update content in `app.py` (profile, skills, experience, education).
- Adjust styling/layout in `templates/index.html`.

## Deployment

The site is currently hosted at https://mavenguy.pythonanywhere.com/; redeploy by syncing updated `app.py`, `templates/`, and dependencies to the host.
