from tkinter import *
window=Tk()
window.title('Document')
window.geometry('400x400')

options=[
    'one',
    'two',
    'three',
    'four',
    'five',
]
def show():
    label=Label(window,text=clicked.get())    
    label.pack()
    
clicked=StringVar()
clicked.set(options[0]) 
drop=OptionMenu(window,clicked,*options)
drop.pack()

my_button=Button(window,text='submit',command=show)
my_button.pack()
window.mainloop()
