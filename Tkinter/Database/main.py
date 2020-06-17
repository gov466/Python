##creating a database with pythin tkinter
from tkinter import  *
from PIL import Image,ImageTk
import sqlite3 

root =Tk()
root.title("my database") 
root.geometry("400x400")

##dataase
##create a database
conn = sqlite3.connect('Address_bool.db')
#curser
c = conn.cursor()

#create table(need to create once so commented later)
 
#c.execute("""CREATE TABLE address(
 #           first_name text,
  #          last_name text,
   #         address text,
    #        city text,
     #       state text,
      #      zipcode integer)""")

def submit():
    conn = sqlite3.connect('Address_bool.db')
    #curser
    c = conn.cursor()
    #insert into table
    c.execute("INSERT INTO address VALUES(:f_name,:l_name, :address,:city , :state, :zipcode)",
              #dictionary
              {
                'f_name':f_name.get(),
                'l_name':l_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()
                       
                  })
    
    conn.commit()

    #close connection
    conn.close()
    ##clear the text box
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)


##query functm
def  query():
    conn = sqlite3.connect('Address_bool.db')
    #curser
    c = conn.cursor()
    #queery the database
    c.execute("SELECT *, oid FROM address")
    records=c.fetchall()
    #print(records)
    
    print_records = ''
    for record in records:
        #print_records += str(record)+"\n"
        print_records += str(record[0]) + " "+ str(record[1])+"\n"
    query_label =Label(root, text =print_records)
    query_label.grid(row=8, column=0, columnspan = 2)
    
    
    
    conn.commit()

    #close connection
    conn.close()

f_name=Entry(root,width=30)
f_name.grid(row=0, column=1, padx=20)

l_name=Entry(root,width=30)
l_name.grid(row=1, column=1, padx=20)

address=Entry(root,width=30)
address.grid(row=2, column=1, padx=20)

city=Entry(root,width=30)
city.grid(row=3, column=1, padx=20)

state=Entry(root,width=30)
state.grid(row=4, column=1, padx=20)

zipcode =Entry(root,width=30)
zipcode.grid(row=5, column=1, padx=20)

 


#create textbox labels
f_name_label=Label(root,text ="First name")
f_name_label.grid(row=0,column=0)

l_name_label=Label(root,text ="Last name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text ="address")
address_label.grid(row=2,column=0)

city_label=Label(root,text ="City")
city_label.grid(row=3,column=0)

state_label=Label(root,text ="State")
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text ="Zipcode")
zipcode_label.grid(row=5,column=0)

 
##create submit buttons

submit_button =Button(root,text ="Add record to database", command=submit)
submit_button.grid(row=6 ,column=0, columnspan =2, pady=10 ,padx= 10, ipadx=100) 

#query button
query_button= Button(root,text="show records", command= query)
query_button.grid(row=7, column =0, columnspan= 2, pady=10, padx= 10, ipadx= 137)



#commitchanges
conn.commit()

#close connection
conn.close()

root.mainloop()
