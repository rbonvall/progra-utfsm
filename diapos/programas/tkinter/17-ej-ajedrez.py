from Tkinter import *

w = Tk()
tablero = Frame(w)
jugadores = Frame(w)

for i in range(1, 9):
    for j in range(1, 9):
        if (i + j) % 2 == 0:
            color = 'black'
        else:
            color = 'white'
        b = Button(tablero, bg=color)
        b.grid(row=i, column=j)



tablero.pack()
entrada.pack()
salida.pack()
w.mainloop()
