from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is Home page <h1>HELLO!</h1>"


@app.route("/<temp>")
def user(temp):
    return "<h1>'Hello!'</h1> <p>{}<p>".format(temp)

if __name__ == "__main__":
    app.run()

