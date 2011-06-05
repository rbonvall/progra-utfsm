from Tkinter import *

def saludar():
    print 'Hola'

w = Tk()

l = Label(w, text='Hola progra')
l.pack()

b1 = Button(w, text='Saludar', command=saludar)
b1.pack()

b2 = Button(w, text='Salir', command=exit)
b2.pack()

w.mainloop()

