from Tkinter import *
from numpy import array
from numpy.random import shuffle

ANCHO = 8
ALTO = 8
MINAS = 10
N = ANCHO * ALTO

# Estos son los colores que tienen los numeros del 0 al 8.
colores = 'white blue green red purple black maroon turquoise gray'.split()

# Crear juego al azar.
campo = array([-1] * MINAS + [0] * (N - MINAS))
shuffle(campo)
campo = campo.reshape((ANCHO, ALTO))

# Contar las minas vecinas en cada celda.
for i in range(ANCHO):
    for j in range(ALTO):
        if campo[i, j] != -1:
            vecindad = campo[max(i - 1, 0):i + 2, max(j - 1, 0):j + 2]
            cuenta = (vecindad == -1).sum()
            campo[i, j] = cuenta

def es_mina(i, j):
    return campo[i, j] == -1

w = Tk()

juego_terminado = BooleanVar()
juego_terminado.set(False)

def descubrir_celda(i, j):
    if campo[i, j] == -1:
        botones[i, j].config(bg='red')
    else:
        n = campo[i, j]
        botones[i, j].config(text=n, fg=colores[n])

def crear_controlador(i, j):
    def c():
        if juego_terminado.get():
            return
        descubrir_celda(i, j)
        if es_mina(i, j):
            botones[i, j].config(text='X')
            juego_terminado.set(True)
    return c

botones = {}
for i in range(ANCHO):
    for j in range(ALTO):
        b = Button(w, command=crear_controlador(i, j), width=1,
                      font=('Arial', 12, 'bold'))
        b.grid(row=i, column=j)

        # Guardar el boton en el diccionario
        # para poder referirse a el mas adelante.
        botones[i, j] = b

w.title('Buscaminas')
w.mainloop()

