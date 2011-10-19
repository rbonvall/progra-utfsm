from numpy import *
# INICIO
a = arange(6)
b = a.reshape((3, 2))
b[0, 1] = 99
print a
print b
