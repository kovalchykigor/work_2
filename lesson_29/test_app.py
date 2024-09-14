from . import base_app


def test_connection():
    conn = base_app.connect_to_db()
    assert conn is not None, "Failed to connect to the database"


def test_insert_user():
    base_app.create_table()
    base_app.insert_user('John', 30)
    users = base_app.fetch_users()
    assert any(user[1] == 'John' for user in users), "Failed to insert user"


def test_update_user():
    base_app.insert_user('Jane', 25)
    users = base_app.fetch_users()
    user_id = users[-1][0]  # Get the last inserted user's ID
    base_app.update_user(user_id, 'Jane Doe', 26)
    users = base_app.fetch_users()
    assert any(user[1] == 'Jane Doe' and user[2] == 26 for user in users), "Failed to update user"


def test_fetch_users():
    base_app.insert_user('Alice', 28)
    users = base_app.fetch_users()

    assert len(users) > 0, "No users found in the database"
    assert any(user[1] == 'Alice' for user in users), "Failed to fetch user 'Alice'"

def test_delete_user():
    base_app.insert_user('Mark', 40)
    users = base_app.fetch_users()
    user_id = users[-1][0]
    base_app.delete_user(user_id)
    users = base_app.fetch_users()
    assert not any(user[0] == user_id for user in users), "Failed to delete user"
