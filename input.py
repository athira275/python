from tkinter import *
window=Tk()

def myclick():
    mylabel=Label(window,text="hello"+" "+e.get())
    mylabel.pack()
    
e=Entry(window,width=50,bg='pink')
e.pack()
e.insert(0,'insert your name')
button=Button(window,text='click here',bg='white',command=myclick)
button.pack()
window.mainloop()
