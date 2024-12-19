
from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

@app.route('/users', methods=['POST'])
def create_user():
    user_id = request.json.get('id')
    user_data = request.json
    users[user_id] = user_data
    return jsonify(user_data), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_data = users.get(user_id)
    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        users[user_id].update(request.json)
        return jsonify(users[user_id])
    else:
        return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)