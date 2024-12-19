import pytest
from app import app
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import db_connect, db_insert_user, db_update_user, db_delete_user, db_get_user_by_username, db_insert_snippet, db_update_snippet, db_delete_snippet, db_get_snippet_by_id, db_filter_snippets, db_insert_comment, User, Comment, Snippet

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# @pytest.fixture(autouse=True)
# def run_around_tests():
#     # Setup: connect to the database and clear the tables
#     conn = db_connect()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM users")
#     cursor.execute("DELETE FROM projects")
#     conn.commit()
#     yield
#     # Teardown: close the database connection
#     conn.close()

def test_create_user(client):
    response = client.post('/users', json={
        'username': 'johndoe',
        'email': 'john@example.com',
        'password': 'password123',
        'first_name': 'John',
        'surname': 'Doe',
        'bio': 'A software developer with 10 years of experience.',
        'skills': ['Python', 'Flask', 'JavaScript']
    })
    assert response.status_code == 201
    assert response.json['username'] == 'johndoe'

def test_get_all_users(client):
    conn = db_connect()
    user = User('johndoe', 'john@example.com', 'password123', 'John', 'Doe', 'A software developer with 10 years of experience.', ['Python', 'Flask', 'JavaScript'])
    db_insert_user(conn, user)
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    # assert response.json[0]['username'] == 'foo_bar'

def test_get_user(client):
    conn = db_connect()
    user = User('johndoe', 'john@example.com', 'password123', 'John', 'Doe', 'A software developer with 10 years of experience.', ['Python', 'Flask', 'JavaScript'])
    db_insert_user(conn, user)
    response = client.get('/users/johndoe')
    assert response.status_code == 200
    assert response.json['username'] == 'johndoe'

def test_update_user(client):
    conn = db_connect()
    user = User('johndoe', 'john@example.com', 'password123', 'John', 'Doe', 'A software developer with 10 years of experience.', ['Python', 'Flask', 'JavaScript'])
    db_insert_user(conn, user)
    response = client.put('/users/johndoe', json={'email': 'john.doe@example.com'})
    assert response.status_code == 200
    assert response.json['email'] == 'john.doe@example.com'

def test_delete_user(client):
    conn = db_connect()
    user = User('johndoe', 'john@example.com', 'password123', 'John', 'Doe', 'A software developer with 10 years of experience.', ['Python', 'Flask', 'JavaScript'])
    db_insert_user(conn, user)
    response = client.delete('/users/johndoe')
    assert response.status_code == 200
    assert response.json['message'] == 'User deleted'

def test_create_snippet(client):
    conn = db_connect()
    snippet = Snippet(None, 'print("Hello, World!")', ['example', 'hello world'], 'Python', 'johndoe')
    db_insert_snippet(conn, snippet)
    response = client.post('/snippets', json={
        'content': 'print("Hello, World!")',
        'language': 'Python',
        'tags': ['example', 'hello world'],
        'user_name': 'johndoe'
    })
    assert response.status_code == 201
    assert response.json['content'] == 'print("Hello, World!")'

def test_get_snippet(client):
    conn = db_connect()
    snippet = Snippet(None, 'print("Hello, World!")', ['example', 'hello world'], 'Python', 'johndoe')
    snippet_id = db_insert_snippet(conn, snippet)
    response = client.get(f'/snippets/{snippet_id}')
    assert response.status_code == 200
    assert response.json['content'] == 'print("Hello, World!")'

def test_update_snippet(client):
    conn = db_connect()
    snippet = Snippet(None, 'print("Hello, World!")', ['example', 'hello world'], 'Python', 'johndoe')
    snippet_id = db_insert_snippet(conn, snippet)
    response = client.put(f'/snippets/{snippet_id}', json={'content': 'print("Hello, Flask!")'})
    assert response.status_code == 200
    assert response.json['content'] == 'print("Hello, Flask!")'

def test_delete_snippet(client):
    conn = db_connect()
    snippet = Snippet(None, 'print("Hello, World!")', ['example', 'hello world'], 'Python', 'johndoe')
    snippet_id = db_insert_snippet(conn, snippet)
    response = client.delete(f'/snippets/{snippet_id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Snippet deleted'

def test_search_snippets(client):
    conn = db_connect()
    snippet = Snippet(None, 'print("Hello, World!")', ['example', 'hello world'], 'Python', 'johndoe')
    db_insert_snippet(conn, snippet)
    response = client.get('/snippets?language=Python')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_comment(client):
    conn = db_connect()
    snippet = Snippet(None, 'print("Hello, World!")', ['example', 'hello world'], 'Python', 'johndoe')
    snippet_id = db_insert_snippet(conn, snippet)
    response = client.post(f'/comments/{snippet_id}', json={
        'user_name': 'janedoe',
        'content': 'Great snippet!',
        'created_at': '2023-10-10T10:00:00'
    })
    assert response.status_code == 201
    assert response.json['content'] == 'Great snippet!'

def test_get_comments(client):
    conn = db_connect()
    snippet = Snippet(None, 'print("Hello, World!")', ['example', 'hello world'], 'Python', 'johndoe')
    snippet_id = db_insert_snippet(conn, snippet)
    comment = Comment(None, snippet_id, 'janedoe', 'Great snippet!', '2023-10-10T10:00:00')
    db_insert_comment(conn, comment)
    response = client.get(f'/comments/{snippet_id}')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# def test_create_project(client):
#     response = client.post('/projects', json={
#         'id': 'project1',
#         'name': 'Project One',
#         'description': 'A sample project'
#     })
#     assert response.status_code == 201
#     assert response.json['name'] == 'Project One'

# def test_get_project(client):
#     conn = db_connect()
#     project = Project('project1', 'Project One', 'A sample project')
#     db_insert_project(conn, project)
#     response = client.get('/projects/project1')
#     assert response.status_code == 200
#     assert response.json['name'] == 'Project One'

# def test_update_project(client):
#     conn = db_connect()
#     project = Project('project1', 'Project One', 'A sample project')
#     db_insert_project(conn, project)
#     response = client.put('/projects/project1', json={'name': 'Updated Project One'})
#     assert response.status_code == 200
#     assert response.json['name'] == 'Updated Project One'

# def test_add_project_member(client):
#     conn = db_connect()
#     project = Project('project1', 'Project One', 'A sample project')
#     db_insert_project(conn, project)
#     response = client.post('/projects/project1/members', json={'id': 'member1'})
#     assert response.status_code == 201
#     assert 'member1' in response.json['user_id']