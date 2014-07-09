x = float(raw_input('x: '))
p = 0
i = 0

print 'Coeficientes:'
entrada = raw_input()
while entrada != 'FIN':
    a = float(entrada)
    p += a * (x ** i)
    i += 1
    entrada = raw_input()
print 'p(x) =', p

