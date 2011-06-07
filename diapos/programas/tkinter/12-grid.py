from Tkinter import *

w = Tk()

ln = Label(w, text='Nombre:')
en = Entry(w)
la = Label(w, text='Apellido:')
ea = Entry(w)

ln.grid(row=0, column=0)
en.grid(row=0, column=1)
la.grid(row=1, column=0)
ea.grid(row=1, column=1)

w.mainloop()

