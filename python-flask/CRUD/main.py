from flask import Flask, jsonify, request

app = Flask(__name__)

users = []


@app.route('/', methods=['GET'])
def main():
    return jsonify({"users": users})


@app.route('/create', methods=['POST'])
def create():
    try:
        data = request.get_json()
        name = data['name']
        anime = data['anime']
        user = {"id": len(users) + 1, "name": name, "anime": anime}
        users.append(user)
        return jsonify({"message": "User created successfully"})
    except Exception as e:
        return jsonify({"message": f"Error {str(e)}"})


@app.route('/read/<int:id>', methods=['GET'])
def read(idi):
    try:
        for user in users:
            if user['id'] == idi:
                return jsonify({"user": user})
            else:
                return jsonify({"message": "No User found"})
    except Exception as e:
        return jsonify({"message": f"Error {str(e)}"})


@app.route('/update/<int:id>', methods=['PUT'])
def update(idi):
    try:
        data = request.get_json()
        name = data['name']
        anime = data['anime']
        for user in users:
            if user['id'] == idi:
                user['name'] = name
                user['anime'] = anime
                return jsonify({"message": "User updated successfully"})
        return jsonify({"message": "User not found"})
    except Exception as e:
        return jsonify({"message": f"Error {str(e)}"})


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(idi):
    try:
        for user in users:
            if user['id'] == idi:
                users.remove(user)
                return jsonify({"message": "User deleted successfully"})
        return jsonify({"message": "User not found"})
    except Exception as e:
        return jsonify({"message": f"Error {str(e)}"})


if __name__ == '__main__':
    app.run(debug=True)
