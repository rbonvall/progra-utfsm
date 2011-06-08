from Tkinter import *
from random import choice

def jugada():
    return choice('piedra papel tijera'.split())

w = Tk()
botones = Frame(w)

humano = StringVar()
humano.set('0')
computador = StringVar()
computador.set('0')

def gano_humano():
    humano.set(int(humano.get()) + 1)
def gano_computador():
    computador.set(int(computador.get()) + 1)

marcador = StringVar()
def actualizar_marcador():
    marcador.set('{0}-{1}'.format(humano.get(), computador.get()))
actualizar_marcador()

mensaje = StringVar()
def actualizar_mensaje(j):
    mensaje.set('El computador eligio ' + j)

def humano_piedra():
    comp = jugada()
    actualizar_mensaje(comp)
    if comp == 'papel':
        gano_computador()
    elif comp == 'tijera':
        gano_humano()
    actualizar_marcador()

def humano_papel():
    comp = jugada()
    actualizar_mensaje(comp)
    if comp == 'tijera':
        gano_computador()
    elif comp == 'piedra':
        gano_humano()
    actualizar_marcador()

def humano_tijera():
    comp = jugada()
    actualizar_mensaje(comp)
    if comp == 'piedra':
        gano_computador()
    elif comp == 'papel':
        gano_humano()
    actualizar_marcador()

b_piedra = Button(botones, text='Piedra', command=humano_piedra)
b_papel  = Button(botones, text='Papel', command=humano_papel)
b_tijera = Button(botones, text='Tijera', command=humano_tijera)

b_piedra.pack(side='left')
b_papel.pack(side='left')
b_tijera.pack(side='left')

l_marcador = Label(textvariable=marcador, font=('Arial', 20))
l_resultado = Label(textvariable=mensaje)

l_marcador.pack(side='top')
l_resultado.pack(side='top')
botones.pack(side='top')

w.title('Cachipun')
w.mainloop()
