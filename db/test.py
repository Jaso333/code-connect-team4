from db import User, db_connect, db_insert_user

def test_db_insert_user():
    conn = db_connect()
    try:
        user = User("foo_bar", "foo@bar.com", "password123", "Foo", "Bar", "Bio of Foo", "Python,SQL")
        db_insert_user(conn, user)
    finally:
        conn.close()

test_db_insert_user()