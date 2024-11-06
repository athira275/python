from tkinter import *
window=Tk()
window.title('Document')
window.geometry('400x400')

def slider():
    ver_label=Label(window,text=vertical_slider.get())
    ver_label.pack()
    hori_label=Label(window,text=horizontal_slider.get())
    hori_label.pack()

vertical_slider=Scale(window,from_=0, to =250,orient=VERTICAL)    
vertical_slider.pack(anchor='w')

horizontal_slider=Scale(window,from_=0, to =250,orient=HORIZONTAL)    
horizontal_slider.pack(anchor='w')

ver_button=Button(window,text='CLICK FOR VALUES',command=slider)
ver_button.pack()
window.mainloop()