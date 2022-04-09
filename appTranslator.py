from googletrans import Translator
from PIL import Image, ImageTk
from tkinter import *

root=Tk()

root.title("Translate of Pk")
root.geometry("500x600")
root.iconbitmap('safe_image.ico')


name=Label(root, text="Translator", fg="yellow", bd=0, bg="#F0F0F0")
name.config(font=('Transformers Movie', 30))
name.pack(pady=10)

box=Text(root,width=30,height=8,font=("ROBOTO",16))
box.pack(pady=20)

button_frame=Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0, END)
    box1.delete(1.0, END)

def translate():
    INPUT=box.get(1.0,END)
    print(INPUT)
    t=Translator()
    d=t.translate(INPUT, src="en", dest="vi")
    box1.insert(END,d.text)

clear_button=Button(button_frame,text="Clear text", font=(("Arial"),10,'bold'),bg='#303030',fg='#FFFFFF', command=clear)
clear_button.place(x=150,y=310)
trans_button=Button(button_frame,text="Translate", font=(("Arial"),10,'bold'),bg='#303030',fg='#FFFFFF',command=translate)
trans_button.place(x=290,y=310)

box1=Text(root,width=30,height=8,font=("ROBOTO",16))
box1.pack(pady=50)





root.mainloop()