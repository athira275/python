from tkinter import *
data=Tk()
def clickhere():
    label=Label(text='hai')
    label.pack()
button1=Button(text='clickhere',bg='black',fg='white',font='poppins',command=clickhere)
button1.pack()
data.geometry('300x400')
data.mainloop()