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


def poner_pieza(pieza, juego, columna):
    # Esta funcion debe modificar el arreglo juego,
    # no debe retornar nada.
    pass

def limpiar_filas(juego):
    # Esta funcion debe modificar el arreglo juego,
    # no debe retornar nada.
    pass


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

