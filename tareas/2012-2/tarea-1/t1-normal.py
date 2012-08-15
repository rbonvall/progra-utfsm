from turtle import *

title('Laberinto')
shape('turtle')
color('brown')
width(5)
speed('fastest')

f = 30
x0, y0 = -200, 200

fila = ':)'
y = 0
while len(fila) > 0:
    fila = raw_input('> ')
    n = len(fila)
    for x in range(n):
        if fila[x] == 'x' or fila[x] == 'X':
            up()
            goto(f * x + x0, f * y + y0)
            seth(90)
            down()
            for i in range(4):
                forward(f)
                right(90)
    y -= 1

up()
goto(-f / 2 + x0, +f / 2 + y0)
seth(0)
down()
color('navy')
width(2)
speed('slowest')

ruta = raw_input('Ruta: ')
n = len(ruta)
for i in range(n):
    d = ruta[i]
    if   d == 'E': seth(0)
    elif d == 'N': seth(90)
    elif d == 'O': seth(180)
    elif d == 'S': seth(270)
    forward(f)

print 'Distancia recorrida:', len(ruta)
raw_input()

