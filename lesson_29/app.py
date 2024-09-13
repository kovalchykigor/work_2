# conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/postgres")

import psycopg2


def connect_to_db():
    conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/postgres")
    return conn


def create_table():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()


def insert_user(name, age):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s);", (name, age))
    conn.commit()
    cursor.close()
    conn.close()


def update_user(user_id, name, age):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = %s, age = %s WHERE id = %s;", (name, age, user_id))
    conn.commit()
    cursor.close()
    conn.close()


def delete_user(user_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s;", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()


def fetch_users():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users
