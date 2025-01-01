import tkinter as tk
from tkinter import messagebox
from function import login_user


# 顯示登入視窗
def show_login(root, login_button, register_button, show_user_interface):
    login_window = tk.Toplevel(root)
    login_window.title("Login")

    # 登入功能
    def login():
        username = username_entry.get()
        password = password_entry.get()
        if login_user(username, password):
            global current_user
            current_user = username
            messagebox.showinfo("Success", "Login successful!")
            login_window.destroy()
            login_button.pack_forget()
            register_button.pack_forget()
            show_user_interface()
        else:
            messagebox.showerror("Error", "Login failed! Please register.")

    # 建立登入視窗元件
    tk.Label(login_window, text="Username:").pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    tk.Label(login_window, text="Password:").pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    tk.Button(login_window, text="Login", command=login).pack()
