import math
import plot

def cuadrado(x):
    return x * x

plot.dibujar_ejes()

plot.color('red')
plot.graficar(math.sin)

plot.color('blue')
plot.graficar(math.exp)

plot.color('green')
plot.graficar(cuadrado)

raw_input()
