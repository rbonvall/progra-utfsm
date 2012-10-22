# Dibujador de obras de arte.
# Autora: Pitonia von Turtle.
#
# No se le ocurra modificar mi programa.
# Soy una artista temperamental.

from poligonos import trasladar, escalar, dibujar
from math import cos, sin, pi
from random import choice
from turtle import color, width, speed

# Preguntar que figura -----------------------------
print 'Que figura?'
print 'a) cuadrado'
print 'b) estrella'
fig = raw_input('---> ').lower()[0]
print

# Crear la figura ----------------------------------
if fig == 'a':
    poligono = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
elif fig == 'b':
    print 'De cuantas puntas?'
    puntas = int(raw_input('---> '))
    print
    poligono = []
    for i in range(2 * puntas):
        r = 1 + (i % 2)
        x = r * cos(2 * pi * i / (2 * puntas))
        y = r * sin(2 * pi * i / (2 * puntas))
        poligono.append((x, y))

# Preguntar el disen~o -----------------------------
print 'Que disen~o?'
print 'a) azulado'
print 'b) ajedrez'
print 'c) colores al azar'
diseno = raw_input('---> ').lower()[0]
print

# Definir la funcion que se encarga del disen~o ----
def cambiar_color(i, j):
    if diseno == 'a':
        color('blue')
    elif diseno == 'b':
        if (i + j) % 2 == 0:
            color('red')
        else:
            color('black')
    elif diseno == 'c':
        colores = ['orange', 'maroon', 'navy',
                   'tan', 'gold', 'darkgreen']
        color(choice(colores))

# Dibujar la grilla del fondo ----------------------
width(3)
speed('fastest')
n = 10
for j in range(n):
    for i in range(n):
        cambiar_color(i, j)
        p = escalar(poligono, 5 + i * 0.8)
        p = trasladar(p, -250 + 50 * i, -250 + 50 * j)
        dibujar(p)

# Dibujar el tubo abstracto emergente --------------
width(5)
for i in range(1, 15):
    p = escalar(poligono, 12 * i)
    cambiar_color(i, 0)
    dibujar(p)

print 'Voila!'
raw_input()

