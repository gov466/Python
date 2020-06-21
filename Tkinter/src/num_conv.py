from tkinter import  *
from PIL import Image,ImageTk
from tkinter.ttk import _to_number
import decimal as d
 

root =Tk()
root.title("my converter") 
root.geometry("550x200")
global o_number
global d_number
global b_number
global h_number

def binarynum():
    global num
    num=bin(b_number.get())
    b_number.delete(0, END)
    b_number.insert(0,str(num))
def octalnum():
    num1=oct(num)
    #num4=oct(h_number.get())
    #num5=oct(d_number.get())
    o_number.delete(0, END)
    o_number.insert(0, str(num1))
  #  o_number.insert(0, str(num4))
   # o_number.insert(0, str(num5))
    
     
def decimalnum():
    num2=d_number.get()
    d_number.delete(0, END)
   # d_number.insert(0, str("num"))
def hexanum():
    num3=h_number.get()
    h_number.delete(0, END)
  #  h_number.insert(0, (hex(num3)))


b_number=Entry(root,width=30)
b_number.grid(row=20, column=1, padx=20)

o_number=Entry(root,width=30)
o_number.grid(row=21, column=1, padx=20)

d_number=Entry(root,width=30)
d_number.grid(row=22, column=1, padx=20)

h_number=Entry(root,width=30)
h_number.grid(row=23, column=1, padx=20)


b_number_label=Label(root,text ="Binary number")
b_number_label.grid(row=20,column=0)

o_number_label=Label(root,text ="Octal number")
o_number_label.grid(row=21,column=0)

d_number_label=Label(root,text ="decimal number")
d_number_label.grid(row=22,column=0)

h_number_label=Label(root,text ="hexadecimal number")
h_number_label.grid(row=23,column=0)

b_number_base=Label(root,text ="2")
b_number_base.grid(row=20,column=4)

o_number_base=Label(root,text ="8")
o_number_base.grid(row=21,column=4)

d_number_base=Label(root,text ="10")
d_number_base.grid(row=22,column=4)

h_number_base=Label(root,text ="16")
h_number_base.grid(row=23,column=4)

binary_button =Button(root,text ="Convert", command=binarynum)
binary_button.grid(row=20 ,column=5, columnspan =4, pady=10 ,padx= 10) 

octal_button =Button(root,text ="Convert", command=octalnum)
octal_button.grid(row=21 ,column=5, columnspan =4, pady=10 ,padx= 10) 

decimal_button =Button(root,text ="Convert", command=decimalnum)
decimal_button.grid(row=22 ,column=5, columnspan =4, pady=10 ,padx= 10) 

hexa_button =Button(root,text ="Convert", command=hexanum)
hexa_button.grid(row=23 ,column=5, columnspan =4, pady=10 ,padx= 10) 



root.mainloop()