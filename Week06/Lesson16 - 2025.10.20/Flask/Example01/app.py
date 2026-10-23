from flask import Flask

# A Flask application object has been created.
app = Flask(__name__)


# The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
# main page url
@app.route("/")
@app.route("/home")
def index():
    return "Welcome to Python Bootcamp Course"


# About page url.
@app.route("/about")
def about():
    return "This is a simple Flask application"


# The string converter in the route() function tells Flask to convert the variable into a string before passing it to the function.
@app.route("/contact/<string:name>")
def contact(name):
    return f"{name}'s contact details here."


# The int converter in the route() function tells Flask to convert the variable into an integer before passing it to the function.
@app.route("/year/<int:year>")
def year(year):
    return f"Year {year} is a leap year."


if __name__ == "__main__":
    app.run(debug=True)
