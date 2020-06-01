'''
Created on May 31, 2020

@author: govind
'''# Simple calculator#
from tkinter import *
import math

root = Tk()
root.title("simple calculator")
e= Entry(root,width=35, borderwidth =5) ##creating an entry box
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) ##dimensions of entry box
#e.insert(0,"Enter your name:")
def button_click(number):  ##function for click of a number
   # e.delete(0,END)
    current =e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def button_clear():
    e.delete(0,END )

def button_add():
    first_number =e.get()
    global f_num
    global math
    math="addition"
    f_num =int(first_number)
    e.delete(0,END)
def button_equal():
    
    second_number= e.get()
    e.delete(0,END)
    
    if math == "addition":
        e.insert(0,f_num + int(second_number))
    if math == "subtraction":
        e.insert(0,f_num - int(second_number))
    if math == "mutlipication":
        e.insert(0,f_num * int(second_number))
    if math == "division":
        e.insert(0,f_num / int(second_number))
def button_sub():
    first_number =e.get()
    global f_num
    global math
    math="subtraction"
    f_num =int(first_number)
    e.delete(0,END) 
def button_mul():
    first_number =e.get()
    global f_num
    global math
    math="multiplication"
    f_num =int(first_number)
    e.delete(0,END)   
def button_div():
    first_number =e.get()
    global f_num
    global math
    math="division"
    f_num =int(first_number)
    e.delete(0,END)
   
  
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
Button_add=Button(root,text="+", padx=39, pady=20, command=button_add)
Button_equal=Button(root,text="=", padx=91, pady=20, command=button_equal)
Button_clear=Button(root,text="Clear", padx=79, pady=20, command=button_clear)
Button_subtract=Button(root,text="-", padx=41, pady=20, command=button_sub)
Button_multiply=Button(root,text="*", padx=40, pady=20, command=button_mul)
Button_divide=Button(root,text="/", padx=41, pady=20, command=button_div)
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

Button_subtract.grid(row=6,column=0)
Button_multiply.grid(row=6,column=1)
Button_divide.grid(row=6,column=2)
#w.grid(row=0,column=0)
#v.grid(row=6,column=15)
root.mainloop()
