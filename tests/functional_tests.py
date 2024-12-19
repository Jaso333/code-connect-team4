import os
import pytest
import requests

BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')

@pytest.fixture(scope='module')
def create_user():
    """Create a user for testing"""
    response = requests.post(f'{BASE_URL}/users', json={
        'id': 1,
        'name': 'John Doe',
        'bio': 'A software developer with 10 years of experience.',
        'skills': ['Python', 'Flask', 'JavaScript'],
        'profile_picture': 'http://example.com/profile.jpg',
        'github_gitlab': 'http://github.com/johndoe'
    })
    return response

def test_create_user(create_user):
    """Test creating a user"""
    assert create_user.status_code == 201
    assert create_user.json()['name'] == 'John Doe'

def test_get_all_users():
    """Test getting all users"""
    response = requests.get(f'{BASE_URL}/users')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_user():
    """Test getting a user"""
    response = requests.get(f'{BASE_URL}/users/1')
    assert response.status_code == 200
    assert response.json()['name'] == 'John Doe'

def test_update_user():
    """Test updating a user"""
    response = requests.put(f'{BASE_URL}/users/1', json={'name': 'Jane Doe'})
    assert response.status_code == 200
    assert response.json()['name'] == 'Jane Doe'

def test_create_snippet():
    """Test creating a snippet"""
    response = requests.post(f'{BASE_URL}/snippets', json={
        'id': 'snippet1',
        'content': 'print("Hello, World!")',
        'language': 'Python',
        'tags': ['example', 'hello world']
    })
    assert response.status_code == 201
    assert response.json()['content'] == 'print("Hello, World!")'

def test_get_snippet():
    """Test getting a snippet"""
    response = requests.get(f'{BASE_URL}/snippets/snippet1')
    assert response.status_code == 200
    assert response.json()['content'] == 'print("Hello, World!")'

def test_update_snippet():
    """Test updating a snippet"""
    response = requests.put(f'{BASE_URL}/snippets/snippet1', json={'content': 'print("Hello, Flask!")'})
    assert response.status_code == 200
    assert response.json()['content'] == 'print("Hello, Flask!")'

def test_delete_snippet():
    """Test deleting a snippet"""
    response = requests.delete(f'{BASE_URL}/snippets/snippet1')
    assert response.status_code == 200
    assert response.json()['message'] == 'Snippet deleted'

def test_search_snippets():
    """Test searching for snippets"""
    response = requests.get(f'{BASE_URL}/snippets?language=Python')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_comment():
    """Test adding a comment to a snippet"""
    response = requests.post(f'{BASE_URL}/comments/snippet1', json={
        'id': 'comment1',
        'content': 'Great snippet!'
    })
    assert response.status_code == 201
    assert response.json()['content'] == 'Great snippet!'

def test_get_comments():
    """Test getting comments for a snippet"""
    response = requests.get(f'{BASE_URL}/comments/snippet1')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_project():
    """Test creating a project"""
    response = requests.post(f'{BASE_URL}/projects', json={
        'id': 'project1',
        'name': 'Project One',
        'description': 'A sample project'
    })
    assert response.status_code == 201
    assert response.json()['name'] == 'Project One'

def test_get_project():
    """Test getting a project"""
    response = requests.get(f'{BASE_URL}/projects/project1')
    assert response.status_code == 200
    assert response.json()['name'] == 'Project One'

def test_update_project():
    """Test updating a project"""
    response = requests.put(f'{BASE_URL}/projects/project1', json={'name': 'Updated Project One'})
    assert response.status_code == 200
    assert response.json()['name'] == 'Updated Project One'

def test_add_project_member():
    """Test adding a member to a project"""
    response = requests.post(f'{BASE_URL}/projects/project1/members', json={'id': 'member1'})
    assert response.status_code == 201
    assert 'member1' in response.json()['members']