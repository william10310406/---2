def create_file(filename):
    # 建立一個空檔案
    with open(filename, "w") as file:
        file.write("")


def open_website(url):
    # 開啟指定的網址
    import webbrowser

    webbrowser.open(url)


def list_files(directory):
    # 列出指定目錄中的所有檔案
    import os

    return os.listdir(directory)


def read_file(filename):
    # 讀取指定檔案的內容
    with open(filename, "r") as file:
        return file.read()


def write_file(filename, content):
    # 將內容寫入指定檔案
    with open(filename, "w") as file:
        file.write(content)


def init_db():
    # 初始化資料庫，建立 users 表格
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
    # 註冊新使用者，將使用者名稱和密碼存入資料庫
    import sqlite3

    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", (username, password)
    )
    conn.commit()
    conn.close()


def login_user(username, password):
    # 登入功能，檢查使用者名稱和密碼是否匹配
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
    # 更新使用者的密碼
    import sqlite3

    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE users SET password = ? WHERE username = ?", (new_password, username)
    )
    conn.commit()
    conn.close()
