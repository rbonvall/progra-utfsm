from Tkinter import *

w = Tk()

f_datos = Frame(w)
f_botones = Frame(w)

l_n = Label(f_datos, text='Nombre:')
e_n = Entry(f_datos)
l_a = Label(f_datos, text='Apellido:')
e_a = Entry(f_datos)
l_e = Label(f_datos, text='Edad:')
e_e = Entry(f_datos)

b_guardar = Button(f_botones, text='Guardar')
b_cerrar = Button(f_botones, text='Cerrar')

l_n.grid(row=0, column=0)
e_n.grid(row=0, column=1)
l_a.grid(row=1, column=0)
e_a.grid(row=1, column=1)
l_e.grid(row=2, column=0)
e_e.grid(row=2, column=1)

b_guardar.pack(side='left')
b_cerrar.pack(side='left')

f_datos.pack()
f_botones.pack()

w.mainloop()

