from turtle import *

title('Laberinto')
shape('turtle')
color('navy')
width(2)
speed('slowest')

f = 30

raw_input()
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

