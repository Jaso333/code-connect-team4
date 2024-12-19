from db import User, db_connect, db_insert_user, db_update_user, db_delete_user

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

test_db_delete_user()
