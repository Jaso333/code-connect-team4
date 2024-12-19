import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_user(client):
    response = client.post('/users', json={
        'id': 1,
        'name': 'John Doe',
        'bio': 'A software developer with 10 years of experience.',
        'skills': ['Python', 'Flask', 'JavaScript'],
        'profile_picture': 'http://example.com/profile.jpg',
        'github_gitlab': 'http://github.com/johndoe'
    })
    assert response.status_code == 201
    assert response.json['name'] == 'John Doe'

def test_get_all_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, dict)

def test_get_user(client):
    response = client.get('/users/1')
    assert response.status_code == 200
    assert response.json['name'] == 'John Doe'

def test_update_user(client):
    response = client.put('/users/1', json={'name': 'Jane Doe'})
    assert response.status_code == 200
    assert response.json['name'] == 'Jane Doe'

def test_create_snippet(client):
    response = client.post('/snippets', json={
        'id': 'snippet1',
        'content': 'print("Hello, World!")',
        'language': 'Python',
        'tags': ['example', 'hello world']
    })
    assert response.status_code == 201
    assert response.json['content'] == 'print("Hello, World!")'

def test_get_snippet(client):
    response = client.get('/snippets/snippet1')
    assert response.status_code == 200
    assert response.json['content'] == 'print("Hello, World!")'

def test_update_snippet(client):
    response = client.put('/snippets/snippet1', json={'content': 'print("Hello, Flask!")'})
    assert response.status_code == 200
    assert response.json['content'] == 'print("Hello, Flask!")'

def test_delete_snippet(client):
    response = client.delete('/snippets/snippet1')
    assert response.status_code == 200
    assert response.json['message'] == 'Snippet deleted'

def test_search_snippets(client):
    response = client.get('/snippets?language=Python')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_comment(client):
    response = client.post('/comments/snippet1', json={
        'id': 'comment1',
        'content': 'Great snippet!'
    })
    assert response.status_code == 201
    assert response.json['content'] == 'Great snippet!'

def test_get_comments(client):
    response = client.get('/comments/snippet1')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_create_project(client):
    response = client.post('/projects', json={
        'id': 'project1',
        'name': 'Project One',
        'description': 'A sample project'
    })
    assert response.status_code == 201
    assert response.json['name'] == 'Project One'

def test_get_project(client):
    response = client.get('/projects/project1')
    assert response.status_code == 200
    assert response.json['name'] == 'Project One'

def test_update_project(client):
    response = client.put('/projects/project1', json={'name': 'Updated Project One'})
    assert response.status_code == 200
    assert response.json['name'] == 'Updated Project One'

def test_add_project_member(client):
    response = client.post('/projects/project1/members', json={'id': 'member1'})
    assert response.status_code == 201
    assert 'member1' in response.json['members']