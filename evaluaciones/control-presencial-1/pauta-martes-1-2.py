anterior = float(raw_input('Dia 1: '))
suma = anterior
for i in range(2, 11):
    actual = float(raw_input('Dia ' + str(i) + ': '))
    suma = suma + actual
    if actual > anterior:
        print 'El promedio hasta ahora es', suma / i
    anterior = actual

