from numpy import array, zeros

print '=== P1 ==='
# P1
tres = array([1, 4, 2])
seis = 2 * tres
print seis
# FIN P1

print '=== P2 ==='
# P2
a = 'papanatas'
a = a.replace('p', 'n')
a = a.replace('n', 'p')
print a
# FIN P2

print '=== P3 ==='
# P3
a = array([[ 0, 99, 33, 11],
           [55, 33,  0, 33],
           [88, 44, 22, 11]])
b = a[1:, 2:]
print b.sum()
# FIN P3

print '=== P4 ==='
# P4
w = ['Hoy', 'hay', 'pan']
p = '\n'
print p.join(w)
# FIN P4

print '=== P5 ==='
# P5
a = zeros(900).astype(int)
a[300:600:200] += 1
print a.sum()
# FIN P5

print '=== P6 ==='
# P6
a = 'abeja:becerro:doberman'
b = a.split('be')
print b[1]
# FIN P6


# PA
am = open('misterio.txt')
ae = open('enigma.txt', 'w')
for x in am:
    xs = x.split()
    ae.write(xs[0] + xs[1])
    ae.write('\n')
am.close()
ae.close()

# FIN PA

print '=== Archivo enigma.txt ==='
print open('enigma.txt').read().rstrip()

