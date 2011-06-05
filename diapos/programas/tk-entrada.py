from Tkinter import *

w = Tk()

v = StringVar()
e = Entry(w, textvariable=v)
e.pack()

def imprimir():
    print v.get()

def cambiar():
    v.set('Hola')

w.mainloop()

