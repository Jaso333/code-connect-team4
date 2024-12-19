import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.db import db_connect, db_insert_user, db_insert_snippet, db_insert_comment, db_insert_project, db_insert_user_project, User, Comment, Snippet, Project, UserProject
import datetime

def generate_test_data():
    conn = db_connect()

    # Create users
    users = [
        User('johndoe', 'john@example.com', 'password123', 'John', 'Doe', 'A software developer with 10 years of experience.', ['Python', 'Flask', 'JavaScript']),
        User('janedoe', 'jane@example.com', 'password123', 'Jane', 'Doe', 'A front-end developer.', ['HTML', 'CSS', 'JavaScript']),
    ]
    for user in users:
        db_insert_user(conn, user)

    # Create snippets
    snippets = [
        Snippet(None, 'print("Hello, World!")', ['example', 'hello world'], 'Python', 'johndoe'),
        Snippet(None, '<h1>Hello, World!</h1>', ['example', 'hello world'], 'HTML', 'janedoe'),
    ]
    for snippet in snippets:
        db_insert_snippet(conn, snippet)

    # Create comments
    comments = [
        Comment(None, 1, 'janedoe', 'Great snippet!', datetime.datetime.now()),
        Comment(None, 2, 'johndoe', 'Nice HTML example!', datetime.datetime.now()),
    ]
    for comment in comments:
        db_insert_comment(conn, comment)

    # Create projects
    projects = [
        Project(None, 'Project One', 'A sample project'),
        Project(None, 'Project Two', 'Another sample project'),
    ]
    for project in projects:
        db_insert_project(conn, project)

    # Create project members
    project_members = [
        UserProject('johndoe', 1),
        UserProject('janedoe', 1),
        UserProject('johndoe', 2),
    ]
    for project_member in project_members:
        db_insert_user_project(conn, project_member)

    conn.close()

if __name__ == "__main__":
    generate_test_data()
    print("Test data generated successfully.")