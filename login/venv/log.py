from flask import Flask, request, render_template

app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    return render_template("start.html")


database = {'virat': '018', 'dhoni': '007', 'sachin': '010'}


@app.route('/form_login', methods=['POST', 'GET'])
def login():
    name1 = request.form['username']
    passkey = request.form['password']
    if name1 not in database:
        return render_template('start.html', info='Invalid Username')
    else:
        if database[name1] != passkey:
            return render_template('start.html', info='Invalid Password')
        else:
            return render_template('home.html', name=name1)


@app.route('/form_logout', methods=['POST', 'GET'])
def logout():
    return render_template('start.html', info='Back to login')


if __name__ == "__main__":
    app.run(debug=True)
