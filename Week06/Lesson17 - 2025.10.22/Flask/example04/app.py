from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)  # Flask application object created


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


@app.route("/main")
def main():
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        message = f"Thank you {name}, your message has been received. "
        return render_template("contact.html", message=message)
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
