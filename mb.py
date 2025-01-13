#Importing_required_libraries
from tkinter import *
import PIL
import tkinter as t
from PIL import *
from PIL import Image, ImageTk, ImagePalette
from tkinter import ttk
from tkinter import messagebox as msg
import mysql.connector
import pandas as pd

win=t.Tk()
win.geometry('1366x768')
win.title('Task Management')

#Creating Canvas
c = Canvas(win, width=1366, height=768, bg='#BF613F')
c.pack(fill='both', expand=True)

c.create_text(80, 40, text='Task Panel', font='Dubai 20')
c.create_line(280,0,280,700, fill="#734338", width=3)

def apn():
                win.destroy()
                import appointment

def std():
                win.destroy()
                import std

def pat():
                win.destroy()
                import pat

def backup():
    #connecting to mysql
    conn = mysql.connector.connect(host='localhost',
                                 database='project',
                                 user='root',
                                 password='root',
                                 charset='utf8')
    cursor=conn.cursor()
    row=cursor.execute("select * from pat")
    df=pd.DataFrame(cursor.fetchall())
    df.to_csv("pat.csv")

    row=cursor.execute("select * from staff")
    df=pd.DataFrame(cursor.fetchall())
    df.to_csv("staff.csv")

    row=cursor.execute("select * from appointments")
    df=pd.DataFrame(cursor.fetchall())
    df.to_csv("appointments.csv")

    row=cursor.execute("select * from bills")
    df=pd.DataFrame(cursor.fetchall())
    df.to_csv("bills.csv")
    


                
#Adding Buttons
b1=Button(win, text='Appointment Management',font=('Dubai',15), bg='#BF8969')
c.create_window(130, 90, window=b1)

b2=Button(win, text='Staff Details',font=('Dubai',15),command=std, bg='#BF8969')
c.create_window(70, 140, window=b2)

b3=Button(win, text='Patient Details',font=('Dubai',15), command=pat, bg='#BF8969')
c.create_window(80, 190, window=b3)

b4=Button(win, text='Manage Bills',font=('Dubai',15), bg='#BF8969')
c.create_window(70, 240, window=b4)

b5=Button(win, text='Data Backup',font=('Dubai',15),
          command=backup, bg='#BF8969')
c.create_window(70, 290, window=b5)


c.create_text(350,80, text = 'Patient ID', font=("Dubai",19))
n=StringVar()
usr=t.Entry(win, font='Dubai 18' ,textvariable=n,width=10,bg='#A65E44')
c.create_window(520,80,window=usr)
usr.focus_set()

def a():
    c.create_text(370,130, text = 'Patient Name', font=("Dubai",19))
    c.create_text(360,200, text = 'S.No', font=("Dubai",19))
    c.create_text(530,200, text = 'Item', font=("Dubai",19))
    c.create_text(700,200, text = 'Amount', font=("Dubai",19))
           
    conn = mysql.connector.connect(host='localhost',database='project',user='root' , password='root',charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select Patient_Name from pat where Patient_ID = '"+n.get()+"'")
    ls = pd.DataFrame(cursor.fetchall())

    n1=StringVar()
    usr=t.Entry(win, font='Dubai 18' ,textvariable=n1,width=10)
    c.create_window(520,130,window=usr)
    usr.config(state = "disabled")
    usr.config(disabledbackground='#A65E44',disabledforeground='black')
    n1.set(str(ls.iloc[0,0]))
    
    cursor.execute("select * from bills where pid = '"+n.get()+"'")
    ls = pd.DataFrame(cursor.fetchall())
    y=200
    for i in range(0, len(ls.index)):
       x=530
       y=y+40
       n2=StringVar()
       usr=t.Entry(win, font='Dubai 18' ,textvariable=n2,width=10)
       c.create_window(360,y,window=usr)
       usr.config(state = "disabled")
       usr.config(disabledbackground='#A65E44',disabledforeground='black')
       n2.set('        '+str(i+1))
       for j in range(0, len(ls.columns)-1):
           n2=StringVar()
           usr=t.Entry(win, font='Dubai 18' ,textvariable=n2,width=10)
           c.create_window(x,y,window=usr)
           usr.config(state = "disabled")
           usr.config(disabledbackground='#A65E44',disabledforeground='black')
           n2.set(str(ls.iloc[i][j+1]))
           x=x+170
           
    x=x-170
    y=y+60
    c.create_text(x-140,y, text = 'Total', font=("Dubai",19))
    n3=StringVar()
    usr=t.Entry(win, font='Dubai 18' ,textvariable=n3,width=10)
    c.create_window(x,y,window=usr)
    usr.config(state = "disabled")
    usr.config(disabledbackground='#A65E44',disabledforeground='black')            
    n3.set(str(ls[2].sum()))
    
b5=Button(win, text='+',font=('Dubai',15),command=a,bg='#BF8969')
c.create_window(620,80,window=b5)


def add():
   win.destroy()
   import add

def update():
   win.destroy()
   import updat

def delete():
   win.destroy()
   import dele

def back():
   win.destroy()
   import win2
   
#Adding Buttons
b1=Button(win, text='Add',font=('Dubai',13), command=add, bg='#BF8969')
c.create_window(310, 30, window=b1)

b2=Button(win, text='Delete',font=('Dubai',13), command=delete, bg='#BF8969')
c.create_window(380, 30, window=b2)

'''b4=Button(win, text='Back',font=('Dubai',13),command=back)
c.create_window(780, 30, window=b4)
'''


win.mainloop()
