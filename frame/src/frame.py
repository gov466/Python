from tkinter import  *
from PIL import Image,ImageTk

root =Tk()
root.title("my perogram")

frame= LabelFrame(root, text="Thi sis my frame", padx=5,pady=5)
frame.pack(padx=10,pady=10)

b= Button(frame, text= "DOnt click")
b2= Button(frame, text= "  click")
b.grid(row=0,column=0)
b2.grid(row=0,column=1)

root.mainloop()
