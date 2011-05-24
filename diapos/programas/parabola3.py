from numpy import *
from numpy.linalg import solve

print 'Ingrese coordenadas x y de tres puntos'
xs = zeros(3)
ys = zeros(3)
for i in range(3):
    linea = raw_input('P{0}: '.format(i + 1))
    x, y = map(float, linea.split())
    xs[i] = x
    ys[i] = y

m = xs.repeat(3).reshape((3, 3)) ** array([2, 1, 0])

abc = solve(m, ys)
a, b, c = abc

print 'La parabola es:'
print '{0} x2 + {1} x + {2}'.format(a, b, c)

