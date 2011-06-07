# coding: utf-8

from Tkinter import *

w = Tk()

f_fecha = Frame(w)
f_edad = Frame(w)

l_dia = Label(f_fecha, text='Dia:')
e_dia = Entry(f_fecha, width=5)
l_mes = Label(f_fecha, text='Mes:')
e_mes = Entry(f_fecha, width=5)
l_anno = Label(f_fecha, text='Año:')
e_anno = Entry(f_fecha, width=5)

l_dia.grid(row=0, column=0)
l_mes.grid(row=0, column=1)
l_anno.grid(row=0, column=2)
e_dia.grid(row=1, column=0)
e_mes.grid(row=1, column=1)
e_anno.grid(row=1, column=2)

b = Button(f_edad, text='Calcular')
v = StringVar()
v.set('Usted tiene 21 años')
l_resultado = Label(f_edad, textvariable=v)

b.pack(side='left')
l_resultado.pack(side='left')

f_fecha.pack(side='top')
f_edad.pack(side='top')

w.mainloop()

