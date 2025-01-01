import tkinter as tk
from tkinter import messagebox
import re
from function import register_user, login_user


# 驗證電子郵件格式
def validate_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email)


# 驗證密碼格式
def validate_password(password):
    return re.match(r"^(?=.*[a-z])(?=.*[A-Z]).+$", password)


# 顯示登入/註冊視窗
def show_login_register(root, login_register_button, show_user_interface):
    login_register_window = tk.Toplevel(root)
    login_register_window.title("Login/Register")

    # 登入功能
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if login_user(username, password):
            global current_user
            current_user = username
            messagebox.showinfo("Success", "Login successful!")
            login_register_window.destroy()
            login_register_button.pack_forget()
            show_user_interface()
        else:
            messagebox.showerror("Error", "Login failed! Please register.")

    # 註冊功能
    def register():
        username = username_entry.get()
        password = password_entry.get()
        if not validate_email(username):
            messagebox.showerror(
                "Error", "Invalid email format. Please use a Gmail address."
            )
            return
        if not validate_password(password):
            messagebox.showerror(
                "Error",
                "Password must contain at least one uppercase and one lowercase letter.",
            )
            return
        register_user(username, password)
        messagebox.showinfo("Success", "Registration successful! You can now log in.")

    # 建立登入/註冊視窗元件
    tk.Label(login_register_window, text="Username (Gmail):").pack()
    username_entry = tk.Entry(login_register_window)
    username_entry.pack()

    tk.Label(login_register_window, text="Password:").pack()
    password_entry = tk.Entry(login_register_window, show="*")
    password_entry.pack()

    tk.Button(login_register_window, text="Login", command=login).pack()
    tk.Button(login_register_window, text="Register", command=register).pack()
