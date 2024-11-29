#Tkinter is a standard GUI (Graphical User Interface) library in Python.
# It provides an interface to the Tk GUI toolkit and is included with most Python installations.
# Tkinter allows you to create windows, dialogs, buttons, menus, text fields, and more.
from tkinter import *

root =Tk()
root.geometry("300x200")
hello = Label(root,text="Hello Karthikeya!")
hello.pack()
root.mainloop()
