
from tkinter import *
import PIL
import tkinter as t
from PIL import *
from PIL import Image, ImageTk, ImagePalette
from tkinter import ttk
from tkinter import messagebox as msg
import mysql.connector
import pandas as pd

#Window
win1=Tk()
win1.geometry('500x300')
win1.title('Enter Patient Details')
win1.maxsize(500,300)
   
#Canvas
c = Canvas(win1, width=500, height=300,bg='#BF613F')
c.pack(fill='both', expand=True)

#Labels
c.create_text(66, 50, text = 'Patient ID', font=("Dubai",17))
c.create_text(36, 90, text = 'Item', font=("Dubai",17))
c.create_text(47, 130, text = 'Amount', font=("Dubai",17))

#TextBox
n1=StringVar()
t1=t.Entry(win1, font='Dubai 18' ,textvariable=n1)
c.create_window(290,50,window=t1)

n2=StringVar()
t2=t.Entry(win1, font='Dubai 18' ,textvariable=n2)
c.create_window(290,90,window=t2)

n3=StringVar()
t3=t.Entry(win1, font='Dubai 18' ,textvariable=n3)
c.create_window(290,130,window=t3)

#Functions
def add():
    conn = mysql.connector.connect(host='localhost',
                                 database='project',
                                 user='root',
                                 password='root',
                                 charset='utf8')
    
    cursor=conn.cursor()
                       
    row=cursor.execute("Insert into bills values('"+n1.get()+
                       "', '"+n2.get()+"', '"+n3.get()+"')")
    conn.commit()
    msg.showinfo('Done',"Record Added Successfully")

    win1.destroy()
    import mb

#Button
ok = Button(win1, text= 'Add', font = 'Dubai 17', command=add,bg='#BF8969')
c.create_window(250, 250, window=ok)

win1.mainloop()


