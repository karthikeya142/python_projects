from tkinter import *
def display():
    data = entry.get()
    print(data)
root =Tk()
root.geometry("300x200")
button=Button(root,text="click here",command=display)
entry =Entry(root)
entry.pack()
button.pack()
root.mainloop()
