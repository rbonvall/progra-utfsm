from turtle import *
from math import pi, cos, sin

def numero_de_lados(p):
    return len(p)

def distancia(a, b):
    xa, ya = a
    xb, yb = b
    dx = xa - xb
    dy = ya - yb
    return (dx ** 2 + dy ** 2) ** 0.5

def calcular_perimetro(p):
    n = numero_de_lados(p)
    perimetro = distancia(p[0], p[n - 1])
    for i in range(n - 1):
        perimetro += distancia(p[i], p[i + 1])
    return perimetro

def escalar(p, f):
    nuevo = []
    for x, y in p:
        nuevo.append((x * f, y * f))
    return nuevo

def trasladar(p, dx, dy):
    nuevo = []
    for x, y in p:
        nuevo.append((x + dx, y + dy))
    return nuevo

def dibujar(p):
    up()
    goto(p[-1])
    down()
    for x, y in p:
        goto(x, y)

def encerrar(p):
    todos_los_x = []
    todos_los_y = []
    for x, y in p:
        todos_los_x.append(x)
        todos_los_y.append(x)
    x0 = min(todos_los_x)
    x1 = max(todos_los_x)
    y0 = min(todos_los_y)
    y1 = max(todos_los_y)
    rectangulo = [(x0, y0), (x0, y1), (x1, y1), (x1, y0)]
    dibujar(rectangulo)

def crear_poligono_regular(n, a):
    poligono = []
    for i in range(n):
        x = a * cos(2 * pi / n)
        y = a * sin(2 * pi / n)
        poligono.append((x, y))
    return poligono


