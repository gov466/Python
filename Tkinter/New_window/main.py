##python tkinter program to open a new window from root
from tkinter import  *
from PIL import Image, ImageTk
from _ast import Lambda

root =Tk()
root.title("Canada") 
root.geometry("633x353") ##to set the geomertry
def open(): ##function for second widow
    global my_img
    top= Toplevel()
    top.title("572 Pharmacy")
    ##my_img= ImageTk.PhotoImage(Image.open("/home/govind/Downloads/instagram.png")) ##imgae in second window
    my_lablel= Label(top, image=my_img).pack()
    btn2 =Button(top,text="close window",command=top.destroy).pack () ##button in second wondow

    
 
##my_img1=ImageTk.PhotoImage(Image.open("/home/govind/eclipse-workspace/Python/Tkinter/src/carousel-canada.jpg")) ##imge for root
##my_label1=Label(root, image=my_img1).pack()
home =Button(text="Home", command=open).place(relx=0.5, rely=0.96, anchor="c") ##button inside root
## =Button(text="572 live", command=open).place(relx=0.5, rely=0.96, anchor="c")
mainloop()
