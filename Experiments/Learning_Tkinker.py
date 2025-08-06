import tkinter as tk

root = tk.Tk()
root.title("My first experiment in Tkinker App")
root.geometry("400x800")

label = tk.Label(root,text="Hello, Welcome to Tkinker Krishnan!")
label.pack(pady=10)

button = tk.Button(root, text="Close", command=root.quit)
button.pack(pady=10)

root.mainloop()