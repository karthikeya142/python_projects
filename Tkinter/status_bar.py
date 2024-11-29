from tkinter import *

def function1():
    print("menu item clicked")
root=Tk()
mymenu = Menu(root)
root.config(menu=mymenu)

submenu= Menu(mymenu)
root.geometry("300x300")
mymenu.add_cascade(label='File', menu= submenu )
submenu.add_command(label="project",command=function1)
submenu.add_command(label="save",command=function1)

status = Label(root, text="this is the current status",bd=2,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)
root.mainloop()