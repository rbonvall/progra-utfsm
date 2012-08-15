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

raiz2 = 2 ** 0.5

ruta = raw_input('Ruta: ')
n = len(ruta)
i = 0
distancia = 0
while i < n:
    d = ruta[i]

    if   d == 'E': seth(0)
    elif d == 'N': seth(90)
    elif d == 'O': seth(180)
    elif d == 'S': seth(270)

    if i + 1 < n:
        s = ruta[i + 1]
    else:
        s = ':)'

    if   ((d == 'E' and s == 'S') or
          (d == 'S' and s == 'O') or
          (d == 'O' and s == 'N') or
          (d == 'N' and s == 'E')):
        right(45)
        forward(f * raiz2)
        distancia += raiz2
        i += 2

    elif ((d == 'E' and s == 'N') or
          (d == 'S' and s == 'E') or
          (d == 'O' and s == 'S') or
          (d == 'N' and s == 'O')):
        left(45)
        forward(f * raiz2)
        distancia += raiz2
        i += 2

    else:
        forward(f)
        distancia += 1
        i += 1

print 'Distancia recorrida:', distancia
raw_input()

