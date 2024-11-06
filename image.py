from tkinter import *
data=Tk()
def clickhere():
    label=Label(text='hello'+m.get())
    label.pack()
m=Entry(data,width=40,bg='yellow')
m.pack()
button1=Button(text='clickhere',bg='black',fg='white',font='poppins',command=clickhere)
button1.pack()
data.geometry('300x400')
data.mainloop()