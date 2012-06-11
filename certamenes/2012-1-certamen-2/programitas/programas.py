# P1
a = [(1, 2, 3, 4), (5, 6, 7)]
print len(a)
# FIN P1

# P2
a = [1, 2]
a.append([3, 4, 5])
print len(a)
# FIN P2

# P3
a = {'a': 'b', 'b': 'c', 'c': 'a'}
print a['a']
# FIN P3

# P4
a = {'a': 'b', 'b': 'c', 'c': 'a'}
print a[a['a']]
# FIN P4

# P5
print 'Por escribir'
# FIN P5

# P6
print 'Por escribir'
# FIN P6

# P7
def f(x):
    x = 5
    return x

x = 10
print f(f(f(x)))
# FIN P7

# P8
def f(a, b):
    return a * b

def g(a, b):
    return f(b, a + b)

a, b = (2, 1)
print f(g(b, a), g(a, b))
# FIN P8

