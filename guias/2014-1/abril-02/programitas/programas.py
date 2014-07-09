print '==== P1 ===='
# P1
a = 13 / 5
b = 13 % 5
c = '2' * a + '3' * b
print c
# FIN P1

print '==== P2 ===='
# P2
a = 18 / 4
b = len(str(a)) % 8
c = b != 1
print not c
# FIN P2

print '==== P3 ===='
# P3
a = '13'
b = '7'
s = a + 2 * b
print int(s) + len(s)
# FIN P3

print '==== P4 ===='
# P4
x = 1 + 2 * 3
y = 8 > x
z = 0 < x
print y and z
# FIN P4

print '==== P5 ===='
# P5
n = 1000
print n % 3 != n / 700
# FIN P5

print '==== P6 ===='
# P6
ocho = int('9207'[len('uno')])
print ocho, not 8
# FIN P6

print '==== P7 ===='
# P7
b = '7100'
c = int(b)
d = b[c % len(b)]
print d + d
# FIN P7

print '==== P8 ===='
# P8
n = 'm'
m = n + 'n'
n = n + m
print m + n
# FIN P8

print '==== P9 ===='
# P9
campo = 'tvoarcoa'
animal = (campo[1] + campo[3]
        + campo[5] + campo[7])
print animal in campo, animal
# FIN P9

print '==== P10 ===='
# P10
valor = 13
string = 'valor'
doble = string * 2
print doble
# FIN P10
