#!/usr/bin/env python

import turtle

turtle.title('Laberinto')
turtle.shape('turtle')
turtle.color('brown')
turtle.width(5)
turtle.speed('fastest')

f = 30


fila = ':)'
y = 0
while len(fila) > 0:
    fila = raw_input('> ')
    n = len(fila)
    for x in range(n):
        if fila[x] == 'x' or fila[x] == 'X':
            turtle.up()
            turtle.goto(f * x, f * y)
            turtle.seth(90)
            turtle.down()
            for i in range(4):
                turtle.forward(f)
                turtle.right(90)
    y -= 1

turtle.up()
turtle.goto(-f / 2, +f / 2)
turtle.seth(0)
turtle.down()
turtle.color('navy')
turtle.width(2)
turtle.speed('slowest')

raiz2 = 2 ** 0.5

ruta = raw_input('Ruta: ')
n = len(ruta)
i = 0
distancia = 0
while i < n - 1:
    d = ruta[i]
    s = ruta[i + 1]

    if   d == 'E': turtle.seth(0)
    elif d == 'N': turtle.seth(90)
    elif d == 'O': turtle.seth(180)
    elif d == 'S': turtle.seth(270)

    if   ((d == 'E' and s == 'S') or
          (d == 'S' and s == 'O') or
          (d == 'O' and s == 'N') or
          (d == 'N' and s == 'E')):
        turtle.right(45)
        turtle.forward(f * raiz2)
        distancia += raiz2
        i += 2

    elif ((d == 'E' and s == 'N') or
          (d == 'S' and s == 'E') or
          (d == 'O' and s == 'S') or
          (d == 'N' and s == 'O')):
        turtle.left(45)
        turtle.forward(f * raiz2)
        distancia += raiz2
        i += 2

    else:
        turtle.forward(f)
        distancia += 1
        i += 1

print 'Distancia recorrida:', distancia
raw_input()

