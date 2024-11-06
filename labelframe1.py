from tkinter import *
data=Tk()
data.title('document')
data.geometry('300x300')
def clickhere():
    label=Label(frame,text='hai')
    label.grid(row=7,column=8)


frame=LabelFrame(data,text='label frame',padx=100,pady=100,bg='black',fg='white')
frame.grid(row=1,column=3)
button=Button(frame,text='click here',command='click here')
button.grid(row=2,column=5)
button=Button(frame,text='quit',command='quit')
button.grid(row=5,column=6)
data.mainloop()
