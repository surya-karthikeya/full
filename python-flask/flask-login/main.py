from flask import Flask, request, redirect, render_template, make_response
from datetime import timedelta

app = Flask(__name__, template_folder="templates")
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=2)


@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        return f"Hello, {username}! <br><a href='/logout'>Logout</a>"
    else:
        return redirect('/register')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        response = make_response(redirect('/'))
        response.set_cookie('username', username, max_age=300)
        return response
    else:
        return render_template('register.html')


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('username', '', expires=0)
    return response


if __name__ == '__main__':
    app.run(debug=True)
