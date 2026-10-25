"""
Jinja2 templates tags:
{{ ... }} -> for expressions to print to the page
{% ... %} -> for statements and variable expressions (if, for, etc.)
{# ... #} -> for comments
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    texts = [
        {"title": "What is Flask", "content": "Flask is a lightweight Python Web framework"},
        {"title": "Learning Jinja2 ", "content": "The templates engine is very useful"},
        {"title": "Virtual Environment", "content": "Isolating dependencies is great"},
    ]
    return render_template("index.html", texts=texts)


@app.route("/users")
def users():
    list_users = [
        {"name": "Jack", "active": True},
        {"name": "Jill", "active": False},
        {"name": "Jim", "active": True},
    ]
    return render_template("users.html", users=list_users)


@app.route("/products")
def products():
    categories = [
        {"name": "Electronic", "products": ["Laptop", "Phone", "Tablet"]},
        {"name": "Book", "products": ["Novel", "Poetry", "History"]},
    ]
    return render_template("products.html", categories=categories)


if __name__ == "__main__":
    app.run(debug=True)
