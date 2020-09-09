from tkinter import  *
from PIL import Image, ImageTk

root =Tk()
root.title("Registration form")
root.geometry("350x250")

def submit():
    END

f_name = Entry(root, width=30)  ##entry fields for name, address etc..
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# create textbox labels
f_name_label = Label(root, text="First name")  ##creating textboxes corresponding to names
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Address")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="course")
address_label.grid(row=2, column=0)

city_label = Label(root, text="Semester")
city_label.grid(row=3, column=0)

state_label = Label(root, text="Contact no")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Email id")
zipcode_label.grid(row=5, column=0)

submit_button =Button(root,text ="Submit", command=submit)
submit_button.grid(row=6 ,column=0, columnspan =2, pady=10 ,padx= 10, ipadx=100)


root.mainloop()