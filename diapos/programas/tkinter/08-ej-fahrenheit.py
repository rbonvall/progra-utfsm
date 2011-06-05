# coding: utf-8
from Tkinter import *

w = Tk()

var_fahrenheit = StringVar()
e = Entry(w, textvariable=var_fahrenheit)

var_celsius = StringVar()
l = Label(w, textvariable=var_celsius)

def convertir():
    f = float(var_fahrenheit.get())
    c = (f - 32.0) * 5.0 / 9.0
    var_celsius.set('{0:.2f} F = {1:.2f} C'.format(f, c))

b = Button(w, text='F → C', command=convertir)

e.pack()
b.pack()
l.pack()

w.title('Convertir')
w.mainloop()

