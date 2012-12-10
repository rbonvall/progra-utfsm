print '== P1 =='
# P1
a = [(1, 2), (3, 4), (5, 6)]
print len(a)
# FIN P1

print '== P2 =='
# P2
a = [[1], [2]]
a.append([3, 4, 5])
print len(a)
# FIN P2

print '== P3 =='
# P3
a = {'a': 'b', 'b': 'c', 'c': 'a'}
print a['a']
# FIN P3

print '== P4 =='
# P4
print len(set(range(5)) & set(range(3)))
# FIN P4

print '== P5 =='
# P5
d = {'a': 'b', 'b': 'c', 'c': 'a'}
a = ['d', 'e', 'a']
for c in d:
    if c in a:
        print d[c]
# FIN P5

print '== P6 =='
# P6
t = [(25, (1, 9)), (15, (2, 11))]
s = 0
for i in t:
    a, b = i
    c, d = b
    s += c
print s
# FIN P6

print '== P7 =='
# P7
def f(x):
    x = 18
    return x

x = 10
print f(f(f(x)))
# FIN P7

print '== P8 =='
# P8
def f(a, b):
    return a * b

def g(a, b):
    return f(b, a + b)

a, b = (2, 1)
print f(g(b, a), g(a, b))
# FIN P8

