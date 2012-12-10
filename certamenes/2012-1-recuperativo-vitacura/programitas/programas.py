print '=== P1 ==='
# P1
a = 20
b = 100
print "a, b"
# FIN P1

print '=== P2 ==='
# P2
c = [2, 3, 4, 5]
print c[sum(c) % len(c)]
# FIN P2

print '=== P3 ==='
# P3
a = 'a' in 'aaa'
b = a or ('b' != 'b')
print a and b
# FIN P3

print '=== P4 ==='
# P4
a = 'el sobre sobre el pupitre'
b = a.split()
print b[3][0] == b[1][4]
# FIN P4

print '=== P5 ==='
# P5
s = 0
a = [(9, (1,  2)),
     (7, (2, -5)),
     (6, (1,  3))]
for t in a:
    x, y = t
    z, w = y
    s += z
print s
# FIN P5

print '=== P6 ==='
# P6
d = {
  'p': ['puma', 'pluma'],
  'd': ['dado', 'dardo'],
  's': ['sota', 'sorda'],
}

for s in d:
    print len(d[s])
# FIN P6

print '=== P7 ==='
# P7
a = 0
b = 1
c = True
while a != b:
    if c:
        a += 2
        b += 3
    else:
        b -= 3
    c = not c
print a
# FIN P7

print '=== P8 ==='
# P8
def f(a, b):
    return a

def g(x, y):
    return y

a, y, b, x = (1, 2, 3, 4)
print f(g(y, x), g(b, a))
# FIN P8

