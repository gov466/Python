from tkinter import  *
from PIL import Image,ImageTk
import sqlite3 

root =Tk()
root.title("my perogram") 
root.geometry("400x400")

##dataase
##create a database
conn = sqlite3.connect('Address_bool.db')
#curser
c = conn.cursor()

#create table
c.execute("""CREATE TABLE addresses(
            first_name text,
            last_name text,
            address text,
            state text,
            zipcode integer)""")

#commitchanges
conn.commit()

#close connection
conn.close()

root.mainloop()
