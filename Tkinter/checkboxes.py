from tkinter import *
def selected():
    label.config(text=checkvalue.get())
root =Tk()
root.geometry("300x300")
checkvalue= BooleanVar()
checkbotton = Checkbutton(root, text="Accept Terms", variable=BooleanVar,command=selected)
checkbotton.pack()

label = Label(root)
label.pack()
answer =Label(root)
answer.pack()

root.mainloop()