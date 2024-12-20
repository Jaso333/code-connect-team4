from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
from functools import wraps
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import db_connect, db_insert_user, db_update_user, db_delete_user, db_get_user_by_username, db_insert_snippet, db_update_snippet, db_delete_snippet, db_get_snippet_by_id, db_filter_snippets, db_insert_comment, db_get_comments_by_snippet_id, db_insert_project, db_get_project_by_id, db_update_project, db_insert_user_project, db_get_all_comments, db_get_all_projects, db_get_user_projects_by_project_id, User, Comment, Snippet, Project, UserProject

app = Flask(__name__)
CORS(app)

# Decorator for handling database connections
def with_db_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = db_connect()
        try:
            return func(conn, *args, **kwargs)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            conn.close()
    return wrapper

# User routes
@app.route('/users', methods=['POST'])
@with_db_connection
def create_user(conn):
    try:
        user = User(
            username=request.json.get('username'),
            email=request.json.get('email'),
            password=request.json.get('password'),
            first_name=request.json.get('first_name'),
            surname=request.json.get('surname'),
            bio=request.json.get('bio'),
            skills=request.json.get('skills')
        )
        db_insert_user(conn, user)
        return jsonify({'username': user.username, 'email': user.email, 'first_name': user.first_name, 'surname': user.surname, 'bio': user.bio, 'skills': user.skills}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to create user: ' + str(e)}), 500

@app.route('/users', methods=['GET'])
@with_db_connection
def get_all_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT username, email, password, first_name, surname, bio, skills FROM users")
    users = cursor.fetchall()
    return jsonify([{'username': user[0], 'email': user[1], 'first_name': user[3], 'surname': user[4], 'bio': user[5], 'skills': user[6]} for user in users])

@app.route('/users/<username>', methods=['GET'])
@with_db_connection
def get_user(conn, username):
    user = db_get_user_by_username(conn, username)
    if user:
        return jsonify({'username': user.username, 'email': user.email, 'first_name': user.first_name, 'surname': user.surname, 'bio': user.bio, 'skills': user.skills})
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<username>', methods=['PUT'])
@with_db_connection
def update_user(conn, username):
    user = db_get_user_by_username(conn, username)
    if user:
        user.email = request.json.get('email', user.email)
        user.password = request.json.get('password', user.password)
        user.first_name = request.json.get('first_name', user.first_name)
        user.surname = request.json.get('surname', user.surname)
        user.bio = request.json.get('bio', user.bio)
        user.skills = request.json.get('skills', user.skills)
        db_update_user(conn, user)
        return jsonify({'username': user.username, 'email': user.email, 'first_name': user.first_name, 'surname': user.surname, 'bio': user.bio, 'skills': user.skills})
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/users/<username>', methods=['DELETE'])
@with_db_connection
def delete_user(conn, username):
    db_delete_user(conn, username)
    return jsonify({'message': 'User deleted'}), 200

# Snippet routes
@app.route('/snippets', methods=['POST'])
@with_db_connection
def create_snippet(conn):
    try:
        snippet = Snippet(
            id=None,
            code=request.json.get('content'),
            tags=request.json.get('tags'),
            language=request.json.get('language'),
            user_name=request.json.get('user_name')
        )
        snippet_id = db_insert_snippet(conn, snippet)
        return jsonify({'id': snippet_id, 'content': snippet.code, 'tags': snippet.tags, 'language': snippet.language, 'user_name': snippet.user_name}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to create snippet: ' + str(e)}), 500

@app.route('/snippets/<snippet_id>', methods=['GET'])
@with_db_connection
def get_snippet(conn, snippet_id):
    snippet = db_get_snippet_by_id(conn, snippet_id)
    if snippet:
        return jsonify({'id': snippet.id, 'content': snippet.code, 'tags': snippet.tags, 'language': snippet.language, 'user_name': snippet.user_name})
    else:
        return jsonify({'error': 'Snippet not found'}), 404

@app.route('/snippets/<snippet_id>', methods=['PUT'])
@with_db_connection
def update_snippet(conn, snippet_id):
    snippet = db_get_snippet_by_id(conn, snippet_id)
    if snippet:
        snippet.code = request.json.get('content', snippet.code)
        snippet.tags = request.json.get('tags', snippet.tags)
        snippet.language = request.json.get('language', snippet.language)
        snippet.user_name = request.json.get('user_name', snippet.user_name)
        db_update_snippet(conn, snippet)
        return jsonify({'id': snippet.id, 'content': snippet.code, 'tags': snippet.tags, 'language': snippet.language, 'user_name': snippet.user_name})
    else:
        return jsonify({'error': 'Snippet not found'}), 404

@app.route('/snippets/<snippet_id>', methods=['DELETE'])
@with_db_connection
def delete_snippet(conn, snippet_id):
    db_delete_snippet(conn, snippet_id)
    return jsonify({'message': 'Snippet deleted'}), 200

@app.route('/snippets', methods=['GET'])
@with_db_connection
def search_snippets(conn):
    user_name = request.args.get('user')
    tag = request.args.get('tag')
    language = request.args.get('language')
    snippets = db_filter_snippets(conn, user_name=user_name, tag=tag, language=language)
    return jsonify([{'id': snippet.id, 'content': snippet.code, 'tags': snippet.tags, 'language': snippet.language, 'user_name': snippet.user_name} for snippet in snippets])

# Comment routes
@app.route('/comments/<snippet_id>', methods=['POST'])
@with_db_connection
def add_comment(conn, snippet_id):
    try:
        comment = Comment(
            id=None,
            snippet_id=snippet_id,
            user_name=request.json.get('user_name'),
            content=request.json.get('content'),
            created_at=request.json.get('created_at')
        )
        comment_id = db_insert_comment(conn, comment)
        return jsonify({'id': comment_id, 'snippet_id': comment.snippet_id, 'user_name': comment.user_name, 'content': comment.content, 'created_at': comment.created_at}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to add comment: ' + str(e)}), 500

@app.route('/comments/<snippet_id>', methods=['GET'])
@with_db_connection
def get_comments(conn, snippet_id):
    comments = db_get_comments_by_snippet_id(conn, snippet_id)
    return jsonify([{'id': comment.id, 'snippet_id': comment.snippet_id, 'user_name': comment.user_name, 'content': comment.content, 'created_at': comment.created_at} for comment in comments])

@app.route('/comments', methods=['GET'])
@with_db_connection
def get_all_comments(conn):
    comments = db_get_all_comments(conn)
    return jsonify([{'id': comment.id, 'snippet_id': comment.snippet_id, 'user_name': comment.user_name, 'content': comment.content, 'created_at': comment.created_at} for comment in comments])

# Project routes
@app.route('/projects', methods=['POST'])
@with_db_connection
def create_project(conn):
    try:
        project = Project(
            id=None,
            name=request.json.get('name'),
            description=request.json.get('description')
        )
        project_id = db_insert_project(conn, project)
        return jsonify({'id': project_id, 'name': project.name, 'description': project.description}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to create project: ' + str(e)}), 500

@app.route('/projects/<project_id>', methods=['PUT'])
@with_db_connection
def update_project(conn, project_id):
    project = Project(
        id=project_id,
        name=request.json.get('name'),
        description=request.json.get('description')
    )
    db_update_project(conn, project)
    return jsonify({'id': project.id, 'name': project.name, 'description': project.description})

@app.route('/projects/<project_id>', methods=['GET'])
@with_db_connection
def get_project(conn, project_id):
    project = db_get_project_by_id(conn, project_id)
    if project:
        return jsonify({'id': project.id, 'name': project.name, 'description': project.description})
    else:
        return jsonify({'error': 'Project not found'}), 404

@app.route('/projects', methods=['GET'])
@with_db_connection
def get_all_projects(conn):
    projects = db_get_all_projects(conn)
    return jsonify([{'id': project.id, 'name': project.name, 'description': project.description} for project in projects])

@app.route('/projects/<project_id>/members', methods=['POST'])
@with_db_connection
def add_project_member(conn, project_id):
    try:
        project_member = UserProject(
            user_name=request.json.get('user_name'),
            project_id=project_id
        )
        db_insert_user_project(conn, project_member)
        return jsonify({'project_id': project_id, 'user_name': project_member.user_name}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to add project member: ' + str(e)}), 500

@app.route('/projects/<project_id>/members', methods=['GET'])
@with_db_connection
def get_project_members(conn, project_id):
    project_members = db_get_user_projects_by_project_id(conn, project_id)
    return jsonify([{'user_name': member.user_name, 'project_id': member.project_id} for member in project_members])

@app.route('/clear_db', methods=['DELETE'])
@with_db_connection
def clear_db(conn):
    """
    Clear the database by deleting all records from the users, snippets, comments, and projects tables.

    Returns:
        response (flask.Response): A JSON response indicating the success of the operation.
    """
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users")
        cursor.execute("DELETE FROM snippets")
        cursor.execute("DELETE FROM comments")
        cursor.execute("DELETE FROM projects")
        conn.commit()
        return jsonify({'message': 'Database cleared'}), 200
    except Exception as e:
        return jsonify({'error': 'Failed to clear database: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)