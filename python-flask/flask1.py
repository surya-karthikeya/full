from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "This is Home page <h1>HELLO!</h1>"


@app.route("/<name>")
def user(name):
    return f"<h1>'Hello!'</h1> <p>{name}<p>"


if __name__ == "__main__":
    app.run()

