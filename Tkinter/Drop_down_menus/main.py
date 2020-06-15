from tkinter import  *
from PIL import Image,ImageTk
 

root =Tk()
root.title("my perogram") 
root.geometry("400x400")

def show():
    myLabel=Label(root,text= clicked.get()).pack()

options=["Monday","Tuesday","Wednesday","Thursday","friday"]

clicked=StringVar()
clicked.set(" Monday")
#drop =OptionMenu(root, clicked, "Monday","Tuesday","Wednesday","Thursday","friday")
drop =OptionMenu(root, clicked, *options)
drop.pack()
myButton = Button(root, text="Show Selection",command=show).pack()
root.mainloop()
