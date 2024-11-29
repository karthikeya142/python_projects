from tkinter import *
import tkinter.messagebox

root=Tk()
response=tkinter.messagebox.askquestion("coffee", 'Do you Like Coffee')
if response == "yes":
    print("here is a coffee for you")

root.mainloop()