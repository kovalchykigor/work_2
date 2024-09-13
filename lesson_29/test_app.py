import app


def test_connection():
    conn = app.connect_to_db()
    assert conn is not None, "Failed to connect to the database"


def test_insert_user():
    app.insert_user('John', 30)
    users = app.fetch_users()
    assert any(user[1] == 'John' for user in users), "Failed to insert user"


def test_update_user():
    app.insert_user('Jane', 25)
    users = app.fetch_users()
    user_id = users[-1][0]  # Get the last inserted user's ID
    app.update_user(user_id, 'Jane Doe', 26)
    users = app.fetch_users()
    assert any(user[1] == 'Jane Doe' and user[2] == 26 for user in users), "Failed to update user"


def test_delete_user():
    app.insert_user('Mark', 40)
    users = app.fetch_users()
    user_id = users[-1][0]
    app.delete_user(user_id)
    users = app.fetch_users()
    assert not any(user[0] == user_id for user in users), "Failed to delete user"
