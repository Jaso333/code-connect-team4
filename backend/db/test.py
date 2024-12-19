from db import User, Snippet, Comment, \
    db_connect, db_insert_user, db_update_user, db_delete_user, db_get_user_by_username, \
    db_insert_snippet, db_update_snippet, db_delete_snippet, \
    db_insert_comment

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