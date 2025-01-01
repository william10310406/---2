import tkinter as tk
from tkinter import messagebox
from function import init_db
from auth import show_login_register
from static.style import configure_root
from static.record import ActionLogger

# 初始化資料庫
init_db()

# 建立 logger 實例
logger = ActionLogger()

# 全域變數
current_user = None


# 顯示使用者介面
def show_user_interface():
    user_interface_frame = tk.Frame(root)
    user_interface_frame.pack()
    tk.Label(user_interface_frame, text=f"Welcome, {current_user}!").pack()
    # 在這裡添加更多使用者介面元件


# 建立主視窗
root = tk.Tk()
root.title("My Tkinter App")
configure_root(root)

# 建立登入/註冊按鈕
login_register_button = tk.Button(
    root,
    text="Login/Register",
    command=lambda: show_login_register(
        root, login_register_button, show_user_interface
    ),
)
login_register_button.pack()

# 啟動主事件迴圈
root.mainloop()
