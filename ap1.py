from tkinter import *
data=Tk()
label=Label(data,text='hai dear',fg='blue',bg='pink')
label.grid(row=0,column=0)
label=Label(data,text='hai dear',fg='blue',bg='pink')
label.grid(row=1,column=1)
label=Label(data,text='hai dear',fg='blue',bg='pink')
label.grid(row=2,column=2)
data.geometry('200x300')
data.minsize(300,400)
data.maxsize(200,600)
label.mainloop()