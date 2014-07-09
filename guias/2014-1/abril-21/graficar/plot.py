from turtle import *

shape('turtle')
speed('fast')
width(5)
X = 5
Y = 5
S = 50

def dibujar_ejes():
    up()
    goto(-X * S,  0); down(); goto(X * S, 0); up()
    goto( 0, -Y * S); down(); goto(0, Y * S); up()

def graficar(f):
    up()
    N = 50
    for i in range(N):
        x = -X + 2 * X * i / float(N)
        y = f(x)
        goto(S * x, S * y)
        down()




