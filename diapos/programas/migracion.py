from numpy import *

m = array([[95,  3],
           [ 5, 97]]) / 100.0

p = zeros(2)
p[0] = float(raw_input('Poblacion ciudad: '))
p[1] = float(raw_input('Poblacion suburbios: '))

print
print 'Anno    Ciudad    Suburbios'
print '---------------------------'
for anno in range(2012, 2022):
    p = dot(m, p)
    print '{0} {1:>10.3f} {2:>10.3f}'.format(anno, p[0], p[1])

