from tkinter import *
data=Tk()
data.title("world")
data.geometry('500x500')
e=Entry(data,width=50,fg='white',bg='blue')
e.grid(row=0,column=0)
e=Entry(data,width=50,fg='white',bg='blue')
e.grid(row=0,column=1)

def clickme():
    my_label=Label(data,text='hello'+" "+e.get())
    my_label.grid(row=3,column=0)
    e.delete(0,END)
def clickme2():
    my_label=Label(data,text='hello'+" "+e.get())
    my_label.grid(row=3,column=1)
    e.delete(0,END)    
mybutton=Button(data,text="enter your name",padx=10,pady=10,bg='blue',fg='white',command=clickme)    
mybutton.grid(row=1,column=0)
mybutton1=Button(data,text="enter your name",padx=10,pady=10,bg='blue',fg='white',command=clickme2)    
mybutton1.grid(row=1,column=1)
data.mainloop()