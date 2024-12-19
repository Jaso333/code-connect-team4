import psycopg2
from psycopg2 import sql

class User:
    def __init__(self, username, email, password, first_name, surname, bio, skills):
        self.username = username
        self.email = email
        self.password = password
        self.first_name = first_name
        self.surname = surname
        self.bio = bio
        self.skills = skills

def db_connect():
    return psycopg2.connect(database="team4",
        host="ghcpchmgmt.postgres.database.azure.com",
        user="team4",
        password="MNb6hG$f5",
        port="5432")

def db_insert_user(conn, user):
    try:
        with conn.cursor() as cursor:
            insert_query = sql.SQL("""
                INSERT INTO users (username, email, password, first_name, surname, bio, skills)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """)
            cursor.execute(insert_query, (user.username, user.email, user.password, user.first_name, user.surname, user.bio, user.skills))
            conn.commit()
            print("User inserted successfully")
    except Exception as e:
        print(f"Error inserting user: {e}")
        conn.rollback()

def db_update_user(conn, user):
    try:
        with conn.cursor() as cursor:
            update_query = sql.SQL("""
                UPDATE users
                SET email = %s, password = %s, first_name = %s, surname = %s, bio = %s, skills = %s
                WHERE username = %s
            """)
            cursor.execute(update_query, (user.email, user.password, user.first_name, user.surname, user.bio, user.skills, user.username))
            conn.commit()
            print("User updated successfully")
    except Exception as e:
        print(f"Error updating user: {e}")
        conn.rollback()

def db_delete_user(conn, username):
    try:
        with conn.cursor() as cursor:
            delete_query = sql.SQL("""
                DELETE FROM users
                WHERE username = %s
            """)
            cursor.execute(delete_query, (username,))
            conn.commit()
            print("User deleted successfully")
    except Exception as e:
        print(f"Error deleting user: {e}")
        conn.rollback()

