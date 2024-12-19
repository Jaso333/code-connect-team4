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

class Snippet:
    def __init__(self, id, code, tags, language, user_name):
        self.id = id
        self.code = code
        self.tags = tags
        self.language = language
        self.user_name = user_name

class Comment:
    def __init__(self, id, snippet_id, user_name, content, created_at):
        self.id = id
        self.snippet_id = snippet_id
        self.user_name = user_name
        self.content = content
        self.created_at = created_at

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

def db_get_user_by_username(conn, username):
    try:
        with conn.cursor() as cursor:
            select_query = sql.SQL("""
                SELECT username, email, password, first_name, surname, bio, skills
                FROM users
                WHERE username = %s
            """)
            cursor.execute(select_query, (username,))
            user_data = cursor.fetchone()
            if user_data:
                user = User(*user_data)
                return user
            else:
                print("User not found")
                return None
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None

def db_insert_snippet(conn, snippet):
    try:
        with conn.cursor() as cursor:
            insert_query = sql.SQL("""
                INSERT INTO snippets (code, tags, language, user_name)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """)
            cursor.execute(insert_query, (snippet.code, snippet.tags, snippet.language, snippet.user_name))
            snippet_id = cursor.fetchone()[0]
            conn.commit()
            print(f"Snippet inserted successfully with ID: {snippet_id}")
            return snippet_id
    except Exception as e:
        print(f"Error inserting snippet: {e}")
        conn.rollback()
        return None

def db_update_snippet(conn, snippet):
    try:
        with conn.cursor() as cursor:
            update_query = sql.SQL("""
                UPDATE snippets
                SET code = %s, tags = %s, language = %s, user_name = %s
                WHERE id = %s
            """)
            cursor.execute(update_query, (snippet.code, snippet.tags, snippet.language, snippet.user_name, snippet.id))
            conn.commit()
            print("Snippet updated successfully")
    except Exception as e:
        print(f"Error updating snippet: {e}")
        conn.rollback()

def db_delete_snippet(conn, snippet_id):
    try:
        with conn.cursor() as cursor:
            delete_query = sql.SQL("""
                DELETE FROM snippets
                WHERE id = %s
            """)
            cursor.execute(delete_query, (snippet_id,))
            conn.commit()
            print("Snippet deleted successfully")
    except Exception as e:
        print(f"Error deleting snippet: {e}")
        conn.rollback()

def db_get_snippet_by_id(conn, snippet_id):
    try:
        with conn.cursor() as cursor:
            select_query = sql.SQL("""
                SELECT id, code, tags, language, user_name
                FROM snippets
                WHERE id = %s
            """)
            cursor.execute(select_query, (snippet_id,))
            snippet_data = cursor.fetchone()
            if snippet_data:
                snippet = Snippet(*snippet_data)
                return snippet
            else:
                print("Snippet not found")
                return None
    except Exception as e:
        print(f"Error fetching snippet: {e}")
        return None

def db_filter_snippets(conn, user_name=None, tag=None, language=None):
    try:
        with conn.cursor() as cursor:
            query = sql.SQL("SELECT id, code, tags, language, user_name FROM snippets WHERE 1=1")
            params = []
            if user_name:
                query += sql.SQL(" AND user_name = %s")
                params.append(user_name)
            if tag:
                query += sql.SQL(" AND tags LIKE %s")
                params.append(f"%{tag}%")
            if language:
                query += sql.SQL(" AND language = %s")
                params.append(language)
            
            cursor.execute(query, params)
            snippets = cursor.fetchall()
            return [Snippet(*snippet) for snippet in snippets]
    except Exception as e:
        print(f"Error filtering snippets: {e}")
        return []

def db_insert_comment(conn, comment):
    try:
        with conn.cursor() as cursor:
            insert_query = sql.SQL("""
                INSERT INTO comments (snippet_id, user_name, content, created_at)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """)
            cursor.execute(insert_query, (comment.snippet_id, comment.user_name, comment.content, comment.created_at))
            comment_id = cursor.fetchone()[0]
            conn.commit()
            print(f"Comment inserted successfully with ID: {comment_id}")
            return comment_id
    except Exception as e:
        print(f"Error inserting comment: {e}")
        conn.rollback()
        return None


