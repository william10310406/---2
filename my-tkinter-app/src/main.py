# filepath: /Volumes/帥哥2TB/程式/主控台2/my-tkinter-app/src/main.py
import tkinter as tk
from tkinter import messagebox
from function import init_db, get_user_info, update_user_info, register_user
from login import show_login
from register import show_register
from static.style import configure_root
from static.record import ActionLogger

# 初始化資料庫
init_db()

# 建立 logger 實例
logger = ActionLogger()

# 全域變數
current_user = None


def show_profile():
    global current_user
    user_info = get_user_info(current_user)
    # 若查無此使用者資料，建立一筆預設紀錄
    if user_info is None:
        # 預設名稱為「使用者」、密碼隨意設 placeholder、其它空白
        register_user(username="使用者", password="password", email="", phone="")
        user_info = get_user_info("使用者")
        # 順便更新 current_user 為「使用者」
        current_user = "使用者"

    profile_window = tk.Toplevel(root)
    profile_window.title("Profile")

    tk.Label(profile_window, text="Username:").pack()
    username_entry = tk.Entry(profile_window)
    username_entry.insert(0, user_info["username"])
    username_entry.pack()

    tk.Label(profile_window, text="Email:").pack()
    email_entry = tk.Entry(profile_window)
    email_entry.insert(0, user_info["email"])
    email_entry.pack()

    tk.Label(profile_window, text="Phone:").pack()
    phone_entry = tk.Entry(profile_window)
    phone_entry.insert(0, user_info["phone"])
    phone_entry.pack()

    def save_profile():
        global current_user  # 確保使用全域的 current_user
        old_name = current_user
        new_name = username_entry.get()
        new_email = email_entry.get()
        new_phone = phone_entry.get()
        update_user_info(old_name, new_name, new_email, new_phone)
        # 更新 current_user
        current_user = new_name
        messagebox.showinfo("Success", "Profile updated successfully!")
        profile_window.destroy()

    tk.Button(profile_window, text="Save", command=save_profile).pack()


def show_user_interface():
    global current_user  # 確保使用全域的 current_user
    user_interface_frame = tk.Frame(root, bg="#f0f0f0")
    user_interface_frame.pack(fill=tk.BOTH, expand=True)
    tk.Label(
        user_interface_frame, text=f"Welcome, {current_user}!", bg="#f0f0f0"
    ).pack()
    tk.Button(user_interface_frame, text="Profile", command=show_profile).pack()


root = tk.Tk()
root.title("My Tkinter App")
configure_root(root)

login_button = tk.Button(
    root,
    text="Login",
    command=lambda: show_login(
        root, login_button, register_button, show_user_interface
    ),
)
login_button.pack()

register_button = tk.Button(root, text="Register", command=lambda: show_register(root))
register_button.pack()

root.mainloop()
