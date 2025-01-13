from tkinter import *
import PIL
import tkinter as t
from PIL import *
from PIL import Image, ImageTk, ImagePalette
from tkinter import ttk
from tkinter import messagebox as msg
import mysql.connector
import pandas as pd

#window
win1=Tk()
win1.geometry('500x420')
win1.title('Enter Staff Details')
win1.maxsize(500,420)
   
#Canvas
c = Canvas(win1, width=500, height=420,bg='#BF613F')
c.pack(fill='both', expand=True)

#Labels
c.create_text(60,50, text = 'Staff ID', font=("Dubai",19))
c.create_text(80,90, text = 'Staff Name', font=("Dubai",19))
c.create_text(40,130, text = 'Age', font=("Dubai",19))
c.create_text(50,170, text = 'D.O.B', font=("Dubai",19))
c.create_text(64,210, text = 'Category', font=("Dubai",19))
c.create_text(90,250, text = 'Specialization', font=("Dubai",19))

#TextBox
n1=StringVar()
t1=t.Entry(win1, font='Dubai 18' ,textvariable=n1)
c.create_window(320,50,window=t1)

n2=StringVar()
t2=t.Entry(win1, font='Dubai 18' ,textvariable=n2)
c.create_window(320,90,window=t2)

n3=StringVar()
t3=t.Entry(win1, font='Dubai 18' ,textvariable=n3)
c.create_window(320,130,window=t3)

n4=StringVar()
t4=t.Entry(win1, font='Dubai 18' ,textvariable=n4)
c.create_window(320,170,window=t4)

n5=StringVar()
t5=t.Entry(win1, font='Dubai 18' ,textvariable=n5)
c.create_window(320,210,window=t5)

n6=StringVar()
t6=t.Entry(win1, font='Dubai 18' ,textvariable=n6)
c.create_window(320,250,window=t6)

#On click of Buttons
def add():
    conn = mysql.connector.connect(host='localhost',
                                 database='project',
                                 user='root',
                                 password='root',
                                 charset='utf8')
    
    cursor=conn.cursor()
                       
    row=cursor.execute("Insert into staff values('"+n1.get()+"', '"
                       +n2.get()+"', '"+n3.get()+"','"+n4.get()+
                       "', '"+n5.get()+"', '"+n6.get()+"')")
    conn.commit()

    msg.showinfo('Done','Record Added Successfully')

    win1.destroy()
    import std

ok = Button(win1, text= 'Add', font = 'Dubai 17', bg='#BF8969', command=add)
c.create_window(250, 370, window=ok)


win1.mainloop()


