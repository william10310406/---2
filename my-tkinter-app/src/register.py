import tkinter as tk
from tkinter import messagebox
import re
from function import register_user


# 驗證電子郵件格式
def validate_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@gmail\.com$", email)


# 驗證密碼格式
def validate_password(password):
    return re.match(r"^(?=.*[a-z])(?=.*[A-Z]).+$", password)


# 顯示註冊視窗
def show_register(root):
    register_window = tk.Toplevel(root)
    register_window.title("Register")

    # 註冊功能
    def register():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        phone = phone_entry.get()
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
        register_user(username, password, email, phone)
        messagebox.showinfo("Success", "Registration successful! You can now log in.")
        register_window.destroy()

    # 建立註冊視窗元件
    tk.Label(register_window, text="Username (Gmail):").pack()
    username_entry = tk.Entry(register_window)
    username_entry.pack()

    tk.Label(register_window, text="Password:").pack()
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack()

    tk.Label(register_window, text="Email:").pack()
    email_entry = tk.Entry(register_window)
    email_entry.pack()

    tk.Label(register_window, text="Phone:").pack()
    phone_entry = tk.Entry(register_window)
    phone_entry.pack()

    tk.Button(register_window, text="Register", command=register).pack()
