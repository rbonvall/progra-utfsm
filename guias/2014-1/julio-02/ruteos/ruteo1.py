entrada = open('a.txt')
salida = open('b.txt', 'w')
p = '{0}-{1}\n'
for x in entrada:
    a = x.index('l')
    b = x.index('i')
    for i in range(3):
        t = p.format(a, b * x[i])
        salida.write(t)
salida.close()
entrada.close()


