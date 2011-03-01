n1 = int(raw_input('Nota 1: '))
n2 = int(raw_input('Nota 2: '))
n3 = int(raw_input('Nota 3: '))

suma = n1 + n2 + n3
promedio = int(round(suma / 3.0))

print 'Su promedio', promedio, 'es',
if promedio < 30:
    print 'pesimo'
elif promedio < 55:
    print 'mediocre'
elif promedio < 80:
    print 'aceptable'
else:
    print 'excelente!'
