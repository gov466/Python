##simple calculator
from tkinter import *

root = Tk()
root.title("simple calculator")
e= Entry(root,width=35, borderwidth =5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#e.insert(0,"Enter your name:")
def button_click(number):
  e.delete(0,END)
  e.insert(0,number)

  
Button_1=Button(root,text="1", padx=40, pady=20, command=lambda: button_click(1))
Button_2=Button(root,text="2", padx=40, pady=20, command=lambda:button_click(2))
Button_3=Button(root,text="3", padx=40, pady=20, command=lambda:button_click(3))
Button_4=Button(root,text="4", padx=40, pady=20, command=lambda:button_click(4))
Button_5=Button(root,text="5", padx=40, pady=20, command=lambda:button_click(5))
Button_6=Button(root,text="6", padx=40, pady=20, command=lambda:button_click(6))
Button_7=Button(root,text="7", padx=40, pady=20, command=lambda:button_click(7))
Button_8=Button(root,text="8", padx=40, pady=20, command=lambda:button_click(8))
Button_9=Button(root,text="9", padx=40, pady=20, command=lambda:button_click(9))
Button_0=Button(root,text="0", padx=40, pady=20, command=lambda:button_click(0))
Button_add=Button(root,text="+", padx=39, pady=20, command=lambda:button_click)
Button_equal=Button(root,text="=", padx=91, pady=20, command=lambda:button_click)
Button_clear=Button(root,text="Clear", padx=79, pady=20, command=lambda:button_click)

Button_1.grid(row=3,column=0)
Button_2.grid(row=3,column=1)
Button_3.grid(row=3,column=2)

Button_4.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_6.grid(row=2,column=2)

Button_7.grid(row=1,column=0)
Button_8.grid(row=1,column=1)
Button_9.grid(row=1,column=2)

Button_0.grid(row=4,column=0)
Button_add.grid(row=5,column=0)
Button_clear.grid(row=4,column=1,columnspan=2)
Button_equal.grid(row=5,column=1,columnspan=2)

#w.grid(row=0,column=0)
#v.grid(row=6,column=15)
root.mainloop()
