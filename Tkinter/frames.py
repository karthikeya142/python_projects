from tkinter import *
# adding properties to the frames

root= Tk()
frame= Frame(root)
frame.pack()

frame2 = Frame(root)
frame2.pack(side=BOTTOM)

root.geometry("300x300")
button = Button(frame, text="button1", highlightthickness=1,highlightbackground="red", padx="5",pady="5")
button2 = Button(frame2,text="button2")

button.pack ()
button2.pack()
root.mainloop()





#  frmes
# from tkinter import *
# root= Tk()
# frame= Frame(root)
# frame.pack()
#
# frame2 = Frame(root)
# frame2.pack(side=BOTTOM)
#
# root.geometry("300x300")
# button = Button(frame, text="button1")
# button2 = Button(frame2,text="button2")
#
# button.pack ()
# button2.pack()
# root.mainloop()