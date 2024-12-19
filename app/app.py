from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}
snippets = {}
comments = {}
projects = {}

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

@app.route('/snippets', methods=['POST'])
def create_snippet():
    snippet_id = request.json.get('id')
    snippet_data = request.json
    snippets[snippet_id] = snippet_data
    return jsonify(snippet_data), 201

@app.route('/snippets/<snippet_id>', methods=['GET'])
def get_snippet(snippet_id):
    snippet_data = snippets.get(snippet_id)
    if snippet_data:
        return jsonify(snippet_data)
    else:
        return jsonify({'error': 'Snippet not found'}), 404

@app.route('/snippets/<snippet_id>', methods=['PUT'])
def update_snippet(snippet_id):
    if snippet_id in snippets:
        snippets[snippet_id].update(request.json)
        return jsonify(snippets[snippet_id])
    else:
        return jsonify({'error': 'Snippet not found'}), 404

@app.route('/snippets/<snippet_id>', methods=['DELETE'])
def delete_snippet(snippet_id):
    if snippet_id in snippets:
        del snippets[snippet_id]
        return jsonify({'message': 'Snippet deleted'}), 200
    else:
        return jsonify({'error': 'Snippet not found'}), 404

@app.route('/snippets', methods=['GET'])
def search_snippets():
    user = request.args.get('user')
    tag = request.args.get('tag')
    language = request.args.get('language')
    filtered_snippets = [snippet for snippet in snippets.values() if
                         (not user or snippet.get('user') == user) and
                         (not tag or tag in snippet.get('tags', [])) and
                         (not language or snippet.get('language') == language)]
    return jsonify(filtered_snippets)

@app.route('/comments/<snippet_id>', methods=['POST'])
def add_comment(snippet_id):
    comment = request.json
    if snippet_id not in comments:
        comments[snippet_id] = []
    comments[snippet_id].append(comment)
    return jsonify(comment), 201

@app.route('/comments/<snippet_id>', methods=['GET'])
def get_comments(snippet_id):
    if snippet_id not in comments:
        return jsonify([]), 200
    return jsonify(comments[snippet_id]), 200

@app.route('/projects', methods=['POST'])
def create_project():
    project_id = request.json.get('id')
    project_data = request.json
    projects[project_id] = project_data
    return jsonify(project_data), 201

@app.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    project_data = projects.get(project_id)
    if project_data:
        return jsonify(project_data)
    else:
        return jsonify({'error': 'Project not found'}), 404

@app.route('/projects/<project_id>', methods=['PUT'])
def update_project(project_id):
    if project_id in projects:
        projects[project_id].update(request.json)
        return jsonify(projects[project_id])
    else:
        return jsonify({'error': 'Project not found'}), 404

@app.route('/projects/<project_id>/members', methods=['POST'])
def add_project_member(project_id):
    if project_id not in projects:
        return jsonify({'error': 'Project not found'}), 404
    member_id = request.json.get('id')
    if 'members' not in projects[project_id]:
        projects[project_id]['members'] = []
    projects[project_id]['members'].append(member_id)
    return jsonify(projects[project_id]), 201

if __name__ == '__main__':
    app.run(debug=True)