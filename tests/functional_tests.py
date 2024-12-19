import os
import pytest
import requests

# Set the base URL for the API from an environment variable, defaulting to 'http://localhost:5000' if not set
BASE_URL = os.getenv('BASE_URL', 'http://localhost:5000')

@pytest.fixture(scope='module')
def create_user():
    """
    Fixture to create a user for testing.

    Sends a POST request to create a user with predefined data.

    Returns:
        response (requests.Response): The response object from the POST request.
    """
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
    """
    Test creating a user.

    Asserts that the user creation response has a status code of 201 and the user's name is 'John Doe'.
    """
    assert create_user.status_code == 201
    assert create_user.json()['name'] == 'John Doe'

def test_get_all_users():
    """
    Test getting all users.

    Sends a GET request to retrieve all users and asserts the response status code is 200 and the response is a dictionary.
    """
    response = requests.get(f'{BASE_URL}/users')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_user():
    """
    Test getting a specific user.

    Sends a GET request to retrieve a user by ID and asserts the response status code is 200 and the user's name is 'John Doe'.
    """
    response = requests.get(f'{BASE_URL}/users/1')
    assert response.status_code == 200
    assert response.json()['name'] == 'John Doe'

def test_update_user():
    """
    Test updating a user.

    Sends a PUT request to update a user's name and asserts the response status code is 200 and the updated name is 'Jane Doe'.
    """
    response = requests.put(f'{BASE_URL}/users/1', json={'name': 'Jane Doe'})
    assert response.status_code == 200
    assert response.json()['name'] == 'Jane Doe'

def test_create_snippet():
    """
    Test creating a snippet.

    Sends a POST request to create a code snippet and asserts the response status code is 201 and the snippet content is 'print("Hello, World!")'.
    """
    response = requests.post(f'{BASE_URL}/snippets', json={
        'id': 'snippet1',
        'content': 'print("Hello, World!")',
        'language': 'Python',
        'tags': ['example', 'hello world']
    })
    assert response.status_code == 201
    assert response.json()['content'] == 'print("Hello, World!")'

def test_get_snippet():
    """
    Test getting a specific snippet.

    Sends a GET request to retrieve a snippet by ID and asserts the response status code is 200 and the snippet content is 'print("Hello, World!")'.
    """
    response = requests.get(f'{BASE_URL}/snippets/snippet1')
    assert response.status_code == 200
    assert response.json()['content'] == 'print("Hello, World!")'

def test_update_snippet():
    """
    Test updating a snippet.

    Sends a PUT request to update a snippet's content and asserts the response status code is 200 and the updated content is 'print("Hello, Flask!")'.
    """
    response = requests.put(f'{BASE_URL}/snippets/snippet1', json={'content': 'print("Hello, Flask!")'})
    assert response.status_code == 200
    assert response.json()['content'] == 'print("Hello, Flask!")'

def test_delete_snippet():
    """
    Test deleting a snippet.

    Sends a DELETE request to delete a snippet by ID and asserts the response status code is 200 and the response message is 'Snippet deleted'.
    """
    response = requests.delete(f'{BASE_URL}/snippets/snippet1')
    assert response.status_code == 200
    assert response.json()['message'] == 'Snippet deleted'

def test_search_snippets():
    """
    Test searching for snippets.

    Sends a GET request to search for snippets by language and asserts the response status code is 200 and the response is a list.
    """
    response = requests.get(f'{BASE_URL}/snippets?language=Python')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_comment():
    """
    Test adding a comment to a snippet.

    Sends a POST request to add a comment to a snippet and asserts the response status code is 201 and the comment content is 'Great snippet!'.
    """
    response = requests.post(f'{BASE_URL}/comments/snippet1', json={
        'id': 'comment1',
        'content': 'Great snippet!'
    })
    assert response.status_code == 201
    assert response.json()['content'] == 'Great snippet!'

def test_get_comments():
    """
    Test getting comments for a snippet.

    Sends a GET request to retrieve comments for a snippet and asserts the response status code is 200 and the response is a list.
    """
    response = requests.get(f'{BASE_URL}/comments/snippet1')
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_project():
    """
    Test creating a project.

    Sends a POST request to create a project and asserts the response status code is 201 and the project's name is 'Project One'.
    """
    response = requests.post(f'{BASE_URL}/projects', json={
        'id': 'project1',
        'name': 'Project One',
        'description': 'A sample project'
    })
    assert response.status_code == 201
    assert response.json()['name'] == 'Project One'

def test_get_project():
    """
    Test getting a specific project.

    Sends a GET request to retrieve a project by ID and asserts the response status code is 200 and the project's name is 'Project One'.
    """
    response = requests.get(f'{BASE_URL}/projects/project1')
    assert response.status_code == 200
    assert response.json()['name'] == 'Project One'

def test_update_project():
    """
    Test updating a project.

    Sends a PUT request to update a project's name and asserts the response status code is 200 and the updated name is 'Updated Project One'.
    """
    response = requests.put(f'{BASE_URL}/projects/project1', json={'name': 'Updated Project One'})
    assert response.status_code == 200
    assert response.json()['name'] == 'Updated Project One'

def test_add_project_member():
    """
    Test adding a member to a project.

    Sends a POST request to add a member to a project and asserts the response status code is 201 and the member ID is in the project's members list.
    """
    response = requests.post(f'{BASE_URL}/projects/project1/members', json={'id': 'member1'})
    assert response.status_code == 201
    assert 'member1' in response.json()['members']

# clear the database after running the tests
def test_clear_db():
    response = requests.delete(f'{BASE_URL}/clear_db')
    assert response.status_code == 200
    assert response.json()['message'] == 'Database cleared'