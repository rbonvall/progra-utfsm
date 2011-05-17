from numpy import *
from numpy.random import random

# note como al imprimir los arreglos
# aparecen perfectamente alineados


a = 5 * ones(40)
print a
print


b = 9 * ones(100)
b[0] = 0
b[-1] = 0
print b
print


creciendo = arange(1, 101)
decreciendo = arange(100, 0, -1)
c = zeros(199)
c[0:100] = creciendo
c[99:199] = decreciendo
print c
print


d = zeros(11)
d[0:11:2] = 1
print d
print


#e = arange(3000) % 3
e = arange(30) % 3
print e


f = random(100) * 2 - 1
print f
print


g = 8.4 + random(100) * (9.7 - 8.4)
print g
print

