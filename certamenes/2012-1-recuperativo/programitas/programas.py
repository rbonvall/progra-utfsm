print '=== P1 ==='
# P1
x = 'y'
y = 'x'
print 'x', 'y'
# FIN P1

print '=== P2 ==='
# P2
x = 1 + 2 * 3
y = 8 > x
z = 0 < x
print y and z
# FIN P2

print '=== P3 ==='
# P3
a = 1452
b = a % 100
c = a / 100
print b + c

# FIN P3

print '=== P4 ==='
# P4
texto = 'a-aa-aaa'
cosas = texto.split('-')
print '\n'.join(cosas)

# FIN P4

print '=== P5 ==='
# P5
s = [(15, 'cm'), (12, 'km'),
     ( 9,  'm'), (17, 'cm')]
t = ''
for c, u in s:
    t += u
print t
# FIN P5

print '=== P6 ==='
# P6
d = {
  'd': {'d': 'x', 's': 'a'},
  's': {'p': 'd', 'm': 'n'},
  'x': {'s': 'x', 'd': 'q'},
}
print d[d['d']['d']]['d']
# FIN P6

print '=== P7 ==='
# P7
a = 100
b = 200
c = 700
while a != b + c:
    if a < b:
        a += b
    if a < c:
        c -= a
print a, b, c
# FIN P7

print '=== P8 ==='
# P8
def f(a, b):
    return a
def g(x, y):
    return y
a, b, x, y = (1, 2, 3, 4)
print g(f(a, x), f(x, b))
# FIN P8

