from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")


@app.route("/user/<username>")
def user(username):
  today = datetime.now().strftime("%Y-%m-%d")
  return render_template("user.html", username=username, today=today)


if __name__ == "__main__":
  app.run(debug=True)
