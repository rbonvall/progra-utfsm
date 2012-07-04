from numpy import array, ones

print '=== P1 ==='
# P1
a = array([11, 22, 33])
b = array([11,  0, 22])
print (a + b) / 11
# FIN P1

print '=== P2 ==='
# P2
p = 'nn\nnn'
print p
# FIN P2

print '=== P3 ==='
# P3
a = array([[77, 11, 33, 22],
           [55, 33,  0, 33],
           [88, 44, 44, 44]])
b = a[:, 1]
print b.sum()
# FIN P3

print '=== P4 ==='
# P4
a = 'En un lugar de la Mancha'
b = a.split()
print map(len, b)
# FIN P4

print '=== P5 ==='
# P5
a = ones((5, 5)).astype(int)
a[0:4, 2:5] *= 0
print a.sum()
# FIN P5

print '=== P6 ==='
# P6
a = 'a:b  c:d  e:f  g:h'
b = a.split(':')
print b[2]
# FIN P6


# PA
am = open('misterio.txt')
ae = open('enigma.txt', 'w')
for x in am:
    ae.write(x[0])
am.close()
ae.close()
# FIN PA

print '=== Archivo enigma.txt ==='
print open('enigma.txt').read()

