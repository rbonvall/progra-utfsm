from numpy import array
separador = '========== P{} =========='

print separador.format(1)
# P1
a = array([77, 11, 33, 22])
b = a / 11
print b
# FIN P1

print separador.format(2)
# P2
a = 'En un lugar de la Mancha'
b = a.split()
print map(len, b)
# FIN P2

print separador.format(3)
# P3
a = array([[77, 11, 33, 22],
           [55, 33,  0, 33],
           [88, 44, 44, 44]])
b = a[:, 1]
print b.sum()
# FIN P3

print separador.format(4)
# P4
a = '{2}{0}{2}{0}'
x, y, z = 'total'.split('t')
print a.format(x, y, z)
# FIN P4


# PA
am = open('misterio.txt')
ae = open('enigma.txt', 'w')
for x in am:
    ae.write(x[0])
am.close()
ae.close()
# FIN PA
