from flask import Flask, render_template, request, make_response

app = Flask(__name__, template_folder="templates")
app.static_folder = "templates/static"


@app.route("/")
def login():
    username = request.cookies.get("username")
    if username:
        return render_template("home.html", username=username)
    else:
        return render_template("login.html")


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    if username:
        response = make_response(render_template("home.html", username=username))
        response.set_cookie("username", username)
        return response
    else:
        return render_template("login.html", error="Please enter a username to register.")


@app.route("/logout",  methods=["POST"])
def logout():
    response = make_response(render_template("login.html"))
    response.set_cookie("username", "", expires=0)
    return response


if __name__ == '__main__':
    app.run()
