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
win1=Tk()
win1.maxsize(400,200)
win1.title('Enter Details')

#Canvas
c = Canvas(win1, width=400, height=200, bg='#BF613F')
c.pack(fill='both', expand=True)

#Input
c.create_text(90,30,text='Enter Patient ID', font=('Dubai',16))

n=StringVar()
t=Entry(win1, font='Dubai 18' ,textvariable=n, width=12)
c.create_window(270,30,window=t)

#Button Functions
def de():
    conn = mysql.connector.connect(host='localhost',
                                 database='project',
                                 user='root',
                                 password='root',
                                 charset='utf8')
    cursor=conn.cursor()
    row=cursor.execute("Delete from appointments where patient_id='"
                       +n.get()+"';")

    row1=cursor.execute("Delete from pat where patient_id='"+n.get()+"';")
    conn.commit()
    msg.showinfo('Done','Record Deleted Successfully')
    win1.destroy()
    import appointment
    
def back():
    win1.destroy()
    import appointment
    
#Buttons    
de=Button(win1, text='Delete', font='Dubai 15', command=de,bg='#BF8969')
c.create_window(140,120,window=de)

re=Button(win1, text='Back', font='Dubai 15', command=back,bg='#BF8969')
c.create_window(220,120,window=re)

win1.mainloop()



