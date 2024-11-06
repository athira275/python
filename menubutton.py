from tkinter import *
window=Tk()
window.title('Document')
window.geometry('400x400')

product=[
    ('sumsung','sumsung'),
    ('vivo','vivo'),
    ('iphone','iphone'),
    ('readme','readme'),
    ('realme','realme'),
    ('asus','asus'),
    ('motto','motto'),
]
choice=StringVar()
choice.set('sumsung')
for text,mode in product:
    Radiobutton(window,text=text,variable=choice,value=mode).pack(anchor='w')

def clickme(value):
    my_label=Label(window,text=value)
    my_label.pack()
mybutton=Button(window,text='click here',command=lambda:clickme(choice.get()))
mybutton.pack()
window.mainloop()        