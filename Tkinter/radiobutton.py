from tkinter import *
def selected():

    label.config(text="Choice of fuel is : "+fuel.get())


root = Tk()
root.geometry("300x300")
fuel = StringVar(value= "Eletric")
radio1 = Radiobutton(root, text="petrol",variable= fuel,value="petrol", command= selected)
radio2 = Radiobutton(root, text="Diesel",variable= fuel,value="Diesel", command= selected)
radio3 = Radiobutton(root, text="Eletric",variable= fuel, value="Eletric",command= selected)
label= Label(root)
label.pack()

radio1.pack()
radio2.pack()
radio3.pack()
root.mainloop()