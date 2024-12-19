import requests

BASE_URL = 'http://localhost:5000'

def test_create_user():
    response = requests.post(f'{BASE_URL}/users', json={
        'id': 1,
        'name': 'John Doe',
        'bio': 'A software developer with 10 years of experience.',
        'skills': ['Python', 'Flask', 'JavaScript'],
        'profile_picture': 'http://example.com/profile.jpg',
        'github_gitlab': 'http://github.com/johndoe'
    })
    assert response.status_code == 201
    assert response.json()['name'] == 'John Doe'
    print('Create User: Passed')

def test_get_all_users():
    response = requests.get(f'{BASE_URL}/users')
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    print('Get All Users: Passed')

def test_get_user():
    response = requests.get(f'{BASE_URL}/users/1')
    assert response.status_code == 200
    assert response.json()['name'] == 'John Doe'
    print('Get User: Passed')

def test_update_user():
    response = requests.put(f'{BASE_URL}/users/1', json={'name': 'Jane Doe'})
    assert response.status_code == 200
    assert response.json()['name'] == 'Jane Doe'
    print('Update User: Passed')

def test_create_snippet():
    response = requests.post(f'{BASE_URL}/snippets', json={
        'id': 'snippet1',
        'content': 'print("Hello, World!")',
        'language': 'Python',
        'tags': ['example', 'hello world']
    })
    assert response.status_code == 201
    assert response.json()['content'] == 'print("Hello, World!")'
    print('Create Snippet: Passed')

def test_get_snippet():
    response = requests.get(f'{BASE_URL}/snippets/snippet1')
    assert response.status_code == 200
    assert response.json()['content'] == 'print("Hello, World!")'
    print('Get Snippet: Passed')

def test_update_snippet():
    response = requests.put(f'{BASE_URL}/snippets/snippet1', json={'content': 'print("Hello, Flask!")'})
    assert response.status_code == 200
    assert response.json()['content'] == 'print("Hello, Flask!")'
    print('Update Snippet: Passed')

def test_delete_snippet():
    response = requests.delete(f'{BASE_URL}/snippets/snippet1')
    assert response.status_code == 200
    assert response.json()['message'] == 'Snippet deleted'
    print('Delete Snippet: Passed')

def test_search_snippets():
    response = requests.get(f'{BASE_URL}/snippets?language=Python')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    print('Search Snippets: Passed')

def test_add_comment():
    response = requests.post(f'{BASE_URL}/comments/snippet1', json={
        'id': 'comment1',
        'content': 'Great snippet!'
    })
    assert response.status_code == 201
    assert response.json()['content'] == 'Great snippet!'
    print('Add Comment: Passed')

def test_get_comments():
    response = requests.get(f'{BASE_URL}/comments/snippet1')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    print('Get Comments: Passed')

def test_create_project():
    response = requests.post(f'{BASE_URL}/projects', json={
        'id': 'project1',
        'name': 'Project One',
        'description': 'A sample project'
    })
    assert response.status_code == 201
    assert response.json()['name'] == 'Project One'
    print('Create Project: Passed')

def test_get_project():
    response = requests.get(f'{BASE_URL}/projects/project1')
    assert response.status_code == 200
    assert response.json()['name'] == 'Project One'
    print('Get Project: Passed')

def test_update_project():
    response = requests.put(f'{BASE_URL}/projects/project1', json={'name': 'Updated Project One'})
    assert response.status_code == 200
    assert response.json()['name'] == 'Updated Project One'
    print('Update Project: Passed')

def test_add_project_member():
    response = requests.post(f'{BASE_URL}/projects/project1/members', json={'id': 'member1'})
    assert response.status_code == 201
    assert 'member1' in response.json()['members']
    print('Add Project Member: Passed')

if __name__ == '__main__':
    test_create_user()
    test_get_all_users()
    test_get_user()
    test_update_user()
    test_create_snippet()
    test_get_snippet()
    test_update_snippet()
    test_delete_snippet()
    test_search_snippets()
    test_add_comment()
    test_get_comments()
    test_create_project()
    test_get_project()
    test_update_project()
    test_add_project_member()