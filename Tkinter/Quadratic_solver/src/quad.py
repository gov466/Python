##python program to solve quadratic equatinons
from tkinter import  *
from PIL import Image,ImageTk
##to display the box(main page)
root =Tk()
root.title("Quadratic solver") 
root.geometry("400x200")

def clear(): ##funtion for clear button
    return 

def calculate(): ##function for calculate button
    return

main_label=Label(root,text ="Equation = x2+bx+c=0")
main_label.grid(row=2,column=1) ##a label in main box


Entry_a=Entry(root,width=30) ##entry for 3 numbers
Entry_a.grid(row=3, column=1, padx=20)

Entry_b=Entry(root,width=30)
Entry_b.grid(row=4, column=1, padx=20)

Entry_c=Entry(root,width=30)
Entry_c.grid(row=5, column=1, padx=20)

Entry_a_label=Label(root,text ="a=") ##lable for entries
Entry_a_label.grid(row=3,column=0)

Entry_b_label=Label(root,text ="b=")
Entry_b_label.grid(row=4,column=0)

Entry_c_label=Label(root,text ="c=")
Entry_c_label.grid(row=5,column=0)
##button for clear and calculate
clear_button =Button(root,text ="Clear", command=clear)
clear_button.grid(row=6 ,column=0, pady=10 ,padx= 5, ipadx=25) 

# calculate button
calculate_button= Button(root,text="Calculate", command= calculate)
calculate_button.grid(row=6, column =1 , pady=10, padx= 5, ipadx= 25)




root.mainloop()