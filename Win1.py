

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
win1 = Tk()
win1.title('Login')
win1.geometry('769x545')
win1.maxsize(769,545)

#Canvas
c = Canvas(win1, width=769, height=545)
c.pack(fill='both', expand=True)

#Background_Image
bg=PhotoImage(file='bg.png')
c.create_image(0,0, image=bg, anchor='nw')

#Label
c.create_text(250, 230, text = 'User ID', font=("Dubai",22), fill='light blue')
c.create_text(250, 300, text = 'Password', font=("Dubai",22), fill='light blue')

#Text_Box
n=StringVar()
usr=t.Entry(win1, font='Dubai 18' ,textvariable=n)
c.create_window(450,230,window=usr)

enter=StringVar()
passd=t.Entry(win1, font='Dubai 18' ,textvariable=enter, show='*')
c.create_window(450, 300, window=passd)

#Functions_of_Buttons

def login():
    #connecting to mysql
    conn = mysql.connector.connect(host='localhost',
                                 database='project',
                                 user='root',
                                 password='root',
                                 charset='utf8')
    cursor=conn.cursor()
    row=cursor.execute("select * from login where user_id='"+n.get()+
                       "' and password='"+enter.get()+"';")
    df=pd.DataFrame(cursor.fetchall())
    
    if(len(df.index)== 1):
        msg.showinfo('Login Successful','Click on OK to Continue')
        win1.destroy()            
        import win2
        
    else:
        msg.showinfo('Alert','Incorrect Username or Password')
        
    conn.commit()
    
def cls():
    n.set('')
    enter.set('')
 
 
#Buttons
ok = Button(win1, text= '  Login  ', font = 'Dubai 17', bg='light blue', command=login)
c.create_window(300, 380, window=ok)

clear = Button(win1, text= '  Clear  ', font = 'Dubai 17', bg='light blue', command=cls)
c.create_window(450, 380, window=clear)



#Adding Bit_Emoji
icon=Image.open('dr.png')
resized= icon.resize((150,158), Image.LANCZOS)
i2= ImageTk.PhotoImage(resized)
c.create_image(380,100, image=i2)



#usr.focus_set()

win1.mainloop()
