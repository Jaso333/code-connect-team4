from db import User, Snippet, Comment, Project, UserProject, \
    db_connect, db_insert_user, db_update_user, db_delete_user, db_get_user_by_username, \
    db_insert_snippet, db_update_snippet, db_delete_snippet, \
    db_insert_comment, db_update_comment, db_delete_comment, db_get_comments_by_snippet_id, \
    db_insert_project, db_update_project, db_delete_project, \
    db_insert_user_project, db_delete_user_project, db_get_user_projects_by_project_id

def test_db_insert_user():
    conn = db_connect()
    try:
        user = User("foo_bar", "foo@bar.com", "password123", "Foo", "Bar", "Bio of Foo", "Python,SQL")
        db_insert_user(conn, user)
    finally:
        conn.close()

def test_db_update_user():
    conn = db_connect()
    try:
        user = User("foo_bar", "foo_updated@bar.com", "newpassword123", "FooUpdated", "BarUpdated", "Updated Bio of Foo", "Python,SQL,Java")
        db_update_user(conn, user)
    finally:
        conn.close()

def test_db_delete_user():
    conn = db_connect()
    try:
        db_delete_user(conn, "foo_bar")
    finally:
        conn.close()

def test_db_get_user_by_username():
    conn = db_connect()
    try:
        user = db_get_user_by_username(conn, "foo_bar")
        if user:
            print(f"Test passed: User found - {user.username}, {user.email}")
        else:
            print("Test failed: User not found")
    finally:
        conn.close()

def test_db_insert_snippet():
    conn = db_connect()
    snippet = Snippet(None, "print('Hello, World!')", "example,hello", "python", "test_user")
    snippet_id = db_insert_snippet(conn, snippet)
    if snippet_id:
        print(f"Test passed: Snippet inserted with ID {snippet_id}")
    else:
        print("Test failed: Snippet insertion failed")
    conn.close()

def test_db_update_snippet():
    conn = db_connect()
    try:
        snippet = Snippet(1, "print('Hello, Updated World!')", "example,hello,updated", "python", "test_user")
        db_update_snippet(conn, snippet)
    finally:
        conn.close()

def test_db_delete_snippet():
    conn = db_connect()
    try:
        db_delete_snippet(conn, 1)
    finally:
        conn.close()

def test_db_insert_comment():
    conn = db_connect()
    try:
        comment = Comment(None, 2, "test_user", "This is a test comment", "2023-10-10 10:00:00")
        comment_id = db_insert_comment(conn, comment)
        if comment_id:
            print(f"Test passed: Comment inserted with ID {comment_id}")
        else:
            print("Test failed: Comment insertion failed")
    finally:
        conn.close()

def test_db_update_comment():
    conn = db_connect()
    try:
        comment = Comment(1, 2, "test_user", "This is an updated test comment", "2023-10-10 11:00:00")
        db_update_comment(conn, comment)
    finally:
        conn.close()

def test_db_delete_comment():
    conn = db_connect()
    try:
        db_delete_comment(conn, 1)
    finally:
        conn.close()

def test_db_get_comments_by_snippet_id():
    conn = db_connect()
    try:
        comments = db_get_comments_by_snippet_id(conn, 2)
        if comments:
            print(f"Test passed: {len(comments)} comments found")
            for comment in comments:
                print(f"Comment ID: {comment.id}, Content: {comment.content}")
        else:
            print("Test failed: No comments found")
    finally:
        conn.close()

def test_db_insert_project():
    conn = db_connect()
    try:
        project = Project(None, "Test Project", "This is a test project")
        project_id = db_insert_project(conn, project)
        if project_id:
            print(f"Test passed: Project inserted with ID {project_id}")
        else:
            print("Test failed: Project insertion failed")
    finally:
        conn.close()

def test_db_update_project():
    conn = db_connect()
    try:
        project = Project(1, "Updated Test Project", "This is an updated test project")
        db_update_project(conn, project)
    finally:
        conn.close()

def test_db_delete_project():
    conn = db_connect()
    try:
        db_delete_project(conn, 1)
    finally:
        conn.close()

def test_db_insert_user_project():
    conn = db_connect()
    try:
        user_project = UserProject("foo_bar", 1)
        db_insert_user_project(conn, user_project)
    finally:
        conn.close()

def test_db_delete_user_project():
    conn = db_connect()
    try:
        db_delete_user_project(conn, "foo_bar", 1)
    finally:
        conn.close()

def test_db_get_user_projects_by_project_id():
    conn = db_connect()
    try:
        user_projects = db_get_user_projects_by_project_id(conn, 1)
        if user_projects:
            print(f"Test passed: {len(user_projects)} user projects found")
            for user_project in user_projects:
                print(f"User: {user_project.user_name}, Project ID: {user_project.project_id}")
        else:
            print("Test failed: No user projects found")
    finally:
        conn.close()