import tkinter as tk
from tkinter import messagebox
from function import init_db, get_user_info, update_user_info
from auth import show_login_register
from static.style import configure_root
from static.record import ActionLogger

# 初始化資料庫
init_db()

# 建立 logger 實例
logger = ActionLogger()

# 全域變數
current_user = None


# 顯示個人資料視窗
def show_profile():
    profile_window = tk.Toplevel(root)
    profile_window.title("Profile")

    user_info = get_user_info(current_user)

    tk.Label(profile_window, text="Username:").pack()
    username_label = tk.Label(profile_window, text=user_info["username"])
    username_label.pack()

    tk.Label(profile_window, text="Email:").pack()
    email_entry = tk.Entry(profile_window)
    email_entry.insert(0, user_info["email"])
    email_entry.pack()

    tk.Label(profile_window, text="Phone:").pack()
    phone_entry = tk.Entry(profile_window)
    phone_entry.insert(0, user_info["phone"])
    phone_entry.pack()

    def save_profile():
        new_email = email_entry.get()
        new_phone = phone_entry.get()
        update_user_info(current_user, new_email, new_phone)
        messagebox.showinfo("Success", "Profile updated successfully!")
        profile_window.destroy()

    tk.Button(profile_window, text="Save", command=save_profile).pack()


# 顯示使用者介面
def show_user_interface():
    user_interface_frame = tk.Frame(root)
    user_interface_frame.pack()
    tk.Label(user_interface_frame, text=f"Welcome, {current_user}!").pack()
    profile_button = tk.Button(
        user_interface_frame, text="Profile", command=show_profile
    )
    profile_button.pack(side=tk.TOP, anchor=tk.NW)
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
