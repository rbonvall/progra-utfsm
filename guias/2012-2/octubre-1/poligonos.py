from turtle import *
from math import sin, cos, tan, pi

def numero_de_lados(poligono):
    return len(poligono)

def distancia(p, q):
    xp, yp = p
    xq, yq = q
    dx = xp - xq
    dy = yp - yq
    return (dx ** 2 + dy ** 2) ** 0.5

def calcular_perimetro(poligono):
    n = numero_de_lados(poligono)
    perimetro = distancia(poligono[0], poligono[n - 1])
    for i in range(n - 1):
        perimetro += distancia(poligono[i], poligono[i + 1])
    return perimetro

def dibujar(poligono):
    up()
    x, y = poligono[-1]
    goto(x, y)
    down()
    for x, y in poligono:
        goto(x, y)

def trasladar(poligono, dx, dy):
    nuevo = []

    for x, y in poligono:
        nuevo.append((x + dx, y + dy))
    return nuevo

def escalar(poligono, f):
    nuevo = []
    for x, y in poligono:
        nuevo.append((f * x, f * y))
    return nuevo

def crear_poligono_regular(n, lado):
    nuevo = []
    for i in range(n):
        x = lado * cos(2 * pi * i / n)
        y = lado * sin(2 * pi * i / n)
        nuevo.append((x, y))
    return nuevo

def encerrar(poligono):
    w = min(x for x, y in poligono)
    e = max(x for x, y in poligono)
    s = min(y for x, y in poligono)
    n = max(y for x, y in poligono)
    cuadrado = [(w, n), (e, n), (e, s), (w, s)]
    dibujar(cuadrado)



p = [(5, 1), (6, 3), (6, 0), (4, -1), (3, 0)]
