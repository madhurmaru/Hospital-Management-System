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
win1.title('Enter Details')
win1.maxsize(400,200)

#Canvas
c = Canvas(win1, width=400, height=200,bg='#BF613F')
c.pack(fill='both', expand=True)

#Labels
c.create_text(92,30,text='Enter Patient ID', font=('Dubai',16))
c.create_text(95,70,text='Enter Item Name', font=('Dubai',16))

#TextBox
n=StringVar()
t=Entry(win1, font='Dubai 18' ,textvariable=n, width=12)
c.create_window(270,30,window=t)

n1=StringVar()
t1=Entry(win1, font='Dubai 18' ,textvariable=n1, width=12)
c.create_window(270,70,window=t1)

#Functions

def de():
    conn = mysql.connector.connect(host='localhost',
                                 database='project',
                                 user='root',
                                 password='root',
                                 charset='utf8')
    cursor=conn.cursor()
    row=cursor.execute("Delete from bills where pid='"+n.get()+
                       "'and item='"+n1.get()+"';")
    
    conn.commit()
    msg.showinfo('Done','Record Deleted Successfully')
    win1.destroy()
    import mb
    
def back():
    win1.destroy()
    import mb
    
#Buttons   
de=Button(win1, text='Delete', font='Dubai 15', command=de,bg='#BF8969')
c.create_window(140,130,window=de)

de=Button(win1, text='Back', font='Dubai 15', command=back, bg='#BF8969')
c.create_window(220,130,window=de)

win1.mainloop()


