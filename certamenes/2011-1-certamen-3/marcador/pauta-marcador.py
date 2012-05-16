from Tkinter import *

NR_JUEGOS = 7

w = Tk()

# JUEGO ACTUAL
juego_actual = StringVar()
juego_actual.set('0')
# FIN JUEGO ACTUAL

modelos_a = [StringVar(value='0') for i in range(NR_JUEGOS)]
modelos_b = [StringVar(value='0') for i in range(NR_JUEGOS)]
labels_a = [Label(w, textvariable=modelos_a[i], width=2) for i in range(NR_JUEGOS)]
labels_b = [Label(w, textvariable=modelos_b[i], width=2) for i in range(NR_JUEGOS)]

def punto_a():
    j = int(juego_actual.get())
    a = int(modelos_a[j].get())
    a = a + 1
    modelos_a[j].set(a)
    if a == 11:
        juego_actual.set(j + 1)

def punto_b():
    j = int(juego_actual.get())
    b = int(modelos_b[j].get())
    b = b + 1
    modelos_b[j].set(b)
    if b == 11:
        juego_actual.set(j + 1)

# BOTONES
b_a = Button(w, text='Alicia', width=7, command=punto_a)
b_b = Button(w, text='Benito', width=7, command=punto_b)
# FIN BOTONES

for i in range(NR_JUEGOS):
    labels_a[i].grid(row=0, column=i + 2)
    labels_b[i].grid(row=1, column=i + 2)

ba.grid(row=0, column=1)
bb.grid(row=1, column=1)

w.title('Marcador')
w.mainloop()
