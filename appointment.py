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

#window
win=Tk()
win.geometry('1366x768')
win.title('Appointment Management')

#Creating Canvas
c = Canvas(win, width=1366, height=768, bg='#BF613F')
c.pack(fill='both', expand=True)

c.create_text(80, 40, text='Task Panel', font='Dubai 20')
c.create_line(280,0,280,700, fill="#734338", width=3)

def std():
                win.destroy()
                import std

def pat():
                win.destroy()
                import pat

def mb():
                win.destroy()
                import mb

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

b1=Button(win, text='Appointment Management',font=('Dubai',15),
          bg='#BF8969')
c.create_window(130, 90, window=b1)

b2=Button(win, text='Staff Details',font=('Dubai',15),
          command=std, bg='#BF8969')
c.create_window(70, 140, window=b2)

b3=Button(win, text='Patient Details',font=('Dubai',15),
          command=pat, bg='#BF8969')
c.create_window(80, 190, window=b3)

b4=Button(win, text='Manage Bills',font=('Dubai',15),
          command=mb, bg='#BF8969')
c.create_window(70, 240, window=b4)

b5=Button(win, text='Data Backup',font=('Dubai',15),
          command=backup, bg='#BF8969')
c.create_window(70, 290, window=b5)


#Functions
def add():
   win.destroy()
   import app

def update():
   win.destroy()
   import update

def delete():
   win.destroy()
   import delete

def back():
   win.destroy()
   import win2
   
#Adding Buttons
b1=Button(win, text='Add',font=('Dubai',13),
          command=add, bg='#BF8969')
c.create_window(310, 30, window=b1)

b2=Button(win, text='Update',font=('Dubai',13),
          command=update, bg='#BF8969')
c.create_window(380, 30, window=b2)

b3=Button(win, text='Delete',font=('Dubai',13),
          command=delete, bg='#BF8969')
c.create_window(450, 30, window=b3)

#Connecting to MySQl
conn = mysql.connector.connect(host='localhost',database='project',
                               user='root' ,
                               password='root',
                               charset='utf8')
cursor = conn.cursor()
cursor.execute("select * from appointments")
ls = pd.DataFrame(cursor.fetchall())
y=80
for i in range(0, len(ls.index)):
   x=360
   y=y+40
   for j in range(0, len(ls.columns)):
        n=StringVar()
        usr=t.Entry(win, font='Dubai 18' ,textvariable=n,width=10,
                    state='disabled')
        c.create_window(x,y,window=usr)       
        usr.config(disabledbackground='#A65E44',disabledforeground='black')
        n.set(str(ls.iloc[i][j]))
        x=x+170

#Labels   
c.create_text(350,80, text = 'Patient ID', font=("Dubai",19))
c.create_text(530,80, text = 'Patient Name', font=("Dubai",19))
c.create_text(700,80, text = 'Date', font=("Dubai",19))
c.create_text(870,80, text = 'Time', font=("Dubai",19))
c.create_text(1040,80, text = 'Doctor', font=("Dubai",19))

win.mainloop()



