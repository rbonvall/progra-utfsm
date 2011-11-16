# P1
s = {78, 15, 91, 15}
print len(s)
# FIN P1

# P2
d = {78: 15, 91: 15}
print len(d)
# FIN P2

# P3
n = (17, 3, 1993)
h = (14, 5, 2011)
print n < h
# FIN P3

# P4
x, y = ((27, 3), 9)
z, w = x
print y + w
# FIN P4

# P5
a = 'acabase'
b = set(a)
c = list(b)
c.sort()
print c[2]
# FIN P5

# P6
t = 'papagayo'
w = t.split('a')
print w[3]
# FIN P6

# P7
def f(a, b):
    return a + 2 * b

a = 5
b = 2
print f(b, a)
# FIN P7


# P8
def f(a):
    return x + a

def g(x):
    return x + a

x = 5
a = 7
print f(x) + g(x)
# FIN P8

