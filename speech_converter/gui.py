from gtts import gTTS
import os
import tkinter as tk

def textspeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save('guiread.mp3')
    os.system('start guiread.mp3')  # Corrected the filename here

root = tk.Tk()
root.title("Text-to-Speech Converter")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

entry = tk.Entry(root, width=50)
canvas.create_window(200, 180, window=entry)

button = tk.Button(text='Convert to Speech', command=textspeech)
canvas.create_window(200, 230, window=button)

root.mainloop()


# from gtts import gTTS
# import os
# from tkinter import *
#
# def textspech():
#     text=entry.get()
#     language='en'
#     output=gTTS(text=text,lang=language,slow=False)
#     output.save('guiread.mp3')
#     os.system('start guiread.mp3')
# root=Tk()
# canvas=Canvas(root,width=400,height=300)
# canvas.pack()
# entry=Entry(root)
# canvas.create_window(200,180,window=entry)
# button=Button(text='Start',command=textspech)
# canvas.create_window(200,230,window=button)
#
# root.mainloop()