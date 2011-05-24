from numpy import *
from numpy.linalg import solve

print 'Ingrese coordenadas x y de tres puntos'
m = zeros((3, 3))
ys = zeros(3)
for i in range(3):
    linea = raw_input('P{0}: '.format(i + 1))
    x, y = map(float, linea.split())

    ys[i] = y
    for j in range(3):
        m[i, j] = x ** (2 - j)

abc = solve(m, ys)
a, b, c = abc

print 'La parabola es:'
print '{0} x2 + {1} x + {2}'.format(a, b, c)

