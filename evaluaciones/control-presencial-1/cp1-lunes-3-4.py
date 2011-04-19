anterior = float(raw_input('Dia 1: '))
subidas = 0
bajadas = 0
for i in range(2, 11):
    actual = float(raw_input('Dia ' + str(i) + ': '))
    diferencia = actual - anterior
    if diferencia < 0:
        bajadas = bajadas + 1
    elif diferencia > 0:
        subidas = subidas + 1
    anterior = actual

print 'El precio subio', subidas, 'veces y bajo', bajadas, 'veces'

