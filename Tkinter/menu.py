from tkinter import *

def function1():
    print("menu item clicked")
root=Tk()
mymenu = Menu(root)
root.config(menu=mymenu)

submenu= Menu(mymenu)

mymenu.add_cascade(label='File', menu= submenu )
submenu.add_command(label="project",command=function1)
submenu.add_command(label="save",command=function1)

root.mainloop()