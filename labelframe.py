from tkinter import *
window=Tk()
window.title('hkjh')
window.geometry('500x500')
def clickhere():
    label=Label(frame,text='heloo welcome')
    label.grid(row=7,column=8)


frame=LabelFrame(window,text='this is labelframe',padx=100,pady=100,bg='green')
frame.grid(row=1,column=3)
button=Button(frame,text='click here',command=clickhere)
button.grid(row=5,column=5)
button1=Button(frame,text='quit',command=window.quit)
button1.grid(row=5,column=6)

window.mainloop()