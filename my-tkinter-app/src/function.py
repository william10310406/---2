def create_file(filename):
    with open(filename, "w") as file:
        file.write("")


def open_website(url):
    import webbrowser

    webbrowser.open(url)


def list_files(directory):
    import os

    return os.listdir(directory)


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def write_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)


def init_db():
    import sqlite3

    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


def register_user(username, password):
    import sqlite3

    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
    )
    conn.commit()
    conn.close()


def login_user(username, password):
    import sqlite3

    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result is None:
        return False
    stored_password = result[0]
    return password == stored_password


def update_user(username, new_password):
    import sqlite3

    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET password = ? WHERE username = ?", (new_password, username)
    )
    conn.commit()
    conn.close()
