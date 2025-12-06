python3 -m venv .venv && source .venv/bin/activate #(optional)
pip install -r requirements.txt
export FLASK_APP=app
export FLASK_ENV=development
export FLASK_RUN_PORT=${PORT:-8000}
flask run
# OR alternative - PORT=${PORT:-8000} python app.py

