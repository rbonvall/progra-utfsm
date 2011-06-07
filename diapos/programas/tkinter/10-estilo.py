from Tkinter import *

w = Tk()

b1 = Button(w, text='Lunes')
b2 = Button(w, text='Martes', fg='blue')
b3 = Button(w, text='Miercoles', bg='red')
b4 = Button(w, text='Jueves', bg='yellow', width=30)
b5 = Button(w, text='Viernes', font=('Courier', 20))

b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()

w.mainloop()

