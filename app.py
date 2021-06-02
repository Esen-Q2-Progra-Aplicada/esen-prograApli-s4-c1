from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    data = {}
    if request.method == "GET":
        company = "balcorp"
        return render_template("login.html", company=company)
    elif request.method == "POST":
        data["secret"] = "6LeAdQcbAAAAAGNn732kkStupieUDdKjQTl38KL_"
        data["response"] = request.form["g-recaptcha-response"]
        response = requests.post(
            "https://www.google.com/recaptcha/api/siteverify", params=data
        )
        print(response)
        if response.status_code == 200:
            messageJson = response.json()
            print(messageJson)
            if messageJson["success"]:
                user = request.form["user"]
                passwd = request.form["passwd"]
                return f"posted {user}::{passwd}"
            else:
                return f"posted {messageJson['error-codes'][0]}"
        else:
            return f"posted error"


if __name__ == "__main__":
    app.run(debug=True)
