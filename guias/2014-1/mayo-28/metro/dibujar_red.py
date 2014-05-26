from turtle import *
from time import sleep
from metro import estaciones, lineas, colores
from figuras import *


def es_estacion_terminal(est):
    for L in lineas:
        estaciones = lineas[L]
        if est == estaciones[0] or est == estaciones[-1]:
            return True
    return False

def es_estacion_combinacion(est):
    c = 0
    for L in lineas:
        estaciones = lineas[L]
        if est in estaciones:
            c += 1
    return c > 1

def misma_linea(est1, est2):
    for L in lineas:
        estaciones = lineas[L]
        if est1 in estaciones and est2 in estaciones:
            return True
    return False

def escalar(lat, lon):
    x = 2000 * (lon + 70.6)
    y = 2000 * (lat + 33.5)
    return (x, y)

def dibujar_lineas():
    shape('turtle')
    speed('slowest')
    width(5)

    for L in lineas:
        print 'Linea', L
        up()
        color(colores[L])
        for est in lineas[L]:
            print 'Estacion', est
            #sleep(0.1)
            lat, lon = estaciones[est]
            x, y = escalar(lat, lon)
            goto(x, y)
            down()

def dibujar_estaciones():
    up()
    color('black')
    speed('fastest')
    width(3)

    for est in estaciones:
        lat, lon = estaciones[est]
        x, y = escalar(lat, lon)
        if es_estacion_combinacion(est):
            dibujar_cuadrado(x, y, 8)
        elif es_estacion_terminal(est):
            dibujar_circunferencia(x, y, 7)
        else:
            dibujar_circunferencia(x, y, 5)

def escribir_nombres():
    up()
    speed('slowest')

    for L in ['2', '4']:
        color(colores[L])

        for est in lineas[L]:
            lat, lon = estaciones[est]
            x, y = escalar(lat, lon)
            goto(x + 10, y - 5)
            down()
            write(est)
            up()


if __name__ == '__main__':
    dibujar_lineas()
    dibujar_estaciones()
    escribir_nombres()
    color('black')
    up()
    home()
    raw_input()

