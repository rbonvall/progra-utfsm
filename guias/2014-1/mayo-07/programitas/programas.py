def pregunta(n):
    linea = 10 * u'\u2500'
    print linea, n, linea


pregunta(1)
# P1
s = {78, 15, 91, 15} 
print len(s) 
# FIN P1

pregunta(2)
# P2
d = {78: 15, 91: 15}
print len(d)
# FIN P2

pregunta(3)
# P3
a = set('elefante')
b = set('antilope')
print len(a & b)
print len(a | b)
# FIN P3

pregunta(4)
# P4
a = {'elefante'}
b = {'antilope'}
print len(a & b)
print len(a | b)
# FIN P4

pregunta(5)
# P5
a = {3, 4, 5}
a |= {5, 6, 7}
print len(a)
# FIN P5

pregunta(6)
# P6
print len(set(range(55)) &
          set(range(99)))
# FIN P6

pregunta(7)
# P7
a = 'acabase' 
b = set(a) 
c = list(b) 
c.sort() 
print c[2] 
# FIN P7

pregunta(8)
# P8
d = {'a': 'b',
     'c': 'd',
     'e': 'a'}
s = {'e', d['e'], d[d['e']]}
print len(s)
# FIN P8

raw_input()
