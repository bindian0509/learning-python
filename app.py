from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Serve the main page."""
    return render_template("index.html", title="Flask Starter")


if __name__ == "__main__":
    app.run(debug=True)

