from tkinter import *
data=Tk()
data.title("world")
data.geometry('500x500')

var_English=StringVar(value='no')
var_Maths=StringVar(value='no')
var_Social=StringVar(value='no')
var_Science=StringVar(value='no')

c=Checkbutton(data,fg='white',bg='blue',text='English',variable=var_English,onvalue='ok',offvalue='no')
c.pack()
d=Checkbutton(data,text='Maths',variable=var_Maths,onvalue='ok',offvalue='no')
d.pack()
e=Checkbutton(data,text='Social',variable=var_Social,onvalue='ok',offvalue='no')
e.pack()
f=Checkbutton(data,text='Science',variable=var_Science,onvalue='ok',offvalue='no')
f.pack()

def click():
    selected_values= f"English:{var_English.get()},Maths:{var_Maths.get()},Social:{var_Social.get()},Science:{var_Science.get()}"
    my_label=Label(data,text=selected_values)
    my_label.pack()

b1=Button(data,text='show value',command=click)
b1.pack()
data.mainloop()