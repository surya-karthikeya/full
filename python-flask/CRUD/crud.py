from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
users = []


@app.route('/create', methods=['POST'])
def create():
    try:
        name = request.json['name']
        anime = request.json['anime']
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            insert_data = f"INSERT INTO users (name, anime) VALUES ('{name}', '{anime}')"
            cur.execute(insert_data)
            con.commit()
        return jsonify({'message': 'User created successfully!'})
    except KeyError as e:
        return jsonify({'error': f'Missing required key{e}'})


@app.route('/', methods=['GET'])
def reads():
    try:
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM users")
            rows = cur.fetchall()
        for row in rows:
            user = {'id': row[0], 'name': row[1], 'anime': row[2]}
            users.append(user)

        return jsonify({'users': users})
    except KeyError as e:
        return jsonify({'error': f'Missing required key{e}'})


@app.route('/read/<user_id>', methods=['GET'])
def read(user_id):
    try:
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
            row = cur.fetchone()

        if row:
            user = {'id': row[0], 'name': row[1], 'anime': row[2]}
            return jsonify(user)
        else:
            return jsonify({'message': 'User not found!'})
    except KeyError as e:
        return jsonify({'error': f'Missing required key{e}'})


@app.route('/update/<user_id>', methods=['PUT'])
def update(user_id):
    try:
        name = request.json['name']
        anime = request.json['anime']

        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE id=?", user_id)
            row = cur.fetchone()
            if row is None:
                return jsonify({'message': 'User not found'})
            else:
                cur.execute("UPDATE users SET name=?, anime=? WHERE id=?", (name, anime, user_id))
                con.commit()

                return jsonify({'message': 'User updated successfully!'})
    except KeyError as e:
        return jsonify({'error': f'Missing required key{e}'})


@app.route('/delete/<user_id>', methods=['DELETE'])
def delete(user_id):
    try:
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE id=?", user_id)
            row = cur.fetchone()
            if row is None:
                return jsonify({'message': 'User not found'})
            else:
                cur.execute("DELETE FROM users WHERE id=?", (user_id,))

                con.commit()
                return jsonify({'message': 'User deleted successfully!'})
    except KeyError as e:
        return jsonify({'error': f'Missing required key{e}'})


if __name__ == '__main__':
    app.run(debug=True)
