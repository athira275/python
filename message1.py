from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry('200x300')

def showmsg():
    messagebox.showinfo(title='click here',message='hai')

def showmsg1():
    messagebox.showerror('clicked',message='click here')

def showmsg2():
    messagebox.showwarning('clicked')


button1=Button(text='click here',bg='brown',fg='white',font='poppins',command=showmsg) 
button1.pack()
button2=Button(text='click here',bg='brown',fg='white',font='poppins',command=showmsg1) 
button2.pack()
button3=Button(text='click here',bg='brown',fg='white',font='poppins',command=showmsg2) 
button3.pack()

window.mainloop()     