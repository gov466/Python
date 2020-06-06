from tkinter import *
from PIL import Image,ImageTk

root=Tk()
root.title("Image viewer")
root.iconbitmap('instagram.png')
my_img1 =ImageTk.Photoimage(Image.open('canadaguide.jpg'))
my_img2 =ImageTk.Photoimage(Image.open('canadaguide.jpg'))
my_img3 =ImageTk.Photoimage(Image.open('canadaguide.jpg'))
my_img4 =ImageTk.Photoimage(Image.open('canadaguide.jpg'))
my_img5 =ImageTk.Photoimage(Image.open('canadaguide.jpg'))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]
my_label=Label(image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

button_back=Button(root,text='<<')
button_exit= Button(root, text-"Exit program",command=root.quit)
button_forward=Button(root,text='>>')
root.mainloop()
