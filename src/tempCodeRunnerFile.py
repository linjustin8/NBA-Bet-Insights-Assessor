import tkinter as tk
from tkinter import Toplevel

def open_modal_window():
    # Create a top-level window
    top = Toplevel(root)
    top.title("Modal Window")
    top.geometry("200x100")

    # Add a label
    label = tk.Label(top, text="This is a modal window")
    label.pack(pady=20)

    # Set modal: no input on the main window until this one is closed
    top.grab_set()

    # Button to close the modal window
    close_button = tk.Button(top, text="Close", command=top.destroy)
    close_button.pack()

    # This ensures the window is positioned above its parent
    top.transient(root)

root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

# Button to open the modal window
open_button = tk.Button(root, text="Open Modal Window", command=open_modal_window)
open_button.pack(pady=50)

root.mainloop()