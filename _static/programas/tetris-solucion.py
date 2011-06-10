from numpy import *
from random import choice
from rotar import rotar90

piezas = {
    'I': array([[1, 1, 1, 1]]),
    'J': array([[1, 1, 1],
                [0, 0, 1]]),
    'L': array([[1, 1, 1],
                [1, 0, 0]]),
    'O': array([[1, 1],
                [1, 1]]),
    'S': array([[0, 1, 1],
                [1, 1, 0]]),
    'Z': array([[1, 1, 0],
                [0, 1, 1]]),
    'T': array([[1, 1, 1],
                [0, 1, 0]]),
}

def pieza_al_azar():
    return piezas[choice(list(piezas))]

def tstr(juego):
    m, n = juego.shape
    linea = '+' + '-' * n + '+'
    numeros = ' ' + ''.join(map(str, range(n))) + ' '
    s = str(juego.astype(int))
    s = s.replace('[[', '|')
    s = s.replace(' [', '|')
    s = s.replace(']]', '|')
    s = s.replace(']', '|')
    s = s.replace(' ', '')
    s = s.replace('0', ' ')
    s = s.replace('1', '#')
    return '\n'.join([linea, s, linea, numeros])

def pstr(pieza):
    s = str(pieza.astype(int))
    s = s.replace('[', '')
    s = s.replace(']', '')
    s = s.replace(' ', '')
    s = s.replace('0', ' ')
    s = s.replace('1', '#')
    return s


def poner_pieza(pieza, juego, col):
    M, N = juego.shape
    m, n = pieza.shape
    for i in range(M + 1 - m):
        ventana = juego[i : i + m, col : col + n]
        suma = pieza + ventana
        if suma.max() > 1:
            i = i - 1
            break
    juego[i : i + m, col : col + n] += pieza

def eliminar_fila(juego, i):
    juego[1:i + 1, :] = juego[0:i, :]
    juego[0, :] = 0

def limpiar_filas(juego):
    M, N = juego.shape
    filas_por_eliminar = []
    for i in range(M):
        if (juego[i, :] > 0).all():
            filas_por_eliminar.append(i)
    for i in filas_por_eliminar:
        eliminar_fila(juego, i)

if __name__ == '__main__':

    juego = zeros((20, 10)).astype(int)
    pieza = pieza_al_azar()

    while True:
        print
        print pstr(pieza)
        print tstr(juego)
        print '0-9)  poner pieza'
        print 'r)    rotar pieza'
        print 'q)    terminar el juego'
        opcion = ''
        while len(opcion) != 1 or opcion not in 'rq0123456789':
            opcion = raw_input('Ingrese su opcion: ')

        if opcion == 'r':
            pieza = rotar90(pieza)
        elif opcion == 'q':
            exit()
        else:
            j = int(opcion)
            poner_pieza(pieza, juego, j)
            limpiar_filas(juego)
            pieza = pieza_al_azar()

