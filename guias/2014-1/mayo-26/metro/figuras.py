# NO MODIFIQUE ESTE ARCHIVO.

from turtle import up, down, goto, seth, circle, forward, left

# Dibuja circunferencia de radio r centrada en (x, y)
def dibujar_circunferencia(x, y, r):
    up()
    goto(x + r, y)
    seth(90)
    down()
    circle(r)

# Dibuja cuadrado de lado a centrado en (x, y)
def dibujar_cuadrado(x, y, a):
    up()
    goto(x + 0.5 * a,
         y - 0.5 * a)
    seth(90)
    down()
    for i in range(4):
        forward(a)
        left(90)

