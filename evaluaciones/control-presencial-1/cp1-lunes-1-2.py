anterior = float(raw_input('Dia 1: '))
mayor_alza = -1
for i in range(2, 11):
    actual = float(raw_input('Dia ' + str(i) + ': '))
    alza = actual - anterior
    if alza > mayor_alza:
        mayor_alza = alza
    anterior = actual

if mayor_alza > 0:
    print 'La mayor alza fue de', mayor_alza, 'pesos'
else:
    print 'No hubo alzas'

