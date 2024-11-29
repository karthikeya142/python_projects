from tkinter import *
def display():
    print("Button Clicked")
root =Tk()
root.geometry("300x200")
button=Button(root,text="click here",command=display)
hello = Label(root,text="Hello Karthikeya!",fg="red",bg="white",font=("Arial",17))
button.pack()
#hello.pack()

root.mainloop()


