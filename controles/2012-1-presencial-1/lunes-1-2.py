print 'Jugador X'
x1 = int(raw_input('Carta 1: '))
x2 = int(raw_input('Carta 2: '))

print 'Jugador Y'
y1 = int(raw_input('Carta 1: '))
y2 = int(raw_input('Carta 2: '))

if x1 == x2 and y1 == y2:
    print 'Empate'
elif x1 == x2:
    print 'Gana X'
elif y1 == y2:
    print 'Gana Y'
elif abs(x1 - x2) < abs(y1 - y2):
    print 'Gana X'
elif abs(x1 - x2) > abs(y1 - y2):
    print 'Gana Y'
else:
    print 'Empate'


