from Tkinter import *

w = Tk()

var = StringVar()
var.set('')

e = Entry(w, textvariable=var)
e.pack()

def mayus():
    s = var.get()
    var.set(s.upper())

def minus():
    s = var.get()
    var.set(s.lower())

def limpiar():
    var.set('')

b1 = Button(w, text='Mayusculizar', command=mayus)
b1.pack()

b2 = Button(w, text='Minusculizar', command=minus)
b2.pack()

b3 = Button(w, text='Limpiar', command=limpiar)
b3.pack()

w.mainloop()

