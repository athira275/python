from tkinter import *
input=Tk()
def clickhere():
    label=Label(text='hai'+m.get())
    label.pack()
m=Entry(input,width=40,bg='green')
m.pack()
button1=Button(text='clickhere',bg='black',fg='white',font='poppins',command=clickhere)
button1.pack()
input.geometry('300x400')
input.mainloop()
