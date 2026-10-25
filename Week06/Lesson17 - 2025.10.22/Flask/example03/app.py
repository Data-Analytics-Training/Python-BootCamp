# * ToDo Application
from flask import Flask, render_template

app = Flask(__name__)  # Flask application object created

todos = [
    {"id": 1, "mission": "Learn Flask", "completed": True},
    {"id": 2, "mission": "Study Jinja2", "completed": False},
    {"id": 3, "mission": "Build virtual environment", "completed": False},
    {"id": 4, "mission": "Make a ToDo list", "completed": True},
]


@app.route("/")
def index():
    return render_template("index.html", todos=todos)


if __name__ == "__main__":
    app.run(debug=True)
