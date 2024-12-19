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

# Example usage:
# conn = psycopg2.connect("dbname=test user=postgres password=secret")
# user = User('john_doe', 'john@example.com', 'securepassword', 'John', 'Doe', 'Bio of John', 'Python,SQL')
# insert_user(conn, user)
# conn.close()