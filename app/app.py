from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

users = {}

@app.route('/users', methods=['POST'])
def create_user():
    user_id = int(request.json.get('id'))
    user_data = {
        'name': request.json.get('name'),
        'bio': request.json.get('bio'),
        'skills': request.json.get('skills'),
        'profile_picture': request.json.get('profile_picture'),
        'github_gitlab': request.json.get('github_gitlab')
    }
    users[user_id] = user_data
    return jsonify(user_data), 201

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user_data = users.get(user_id)
    if user_data:
        return jsonify(user_data)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        user_data = users[user_id]
        user_data.update({
            'name': request.json.get('name', user_data['name']),
            'bio': request.json.get('bio', user_data['bio']),
            'skills': request.json.get('skills', user_data['skills']),
            'profile_picture': request.json.get('profile_picture', user_data['profile_picture']),
            'github_gitlab': request.json.get('github_gitlab', user_data['github_gitlab'])
        })
        return jsonify(user_data)
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/example_user', methods=['GET'])
def create_example_user():
    example_user = {
        'id': 1,
        'name': 'John Doe',
        'bio': 'A software developer with 10 years of experience.',
        'skills': ['Python', 'Flask', 'JavaScript'],
        'profile_picture': 'http://example.com/profile.jpg',
        'github_gitlab': 'http://github.com/johndoe'
    }
    users[example_user['id']] = example_user
    return jsonify(example_user), 201

if __name__ == '__main__':
    app.run(debug=True)