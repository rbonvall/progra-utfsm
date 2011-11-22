n = int(raw_input('Cuantos dias? '))

anterior = float(raw_input('Dia 1: '))
mayor_alza = 0.0

for i in range(2, n + 1):
    actual = float(raw_input('Dia ' + str(i) + ': '))
    diferencia = actual - anterior
    if diferencia > mayor_alza:
        mayor_alza = diferencia
    anterior = actual

if mayor_alza > 0.0:
    print 'La mayor alza fue de', mayor_alza, 'pesos'
else:
    print 'No hubo alzas'
