from tkinter import *
from tkinter import messagebox
data=Tk()
data.geometry('300x300')

def showmsg():
    messagebox.showinfo(title='click here',message='heloo')

def showmsg1():
    messagebox.showerror('clicked',message='click here')

def showmsg2():
    messagebox.showwarning('clicked')


button1=Button(text='clickhere',bg='black',fg='white',font='poppins',command=showmsg)
button1.pack()
button2=Button(text='clickhere',bg='black',fg='white',font='poppins',command=showmsg1)
button2.pack()
button3=Button(text='clickhere',bg='black',fg='white',font='poppins',command=showmsg2)
button3.pack()

data.mainloop()