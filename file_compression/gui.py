import  tkinter as tk
from tkinter import filedialog

from compress_module import compress, decompres

def open_file():
    filename =filedialog.askopenfilename(initialdir="/",title="Select a file to compress ")
    return filename
def compression(i,o):
    compress(i,o)
    # decompres(o,o)
    # compress(i,o+".compressed")
    # decompres(o+".compressed",o)

window = tk.Tk()
window.title("compression engine")
window.geometry("600x400")
input_entry = tk.Entry(window)

output_entry =tk.Entry(window)
input_label= tk.Label(window,text=f'File to be Compressed')

output_label= tk.Label(window,text=f'Name of the Compressed file')
compress_button =tk.Button(window,text="Compress",command=lambda: compress(open_file(),"com.txt"))

# input_label.grid(row=0,column=0)
# input_entry.grid(row=0,column=1)
# output_label.grid(row=1,column=0)
# output_entry.grid(row=1,column=1)
compress_button.grid(row=2,column=1)


window.mainloop()