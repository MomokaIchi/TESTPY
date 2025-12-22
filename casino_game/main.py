import tkinter as tk

def on_click():
    label.config(text="Button pressed")

root = tk.Tk()
root.title("Casino Game")
root.geometry("400x300")

label = tk.Label(root, text="Welcome to Casino", font=("Arial", 14))
label.pack(pady=20)

# button = tk.Button(root, text="Test botton")

button = tk.Button(root, text="click me", command=on_click)
button.pack()

root.mainloop()