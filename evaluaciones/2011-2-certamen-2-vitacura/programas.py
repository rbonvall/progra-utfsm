# P1
d = {'a': 'b', 'b': 'c'}
print d['b']
# FIN P1

# P2
k = ['a', 'b', 'b', 'c']
print k[1]
# FIN P2

# P3
p = (3, 1, 2)
q = (3, 1)
print p < q
# FIN P3

# P4
x, y = ((2, 8), 16)
z, w = x
print y + w
# FIN P4

# P5
a = 'estanque'
b = 'tan'
c = b in a
d = a[3] in b
print c and d
# FIN P5

# P6
print len({
    0: ['a', 'bcd'],
    1: ['ef', 'ghij', 'k'],
    2: ['l'],
}[1][1][1])
# FIN P6

# P7
def f(x, y, z):
    return x + y * z

w, i = (0, 1)
a = f('w', 'i', 2)
b = f( w ,  i , 2)
print a * b
# FIN P7


# P8
def f(d):
    return d[1]

a = f('pala')
b = f({2: 3, 1: 4})
print a * b
# FIN P8

