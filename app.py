from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        company = "balcorp"
        return render_template("login.html", company=company)
    elif request.method == "POST":
        month = request.form["month"]
        return f"posted month:{month}"


if __name__ == "__main__":
    app.run(debug=True)
