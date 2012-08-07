#!/usr/bin/env python

import turtle

turtle.title('Laberinto')
turtle.shape('turtle')
turtle.color('navy')
turtle.width(2)
turtle.speed('slowest')

f = 30

raw_input()
ruta = raw_input('Ruta: ')
n = len(ruta)
for i in range(n):
    d = ruta[i]
    if   d == 'E': turtle.seth(0)
    elif d == 'N': turtle.seth(90)
    elif d == 'O': turtle.seth(180)
    elif d == 'S': turtle.seth(270)
    turtle.forward(f)

print 'Distancia recorrida:', len(ruta)
raw_input()

