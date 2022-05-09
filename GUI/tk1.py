import tkinter as tk

root = tk.Tk() #creates the overall tk window
"""The first argument to a Tk widget is the parent in which it will be placedThe padx and pady arguments add padding
horizontally and vertically"""
label = tk.Label(root, text="Hello World", padx=100, pady=100) #will hold our "Hello World" text
label.pack() #label.pack() is then called as a way of placing the label into the root

root.mainloop()#root.mainloop() is responsible for showing the window.
