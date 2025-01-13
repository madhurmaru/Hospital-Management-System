from tkinter import *
import PIL
import tkinter as t
from PIL import *
from PIL import Image, ImageTk, ImagePalette
from tkinter import ttk
from tkinter import messagebox as msg
import mysql.connector
import pandas as pd

win1=Tk()
win1.geometry('500x500')
win1.title('Enter Patient Details')
win1.maxsize(500,500)
   
c = Canvas(win1, width=500, height=500,bg='#BF613F')
c.pack(fill='both', expand=True)

c.create_text(66, 50, text = 'Patient ID', font=("Dubai",17))
c.create_text(85, 90, text = 'Patient Name', font=("Dubai",17))
c.create_text(47, 130, text = 'D.O.B', font=("Dubai",17))
c.create_text(35, 170, text = 'Age', font=("Dubai",17))
c.create_text(73, 210, text = 'Contact No.', font=("Dubai",17))
c.create_text(63, 250, text = 'App_Date', font=("Dubai",17))
c.create_text(63, 290, text = 'App_Time', font=("Dubai",17))
c.create_text(45, 330, text = 'Doctor', font=("Dubai",17))

n1=StringVar()
t1=t.Entry(win1, font='Dubai 18' ,textvariable=n1)
c.create_window(300,50,window=t1)

n2=StringVar()
t2=t.Entry(win1, font='Dubai 18' ,textvariable=n2)
c.create_window(300,90,window=t2)

n3=StringVar()
t3=t.Entry(win1, font='Dubai 18' ,textvariable=n3)
c.create_window(300,130,window=t3)

n4=StringVar()
t4=t.Entry(win1, font='Dubai 18' ,textvariable=n4)
c.create_window(300,170,window=t4)

n5=StringVar()
t5=t.Entry(win1, font='Dubai 18' ,textvariable=n5)
c.create_window(300,210,window=t5)

n6=StringVar()
t6=t.Entry(win1, font='Dubai 18' ,textvariable=n6)
c.create_window(300,250,window=t6)

n7=StringVar()
t7=t.Entry(win1, font='Dubai 18' ,textvariable=n7)
c.create_window(300,290,window=t7)

n8=StringVar()
t8=t.Entry(win1, font='Dubai 18' ,textvariable=n8)
c.create_window(300,330,window=t8)

def add():
    conn = mysql.connector.connect(host='localhost',
                                 database='project',
                                 user='root',
                                 password='root',
                                 charset='utf8')
    
    cursor=conn.cursor()
                       
    row=cursor.execute("Insert into appointments values('"+n1.get()+"', '"
                       +n2.get()+"', '"+n6.get()+"', '"+n7.get()+"', '"
                       +n8.get()+"')")
    row1=cursor.execute("Insert into pat values('"+n1.get()+"', '"+n2.get()+
                        "','"+n3.get()+"', '"+n5.get()+"', '"+n4.get()+"', '"
                        +n8.get()+"')")
    conn.commit()

    win1.destroy()
    import appointment
    
def re():
    win1.destroy()
    import appointment

ok = Button(win1, text= 'Add', font = 'Dubai 17', bg='#BF8969', command=add)
c.create_window(200, 400, window=ok)

back = Button(win1, text= 'Back', font = 'Dubai 17', bg='#BF8969', command=re)
c.create_window(300, 400, window=back)

win1.mainloop()


