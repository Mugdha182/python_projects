from tkinter import *
from tkinter import messagebox
from gtts import gTTS
import os

t=Tk()
t.geometry('400x400')
t.configure(bg='lightblue')
t.title("Text to Speech Conversion")

lbl1=Label(text="Enter text",font=('Times New Roman',15))
lbl1.pack(pady=(20,10))

inp1=Entry(width=50,font=('Times New Roman',11))
inp1.pack()

lbl2=Label(text="Filename (eg. audio.mp3)",font=('Times New Roman',15))
lbl2.pack(pady=(20,10))

inp2=Entry()
inp2.pack()


def text_to_speech():
    text=inp1.get()
    language='en'
    filename=inp2.get()
    if text:
        tts = gTTS(text=text, lang=language)
        tts.save(filename)
        os.system(f'start {filename}')


btn1=Button(text="Convert",command=text_to_speech,font=('Times New Roman',13))
btn1.pack(pady=(20,10))

t.mainloop()
