from flask import Flask, request, redirect, render_template, make_response
from datetime import timedelta

app = Flask(__name__, template_folder="templates")
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=3)
registration_count = 0
users = []


class User:
    def __init__(self, username):
        self.username = username
        self.profile = {}


@app.route('/')
def index():
    username = request.cookies.get('username')
    if username:
        return f"Hello, {username}! <br><a href='/profile'>Profile</a> || <a href='/logout'>Logout</a>"
    else:
        return redirect('/register')


@app.route('/register', methods=['GET', 'POST'])
def register():
    global registration_count, users
    if request.method == 'POST':
        username = request.form['username']
        user = User(username)
        users.append(user)
        response = make_response(redirect('/'))
        response.set_cookie('username', username, max_age=300)
        registration_count += 1
        return response
    else:
        return render_template('register.html')


@app.route('/logout')
def logout():
    response = make_response(redirect('/'))
    response.set_cookie('username', '', expires=0)
    return response


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    username = request.cookies.get('username')
    user = get_user_by_username(username)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user.profile['name'] = name
        user.profile['email'] = email
    return render_template('profile.html', user=user)


@app.route('/stats')
def stats():
    return f"Number of registrations: {registration_count} <br> Usernames: {[user.username for user in users]}"


def get_user_by_username(username):
    for user in users:
        if user.username == username:
            return user
    return None


if __name__ == '__main__':
    app.run(debug=True)
