from tkinter import *
from tkinter import messagebox

import bcrypt

def validate(password):
    hash =b'$2b$12$qKLrVh2lCuZqNmIzd02Uc.AJakcToSE04TNh.Ia1Sn8P.1l1cGdxe'
    password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(password, hash):
        messagebox.showinfo("Information","login sudccessfull")
    else:
        messagebox.showinfo("Information","Invalid Password")

root =Tk()
root.geometry('600x300')
password_entry=Entry(root)
password_entry.grid(row=0,column=2)
password_entry.get()
button =Button(root,text='validate',command=lambda : validate(password_entry.get()))
button.grid(row=1, column=2, columnspan=3)
root.mainloop()