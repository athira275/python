from tkinter import *
window=Tk()
def clickhere():
    label=Label(text='heloo welcome')
    label.pack()
button1=Button(text='clickhere',bg='red',fg='white',font='poppins',command=clickhere)
button1.pack()
window.geometry('200x400')
window.mainloop()