from tkinter import *
def selected():
    sugar=sugar_var.get()
    ice =ice_var.get()
    cream =cream_var.get()
    if sugar:sugar= " Sugar"
    else: sugar= " NO Sugar"
    if ice: ice=" Ice"
    else: ice= " No Ice"
    if cream: cream=" Cream"
    else: cream: cream =" NO Cream"
    label.config(text="Option selected are: "+"\n"+ sugar +"\n" + ice +"\n" + cream)



root = Tk()
root.geometry("300x300")
sugar_var =BooleanVar()
ice_var=BooleanVar()
cream_var =BooleanVar()
suger_checkbox = Checkbutton(root, text="suger",variable=sugar_var, command= selected)
ice_checkbox = Checkbutton(root, text="Ice",variable=ice_var, command= selected)
cream_checkbox = Checkbutton(root, text="Cream",variable=cream_var, command= selected)
label= Label(root)
label.pack()

suger_checkbox.pack()
ice_checkbox.pack()
cream_checkbox.pack()
root.mainloop()