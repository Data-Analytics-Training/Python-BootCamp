from flask import Flask, request, render_template, redirect

app = Flask(__name__)

contacts = [{"name": "Jack", "surname": "Dow"}, {"name": "Jim", "surname": "Down"}]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        print(request.form)
        name = str(request.form.get("name", False))
        surname = str(request.form.get("surname", False))
        if name and surname:
            contacts.append({"name": name, "surname": surname})
            return redirect("/")

    return render_template("index.html", contacts=contacts)


if __name__ == "__main__":
    app.run(debug=True)
