from tkinter import * #importing the package

root = Tk()`##to form the main page
def myClick():

  w = Label(root, text="Hello, world!")
  v = Label(root, text="Hello, world!2")
  w.pack()
myButton=Button(root,text="click me!",command=myClick) #button
myButton.pack() #pack into main page

#w.grid(row=0,column=0) ##we can give posisiton to text
#v.grid(row=6,column=15)
root.mainloop() ##to run as continous loop
