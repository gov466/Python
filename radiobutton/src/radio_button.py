from tkinter import  *
from PIL import Image,ImageTk
from _ast import Lambda

root =Tk()
root.title("my perogram")

r=IntVar()
r.set("2")

def clicked(value):
    myLabel= Label(root,text=r.get())
    myLabel.pack()
    
Radiobutton(root, text= "option 1", variable=r , value= 1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text= "option 2", variable= r, value= 2, command=lambda: clicked(r.get())).pack()
##Radiobutton(root, text= "option 3", variable= r, value= 1).pack()

myLabel= Label(root,text=r.get())
myLabel.pack()

myButton =Button(root, text="click me", command= lambda:clicked(r.get()))
myButton.pack()
root.mainloop()
