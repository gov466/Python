from tkinter import *
from PIL import Image,ImageTk
from distutils import command
from _ast import Lambda
from apport.hookutils import command_available

root=Tk()
root.title("Image viewer")
##root.iconbitmap('icon.ico')
try:
    root.wm_iconbitmap('icon.ico')
    root.mainloop()
except TclError:
    print('No ico file found') 
my_img1 =ImageTk.PhotoImage(Image.open('img_20180228_094714.jpg'))
my_img2 =ImageTk.PhotoImage(Image.open('0.png'))
my_img3 =ImageTk.PhotoImage(Image.open('canadaguide.jpg'))
my_img4 =ImageTk.PhotoImage(Image.open('canadaguide.jpg'))
my_img5 =ImageTk.PhotoImage(Image.open('canadaguide.jpg'))

image_list=[my_img1, my_img2, my_img3, my_img4, my_img5]
my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward= Button(root, text=">>",command=lambda : forward(image_number+1))
    button_back= Button(root, text="<<",command=lambda: back(image_number-1))    
    my_label.grid(row=0,column=0,columnspan=3)

def back():
     global my_label
     global button_forward
     global button_back

button_back=Button(root,text='<<',command=lambda:back)
button_exit= Button(root, text="Exit program",command=root.quit)
button_forward=Button(root,text='>>',command=lambda:forward(2))
button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)
root.mainloop()
