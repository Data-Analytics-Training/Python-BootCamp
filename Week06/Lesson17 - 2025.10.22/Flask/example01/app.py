from flask import Flask, redirect, render_template, url_for, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/user/<username>")
def user(username):
    return render_template("user.html", username=username)


@app.route("/main")
def main():
    return redirect(url_for("index"))


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        message = f"Thank you, {name}"
        return render_template("contact.html", message=message)

    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
