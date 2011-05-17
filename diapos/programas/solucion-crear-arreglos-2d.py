from numpy import *

a = 9 * ones((5, 5))
a[2, 2] = 0
print a
print

b = 8 * ones((5, 5))
b[3, :] = 1
print b
print

c = 8 * ones((5, 5))
c[3, :] = arange(5)
print c
print

d = zeros((5, 5))
d[0::2, :] = arange(5)
d[1::2, :] = arange(4, -1, -1)
print d
print

valores = 1.0 + arange(25) % 3
e = valores.reshape((5, 5))
print e
print


