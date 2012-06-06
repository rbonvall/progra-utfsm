# P1
a = [(1, 2, 3, 4), (5, 6, 7)]
print len(a)
# FIN P1

# P2
a = {'a': 'b', 'b': 'c', 'c': 'd'}
print a['a']
# FIN P2

# P3
# FIN P3

# P4
a = {'a': 'b', 'b': 'c', 'c': 'd'}
print a[a['a']]
# FIN P4

# P5
# FIN P5

# P6
#FIN P6

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

