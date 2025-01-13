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
win1.geometry('500x500')
win1.title('Enter Patient Details')

#Canvas
c = Canvas(win1, width=400, height=400,bg='#BF613F')
c.pack(fill='both', expand=True)

#Labels
c.create_text(66, 50, text = 'Patient ID', font=("Dubai",17))
c.create_text(85, 90, text = 'Patient Name', font=("Dubai",17))
c.create_text(47, 130, text = 'D.O.B', font=("Dubai",17))
c.create_text(35, 170, text = 'Age', font=("Dubai",17))
c.create_text(73, 210, text = 'Contact No.', font=("Dubai",17))
c.create_text(63, 250, text = 'App_Date', font=("Dubai",17))
c.create_text(63, 290, text = 'App_Time', font=("Dubai",17))
c.create_text(45, 330, text = 'Doctor', font=("Dubai",17))


#TextBox
n1=StringVar()
t1=t.Entry(win1, font='Dubai 18' ,textvariable=n1)
c.create_window(290,50,window=t1)

n2=StringVar()
t2=t.Entry(win1, font='Dubai 18' ,textvariable=n2)
t2.configure(state = 'readonly')
c.create_window(290,90,window=t2)

n3=StringVar()
t3=t.Entry(win1, font='Dubai 18' ,textvariable=n3)
t3.configure(state = 'readonly')
c.create_window(290,130,window=t3)

n4=StringVar()
t4=t.Entry(win1, font='Dubai 18' ,textvariable=n4)
t4.configure(state = 'readonly')
c.create_window(290,170,window=t4)

n5=StringVar()
t5=t.Entry(win1, font='Dubai 18' ,textvariable=n5)
t5.configure(state = 'readonly')
c.create_window(290,210,window=t5)

n6=StringVar()
t6=t.Entry(win1, font='Dubai 18' ,textvariable=n6)
t6.configure(state = 'readonly')
c.create_window(290,250,window=t6)

n7=StringVar()
t7=t.Entry(win1, font='Dubai 18' ,textvariable=n7)
t7.configure(state = 'readonly')
c.create_window(290,290,window=t7)

n8=StringVar()
t8=t.Entry(win1, font='Dubai 18' ,textvariable=n8)
t8.configure(state = 'readonly')
c.create_window(290,330,window=t8)





def ok():
    t1.configure(state = 'readonly')
    conn = mysql.connector.connect(host='localhost',
                                 database='project',
                                 user='root',
                                 password='root',
                                 charset='utf8')
    cursor=conn.cursor()
    row=cursor.execute("select * from appointments where patient_id='"
                       +n1.get()+"';")

    df=pd.DataFrame(cursor.fetchall())
    

    if(len(df.index)== 1):
                t2.configure(state='normal')
                t3.configure(state='normal')
                t4.configure(state='normal')
                t5.configure(state='normal')
                t6.configure(state='normal')
                t7.configure(state='normal')
                t8.configure(state='normal')
                
                n1.set(df.loc[0,0])
                n2.set(df.loc[0,1])
                n6.set(df.loc[0,2])
                n7.set(df.loc[0,3])
                n8.set(df.loc[0,4])

    row=cursor.execute("select * from pat where patient_id='"+n1.get()+"';")

    df=pd.DataFrame(cursor.fetchall())
    

    if(len(df.index)== 1):
        n3.set(df.loc[0,2])
        n5.set(df.loc[0,3])
        n4.set(df.loc[0,4])
    
                
def update():
    abc = mysql.connector.connect(host='localhost',
                                 database='project',
                                 user='root',
                                 password='root',
                                 charset='utf8')
    cursor=abc.cursor()
    a=cursor.execute("update appointments set patient_name='"+n2.get()
                     +"', appointment_date='"+n6.get()+
                     "', appointment_time='"+n7.get()+
                     "',doctor_name='"+n8.get()+
                     "' where patient_id='"+n1.get()+"';")

    a1=cursor.execute("update pat set patient_name='"+n2.get()
                      +"', dob='"+n3.get()+"', no ='"+n5.get()
                      +"',age ='"+n4.get()+"',doctor='"+n8.get()
                      +"' where patient_id='"+n1.get()+"';") 

    abc.commit()
    msg.showinfo('Done', 'Record updated successfully')
    win1.destroy()
    import appointment

def back():
    win1.destroy()
    import appointment

ok = Button(win1, text= '+', font = 'Dubai 15', bg='#BF8969',command=ok)
c.create_window(440, 50, window=ok)

upd = Button(win1, text= 'Update', font = 'Dubai 15',
             bg='#BF8969',command=update)
c.create_window(200, 400, window=upd)

back = Button(win1, text= 'Back', font = 'Dubai 15',
              bg='#BF8969',command=back)
c.create_window(290, 400, window=back)

win1.mainloop()




