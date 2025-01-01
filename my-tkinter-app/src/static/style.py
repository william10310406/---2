import tkinter as tk


def configure_root(root):
    root.title("My Tkinter App")
    root.geometry("800x600")
    root.configure(bg="#f0f0f0")


def add_scrollbar(frame):
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    return scrollbar


def make_draggable(widget):
    def on_drag(event):
        widget.place(x=widget.winfo_x() + event.x, y=widget.winfo_y() + event.y)

    widget.bind("<Button-1>", lambda event: widget.bind("<B1-Motion>", on_drag))
    widget.bind("<ButtonRelease-1>", lambda event: widget.unbind("<B1-Motion>"))
