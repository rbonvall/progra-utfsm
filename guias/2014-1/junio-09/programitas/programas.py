def pregunta(n):
    linea = 10 * u'\u2500'
    print linea, n, linea


pregunta(1)
# P1
a = 'na\na\na'
print a
# FIN P1

pregunta(2)
# P2
a = 'pato pintor'
print a.replace('p', 'g')
# FIN P2

pregunta(3)
# P3
a = 'un buen pudu azul'
print a.replace('x', 'u')
# FIN P3

pregunta(4)
# P4
a = 'un {0} pudu azul'
print a.format('mal').upper()
# FIN P4

pregunta(5)
# P5
a = ['pan', 'cafe', 'te']
print a[1][1].join(a)
# FIN P5

pregunta(6)
# P6
a = ['pan', 'cafe', 'te']
print a[1].split('a')[1]
# FIN P6

pregunta(7)
# P7
a = 'ay, ahi hay pan'
print len(a)
print len(a.split())
print len(a.split('h'))
print len(a.split('a'))
print len(a.split('ay'))
# FIN P7

pregunta(8)
# P8
a = 'El sobre esta sobre esta mesa'
b = a.split()
print a[2] == a[8]
print a[0] == a[7]
print b[3] == b[5]
print b[2][1] == b[5][2]
print len(set(a))
print len(set(b))
# FIN P8
