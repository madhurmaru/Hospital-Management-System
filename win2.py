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


#Window
win=Tk()
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
    
    
def mb():
            win.destroy()
            import mb
                
#Adding Buttons
b1=Button(win, text='Appointment Management',font=('Dubai',15),
          command=apn, bg='#BF8969')
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

     
win.mainloop()






