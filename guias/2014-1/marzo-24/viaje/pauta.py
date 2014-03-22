tramo = -1
total = 0
while tramo != 0:
    tramo = int(raw_input('Tramo: '))
    total += tramo
horas = total / 60
minutos = total % 60
if horas == 1:
    print 'Total: 1 hora y', minutos, 'minutos'
else:
    print 'Total:', horas, 'horas y', minutos, 'minutos'
