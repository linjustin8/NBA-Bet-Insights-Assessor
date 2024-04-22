import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

# Configuring row weights
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)

# Widget with specific vertical alignment and expansion
label = tk.Label(root, text="Flexible Vertical Placement", bg="khaki")
label.grid(row=0, column=0, sticky="NS", rowspan=2)

root.mainloop()
